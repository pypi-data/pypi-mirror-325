import argparse
import json
import os
import sys
from collections import defaultdict
from typing import Optional
from xml.etree import ElementTree
from xml.etree.ElementTree import XML

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from menschmachine.log import get_logger
from menschmachine.platform_adapter import LocalFilesystemAdapter
from prompt_toolkit.shortcuts import button_dialog, input_dialog
# noinspection PyProtectedMember
from websocket import _exceptions

from flashcommit import get_api_url, logger, set_batch_mode, is_batch_mode
from flashcommit.client.queryclient import QueryClient
from flashcommit.client.reviewclient import ReviewClient
from flashcommit.client.reviewclientV3 import ReviewClientV3
from flashcommit.flash_commit_adapter import FlashCommitAdapter
from flashcommit.gitclient import GitClient
from flashcommit.prompt_generator import PromptGenerator
from flashcommit.ui import UI
from flashcommit.version import version

NO_API_KEY_MSG = "CODEX_API_KEY environment variable not set"
NO_CHANGES_FOUND_MSG = "[yellow]No changes found.[/yellow]"
QUERY_PROGRESS_MSG = "[cyan]Thinking about your question..."
REVIEWING_PROGRESS_MSG = "[cyan]Reviewing your changes..."
COMMIT_MSG_PROGRESS_MSG = "[cyan]Generating your commit message..."


def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d


def from_xml(param) -> dict:
    xml_start = param.index("<")
    xml_end = param.rfind(">")
    xml_string = param[xml_start:xml_end + 1]
    soup = BeautifulSoup(xml_string, "html5lib")
    try:
        xml: XML = ElementTree.fromstring(str(soup))
    except:
        logger.error(f"Cannot parse xml {soup}")
        raise
    to_dict = etree_to_dict(xml)
    return to_dict["html"]["body"]


def extract_dicts_with_key(data, key: str):
    result = []

    def recursive_search(item):
        if isinstance(item, dict):
            if key in item:
                result.append(item)
            for value in item.values():
                recursive_search(value)
        elif isinstance(item, list):
            for element in item:
                recursive_search(element)

    recursive_search(data)
    return result


class FlashCommit:
    def __init__(self):
        load_dotenv()
        self.current_task = None
        self.current_progress = None
        self.git_client = GitClient()
        self.platform_adapter = LocalFilesystemAdapter(get_logger(), is_batch_mode())
        self.git_client.codex_client = self.create_client()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def review(self) -> None:
        try:
            diff = self.git_client.get_diff()
            if diff:
                with self.platform_adapter.show_progress(REVIEWING_PROGRESS_MSG):
                    comments = self.create_review_client().review(diff)
                self.handle_review(comments)
            else:
                logger.info(NO_CHANGES_FOUND_MSG)
        except Exception as e:
            logger.error(f"Error reviewing your changes: {str(e)}", exc_info=True)
            if isinstance(e, _exceptions.WebSocketException):
                logger.error("WebSocket connection error. Please check your internet connection.")
            elif isinstance(e, json.JSONDecodeError):
                logger.error("Error parsing server response. Please try again later.")
            sys.exit(3)

    def handle_review(self, changes):
        self.parse_review(changes)

    def parse_review(self, review_steps):

        adapter = FlashCommitAdapter(self.git_client, self.create_client(), self.platform_adapter)
        if not is_batch_mode():
            UI(adapter, review_steps).run()
        else:
            for file_, content, intention in review_steps:
                adapter.replace(file_, intention, content)

    def create_client(self) -> QueryClient:
        apikey = self.get_api_key()
        try:
            client = QueryClient(get_api_url() + "/v3/flashcommit/websocket/agent/query", apikey, self.platform_adapter,
                                 self.git_client)

            client.auth()
            return client
        except _exceptions.WebSocketBadStatusException as e:
            logger.error(f"Cannot connect to server: {e.status_code}")
            if e.status_code == 403:
                logger.error("You are not authorized to access this server, check your api key")
            sys.exit(3)

    def create_review_client(self) -> ReviewClient:
        apikey = self.get_api_key()
        try:
            client = ReviewClientV3(get_api_url() + "/v3/flashcommit/websocket/review", apikey, self.platform_adapter,
                                    self.git_client)

            client.auth()
            return client
        except _exceptions.WebSocketBadStatusException as e:
            logger.error(f"Cannot connect to server: {e.status_code}")
            if e.status_code == 403:
                logger.error("You are not authorized to access this server, check your api key")
            sys.exit(3)

    @staticmethod
    def get_api_key() -> Optional[str]:
        apikey = os.getenv("CODEX_API_KEY")
        if not apikey:
            raise ValueError(NO_API_KEY_MSG)
        return apikey

    @staticmethod
    def display_answer(comments: str) -> None:
        print(comments)

    def get_commit_message_prompt(self) -> Optional[str]:
        diff = self.git_client.get_diff()
        if not diff:
            return None
        return PromptGenerator.get_commit_message_prompt(diff)

    def generate_message(self) -> Optional[str]:
        try:
            prompt = self.get_commit_message_prompt()
            if prompt:
                with self.platform_adapter.show_progress(COMMIT_MSG_PROGRESS_MSG):
                    client = self.create_client()
                    answer = client.to_json(client.send_single_query(prompt, temperature=0.3))
                return answer["msg"]
            else:
                logger.console.print(NO_CHANGES_FOUND_MSG)
                return None
        except Exception:
            logger.error("Error generating a commit message", exc_info=True)
            return None

    def commit(self, add_all: bool = False) -> None:
        message = self.generate_message()
        if message is None:
            return
        result = button_dialog(
            title='Use this as the commit message?',
            text=message,
            buttons=[
                ('Yes', 2),
                ('Edit', 1),
                ('No', 3),
                ('Try again', 4)
            ],
        ).run()
        if result == 1:
            edited_message = input_dialog(
                title='Edit Commit Message',
                text='Edit your commit message:',
                default=message
            ).run()
            if edited_message:
                self.git_client.commit(edited_message, add_all)
                logger.info("Changes committed successfully.")
        elif result == 2:
            self.git_client.commit(message, add_all)
            logger.info("Changes committed successfully.")
        elif result == 3:
            return
        elif result == 4:
            self.commit()

    def full_flash(self, query):
        set_batch_mode(True)
        assert is_batch_mode()
        logger.info("1. step querying")
        self.query(query)
        logger.info("2. step commiting")
        self.git_client.commit(query, True)
        logger.info("3. full loop done")

    def query(self, query):
        with self.platform_adapter.show_progress(QUERY_PROGRESS_MSG):
            msg = self.create_client().query(query, temperature=0.6)
        try:
            comments = msg["answer"]
            logger.debug(f"{msg}")
            if "changes" in msg and len(msg["changes"]) > 0:
                adapter = FlashCommitAdapter(self.git_client, self.create_client(),
                                             self.platform_adapter)
                if not is_batch_mode():
                    UI(adapter, msg["changes"], comments.strip()).run()
                else:
                    for obj in msg["changes"]:
                        adapter.replace(obj["filename"], obj["intention"], obj["source"])
                    self.display_answer(comments.strip())
            else:
                self.display_answer(comments.strip())
        except Exception:
            logger.error(f"Error processing your query, msg: {msg}", exc_info=True)

    def send_ignore(self, file_: str, comment_: str, diff_: str) -> None:
        self.create_client().save_ignore(file_, comment_, diff_)

    def replay(self, json_file: str) -> None:
        try:
            with open(json_file, "r") as f:
                recv = f.read()
                answer_msg = json.loads(recv)
                answer = answer_msg["message"]["answer"]
                self.handle_review(answer)
        except FileNotFoundError:
            logger.error(f"File not found: {json_file}")
            sys.exit(1)
        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error replaying from file {json_file}: {str(e)}", exc_info=True)
            sys.exit(1)
        logger.info(f"Successfully replayed review from {json_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Flash Commit - Revolutionizing your coding workflow',
        epilog='For more information, visit: https://github.com/MenschMachine/flashcommit'
    )
    parser.add_argument('-m', '--message', help='Generate a commit message', action='store_true')
    parser.add_argument('-c', '--commit', help='Generate a commit message and commit the changes (implies -m)',
                        action='store_true')
    parser.add_argument('-a', '--add-all', help='When committing, add all changed and new files to the index',
                        action='store_true')
    parser.add_argument('-q', '--query', help='Submit a query about the whole codebase', action='store', type=str)
    parser.add_argument('-r', '--review', help='Review the current changes - the default action', action='store_true')
    parser.add_argument('-V', '--version', help='Show version information and exit', action='store_true')
    parser.add_argument('-b', '--batch', help='Batch mode, no interactive displays, assume yes on everything',
                        default=False,
                        action='store_true')
    parser.add_argument('-R', '--replay', action='store', help=argparse.SUPPRESS)
    parser.add_argument('-F', '--full', action='store', type=str,
                        help="Full automatic development loop: apply the changes and commit them directly")
    parser.add_argument('-P', '--project-directory', action='store', type=str,
                        help="The root directory of the codebase we are talking about")
    parser.add_argument('--full-from-file', action='store', type=str,
                        help="Full automatic development loop, but read instructions from a file")
    args = parser.parse_args()

    if args.project_directory is not None:
        os.chdir(args.project_directory)

    if args.version:
        print(version)
        sys.exit(0)
    set_batch_mode(args.batch)
    with FlashCommit() as flash:
        if args.commit:
            flash.commit(args.add_all)
        elif args.replay:
            flash.replay(args.replay)
        elif args.message:
            flash.generate_message()
        elif args.query is not None:
            flash.query(args.query)
        elif args.full is not None:
            flash.full_flash(args.full)
        elif args.full_from_file is not None:
            with open(args.full_from_file, "r") as f:
                instructions = f.read()
                flash.full_flash(instructions)
        elif args.review or (not args.commit and not args.message and args.query is None):
            flash.review()


if __name__ == "__main__":
    main()

import json
import os

from typing_extensions import Tuple

from flashcommit import logger
from flashcommit.client import BaseClient


class QueryClient(BaseClient):

    def query(self, query, temperature: float | None = None) -> dict:

        file_list = self.platform_adapter.get_file_list(self.filter_files)

        def loop() -> dict:
            recv = self.ws.recv()
            logger.debug(f"Received {recv}")
            answer_msg = self.to_json(recv)
            if "message" in answer_msg:
                return answer_msg["message"]
            elif "question" in answer_msg:
                q = answer_msg["question"]
                a = self.platform_adapter.ask_user(q)
                self.ws.send(a)
                return loop()
            elif "type" in answer_msg and answer_msg["type"] == "create_file_request":
                self._create_file(answer_msg)
                self.ws.send("True")
                return loop()
            elif "regex" in answer_msg:
                q = answer_msg["regex"]
                matching_files = self.platform_adapter.search_files(q)
                self.ws.send(json.dumps(matching_files))
                return loop()
            elif "files" in answer_msg:
                files = {}
                files_requested = answer_msg["files"]
                for f in files_requested:
                    logger.info(f"Received file request for {f}")
                    files[f] = self.platform_adapter.read_file(f)
                self.ws.send(json.dumps(files))
                return loop()
            elif not answer_msg:
                return {"answer": "MenschMachine is unable to answer your request, please try again later"}
            else:
                raise ValueError(f"Unknown query: {answer_msg}")

        self._send_msg("query", {"question": query, "file_list": file_list}, temperature=temperature)
        return loop()

    # noinspection PyMethodMayBeStatic
    def _create_file(self, answer_msg):
        filepath = answer_msg["filepath"]
        content = answer_msg["content"]
        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content)
            f.flush()
            logger.info(f"Created file {filepath}")

    def send_file_query(self, query: str, file_list: list[str]) -> Tuple[str, str]:
        self._send_msg("file_list", {"question": query, "file_list": file_list})
        recv = self.ws.recv()
        if not recv:
            raise ValueError("No response received")
        try:
            file_request = self.to_json(recv)
            files_requested = file_request["message"]["files"]
            original_query = file_request["message"]["original_query"]
            return files_requested, original_query
        except:
            logger.error(f"Cannot process response '{recv}'", exc_info=True)
            raise

    def send_single_query(self, query: str, temperature: float | None = None) -> str:
        self._send_msg("query", {"question": query}, temperature=temperature)
        recv = self.ws.recv()
        if not recv:
            raise ValueError("No response received")
        return self.to_json(recv)["message"]["answer"]

    def send_query_with_files(self, query: str, files: dict[str, str], temperature: float | None = None) -> dict:
        self._send_msg("query", {"question": query, "files": files}, temperature)
        recv = self.ws.recv()
        try:
            answer_msg = json.loads(recv)
            return answer_msg["message"]
        except:
            logger.error(f"Cannot parse answer {recv}")
            raise

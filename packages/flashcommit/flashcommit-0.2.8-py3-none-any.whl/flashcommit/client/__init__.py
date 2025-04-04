import json
from urllib.parse import urlparse, urlunparse

import requests
from menschmachine.filetypes.file_types import get_file_type, FileType
from menschmachine.platform_adapter import PlatformAdapter
from websocket import create_connection

from flashcommit import CodexJsonEncoder, logger, get_api_url
from flashcommit.gitclient import GitClient


def ws_to_http_base(ws_url: str) -> str:
    # Parse the WebSocket URL
    parsed_url = urlparse(ws_url)

    # Define the scheme mapping
    scheme_mapping = {
        'ws': 'http',
        'wss': 'https'
    }

    # Get the new scheme, defaulting to 'http' if not in the mapping
    new_scheme = scheme_mapping.get(parsed_url.scheme, 'http')

    # Create a new tuple with the updated scheme and empty path
    new_components = (new_scheme, parsed_url.netloc, '', '', '', '')

    # Reconstruct the URL with the new scheme and without the path
    http_url = urlunparse(new_components)

    return http_url


class BaseClient:
    def __init__(self, url: str, api_key: str, platform_adapter: PlatformAdapter, git_client: GitClient):
        self.ws = None
        self.platform_adapter = platform_adapter
        self.authenticated = False
        self.url = url
        self.http_url = ws_to_http_base(get_api_url())
        self.api_key = api_key
        self.git_client = git_client
        self.git_files = self.git_client.get_git_files()

    def filter_files(self, filename: str) -> bool:
        ft: FileType = get_file_type(filename)
        if filename.startswith("./"):
            filename = filename[2:]
        is_in = ft != FileType.ASSET and ft != FileType.BINARY and filename in self.git_files
        return is_in

    def to_json(self, param):
        response = requests.post(self.http_url + "/json", json={"input": param})
        response.raise_for_status()
        return response.json()

    def to_patch(self, diff, filename, source):
        response = requests.post(self.http_url + "/patch", json={"diff": diff, "filename": filename, "source": source})
        response.raise_for_status()
        return response.json()

    def save_ignore(self, file: str, comment: str, diff: str) -> dict:
        response = requests.put(self.http_url + "/user/settings",
                                json={
                                    "type": "review/ignore",
                                    "operation": "ADD",
                                    "payload": {
                                        "diff": diff,
                                        "filename": file,
                                        "comment": comment
                                    }
                                })
        response.raise_for_status()
        return response.json()

    def disconnect(self):
        self.ws.close()

    def read_files_requested(self, files_requested):
        file_contents = dict()
        for f in files_requested:
            logger.info(f"Codex is asking for file {f}")
            file_contents[f] = self.platform_adapter.read_file(f)
        return file_contents

    def _send_msg(self, type_: str, message: dict, temperature: float | None = None) -> None:
        msg = self._get_msg(type_, message, temperature)
        self.ws.send(msg)

    def auth(self):
        self.ws = create_connection(self.url)
        auth_msg = self._get_msg("auth", {"apiKey": self.api_key})
        self.ws.send(auth_msg)
        auth_result = json.loads(self.ws.recv())
        if "message" in auth_result:
            if "status" in auth_result["message"]:
                if auth_result["message"]["status"] == "authenticated":
                    self.authenticated = True
        return self.authenticated

    @staticmethod
    def _get_msg(type_: str, message: dict, temperature: float | None = None) -> str:
        if temperature is None:
            return json.dumps({"type": type_, "message": message}, cls=CodexJsonEncoder)
        else:
            return json.dumps({"type": type_, "temperature": temperature, "message": message}, cls=CodexJsonEncoder)

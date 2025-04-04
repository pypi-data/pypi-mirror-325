import json
import logging.config
import os
import pathlib
import sys
import tempfile
from typing import Optional

import yaml
from dotenv import load_dotenv
from pydantic import BaseModel
from rich.console import Console
from rich.theme import Theme

# BEGIN INIT

load_dotenv()

_api_url = os.getenv("CODEX_API_URL", "wss://api.codexanalytica.com")

source_dir = pathlib.Path(__file__).parent.resolve()
with open(f'{source_dir}/logging.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())
    try:
        if os.path.isdir('/tmp'):
            config["handlers"]["file"]["filename"] = f"/tmp/flashcommit.log"
        else:
            config["handlers"]["file"]["filename"] = f"{tempfile.gettempdir()}/flashcommit.log"
    except:
        pass
    logging.config.dictConfig(config)

_logger = logging.getLogger("flashcommit")

_batch_mode = False


def set_batch_mode(batch_mode: bool) -> None:
    global _batch_mode
    _batch_mode = batch_mode
    if not sys.stdin.isatty():
        _batch_mode = True


def is_batch_mode() -> bool:
    return _batch_mode


class Log:

    def __init__(self):
        super().__init__()
        self.theme = Theme({
            "info": "green",
            "warning": "magenta",
            "error": "bold red"
        })
        self.console = Console(theme=self.theme)

    def debug(self, msg):
        _logger.debug(msg)

    def exception(self, e):
        _logger.exception(e)

    def error(self, msg, exc_info: bool = False):
        _logger.error(msg, exc_info=exc_info)

    def warn(self, msg, exc_info: bool = False):
        _logger.warning(msg, exc_info=exc_info)

    def info(self, msg):
        _logger.info(msg)


logger = Log()


# END INIT


class RepoDetails(BaseModel):
    url: str
    repository: str
    owner: Optional[str]


class Commit(BaseModel):
    author: str
    committer: str
    message: str
    id: str


class Review(BaseModel):
    path: str
    position: int
    body: str


def get_api_url() -> str:
    return _api_url


class CodexJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseModel):
            return vars(obj)
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

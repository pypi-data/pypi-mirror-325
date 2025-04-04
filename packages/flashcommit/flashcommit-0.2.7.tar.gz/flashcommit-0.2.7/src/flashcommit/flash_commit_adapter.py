from menschmachine.platform_adapter import PlatformAdapter

from flashcommit import logger
from flashcommit.client import BaseClient
from flashcommit.gitclient import GitClient, PatchResult


class FlashCommitAdapter:
    def __init__(self, git_client: GitClient, codex_client: BaseClient, adapter: PlatformAdapter):
        super().__init__()
        self.adapter = adapter
        self.codex_client = codex_client
        self.git_client = git_client

    def apply(self, file: str, comment: str, diff: str) -> list[PatchResult]:
        try:
            logger.info(f"Applying {comment} to {file}")
            return self.git_client.patch(comment, diff, file)
        except Exception as e:
            logger.exception(e)
            raise ValueError(f"Cannot apply: {diff} for {file}")

    # noinspection PyMethodMayBeStatic
    def skip(self, file: str, comment: str, diff: str):
        logger.info(f"Skipping {comment} for {file}")

    def ignore(self, file: str, comment: str, diff: str):
        logger.info(f"Ignoring {comment} for {file}")
        self.codex_client.save_ignore(file, comment, diff)

    def replace(self, file: str, intention: str, content: str):
        self.adapter.write_file(file, content)

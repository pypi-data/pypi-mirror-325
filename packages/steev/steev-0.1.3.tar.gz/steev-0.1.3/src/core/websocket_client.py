import threading
from typing import TYPE_CHECKING

import click

from src.core.runner import get_runner
from src.core.websocket_base import WebSocketClientBase
from src.models import message
from src.utils.credentials import cred
from src.version import __version__

if TYPE_CHECKING:
    from src.utils.credentials import Credential


class WebSocketClient(WebSocketClientBase):
    def __init__(self, url: str, cred: "Credential" = cred):
        super().__init__(url, cred)
        self.code_stack: list[str] | str = []
        self.review_stack: list[str] | str = []
        self.is_code_review_finished = threading.Event()
        self.is_generate_code_finished = threading.Event()
        self.is_start_generate_code = threading.Event()
        self.is_error = False

    def success(self, data: message.SuccessMessage):
        pass

    def error(self, data: message.ErrorMessage):
        if data.code == "unsupported_task":
            click.echo(click.style("Unsupported task", fg="red"), err=True)
            click.echo(
                (
                    f"\nCurrent version of steev ({__version__}) does not support this task.\n"
                    "steev only supports huggingface TRL and unsloth training.\n"
                    "We will support more tasks. Please request at https://github.com/tbd-labs-ai/steev/issues\n"
                    "Read docs for more information:\n"
                    "  DOCS:\t "
                    + click.style("https://tbd-labs-ai.github.io/steev-docs/tutorials/overview/\n", fg="blue")
                ),
                err=True,
            )
            self.is_error = True
            self.is_code_review_finished.set()
        else:
            click.echo(click.style("Error", fg="red"), err=True)

    def alert(self, data: message.AlertMessage):
        pass

    def abort(self, data: message.AbortMessage):
        click.echo(click.style("Abort command by user", fg="red"), err=True)
        runner = get_runner()
        if runner:
            runner.terminate()

    def log_finish(self, data: message.FinishLogAnalysis):
        click.echo("Finish log analysis")
        self.log_finished.set()

    def code_chunk(self, data: message.CodeGenerateChunk):
        if not self.is_start_generate_code.is_set():
            self.is_start_generate_code.set()
        self.code_stack.append(data.chunk)  # type: ignore
        click.echo(data.chunk, nl=False)

    def code_finished(self, data: message.CodeGenerateFinished):
        self.is_generate_code_finished.set()

    def code_review_chunk(self, data: message.CodeReviewChunk):
        self.review_stack.append(data.chunk)  # type: ignore
        click.echo(data.chunk, nl=False)

    def code_review_finished(self, data: message.CodeReviewFinished):
        self.is_code_review_finished.set()

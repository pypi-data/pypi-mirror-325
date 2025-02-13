import sys
from types import TracebackType

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from rich.console import Console
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich.traceback import Traceback

from flock.core.logging.logger import flock_logger


class ErrorHandler:
    """Handles error formatting and display using Rich."""

    def __init__(self, console: Console | None = None):
        self.console = console or Console()

    def format_exception(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        exc_tb: TracebackType,
        *,
        show_locals: bool = True,
    ) -> Panel:
        """Format an exception with Rich styling."""
        # Create a Rich traceback
        rich_tb = Traceback.from_exception(
            exc_type,
            exc_value,
            exc_tb,
            show_locals=show_locals,
        )

        # If there's source code available, syntax highlight it
        if exc_tb and exc_tb.tb_frame.f_code.co_filename != "<string>":
            try:
                with open(exc_tb.tb_frame.f_code.co_filename) as f:
                    source = f.read()
                syntax = Syntax(
                    source,
                    "python",
                    line_numbers=True,
                    highlight_lines={exc_tb.tb_lineno},
                )
            except:
                syntax = None
        else:
            syntax = None

        # Create a panel with the traceback
        return Panel(
            rich_tb,
            title=f"[red]{exc_type.__name__}[/]: {exc_value!s}",
            border_style="red",
            padding=(1, 2),
        )

    def handle_exception(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException,
        exc_tb: TracebackType,
    ) -> None:
        """Handle an exception by formatting and displaying it."""
        panel = self.format_exception(exc_type, exc_value, exc_tb)
        self.console.print(panel)
        # Also log the error through our logger
        flock_logger.error(
            f"Exception occurred: {exc_type.__name__}: {exc_value!s}",
            error_type=exc_type.__name__,
            error_details=str(exc_value),
        )

    def install(self) -> None:
        """Install this error handler as the default exception handler."""
        sys.excepthook = self.handle_exception


# Global error handler instance
error_handler = ErrorHandler()

import time

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from rich.console import Console
    from rich.live import Live

from collections.abc import Callable, Generator
from contextlib import contextmanager
from functools import wraps
from typing import Any, TypeVar

from flock.core.logging.formatters import PerformanceFormatter, StructuredFormatter

T = TypeVar("T")


class PerformanceHandler:
    """Handles performance tracking and reporting."""

    def __init__(self, console: Console | None = None):
        self.console = console or Console()
        self.timings: dict[str, float] = {}
        self.enabled = False

    def enable(self):
        """Enable performance tracking."""
        self.enabled = True

    def disable(self):
        """Disable performance tracking."""
        self.enabled = False

    def _get_time(self) -> float:
        """Get current time in a workflow-safe way."""
        try:
            # Try to get workflow time first
            return workflow.now().timestamp()
        except workflow._NotInWorkflowEventLoopError:
            # Fall back to system time if not in workflow
            return time.time()

    @contextmanager
    def track_time(self, operation_name: str) -> Generator[None, None, None]:
        """Context manager for tracking operation execution time."""
        if not self.enabled:
            yield
            return

        start_time = self._get_time()
        try:
            yield
        finally:
            end_time = self._get_time()
            duration = end_time - start_time
            self.timings[operation_name] = duration

    def track_operation(self, operation_name: str) -> Callable[[Callable[..., T]], Callable[..., T]]:
        """Decorator for tracking function execution time."""

        def decorator(func: Callable[..., T]) -> Callable[..., T]:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> T:
                with self.track_time(operation_name):
                    return func(*args, **kwargs)

            return wrapper

        return decorator

    def display_timings(self) -> None:
        """Display all tracked timings in a tree format."""
        if self.timings:
            tree = PerformanceFormatter.create_timing_tree(self.timings)
            self.console.print(tree)

    def clear_timings(self) -> None:
        """Clear all tracked timings."""
        self.timings.clear()


class LiveUpdateHandler:
    """Handles live updates for long-running operations."""

    def __init__(self, console: Console | None = None):
        self.console = console or Console()

    @contextmanager
    def progress_tracker(self, description: str = "Progress") -> Generator[Any, None, None]:
        """Context manager for tracking progress with a live display."""
        progress = StructuredFormatter.create_progress_bar(description)
        with Live(progress, console=self.console, refresh_per_second=4) as live:
            task = progress.add_task(description, total=100)
            try:
                yield lambda p: progress.update(task, completed=p)
            finally:
                progress.update(task, completed=100)

    def update_workflow_status(
        self, workflow_id: str, status: str, details: dict[str, Any], refresh_per_second: int = 1
    ) -> Live:
        """Create a live updating workflow status panel."""
        panel = StructuredFormatter.create_workflow_panel(workflow_id, status, details)
        return Live(panel, console=self.console, refresh_per_second=refresh_per_second)

    def update_activity_status(
        self, activity_id: str, name: str, status: str, details: dict[str, Any], refresh_per_second: int = 1
    ) -> Live:
        """Create a live updating activity status panel."""
        panel = StructuredFormatter.create_activity_panel(activity_id, name, status, details)
        return Live(panel, console=self.console, refresh_per_second=refresh_per_second)


# Global instances for convenience
performance_handler = PerformanceHandler()
live_update_handler = LiveUpdateHandler()

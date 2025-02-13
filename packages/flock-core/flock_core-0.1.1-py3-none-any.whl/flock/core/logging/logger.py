from typing import Any

from temporalio import workflow

from flock.core.logging.formatters import AgentResultFormatter

with workflow.unsafe.imports_passed_through():
    from rich.console import Console
    from rich.theme import Theme

# Custom theme for different log levels
THEME = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "red",
    "debug": "grey50",
    "success": "green",
    "workflow": "blue",
    "activity": "magenta",
})


class LogLevel:
    NONE = 0  # No logging except errors
    MINIMAL = 1  # Only agent outputs
    BASIC = 2  # Agent outputs + basic workflow info
    VERBOSE = 3  # Everything including debug info


class FlockLogger:
    """Custom logger for Flock that integrates with Rich and respects Temporal constraints."""

    def __init__(self, name: str = "flock", console: Console | None = None, level: int = LogLevel.MINIMAL):
        self.name = name
        self.console = console or Console(theme=THEME)
        self._workflow_id: str | None = None
        self._activity_id: str | None = None
        self.level = level

    def set_level(self, level: int) -> None:
        """Set the logging level."""
        self.level = level

    def set_context(self, workflow_id: str | None = None, activity_id: str | None = None) -> None:
        """Set the current workflow and activity context."""
        self._workflow_id = workflow_id
        self._activity_id = activity_id

    def _format_message(self, level: str, message: str, **kwargs: Any) -> str:
        """Format log message with context but without timestamps (for Temporal compatibility)."""
        context_parts = []
        if self._workflow_id:
            context_parts.append(f"[workflow]workflow={self._workflow_id}[/]")
        if self._activity_id:
            context_parts.append(f"[activity]activity={self._activity_id}[/]")

        # Add any additional context from kwargs
        for key, value in kwargs.items():
            if key not in ("workflow_id", "activity_id"):
                context_parts.append(f"{key}={value}")

        context_str = " ".join(context_parts)
        return f"[{level}]{level.upper()}[/] {message} {context_str if context_str else ''}"

    def info(self, message: str, **kwargs: Any) -> None:
        """Log an info message."""
        if self.level >= LogLevel.BASIC:
            self.console.print(self._format_message("info", message, **kwargs))

    def warning(self, message: str, **kwargs: Any) -> None:
        """Log a warning message."""
        if self.level >= LogLevel.BASIC:
            self.console.print(self._format_message("warning", message, **kwargs))

    def error(self, message: str, **kwargs: Any) -> None:
        """Log an error message."""
        # Errors are always logged regardless of level
        self.console.print(self._format_message("error", message, **kwargs))

    def debug(self, message: str, **kwargs: Any) -> None:
        """Log a debug message."""
        if self.level >= LogLevel.VERBOSE:
            self.console.print(self._format_message("debug", message, **kwargs))

    def success(self, message: str, **kwargs: Any) -> None:
        """Log a success message."""
        if self.level >= LogLevel.BASIC:
            self.console.print(self._format_message("success", message, **kwargs))

    def workflow_event(self, message: str, **kwargs: Any) -> None:
        """Log a workflow-specific event."""
        if self.level >= LogLevel.BASIC:
            self.console.print(self._format_message("workflow", message, **kwargs))

    def activity_event(self, message: str, **kwargs: Any) -> None:
        """Log an activity-specific event."""
        if self.level >= LogLevel.BASIC:
            self.console.print(self._format_message("activity", message, **kwargs))

    def result(self, message: dict, agent_name, **kwargs: Any) -> None:
        """Log a result message."""
        if self.level >= LogLevel.MINIMAL:
            AgentResultFormatter.print_result(message, agent_name, self.console)


# Global logger instance with minimal logging by default
flock_logger = FlockLogger(level=LogLevel.MINIMAL)

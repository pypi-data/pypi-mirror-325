from typing import Any

from devtools import pprint
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
    from rich.table import Table


class StructuredFormatter:
    """Formats structured data for Rich output."""

    @staticmethod
    def create_status_table(data: dict[str, Any]) -> Table:
        """Create a Rich table for displaying status information."""
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Key")
        table.add_column("Value")

        for key, value in data.items():
            table.add_row(str(key), str(value))

        return table

    @staticmethod
    def create_progress_bar(description: str = "Progress") -> Progress:
        """Create a Rich progress bar with time tracking."""
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
        )

    @staticmethod
    def create_workflow_panel(
        workflow_id: str, status: str, details: dict[str, Any], title: str = "Workflow Status"
    ) -> Panel:
        """Create a Rich panel for workflow information."""
        table = StructuredFormatter.create_status_table({"Workflow ID": workflow_id, "Status": status, **details})
        return Panel(table, title=title, border_style="blue")

    @staticmethod
    def create_activity_panel(
        activity_id: str, name: str, status: str, details: dict[str, Any], title: str = "Activity Status"
    ) -> Panel:
        """Create a Rich panel for activity information."""
        table = StructuredFormatter.create_status_table(
            {"Activity ID": activity_id, "Name": name, "Status": status, **details}
        )
        return Panel(table, title=title, border_style="magenta")


class PerformanceFormatter:
    """Formats performance metrics for Rich output."""

    @staticmethod
    def create_timing_tree(timings: dict[str, float]) -> str:
        """Create a tree-like structure showing execution timings."""
        if not timings:
            return "No timings recorded"

        result = "Performance Metrics:\n"
        for operation, duration in timings.items():
            result += f"├── {operation}: {duration:.3f}s\n"
        return result[:-1]  # Remove trailing newline

    @staticmethod
    def create_performance_panel(metrics: dict[str, Any], title: str = "Performance Metrics") -> Panel:
        """Create a panel showing performance metrics."""
        table = StructuredFormatter.create_status_table(metrics)
        return Panel(table, title=title, border_style="cyan")


class AgentResultFormatter:
    """Formats agent results in a beautiful Rich table."""

    @staticmethod
    def format_result(result: dict[str, Any], agent_name: str) -> Panel:
        """Format an agent's result as a Rich panel containing a table."""
        # Create a table with a nice header
        table = Table(
            show_header=True,
            header_style="bold green",
            title=f"Agent Results: {agent_name}",
            title_style="bold blue",
            border_style="bright_blue",
        )
        table.add_column("Output", style="cyan")
        table.add_column("Value", style="green")

        # Add each result to the table
        for key, value in result.items():
            # Format multi-line values (like blog headers) nicely
            if isinstance(value, (list, tuple)) or (isinstance(value, str) and "\n" in value):
                formatted_value = "\n".join(value) if isinstance(value, (list, tuple)) else value
                # Add some padding for multi-line values
                table.add_row(key, f"\n{formatted_value}\n")
            else:
                table.add_row(key, str(value))

        pprint(result)

        # Wrap the table in a panel for a nice border
        return Panel(
            table,
            title="🎯 Agent Output",
            title_align="left",
            border_style="blue",
            padding=(1, 2),
        )

    @staticmethod
    def print_result(result: dict[str, Any], agent_name: str, console: Console | None = None) -> None:
        """Print an agent's result using Rich formatting."""
        console = console or Console()
        panel = AgentResultFormatter.format_result(result, agent_name)
        console.print(panel)

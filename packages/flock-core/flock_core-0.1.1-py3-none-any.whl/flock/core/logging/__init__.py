"""Flock logging system with Rich integration and Temporal compatibility."""

from flock.core.logging.error_handler import error_handler
from flock.core.logging.formatters import PerformanceFormatter, StructuredFormatter
from flock.core.logging.handlers import live_update_handler, performance_handler
from flock.core.logging.logger import flock_logger

# Install the Rich error handler by default
error_handler.install()

__all__ = [
    "PerformanceFormatter",
    "StructuredFormatter",
    "error_handler",
    "flock_logger",
    "live_update_handler",
    "performance_handler",
]

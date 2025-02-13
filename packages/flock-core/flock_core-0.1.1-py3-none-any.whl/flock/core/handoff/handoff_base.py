from typing import Any

from flock.core.agent import Agent
from flock.core.context import FlockContext


class HandoffBase:
    """Base class for handoff implementations."""

    next_agent: str | Agent
    input: dict[str, Any]
    context: FlockContext

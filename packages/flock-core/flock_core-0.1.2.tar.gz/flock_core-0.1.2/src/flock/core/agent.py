from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Literal, TypeVar

import cloudpickle
from pydantic import BaseModel, Field

from flock.core.context import FlockContext
from flock.core.logging import flock_logger, live_update_handler, performance_handler
from flock.core.serializable import Serializable

T = TypeVar("T", bound="Agent")


@dataclass
class AgentConfig:
    save_to_file: bool = False
    data_type: Literal["json", "cloudpickle", "msgpack"] = "cloudpickle"


class Agent(Serializable, BaseModel, ABC):
    """Base class for all agents in the framework.

    Attributes:
      - name: A unique identifier for the agent.
      - model: The model identifier (e.g., an LLM specification).
      - description: A human‑readable description of the agent.
      - hand_off: Defines the next agent to invoke (can be a string or callable).
      - termination: (Optional) A termination condition or phrase; can be used in lifecycle hooks.

    Lifecycle Hooks:
      - initialize(): Called before the agent runs.
      - terminate(): Called after the agent finishes running.

    Temporal Execution:
      The default run_temporal() method serializes the agent and the current FlockContext
      and calls a Temporal activity (run_agent_activity) to perform the execution in a Temporal worker.
      Subclasses may override run_temporal() if custom behavior is required.
    """

    name: str = Field(description="Identifier name for the agent")
    model: str = Field(default="", description="Model of the agent")
    description: str | Callable[..., str] = Field(default="", description="Description of the agent")
    # Use a default factory for hand_off so it defaults to an empty list.
    hand_off: list[str | Callable[..., Any]] = Field(default_factory=list, description="Handoff to another agent")
    termination: str | None = Field(default=None, description="Optional termination condition or phrase")

    def register(self, registry) -> None:
        """Register this agent with the provided registry."""
        registry.register_agent(self)

    @abstractmethod
    async def run(self, context: FlockContext) -> dict:
        """Execute the agent's logic locally.

        This method must be implemented by each concrete agent.
        """
        pass

    async def run_temporal(self, context: FlockContext) -> dict:
        """Execute the agent's logic via Temporal."""
        # Run initialization tasks
        await self.initialize(context)

        from temporalio.client import Client

        from flock.workflow.agent_activities import run_agent_activity
        from flock.workflow.temporal_setup import run_activity

        try:
            with performance_handler.track_time("temporal_connection"):
                flock_logger.info("Connecting to Temporal service...")
                client = await Client.connect("localhost:7233", namespace="default")

            # Convert the FlockContext to a serializable dictionary
            context_data = {
                "state": context.state,
                "history": [record.__dict__ for record in context.history],
                "agent_definitions": [definition.__dict__ for definition in context.agent_definitions],
            }
            agent_data = self.dict()

            # Execute the Temporal activity
            with performance_handler.track_time("temporal_execution"):
                with live_update_handler.update_workflow_status(self.name, "Running", {"phase": "temporal_activity"}):
                    result = await run_activity(
                        client,
                        self.name,
                        run_agent_activity,
                        {"agent_data": agent_data, "context_data": context_data},
                    )

            flock_logger.success(f"Temporal activity completed: {self.name}")
            return result

        except Exception as e:
            flock_logger.error(f"Temporal execution failed: {e}", agent=self.name)
            raise
        finally:
            await self.terminate(context)

    async def initialize(self, context: FlockContext) -> None:
        """Lifecycle hook for agent initialization."""
        flock_logger.set_context(workflow_id=context.state.get("workflow_id"))
        flock_logger.info(f"Initializing agent: {self.name}")
        flock_logger.debug("Agent configuration", config=self.dict())
        flock_logger.debug("Context state", state=context.state)

    async def terminate(self, context: FlockContext) -> None:
        """Lifecycle hook for agent termination."""
        if self.termination and context.get_variable("init_input") == self.termination:
            flock_logger.warning(
                "Termination condition met",
                condition=self.termination,
                input=context.get_variable("init_input"),
            )
        flock_logger.info(f"Terminating agent: {self.name}")

    def to_dict(self) -> dict[str, Any]:
        def convert_callable(obj):
            if callable(obj) and not isinstance(obj, type):
                return cloudpickle.dumps(obj).hex()  # Serialize functions to hex string
            if isinstance(obj, list):
                return [convert_callable(x) for x in obj]
            if isinstance(obj, dict):
                return {k: convert_callable(v) for k, v in obj.items()}
            return obj

        # Use Pydantic's model_dump and handle callables
        return convert_callable(self.model_dump())

    @classmethod
    def from_dict(cls: type[T], data: dict[str, Any]) -> T:
        def convert_callable(obj):
            if isinstance(obj, str) and len(obj) > 2:
                try:
                    # Try to deserialize hex string back to callable
                    return cloudpickle.loads(bytes.fromhex(obj))
                except:
                    return obj
            if isinstance(obj, list):
                return [convert_callable(x) for x in obj]
            if isinstance(obj, dict):
                return {k: convert_callable(v) for k, v in obj.items()}
            return obj

        # Convert callable strings back to functions
        converted = convert_callable(data)
        return cls(**converted)

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Literal

from flock.core.context_vars import FLOCK_LAST_AGENT, FLOCK_LAST_RESULT
from flock.core.logging import flock_logger, performance_handler
from flock.core.serializable import Serializable


@dataclass
class AgentRunRecord:
    agent: str = field(default="")  # Agent name
    input_data: dict[str, Any] = field(default_factory=dict)
    output_data: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default="")
    hand_off: str = field(default="")  # Next agent name


@dataclass
class AgentDefinition:
    agent_type: str = field(default="")
    agent_name: str = field(default="")
    agent_data: dict = field(default=dict)
    serializer: Literal["json", "cloudpickle", "msgpack"] = field(default="cloudpickle")


@dataclass
class FlockContext(Serializable):
    state: dict[str, Any] = field(default_factory=dict)
    history: list[AgentRunRecord] = field(default_factory=list)
    agent_definitions: dict[str, AgentDefinition] = field(default_factory=dict)
    run_id: str = field(default="")
    workflow_id: str = field(default="")
    workflow_timestamp: str = field(default="")

    def record(self, agent_name: str, data: dict[str, Any], timestamp: str, hand_off: str) -> None:
        """Record an agent run and update the state with the agent's output."""
        try:
            with performance_handler.track_time("record_agent_run"):
                flock_logger.info(f"Recording agent run: {agent_name}")
                record = AgentRunRecord(
                    agent=agent_name, output_data=data.copy(), timestamp=timestamp, hand_off=hand_off
                )
                self.history.append(record)
                flock_logger.debug(
                    "Created run record",
                    agent=agent_name,
                    output_keys=list(data.keys()),
                )

                self.set_variable(f"{agent_name}.result", data)
                self.set_variable(FLOCK_LAST_RESULT, data)
                self.set_variable(FLOCK_LAST_AGENT, agent_name)
                flock_logger.debug("Updated context state with agent output")

        except Exception as e:
            flock_logger.error(
                "Failed to record agent run",
                agent=agent_name,
                error=str(e),
            )
            raise

    def get_variable(self, key: str) -> Any:
        """Get the current value of a state variable."""
        try:
            with performance_handler.track_time("get_variable"):
                value = self.state.get(key)
                if value is None:
                    flock_logger.warning(f"Variable not found in state: {key}")
                else:
                    flock_logger.debug(f"Retrieved variable: {key}")
                return value
        except Exception as e:
            flock_logger.error(
                "Failed to get variable",
                key=key,
                error=str(e),
            )
            raise

    def set_variable(self, key: str, value: Any) -> None:
        """Set the value of a state variable."""
        try:
            with performance_handler.track_time("set_variable"):
                self.state[key] = value
                flock_logger.debug(f"Set variable: {key}")
        except Exception as e:
            flock_logger.error(
                "Failed to set variable",
                key=key,
                error=str(e),
            )
            raise

    def deepcopy(self) -> "FlockContext":
        """Create a deep copy of the context."""
        try:
            with performance_handler.track_time("context_deepcopy"):
                flock_logger.debug("Creating deep copy of context")
                copy = FlockContext.from_dict(self.to_dict())
                flock_logger.debug(
                    "Context copied",
                    state_vars=len(copy.state),
                    history_records=len(copy.history),
                )
                return copy
        except Exception as e:
            flock_logger.error(
                "Failed to create context copy",
                error=str(e),
            )
            raise

    def get_agent_history(self, agent_name: str) -> list[AgentRunRecord]:
        """Return all agent run records for a given agent name."""
        try:
            with performance_handler.track_time("get_agent_history"):
                records = [record for record in self.history if record.agent == agent_name]
                flock_logger.debug(
                    f"Retrieved history records for {agent_name}",
                    count=len(records),
                )
                return records
        except Exception as e:
            flock_logger.error(
                "Failed to get history records",
                agent=agent_name,
                error=str(e),
            )
            raise

    def next_input_for(self, agent) -> Any:
        """By default, the next input for an agent is taken from the context state.

        If the agent.input is a comma-separated list (e.g., "input1, input2"),
        this method will return a dictionary with keys for each of the input names,
        fetching the latest values from the state.

        If only a single input is specified, the raw value is returned.
        """
        try:
            with performance_handler.track_time("next_input_preparation"):
                flock_logger.info(f"Preparing next input for agent: {agent.name}")

                if hasattr(agent, "input") and isinstance(agent.input, str):
                    keys = [k.strip() for k in agent.input.split(",") if k.strip()]
                    flock_logger.debug(f"Input keys: {keys}")

                    if len(keys) == 1:
                        value = self.get_variable(keys[0])
                        flock_logger.debug(f"Single input value retrieved for key: {keys[0]}")
                        return value
                    else:
                        values = {key: self.get_variable(key) for key in keys}
                        flock_logger.debug(f"Multiple input values retrieved for keys: {keys}")
                        return values
                else:
                    # Fallback to "init_input"
                    flock_logger.debug("No input defined, falling back to init_input")
                    return self.get_variable("init_input")
        except Exception as e:
            flock_logger.error(
                "Failed to prepare next input",
                agent=getattr(agent, "name", str(agent)),
                error=str(e),
            )
            raise

    def get_agent_definition(self, agent_name: str) -> AgentDefinition | None:
        """Get the definition for a specific agent."""
        try:
            with performance_handler.track_time("get_agent_definition"):
                for definition in self.agent_definitions:
                    if definition.name == agent_name:
                        flock_logger.debug(f"Retrieved definition for agent: {agent_name}")
                        return definition

                flock_logger.warning(f"No definition found for agent: {agent_name}")
                return None
        except Exception as e:
            flock_logger.error(
                "Failed to get agent definition",
                agent=agent_name,
                error=str(e),
            )
            raise

    def add_agent_definition(self, agent_type: type, agent_name: str, agent_data: Any) -> None:
        """Add a new agent definition to the context."""
        try:
            with performance_handler.track_time("add_agent_definition"):
                definition = AgentDefinition(
                    agent_type=agent_type.__name__,
                    agent_name=agent_name,
                    agent_data=agent_data,
                )
                self.agent_definitions[agent_name] = definition
                flock_logger.info(
                    f"Added agent definition",
                    agent=agent_name,
                    type=agent_type.__name__,
                )
        except Exception as e:
            flock_logger.error(
                "Failed to add agent definition",
                agent=agent_name,
                type=agent_type.__name__,
                error=str(e),
            )
            raise

    # Allow dict-like access for convenience.
    def __getitem__(self, key: str) -> Any:
        value = self.state[key]
        return value

    def __setitem__(self, key: str, value: Any) -> None:
        self.state[key] = value

    def to_dict(self) -> dict[str, Any]:
        """Convert the context to a dictionary for serialization."""
        try:
            with performance_handler.track_time("context_to_dict"):
                flock_logger.debug("Converting context to dictionary")

                def convert(obj):
                    if isinstance(obj, datetime):
                        return obj.isoformat()
                    if hasattr(obj, "__dataclass_fields__"):  # Is a dataclass
                        return asdict(obj, dict_factory=lambda x: {k: convert(v) for k, v in x})
                    return obj

                result = convert(asdict(self))
                flock_logger.debug(
                    "Context converted to dictionary",
                    state_size=len(result.get("state", {})),
                    history_size=len(result.get("history", [])),
                )
                return result
        except Exception as e:
            flock_logger.error(
                "Failed to convert context to dictionary",
                error=str(e),
            )
            raise

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "FlockContext":
        """Create a context instance from a dictionary."""
        try:
            with performance_handler.track_time("context_from_dict"):
                flock_logger.debug("Creating context from dictionary")

                def convert(obj):
                    if isinstance(obj, dict):
                        if "timestamp" in obj:  # AgentRunRecord
                            return AgentRunRecord(**{**obj, "timestamp": datetime.fromisoformat(obj["timestamp"])})
                        if "agent_type" in obj:  # AgentDefinition
                            return AgentDefinition(**obj)
                        return {k: convert(v) for k, v in obj.items()}
                    if isinstance(obj, list):
                        return [convert(v) for v in obj]
                    return obj

                converted = convert(data)
                context = cls(**converted)
                flock_logger.debug(
                    "Created context from dictionary",
                    state_vars=len(context.state),
                    history_records=len(context.history),
                )
                return context
        except Exception as e:
            flock_logger.error(
                "Failed to create context from dictionary",
                error=str(e),
            )
            raise

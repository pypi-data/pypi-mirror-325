from collections.abc import Callable

from flock.core.agent import Agent
from flock.core.logging import flock_logger, performance_handler


class Registry:
    """Registry for storing and managing agents and tools.

    This singleton class maintains a centralized registry of agents and tools,
    which is particularly important for Temporal workflows where only basic Python
    types can be passed between activities.
    """

    _instance = None

    def __new__(cls):
        """Singleton pattern implementation."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            with performance_handler.track_time("registry_initialization"):
                flock_logger.info("Initializing new Registry instance")
                cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize the registry's storage."""
        self._agents: list[Agent] = []
        self._tools: list[tuple[str, Callable]] = []
        flock_logger.debug("Registry storage initialized")

    def register_tool(self, tool_name: str, tool: Callable) -> None:
        """Register a tool with the registry.

        Args:
            tool_name: The name to register the tool under
            tool: The tool function to register
        """
        try:
            with performance_handler.track_time("tool_registration"):
                self._tools.append((tool_name, tool))
                flock_logger.info(f"Registered tool: {tool_name}")
                flock_logger.debug("Tool details", tool_name=tool_name, tool_type=type(tool).__name__)
        except Exception as e:
            flock_logger.error(
                "Tool registration failed",
                tool_name=tool_name,
                error=str(e),
            )
            raise

    def register_agent(self, agent: Agent) -> None:
        """Register an agent with the registry.

        Args:
            agent: The agent instance to register
        """
        try:
            with performance_handler.track_time("agent_registration"):
                self._agents.append(agent)
                flock_logger.info(f"Registered agent: {agent.name}")
                flock_logger.debug(
                    "Agent details",
                    name=agent.name,
                    type=type(agent).__name__,
                    model=agent.model,
                )
        except Exception as e:
            flock_logger.error(
                "Agent registration failed",
                agent_name=getattr(agent, "name", "unknown"),
                error=str(e),
            )
            raise

    def get_agent(self, name: str) -> Agent | None:
        """Retrieve an agent by name.

        Args:
            name: The name of the agent to retrieve

        Returns:
            The agent instance if found, None otherwise
        """
        try:
            with performance_handler.track_time("agent_retrieval"):
                for agent in self._agents:
                    if agent.name == name:
                        flock_logger.debug(f"Retrieved agent: {name}")
                        return agent

                flock_logger.warning(f"Agent not found: {name}")
                return None
        except Exception as e:
            flock_logger.error(
                "Agent retrieval failed",
                agent_name=name,
                error=str(e),
            )
            raise

    def get_tool(self, name: str) -> Callable | None:
        """Retrieve a tool by name.

        Args:
            name: The name of the tool to retrieve

        Returns:
            The tool function if found, None otherwise
        """
        try:
            with performance_handler.track_time("tool_retrieval"):
                for tool_name, tool in self._tools:
                    if tool_name == name:
                        flock_logger.debug(f"Retrieved tool: {name}")
                        return tool

                flock_logger.warning(f"Tool not found: {name}")
                return None
        except Exception as e:
            flock_logger.error(
                "Tool retrieval failed",
                tool_name=name,
                error=str(e),
            )
            raise

    def get_tools(self, names: list[str] | None) -> list[Callable]:
        """Retrieve multiple tools by name.

        Args:
            names: List of tool names to retrieve

        Returns:
            List of found tool functions (may be empty if none found)
        """
        try:
            with performance_handler.track_time("tools_retrieval"):
                if not names:
                    flock_logger.debug("No tool names provided")
                    return []

                tools = [self.get_tool(name) for name in names]
                found_tools = [name for name, tool in zip(names, tools) if tool is not None]

                if found_tools:
                    flock_logger.debug(
                        "Retrieved tools",
                        requested=len(names),
                        found=len(found_tools),
                    )
                    return [tool for tool in tools if tool is not None]

                flock_logger.warning("No tools found", requested=names)
                return []
        except Exception as e:
            flock_logger.error(
                "Tools retrieval failed",
                tool_names=names,
                error=str(e),
            )
            raise

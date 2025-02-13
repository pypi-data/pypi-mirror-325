# src/your_package/core/manager.py
import contextlib
import os
import uuid
from typing import TypeVar

from flock.core.agent_registry import Registry
from flock.core.context import FlockContext
from flock.core.context_vars import FLOCK_CURRENT_AGENT, FLOCK_INITIAL_INPUT, FLOCK_LOCAL_DEBUG, FLOCK_RUN_ID
from flock.core.logging import flock_logger, performance_handler
from flock.core.logging.formatters import AgentResultFormatter
from flock.core.logging.logger import FlockLogger, LogLevel
from flock.workflow.activities import run_agent
from flock.workflow.temporal_setup import create_temporal_client, setup_worker
from flock.workflow.workflow import FlockWorkflow

from .agent import Agent

T = TypeVar("T", bound=Agent)


class Flock:
    """Manages creation and execution of agents.
    This is a high-level class that the user interacts with directly.
    """

    def __init__(
        self,
        model: str = "openai/gpt-4o",
        log_level: int = LogLevel.MINIMAL,
        enable_performance_tracking: bool = False,
        local_debug: bool = False,
    ):
        """Initialize the Flock.

        Args:
            model: The default model to use for agents.
            log_level: The logging verbosity level:
                - LogLevel.NONE: No logging except errors
                - LogLevel.MINIMAL: Only agent outputs (default)
                - LogLevel.BASIC: Agent outputs + basic workflow info
                - LogLevel.VERBOSE: Everything including debug info
            log_format: The logging format to use:
                - LogFormat.SIMPLE: Simple message format (default)
                - LogFormat.STRUCTURED: Table-like structured format
            enable_performance_tracking: Whether to track and display performance metrics.
            local_debug: Whether to run in local debug mode (default: False).
        """
        self.agents: dict[str, Agent] = {}
        self.registry = Registry()
        self.context = FlockContext()
        self.model = model
        self.enable_performance_tracking = enable_performance_tracking
        self.local_debug = local_debug

        # Configure performance tracking
        if enable_performance_tracking:
            performance_handler.enable()
        else:
            performance_handler.disable()

        # Set LOCAL_DEBUG environment variable for console detection
        if local_debug:
            os.environ["LOCAL_DEBUG"] = "1"
        elif "LOCAL_DEBUG" in os.environ:
            del os.environ["LOCAL_DEBUG"]

        # Configure logging
        global flock_logger
        flock_logger = FlockLogger(level=log_level)
        flock_logger.info("Initialized Flock", model=model, local_debug=local_debug)

    def add_agent(self, agent: T) -> T:
        if not agent.model:
            agent.model = self.model

        if agent.name in self.agents:
            flock_logger.debug(f"Agent {agent.name} already exists, returning existing instance")
            return self.agents[agent.name]

        self.agents[agent.name] = agent
        self.registry.register_agent(agent)
        self.context.add_agent_definition(type(agent), agent.name, agent.to_dict())
        if hasattr(agent, "tools") and agent.tools:
            for tool in agent.tools:
                self.registry.register_tool(tool.__name__, tool)
                flock_logger.debug(f"Registered tool: {tool.__name__}")

        flock_logger.info(f"Added agent: {agent.name}", model=agent.model)
        return agent

    def add_tool(self, tool_name: str, tool: callable):
        self.registry.register_tool(tool_name, tool)
        flock_logger.debug(f"Registered tool: {tool_name}")

    async def _run_local_debug_workflow(self, box_result: bool = True):
        if self.enable_performance_tracking:
            perf_context = performance_handler.track_time("local_workflow")
        else:
            perf_context = contextlib.nullcontext()

        with perf_context:
            flock_logger.info("Running workflow in local debug mode")
            result = await run_agent(self.context)

            # Format and display the result (always shown regardless of log level)
            agent_name = self.context.get_variable(FLOCK_CURRENT_AGENT)
            AgentResultFormatter.print_result(result, agent_name)

            if self.enable_performance_tracking:
                performance_handler.display_timings()

            if box_result:
                from box import Box

                flock_logger.debug("Boxing result")
                return Box(result)
            return result

    async def _run_temporal_workflow(self, box_result: bool = True):
        if self.enable_performance_tracking:
            perf_context = performance_handler.track_time("temporal_workflow")
        else:
            perf_context = contextlib.nullcontext()

        with perf_context:
            flock_logger.info("Connecting to Temporal and starting worker...")

            await setup_worker(workflow=FlockWorkflow, activity=run_agent)

            flock_logger.info("Starting workflow execution")

            flock_client = await create_temporal_client()
            result = await flock_client.execute_workflow(
                FlockWorkflow.run,
                self.context.to_dict(),
                id=self.context.get_variable(FLOCK_RUN_ID),
                task_queue="flock-queue",
            )

            # Format and display the result (always shown regardless of log level)
            agent_name = self.context.get_variable(FLOCK_CURRENT_AGENT)
            flock_logger.result(result, agent_name)

            if self.enable_performance_tracking:
                performance_handler.display_timings()

            if box_result:
                from box import Box

                flock_logger.debug("Boxing result")
                return Box(result)
            return result

    async def run_async(
        self,
        start_agent: Agent | str,
        input: str,
        context: FlockContext = None,
        run_id: str = "",
        box_result: bool = True,
    ) -> dict:
        """Entry point for running an agent system."""
        try:
            if self.enable_performance_tracking:
                perf_context = performance_handler.track_time("run_setup")
            else:
                perf_context = contextlib.nullcontext()

            with perf_context:
                if isinstance(start_agent, str):
                    flock_logger.debug(f"Looking up agent by name: {start_agent}")
                    start_agent = self.registry.get_agent(start_agent)
                    if not start_agent:
                        raise ValueError(f"Agent '{start_agent}' not found in registry")

                if context:
                    flock_logger.debug("Using provided context")
                    self.context = context

                flock_logger.info("Setting up run context", agent=start_agent.name, input=input)
                self.context.set_variable(FLOCK_CURRENT_AGENT, start_agent.name)
                self.context.set_variable(FLOCK_INITIAL_INPUT, input)
                self.context.set_variable(FLOCK_LOCAL_DEBUG, self.local_debug)

                if not run_id:
                    run_id = start_agent.name + "_" + uuid.uuid4().hex[:4]
                    flock_logger.debug(f"Generated run ID: {run_id}")

                self.context.set_variable(FLOCK_RUN_ID, run_id)

            if self.enable_performance_tracking:
                performance_handler.display_timings()

            # we can run the flow locally for debugging purposes
            if self.local_debug:
                return await self._run_local_debug_workflow(box_result)
            else:
                return await self._run_temporal_workflow(box_result)

        except Exception as e:
            flock_logger.error(
                "Run failed",
                error=str(e),
                agent=getattr(start_agent, "name", str(start_agent)),
                input=input,
            )
            raise

from collections.abc import Callable
from typing import Any

from pydantic import Field
from temporalio import activity

from flock.core.agent import Agent
from flock.core.context import FlockContext
from flock.core.logging import flock_logger, live_update_handler, performance_handler


@activity.defn
async def run_user_agent_activity(context: dict[str, Any]) -> dict[str, Any]:
    """Temporal activity to process a user agent task.

    Expects context to contain:
      - "model": the model name
      - "agent_input": the key used for the input
      - "output": the agent output specification
      - "init_input": the initial input
      - "tools": (optional) list of tools
    """
    try:
        import dspy

        flock_logger.info("Starting user agent activity", context=context)

        with performance_handler.track_time("model_configuration"):
            model = context.get("model")
            agent_input = context.get("agent_input")
            output = context.get("output")
            init_input = context.get("init_input")
            tools = context.get("tools")

            flock_logger.debug(
                "Configuring model",
                model=model,
                input=agent_input,
                output=output,
            )

            lm = dspy.LM(model)
            dspy.configure(lm=lm)

        with performance_handler.track_time("task_execution"):
            if tools:
                flock_logger.info("Creating ReAct task with tools", num_tools=len(tools))
                agent_task = dspy.ReAct(f"{agent_input} -> {output}", tools=tools)
            else:
                flock_logger.info("Creating Predict task")
                agent_task = dspy.Predict(f"{agent_input} -> {output}")

            kwargs = {agent_input: init_input}
            flock_logger.info("Executing task", kwargs=kwargs)
            result = agent_task(**kwargs).toDict()
            result[agent_input] = init_input

            flock_logger.success("Task completed successfully")
            return result

    except Exception as e:
        flock_logger.error(
            "User agent activity failed",
            error=str(e),
            context=context,
        )
        raise


class UserAgent(Agent):
    """An agent that evaluates declarative inputs with user interaction capabilities.

    This agent extends the base Agent class with the ability to interact with users
    during execution, while maintaining compatibility with both local and Temporal
    execution modes.

    Attributes:
        input: Input domain for the agent
        output: Output types for the agent
        tools: Tools the agent is allowed to use
        require_confirmation: Whether to require user confirmation before proceeding
    """

    input: str = Field(default="", description="Input domain for the agent")
    output: str = Field(default="", description="Output types for the agent")
    tools: list[Callable] | None = Field(default=None, description="Tools the agent is allowed to use")
    require_confirmation: bool = Field(default=False, description="Whether to require user confirmation")

    async def _configure_model(self) -> tuple[Any, Any]:
        """Configure the model and create the appropriate task."""
        try:
            with performance_handler.track_time("model_configuration"):
                import dspy

                flock_logger.debug(
                    "Configuring model",
                    model=self.model,
                    input=self.input,
                    output=self.output,
                )

                lm = dspy.LM(self.model)
                dspy.configure(lm=lm)

                if self.tools:
                    flock_logger.info("Creating ReAct task with tools", num_tools=len(self.tools))
                    agent_task = dspy.ReAct(f"{self.input} -> {self.output}", tools=self.tools)
                else:
                    flock_logger.info("Creating Predict task")
                    agent_task = dspy.Predict(f"{self.input} -> {self.output}")

                return lm, agent_task

        except Exception as e:
            flock_logger.error(
                "Model configuration failed",
                error=str(e),
                agent=self.name,
            )
            raise

    async def _execute_task(self, task: Any, context: FlockContext) -> dict[str, Any]:
        """Execute the configured task."""
        try:
            with performance_handler.track_time("task_execution"):
                kwargs = {self.input: context.get_variable("init_input")}
                flock_logger.info("Executing task", kwargs=kwargs)

                with live_update_handler.update_activity_status(
                    self.name,
                    "Executing Task",
                    "Running",
                    {"input": kwargs},
                ):
                    result = task(**kwargs).toDict()
                    result[self.input] = kwargs[self.input]

                flock_logger.success("Task executed successfully")
                return result

        except Exception as e:
            flock_logger.error(
                "Task execution failed",
                error=str(e),
                agent=self.name,
                kwargs=kwargs,
            )
            raise

    async def run(self, context: FlockContext) -> dict[str, Any]:
        """Run the agent on a task with optional user interaction."""
        try:
            flock_logger.info(f"Starting user agent: {self.name}")

            # Configure model and task
            _, task = await self._configure_model()

            # Execute with user confirmation if required
            if self.require_confirmation:
                with live_update_handler.update_activity_status(
                    self.name,
                    "Awaiting User Confirmation",
                    "Paused",
                    {"agent": self.name},
                ):
                    flock_logger.info("Waiting for user confirmation")
                    # Here you would implement user confirmation logic
                    # For now, we'll just proceed
                    pass

            # Execute the task
            result = await self._execute_task(task, context)
            return result

        except Exception as e:
            flock_logger.error(
                "User agent execution failed",
                error=str(e),
                agent=self.name,
            )
            raise

    async def run_temporal(self, context: FlockContext) -> dict[str, Any]:
        """Run the user agent via Temporal."""
        try:
            from temporalio.client import Client

            from flock.workflow.temporal_setup import run_activity

            with performance_handler.track_time("temporal_setup"):
                flock_logger.info(f"Starting temporal user agent: {self.name}")
                client = await Client.connect("localhost:7233", namespace="default")

                # Prepare context for temporal activity
                activity_context = {
                    "model": self.model,
                    "agent_input": self.input,
                    "output": self.output,
                    "init_input": context.get_variable("init_input"),
                    "tools": self.tools,
                }

            with live_update_handler.update_workflow_status(
                self.name,
                "Running",
                {"phase": "user_agent_execution"},
            ):
                # Execute the activity
                with performance_handler.track_time("temporal_execution"):
                    flock_logger.info("Starting user agent activity")
                    result = await run_activity(
                        client,
                        self.name,
                        run_user_agent_activity,
                        activity_context,
                    )

                flock_logger.success(
                    "Temporal user agent completed successfully",
                    agent=self.name,
                )
                return result

        except Exception as e:
            flock_logger.error(
                "Temporal user agent execution failed",
                error=str(e),
                agent=self.name,
            )
            raise

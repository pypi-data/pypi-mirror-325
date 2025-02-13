from collections.abc import Callable
from typing import Any

from pydantic import Field

from flock.core.agent import Agent
from flock.core.context import FlockContext
from flock.core.logging import flock_logger, live_update_handler, performance_handler


class TriggerAgent(Agent):
    """An agent that executes based on specific triggers/conditions.

    Attributes:
        input: Input domain for the agent
        output: Output types for the agent
        tools: Tools the agent is allowed to use
        trigger_condition: Callable that evaluates whether the agent should execute
        trigger_check_interval: How often to check the trigger condition (in seconds)
        max_wait_time: Maximum time to wait for trigger (in seconds)
    """

    input: str = Field(default="", description="Input domain for the agent")
    output: str = Field(default="", description="Output types for the agent")
    tools: list[Callable] | None = Field(default=None, description="Tools the agent is allowed to use")
    trigger_condition: Callable[[dict[str, Any]], bool] = Field(
        ..., description="Function that evaluates trigger conditions"
    )
    trigger_check_interval: float = Field(default=1.0, description="Interval between trigger checks (seconds)")
    max_wait_time: float = Field(default=60.0, description="Maximum time to wait for trigger (seconds)")

    async def _evaluate_trigger(self, context: FlockContext) -> bool:
        """Evaluate the trigger condition."""
        try:
            with performance_handler.track_time("trigger_evaluation"):
                flock_logger.debug("Evaluating trigger condition", agent=self.name)
                result = self.trigger_condition(context.state)
                flock_logger.debug(
                    "Trigger evaluation result",
                    triggered=result,
                    agent=self.name,
                )
                return result
        except Exception as e:
            flock_logger.error(
                "Trigger evaluation failed",
                error=str(e),
                agent=self.name,
            )
            raise

    async def _execute_action(self, context: FlockContext) -> dict[str, Any]:
        """Execute the agent's action once triggered."""
        try:
            with performance_handler.track_time("action_execution"):
                flock_logger.info("Executing triggered action", agent=self.name)
                # Here you would implement the actual action logic
                # For now, we'll just return a simple result
                result = {"status": "completed", "trigger_time": context.state.get("current_time")}
                flock_logger.success("Action executed successfully", agent=self.name)
                return result
        except Exception as e:
            flock_logger.error(
                "Action execution failed",
                error=str(e),
                agent=self.name,
            )
            raise

    async def run(self, context: FlockContext) -> dict[str, Any]:
        """Run the agent, waiting for and responding to triggers."""
        import asyncio
        import time

        try:
            flock_logger.info(f"Starting trigger agent: {self.name}")
            start_time = time.time()
            triggered = False

            with live_update_handler.progress_tracker("Waiting for trigger") as update_progress:
                while (time.time() - start_time) < self.max_wait_time:
                    # Update progress based on elapsed time
                    elapsed = time.time() - start_time
                    progress = min(elapsed * 100 / self.max_wait_time, 100)
                    update_progress(progress)

                    # Check trigger with status tracking
                    with live_update_handler.update_activity_status(
                        self.name,
                        "Checking Trigger",
                        "Running",
                        {
                            "elapsed_time": f"{elapsed:.1f}s",
                            "max_wait_time": f"{self.max_wait_time:.1f}s",
                        },
                    ):
                        if await self._evaluate_trigger(context):
                            triggered = True
                            break

                    await asyncio.sleep(self.trigger_check_interval)

                if not triggered:
                    flock_logger.warning(
                        "Trigger timeout reached",
                        max_wait_time=self.max_wait_time,
                        agent=self.name,
                    )
                    return {"error": "Trigger timeout", "max_wait_time": self.max_wait_time}

                # Execute action when triggered
                result = await self._execute_action(context)
                return result

        except Exception as e:
            flock_logger.error(
                "Trigger agent execution failed",
                error=str(e),
                agent=self.name,
            )
            raise

    async def run_temporal(self, context: FlockContext) -> dict[str, Any]:
        """Run the trigger agent via Temporal."""
        try:
            from temporalio.client import Client

            from flock.workflow.agent_activities import run_agent_activity
            from flock.workflow.temporal_setup import run_activity

            with performance_handler.track_time("temporal_setup"):
                flock_logger.info(f"Starting temporal trigger agent: {self.name}")
                client = await Client.connect("localhost:7233", namespace="default")

            with live_update_handler.update_workflow_status(
                self.name,
                "Running",
                {
                    "phase": "trigger_monitoring",
                    "check_interval": self.trigger_check_interval,
                    "max_wait_time": self.max_wait_time,
                },
            ):
                # First activity: Monitor trigger
                context_data = {
                    "state": context.state,
                    "history": [record.__dict__ for record in context.history],
                    "agent_definitions": [definition.__dict__ for definition in context.agent_definitions],
                }
                agent_data = self.dict()

                with performance_handler.track_time("temporal_trigger_monitoring"):
                    flock_logger.info("Starting trigger monitoring activity")
                    monitor_result = await run_activity(
                        client,
                        f"{self.name}_monitor",
                        run_agent_activity,
                        {"agent_data": agent_data, "context_data": context_data},
                    )

                if monitor_result.get("error"):
                    flock_logger.warning(
                        "Trigger monitoring ended without activation",
                        reason=monitor_result["error"],
                        agent=self.name,
                    )
                    return monitor_result

                # Second activity: Execute action
                with performance_handler.track_time("temporal_action_execution"):
                    flock_logger.info("Starting action execution activity")
                    action_result = await run_activity(
                        client,
                        f"{self.name}_action",
                        run_agent_activity,
                        {"agent_data": agent_data, "context_data": context_data},
                    )

                flock_logger.success(
                    "Temporal trigger agent completed successfully",
                    agent=self.name,
                )
                return action_result

        except Exception as e:
            flock_logger.error(
                "Temporal trigger agent execution failed",
                error=str(e),
                agent=self.name,
            )
            raise

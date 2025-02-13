from collections.abc import Callable
from typing import Any

import dspy  # your dspy package for LM, Predict, ReAct, etc.
from pydantic import Field

from flock.core.agent import Agent
from flock.core.context import FlockContext
from flock.core.logging import flock_logger, performance_handler


class DeclarativeAgent(Agent):
    """An agent that evaluates declarative inputs.

    Attributes:
      input: A comma‐separated list of input keys.
             If a key is not found in the incoming FlockContext and only one input is expected,
             then the value of "init_input" is used.
      output: A comma‐separated list of output keys (any type annotations after ":" are ignored).
      tools: An optional list of callables (tools) that the agent is allowed to use.
      use_cache: Whether to cache agent results.
    """

    input: str = Field(description="Comma-separated input keys (e.g., 'blog_idea' or 'url, context')")
    output: str = Field(description="Comma-separated output keys (e.g., 'title, headers')")
    tools: list[Callable[..., Any]] | None = Field(default=None, description="Tools the agent is allowed to use")
    use_cache: bool = Field(default=False, description="Whether to use the cache for this agent")

    def _parse_keys(self, keys_str: str) -> list[str]:
        """Split a comma‐separated string and strip any type annotations.
        For example, "a, b: list[str]" becomes ["a", "b"].
        """
        keys = []
        for part in keys_str.split(","):
            part = part.strip()
            if not part:
                continue
            # Remove any type annotation (everything after a colon)
            if ":" in part:
                key = part.split(":", 1)[0].strip()
            else:
                key = part
            keys.append(key)
        return keys

    def _build_input(self, context: FlockContext) -> dict:
        """Build the dictionary of inputs for the agent based on its input specification.

        For each key in the agent's input string:
          - If the key is "context" (case-insensitive), pass the entire FlockContext.
          - Otherwise, use context.get_variable() to fetch the value.
          - If the key is not found and only one key is expected, default to context["init_input"].
        """
        input_keys = self._parse_keys(self.input)
        inputs = {}
        for key in input_keys:
            if key.lower() == "context":
                inputs[key] = context
            else:
                value = context.get_variable(key)
                if value is None and len(input_keys) == 1:
                    value = context.get_variable("init_input")
                inputs[key] = value
        return inputs

    def _configure_task(self):
        """Configure the dspy language model and choose a task constructor.
        If tools are provided, ReAct is used; otherwise, Predict.
        """
        with performance_handler.track_time("model_configuration"):
            flock_logger.debug(f"Configuring {self.model} for {'ReAct' if self.tools else 'Predict'} task")
            lm = dspy.LM(self.model)
            dspy.configure(lm=lm)
            return dspy.ReAct if self.tools else dspy.Predict

    async def _evaluate(self, context: FlockContext, input_overrides: dict | None = None) -> dict:
        """Evaluate the agent by:
        1. Building an input dictionary from the FlockContext (merging any overrides),
        2. Building a prompt like "input1, input2 -> output1, output2",
        3. Instantiating and executing the dspy task (Predict or ReAct),
        4. Returning the resulting dictionary.
        """
        try:
            # Build inputs
            with performance_handler.track_time("input_preparation"):
                inputs = self._build_input(context)
                if input_overrides:
                    inputs.update(input_overrides)
                input_keys = self._parse_keys(self.input)
                output_keys = self._parse_keys(self.output)
                prompt = f"{', '.join(input_keys)} -> {', '.join(output_keys)}"
                flock_logger.debug("Prepared inputs", inputs=inputs, prompt=prompt)

            # Configure and execute task
            with performance_handler.track_time("task_execution"):
                task_constructor = self._configure_task()
                if self.tools:
                    flock_logger.info("Creating ReAct task with tools", num_tools=len(self.tools))
                    agent_task = task_constructor(prompt, tools=self.tools)
                else:
                    flock_logger.info("Creating Predict task")
                    agent_task = task_constructor(prompt)

                flock_logger.info("Executing task...")
                result = agent_task(**inputs).toDict()

            # Process result
            for key in input_keys:
                result.setdefault(key, inputs.get(key))
            flock_logger.success("Task completed successfully", output_keys=list(result.keys()))
            return result

        except Exception as e:
            flock_logger.error(
                "Task execution failed",
                error=str(e),
                agent=self.name,
                inputs=inputs,
                prompt=prompt,
            )
            raise

    async def run(self, context: FlockContext) -> dict:
        """Run the agent on the provided FlockContext (locally)."""
        flock_logger.info(f"Running agent locally: {self.name}")
        return await self._evaluate(context)

    async def run_temporal(self, context: FlockContext) -> dict:
        """Run the agent via Temporal by serializing its parameters and the FlockContext and
        calling a dedicated Temporal activity.
        """
        from temporalio.client import Client

        from flock.workflow.agent_activities import run_declarative_agent_activity
        from flock.workflow.temporal_setup import run_activity

        try:
            with performance_handler.track_time("temporal_setup"):
                # Connect to Temporal (adjust the host/namespace as needed)
                flock_logger.info("Connecting to Temporal...")
                client = await Client.connect("localhost:7233", namespace="default")

                # Serialize the FlockContext and agent
                flock_logger.debug("Serializing context and agent data")
                context_data = {
                    "state": context.state,
                    "history": [record.__dict__ for record in context.history],
                    "agent_definitions": [definition.__dict__ for definition in context.agent_definitions],
                }
                agent_data = self.dict()

            # Run the activity
            with performance_handler.track_time("temporal_activity"):
                flock_logger.info(f"Starting Temporal activity: {self.name}")
                result = await run_activity(
                    client,
                    self.name,
                    run_declarative_agent_activity,
                    {"agent_data": agent_data, "context_data": context_data},
                )
                flock_logger.success("Temporal activity completed successfully")
                return result

        except Exception as e:
            flock_logger.error(f"Temporal execution failed: {e}", agent=self.name)
            raise

import asyncio
import uuid
from typing import Any

from pydantic import Field

from flock.core.context import FlockContext
from flock.core.logging import flock_logger, live_update_handler, performance_handler

from .declarative_agent import DeclarativeAgent


class BatchAgent(DeclarativeAgent):
    """A DeclarativeAgent that processes an iterable input in batches.

    Additional Attributes:
      iter_input: The key in the FlockContext that holds the iterable (a list).
      batch_site: The number of items per batch.

    For each batch, the agent’s input dictionary is built from the FlockContext with the
    value for the iter_input key overridden by the current batch. The outputs across batches
    are then aggregated.
    """

    iter_input: str = Field(default="", description="Key of the iterable input (must be a list in the FlockContext)")
    batch_size: int = Field(default=1, description="Batch size (number of items per batch)")

    async def run(self, context: FlockContext) -> dict:
        """Run the BatchAgent locally by partitioning the iterable and aggregating the results."""
        try:
            with performance_handler.track_time("batch_preparation"):
                flock_logger.info(f"Starting batch processing for agent: {self.name}")
                iterable = context.get_variable(self.iter_input)
                if not isinstance(iterable, list):
                    error_msg = f"Expected a list for key '{self.iter_input}' in context."
                    flock_logger.error(error_msg)
                    return {"error": error_msg}

                # Partition the iterable into batches
                batches: list[list[Any]] = [
                    iterable[i : i + self.batch_size] for i in range(0, len(iterable), self.batch_size)
                ]
                num_batches = len(batches)
                flock_logger.info(
                    "Prepared batches",
                    total_items=len(iterable),
                    batch_size=self.batch_size,
                    num_batches=num_batches,
                )

            # Process batches with progress tracking
            with live_update_handler.progress_tracker(f"Processing {num_batches} batches") as update_progress:
                tasks = []
                for i, batch in enumerate(batches):
                    flock_logger.debug(f"Creating task for batch {i + 1}/{num_batches}", batch_size=len(batch))
                    tasks.append(self._evaluate(context, input_overrides={self.iter_input: batch}))
                    update_progress((i + 1) * 100 / num_batches)

                with performance_handler.track_time("batch_processing"):
                    batch_results = await asyncio.gather(*tasks)
                    flock_logger.success(f"Completed processing {num_batches} batches")

            # Aggregate the outputs
            with performance_handler.track_time("result_aggregation"):
                flock_logger.info("Aggregating batch results")
                output_keys = self._parse_keys(self.output)
                aggregated = {key: [] for key in output_keys}
                for i, res in enumerate(batch_results):
                    flock_logger.debug(f"Aggregating results from batch {i + 1}/{num_batches}")
                    for key in output_keys:
                        aggregated[key].append(res.get(key))
                aggregated["batch_results"] = batch_results
                flock_logger.success("Successfully aggregated all batch results")
                return aggregated

        except Exception as e:
            flock_logger.error(
                "Batch processing failed",
                error=str(e),
                agent=self.name,
                iter_input=self.iter_input,
            )
            raise

    async def run_temporal(self, context: FlockContext) -> dict:
        """Run the BatchAgent via Temporal.

        For each batch, the agent's evaluation is performed as a separate Temporal activity.
        The results are then aggregated.
        """
        try:
            with performance_handler.track_time("temporal_setup"):
                flock_logger.info(f"Starting temporal batch processing for agent: {self.name}")

                from temporalio.client import Client

                from flock.workflow.agent_activities import run_declarative_agent_activity
                from flock.workflow.temporal_setup import run_activity

                # Connect to Temporal
                flock_logger.info("Connecting to Temporal service...")
                client = await Client.connect("localhost:7233", namespace="default")

                # Validate and prepare input
                iterable = context.get_variable(self.iter_input)
                if not isinstance(iterable, list):
                    error_msg = f"Expected a list for key '{self.iter_input}' in context."
                    flock_logger.error(error_msg)
                    return {"error": error_msg}

                # Partition into batches
                batches: list[list[Any]] = [
                    iterable[i : i + self.batch_size] for i in range(0, len(iterable), self.batch_size)
                ]
                num_batches = len(batches)
                flock_logger.info(
                    "Prepared batches for temporal processing",
                    total_items=len(iterable),
                    batch_size=self.batch_size,
                    num_batches=num_batches,
                )

            # Process batches with status updates
            with live_update_handler.update_workflow_status(
                self.name, "Running", {"phase": "batch_processing", "total_batches": num_batches}
            ):
                tasks = []
                for i, batch in enumerate(batches):
                    flock_logger.debug(f"Creating temporal task for batch {i + 1}/{num_batches}", batch_size=len(batch))
                    # Prepare context for this batch
                    new_state = context.state.copy()
                    new_state[self.iter_input] = batch
                    context_data = {
                        "state": new_state,
                        "history": [],  # you might choose to pass along history if needed
                        "agent_definitions": [],
                    }
                    agent_data = self.dict()
                    task_id = f"{self.name}_{uuid.uuid4().hex[:4]}"

                    # Create temporal activity task
                    tasks.append(
                        run_activity(
                            client,
                            task_id,
                            run_declarative_agent_activity,
                            {"agent_data": agent_data, "context_data": context_data},
                        )
                    )

                with performance_handler.track_time("temporal_batch_processing"):
                    batch_results = await asyncio.gather(*tasks)
                    flock_logger.success(f"Completed temporal processing of {num_batches} batches")

            # Aggregate the outputs
            with performance_handler.track_time("temporal_result_aggregation"):
                flock_logger.info("Aggregating temporal batch results")
                output_keys = self._parse_keys(self.output)
                aggregated = {key: [] for key in output_keys}
                for i, res in enumerate(batch_results):
                    flock_logger.debug(f"Aggregating results from temporal batch {i + 1}/{num_batches}")
                    for key in output_keys:
                        aggregated[key].append(res.get(key))
                aggregated["batch_results"] = batch_results
                flock_logger.success("Successfully aggregated all temporal batch results")
                return aggregated

        except Exception as e:
            flock_logger.error(
                "Temporal batch processing failed",
                error=str(e),
                agent=self.name,
                iter_input=self.iter_input,
            )
            raise

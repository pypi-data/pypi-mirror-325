from datetime import timedelta

from temporalio import workflow

from flock.core.context import FlockContext
from flock.core.logging import flock_logger
from flock.workflow.activities import run_agent

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from flock.workflow.activities import run_agent


@workflow.defn
class FlockWorkflow:
    def __init__(self) -> None:
        self.context = None

    @workflow.run
    async def run(self, context_dict: dict) -> dict:
        self.context = FlockContext.from_dict(context_dict)
        self.context.workflow_id = workflow.info().workflow_id
        self.context.workflow_timestamp = workflow.info().start_time.strftime("%Y-%m-%d %H:%M:%S")

        try:
            flock_logger.set_context(workflow_id=self.context.workflow_id)
            flock_logger.workflow_event(f"Starting workflow execution at {self.context.workflow_timestamp}")

            result = await workflow.execute_activity(
                run_agent, self.context, start_to_close_timeout=timedelta(minutes=5)
            )

            self.context.set_variable(
                "flock.result",
                {
                    "result": result,
                    "success": True,
                },
            )

            flock_logger.workflow_event("Workflow completed successfully")
            return result

        except Exception as e:
            flock_logger.error(f"Workflow execution failed: {e}")
            self.context.set_variable(
                "flock.result",
                {
                    "result": f"Failed: {e}",
                    "success": False,
                },
            )
            return self.context

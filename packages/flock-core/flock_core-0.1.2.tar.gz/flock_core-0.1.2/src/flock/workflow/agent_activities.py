from temporalio import activity

from flock.agents.declarative_agent import DeclarativeAgent
from flock.core.context import FlockContext


@activity.defn
async def run_declarative_agent_activity(params: dict) -> dict:
    """Temporal activity to run a declarative (or batch) agent.

    Expects a dictionary with:
      - "agent_data": a dict representation of the agent (as produced by .dict()),
      - "context_data": a dict containing the FlockContext state and optionally other fields.

    The activity reconstructs the agent and a FlockContext, then calls the agent’s _evaluate() method.
    """
    agent_data = params.get("agent_data")
    context_data = params.get("context_data", {})
    # Reconstruct the agent from its serialized representation.
    agent = DeclarativeAgent.parse_obj(agent_data)
    # Reconstruct the FlockContext from the state.
    state = context_data.get("state", {})
    # (For simplicity, we ignore history and agent_definitions here. You can extend this if needed.)
    context = FlockContext(state=state)
    result = await agent._evaluate(context)
    return result

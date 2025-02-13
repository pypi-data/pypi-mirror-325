"""Defines Temporal activities for running a chain of agents."""

from datetime import datetime

from temporalio import activity

from flock.core.agent import Agent
from flock.core.agent_registry import Registry
from flock.core.context import FlockContext
from flock.core.context_vars import FLOCK_CURRENT_AGENT, FLOCK_INITIAL_INPUT
from flock.core.handoff.handoff_base import HandoffBase
from flock.core.logging import flock_logger


@activity.defn
async def run_agent(context: FlockContext) -> dict:
    """Runs a chain of agents using the provided context.

    The context contains:
      - A state (e.g., "init_input", "current_agent", etc.),
      - A history of agent runs.

    Each agent uses the current value of the variable specified in its `input` attribute.
    After each run, its output is merged into the context state.
    The default handoff behavior is to fetch the next agent's input automatically from the context.
    """
    registry = Registry()
    current_agent_name = context.get_variable(FLOCK_CURRENT_AGENT)
    flock_logger.info(f"Starting agent chain with initial agent", agent=current_agent_name)

    agent = registry.get_agent(current_agent_name)
    if not agent:
        flock_logger.error(f"Agent not found", agent=current_agent_name)
        return {"error": f"Agent '{current_agent_name}' not found."}

    while agent:
        # Determine the input for this agent.
        # (Preferably, the agent's input key is used; otherwise "init_input" is assumed.)
        agent_input = (
            context.get_variable(agent.input)
            if getattr(agent, "input", None)
            else context.get_variable(FLOCK_INITIAL_INPUT)
        )
        flock_logger.info(
            "Determined agent input", agent=agent.name, input_source=getattr(agent, "input", "FLOCK_INITIAL_INPUT")
        )

        # Prepare a deep copy of the state for the agent's run.
        local_context = FlockContext.from_dict(context.to_dict())
        local_context.set_variable(
            f"{agent.name}.{agent.input}", agent_input
        )  # ensure the agent's expected input is set

        # Execute the agent.
        flock_logger.info("Executing agent", agent=agent.name)
        result = await agent.run(local_context)
        flock_logger.info("Agent execution completed", agent=agent.name)

        # If no handoff is defined, return the result.
        if not agent.hand_off:
            # Record the agent's execution.
            context.record(agent.name, result, timestamp=datetime.now(), hand_off=None)
            flock_logger.info("No handoff defined, completing chain", agent=agent.name)
            return result

        # Determine the next agent.
        if callable(agent.hand_off):
            # The handoff function may override the default behavior:
            # it can explicitly return a dict with "next_agent" and optionally "input"
            flock_logger.info("Executing handoff function", agent=agent.name)
            handoff_data: HandoffBase = agent.hand_off(context, result)
            if isinstance(handoff_data.next_agent, Agent):
                next_agent_name = handoff_data.next_agent.name
            else:
                next_agent_name = handoff_data.next_agent

            # Use the provided new input if present, otherwise let the context update be automatic.
            if handoff_data.input:
                context.state["init_input"] = handoff_data["input"]
                flock_logger.debug("Using handoff-provided input", agent=agent.name)
            if handoff_data.context_params:
                context.state.update(handoff_data.context_params)
                flock_logger.debug("Updated context with handoff params", agent=agent.name)
        elif isinstance(agent.hand_off, str | Agent):
            next_agent_name = agent.hand_off if isinstance(agent.hand_off, str) else agent.hand_off.name

        else:
            return {"error": "Unsupported hand_off type."}
        context.record(agent.name, result, timestamp=datetime.now(), hand_off=next_agent_name)
        # Update the current agent and prepare the next input automatically.
        next_agent = registry.get_agent(next_agent_name)
        if not next_agent:
            flock_logger.error("Next agent not found", agent=next_agent_name)
            return {"error": f"Next agent '{next_agent_name}' not found."}

        context.state["current_agent"] = next_agent.name
        # By default, the next input is determined from the current state using next_input_for().
        context.state["init_input"] = context.next_input_for(next_agent)
        flock_logger.info("Handing off to next agent", current=agent.name, next=next_agent.name)
        agent = next_agent

    # If the loop ever terminates without a final result, return the latest state value.
    flock_logger.info("Chain completed, returning final state")
    return context.get_variable("init_input")


@activity.defn
async def get_next_agent(name: str) -> Agent | None:
    """Retrieves the agent with the given name from the registry."""
    flock_logger.debug("Looking up next agent", agent=name)
    registry = Registry()
    agent = registry.get_agent(name)
    if not agent:
        flock_logger.warning("Next agent not found", agent=name)
    return agent

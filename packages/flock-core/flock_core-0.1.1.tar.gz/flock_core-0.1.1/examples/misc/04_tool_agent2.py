import asyncio

from devtools import debug

from flock.core.agents.declarative_agent import DeclarativeAgent
from flock.core.flock import Flock
from flock.core.tools import basic_tools

MODEL = "openai/gpt-4o"


async def main():
    agent_runner = Flock()

    agent = DeclarativeAgent(
        name="my_celebrity_age_agent",
        input="a_person",
        output="persons_age_in_days",
        tools=[basic_tools.web_search_tavily, basic_tools.code_eval],
    )
    agent_runner._add_agent(agent)

    result = await agent_runner.run_async(
        local_debug=True,
        start_agent=agent,
        input="Johnny Depp",
    )
    debug(result)


if __name__ == "__main__":
    asyncio.run(main())

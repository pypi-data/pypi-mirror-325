import asyncio

from devtools import debug

from flock.core.agents.declarative_agent import DeclarativeAgent
from flock.core.flock import Flock
from flock.core.tools import basic_tools

MODEL = "openai/gpt-4o"


def web_search(query: str):
    return "The best search result for your query is: 'Cats are cute'"


async def main():
    agent_runner = Flock()

    agent = DeclarativeAgent(
        model="azure/ara-gpt4o",
        name="my_research_agent",
        input="research_topic",
        output="research_result",
        tools=[basic_tools.web_search_tavily],
    )
    agent_runner._add_agent(agent)

    result = await agent_runner.run_async(
        local_debug=True,
        start_agent=agent,
        input="Reinforcement Learning",
    )
    debug(result)


if __name__ == "__main__":
    asyncio.run(main())

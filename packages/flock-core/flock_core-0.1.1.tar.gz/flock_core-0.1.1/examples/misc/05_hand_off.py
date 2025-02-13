import asyncio

from devtools import debug

from flock.core.agents.batch_agent import BatchAgent
from flock.core.agents.declarative_agent import DeclarativeAgent
from flock.core.flock import Flock
from flock.core.tools import basic_tools

MODEL = "openai/gpt-4o"


async def main():
    flock, context = Flock.create()

    project_plan_agent = DeclarativeAgent(
        name="project_plan_agent",
        input="project_idea",
        output="catchy_project_name, project_pitch, project_plan_headings: list[str]",
        tools=[basic_tools.web_search_tavily, basic_tools.code_eval],
    )
    flock.add_agent(project_plan_agent)

    content_agent = BatchAgent(
        name="batchAgent",
        iter_input="project_plan_headings",
        input="context,project_plan_headings",
        output="project_plan_heading, project_plan_content_for_heading",
        batch_size=4,
    )
    flock.add_agent(content_agent)

    project_plan_agent.hand_off = content_agent

    result = await flock.run_async(
        context,
        start_agent=project_plan_agent,
        input="a web application that creates a documentation, specialized to be consumed by LLMs, for a given github repository",
        local_debug=True,
    )
    debug(result)


if __name__ == "__main__":
    asyncio.run(main())

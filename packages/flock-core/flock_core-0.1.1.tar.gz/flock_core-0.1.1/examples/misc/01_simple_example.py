import asyncio

from flock.agents import DeclarativeAgent
from flock.core import Flock

MODEL = "openai/gpt-4o"


async def main():
    # --------------------------------
    # Create the flock and context
    # --------------------------------
    # The flock is the place where all the agents are at home
    # set local_debug to True to run the flock without needing Temporal
    # Temporal is a workflow engine that the flock uses to run agents
    flock = Flock(model=MODEL, local_debug=True)

    # --------------------------------
    # Create an agent
    # --------------------------------
    # The Flock doesn't believe in prompts (see the readme for more info)
    # The Flock just declares what agents get in and what agents produce
    # bloggy takes in a blog_idea and outputs a funny_blog_title and blog_headers
    bloggy = DeclarativeAgent(name="bloggy", input="blog_idea", output="funny_blog_title, blog_headers")
    flock.add_agent(bloggy)

    # --------------------------------
    # Run the flock
    # --------------------------------
    # Tell the flock who is the starting and what input to give it
    await flock.run_async(start_agent=bloggy, input="a blog about cats")


if __name__ == "__main__":
    asyncio.run(main())

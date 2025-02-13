import asyncio

from devtools import pprint

from flock.core.agents.declarative_agent import DeclarativeAgent
from flock.core.flock import Flock

MODEL = "openai/gpt-4o"


async def main():
    # --------------------------------
    # Create the flock and context
    # --------------------------------
    # The flock is the place where all the agents are at home
    # The context is everything that happened in the flock
    flock, context = Flock.create()

    # --------------------------------
    # Create an agent
    # --------------------------------
    # The Flock doesn't believe in prompts (see the readme for more info)
    # The Flock just declares what agents get in and what agents produce
    # bloggy takes in a blog_idea and outputs a funny_blog_title and blog_headers
    bloggy = DeclarativeAgent(name="bloggy", input="blog_idea", output="funny_blog_title, blog_headers", model=MODEL)
    # Let's add bloggy to the flock
    flock.add_agent(bloggy)

    # --------------------------------
    # Deploy the flock
    # --------------------------------
    # Deploy the agent system as a docker container which exposes an endpoint to start the flock
    # local_debug makes it easier to debug the flock
    result = flock.deploy_as_docker(mode="single")
    # print status information
    pprint(result)


if __name__ == "__main__":
    asyncio.run(main())

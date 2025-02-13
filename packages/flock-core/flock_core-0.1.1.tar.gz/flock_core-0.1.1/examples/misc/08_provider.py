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
    # Run the flock
    # --------------------------------
    # By giving the flock a start_agent and an input, we can run the flock
    # local_debug makes it easier to debug the flock
    result = await flock.run_async(context=context, start_agent=bloggy, input="a blog about cats", local_debug=True)
    # earn the fruits of the flock's labor
    pprint(result)


{
    "funny_blog_title": '"Whisker Me This: The Purr-fect Guide to Feline Shenanigans"',
    "blog_headers": (
        '1. "The Cat\'s Pajamas: Why Your Feline Friend is Secretly a Fashion Icon"\n'
        '2. "Nine Lives, One Litter Box: The Mysteries of Cat Hygiene"\n'
        '3. "Paws and Reflect: The Philosophical Musings of Your Cat"\n'
        '4. "Meow-sic to My Ears: Understanding the Symphony of Cat Sounds"\n'
        '5. "Fur Real: Debunking Myths About Cats and Their Quirky Behaviors"\n'
        '6. "The Great Catsby: How to Host a Cat-Themed Party That’s the Cat’s Meow"\n'
        '7. "Tail Tales: The Secret Language of Cat Tails and What They’re Really Saying"'
    ),
    "blog_idea": "a blog about cats",
}


if __name__ == "__main__":
    asyncio.run(main())

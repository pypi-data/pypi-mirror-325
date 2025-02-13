import asyncio

from devtools import debug

from flock.agents.declarative_agent import DeclarativeAgent
from flock.core.flock import Flock
from flock.core.tools import basic_tools


async def main():
    agent_runner = Flock()

    agent = DeclarativeAgent(
        name="my_agent",
        input="url",
        output="""
        title, headings: list[str], 
        entities_and_metadata: list[dict[str, str]], 
        type:Literal['news', 'blog', 'opinion piece', 'tweet']
        """,
        tools=[basic_tools.get_web_content_as_markdown],
    )
    # No need to explicitly add the agent - it auto-registers itself

    result = await agent_runner.run_async(
        local_debug=True,
        start_agent=agent,
        input="https://lite.cnn.com/travel/alexander-the-great-macedon-persian-empire-darius/index.html",
    )
    debug(result)
    debug(result.title)


"""
example output:
{
    'title': 'How Alexander the Great redrew the map of the world',
    'headings': [
        'A mysterious death',
        ''He overcame everything'',
        'Projecting our fantasies',
        'A racist legacy?',
        'Following in Alexander's footsteps',
        'End of the rainbow'
    ],
    'type': 'news',
    'long_text': 'https://lite.cnn.com/travel/alexander-the-great-macedon-persian-empire-darius/index.html'
    'entities_and_metadata': [
        {
            'name': 'Alexander the Great',
            'type': 'historical figure'
        },
        {
            'name': 'Darius III',
            'type': 'historical figure'
        },
        {
            'name': 'Macedon',
            'type': 'location'
        },
        {
            'name': 'Persian Empire',
            'type': 'historical entity'
        },
        {
            'name': 'Egypt',
            'type': 'location'
        },
        {
            'name': 'Turkey',
            'type': 'location'
        },
        {
            'name': 'Pakistan',
            'type': 'location'
        },
        {
            'name': 'Greece',
            'type': 'location'
        },
        {
            'name': 'Paul Cartledge',
            'type': 'historian'
        },
        {
            'name': 'Pierre Briant',
            'type': 'historian'
        },
        {
            'name': 'Peter Sommer',
            'type': 'tour operator'
        },
        {
            'name': 'Royal Palace of Aigai',
            'type': 'historical site'
        },
        {
            'name': 'Shahnamah',
            'type': 'literary work'
        },
        {
            'name': 'Mega Alexandros',
            'type': 'blog'
        }
    ],
}
"""


if __name__ == "__main__":
    asyncio.run(main())

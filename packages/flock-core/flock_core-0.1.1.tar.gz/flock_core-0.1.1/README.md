# flock

white duck flock (engl. Herde/Schwarm) ist ein KI-gestütztes Agentenframework. Agenten sind Applikationen die autark und autonom entscheiden wie sie ein Problem lösen, und je nach konfiguration auch selber entscheiden wie sie untereinander kommunizieren. Ein zusammenschluss mehrerer Agenten ist ein Agentensystem.

Wir dachten da vielleicht als Logo einfach eine Herde/Schwarm an Freds, oder ähnlich wie Huggingface an einen James Bond Fred (vgl. https://huggingface.co/docs/smolagents/en/index) oder natürlich auch gerne eine Herde an James Bond Freds!


White Duck Flock (engl. Herde/Schwarm) ist ein KI-gestütztes Agentenframework. Agenten sind Applikationen, die autark und autonom entscheiden, wie sie ein Problem lösen – und je nach Konfiguration auch selbst bestimmen, wie sie untereinander kommunizieren. Ein Zusammenschluss mehrerer Agenten bildet ein Agentensystem.

Als Logo dachten wir vielleicht an eine Herde/Schwarm von Freds – oder, ähnlich wie Hugging Face, an einen James-Bond-Fred (vgl. https://huggingface.co/docs/smolagents/en/index). Alternativ natürlich auch gerne eine ganze Herde an James-Bond-Freds!




```python
MODEL = "openai/gpt-4o"

async def main():
 
    #--------------------------------
    # Create the flock and context
    #--------------------------------
    # The flock is the place where all the agents are at home
    # The context is everything that happened in the flock
    flock, context = Flock.create()

    #--------------------------------
    # Create an agent
    #--------------------------------
    # The Flock doesn't believe in prompts (see the readme for more info)
    # The Flock just declares what agents get in and what agents produce
    # bloggy takes in a blog_idea and outputs a funny_blog_title and blog_headers
    bloggy = DeclarativeAgent(
        name="bloggy",
        input="blog_idea",
        output="funny_blog_title, blog_headers",
        model=MODEL
    )
    # Let's add bloggy to the flock
    flock.add_agent(bloggy)

    #--------------------------------
    # Run the flock
    #--------------------------------
    # By giving the flock a start_agent and an input, we can run the flock
    # local_debug makes it easier to debug the flock
    result = await flock.run_async(
        context=context,
        start_agent=bloggy,
        input="a blog about cats",
        local_debug=True
    )
    # earn the fruits of the flock's labor
    print(result)

```

Problems with other agent frameworks

- Instead of writing software you need to write pages long natural language prompts
- One crash and your whole agent system is dead
- Demand having your system be a real DAG and a real state machine

How Flock tries to solve it:

- Just declare what your agents get ind, and what they should return
- First grade temporalio support. Retry, Error, Timeout etc etc are somethi
- Chain your agents together in any kind you want

## Philosophy & Design Principles

### Say goodbye to prompting

Sometimes you see agents with a 200 lines of text system prompt.
How do evaluate if this is the most optimal prompt for your use case? How would changes affect the performance?
Questions for there is no easy answer.

How does a good prompt look like? What happens with your prompt if you switch models?

With flock you just tell an agent what kind of input it gets, and what it should output. Done. Easy peasy.

The philosophy behind this approach is simple: by focusing on the interface (inputs and outputs) rather than implementation details (prompts), we create more maintainable and adaptable systems. This declarative approach means:
- Your agents are model-agnostic
- Behavior can be tested and validated objectively
- Changes are localized and predictable
- Integration with other systems becomes straightforward

### Testable

Reducing the need for fuzzy natural language to a minimum agents become easily testable, evaluable.
Flock comes with tools to know exactly how good your agents and therefore the agent system is performing.

This focus on testability isn't just about catching bugs - it's about building confidence in your AI systems:
- Clear input/output contracts make unit testing straightforward
- Type safety ensures data consistency
- Performance metrics are built into the framework
- Behavior can be validated systematically

### Production ready

Would you run your agent system in critical environments? The answer is probably no, since with most frameworks one dead endpoint or uncatched exception will break the whole agent system.

Flock uses Temporal as its workflow engine which comes with battle-hardened retry, failure, exception options.

This production-readiness is achieved through several key design decisions:
- Temporal workflow engine for durability and reliability
- Strong typing for predictable behavior
- Modular architecture for maintainability
- Built-in monitoring and debugging capabilities

## Core Features

- **Declarative Agent System**: Define agents with clear input/output specifications and optional tool capabilities
- **Temporal Workflow Integration**: Built-in support for durable execution and state management using Temporal
- **Tool Integration**: Easy integration of external tools like web search, code evaluation, and math computation
- **Type Safety**: Strong typing support for agent inputs and outputs
- **DSPy Integration**: Seamless integration with DSPy for LLM interactions
- **Flexible Architecture**: Support for agent chaining, hand-offs, and complex workflows

## Architecture and Flow

![alt text](docs/img/charts/agent_workflow_inv.png) 


![alt text](docs/img/charts/core_architecture_inv.png) 

## Requirements

Nothing. Temporal is not needed for development but recommended

Either clone https://github.com/temporalio/docker-compose and up the compose

or install the temporal cli

https://docs.temporal.io/cli

## Installation

```bash
pip install flock
```

## Quick Start

Here's a simple example of creating and using an agent:

```python
import asyncio
from flock.core.agents.declarative_agent import DeclarativeAgent
from flock.core.flock import Flock

async def main():
    # Initialize Flock
    agent_runner = Flock()

    # Create a simple agent
    agent = DeclarativeAgent(
        name="blog_title_agent",
        input="blog_idea",
        output="funny_blog_title",
    )
    agent_runner.add_agent(agent)

    # Run the agent
    result = await agent_runner.run_async(
        start_agent=agent,
        input="a blog about cats",
        local_debug=True,
    )
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

## Web Application

![alt text](docs/img/app.png)

Flock comes with a built-in web interface for managing and monitoring your agents. The web app provides a rich, interactive environment for working with your agent systems.

TODO: Expand

### Running the Web App

```bash
# After installing flock
flock
# Or with uv
uv run flock
```

### Features

- **Dashboard**: Overview of your agent systems and their status
- **Agent Management**: 
  - List and filter agents
  - View agent details and configuration
  - Monitor production readiness
  - Track agent history
- **Agent Systems**: Manage complex agent workflows and interactions
- **History**: View execution history and results
- **Tools**: Access and manage available tools
- **Playground**: Interactive environment for testing agents
- **Settings**: Configure system preferences and integrations

### Technical Details

The web application is built with:
- FastHTML for UI components
- MonsterUI for enhanced UI elements
- Interactive features using D3.js and interact.js
- Real-time updates and monitoring
- Responsive design for different screen sizes

### Interface Structure

```
Web Interface
├── Sidebar Navigation
│   ├── Dashboard
│   ├── Agents
│   ├── Agent Systems
│   ├── History
│   ├── Tools
│   ├── Playground
│   └── Settings
├── Main Content Area
│   ├── Agent List
│   └── Agent Details
└── Interactive Features
    ├── Theme Switching
    ├── Search Functionality
    └── Real-time Updates
```

## Advanced Usage

### Agents with Tools

Agents can use tools to interact with external systems:

```python
from flock.core.tools import basic_tools

agent = DeclarativeAgent(
    name="research_agent",
    input="research_topic",
    output="research_result",
    tools=[basic_tools.web_search_tavily],
)
```

### Type-Safe Outputs

Define complex output types for structured responses:

```python
agent = DeclarativeAgent(
    name="analysis_agent",
    input="long_text",
    output="""
        title: str,
        headings: list[str],
        entities_and_metadata: list[dict[str, str]],
        type: Literal['news', 'blog', 'opinion piece', 'tweet']
    """,
)
```

### Agent Chaining

Create chains of agents that can hand off tasks:

```python
# First agent in chain
project_plan_agent = DeclarativeAgent(
    name="project_plan_agent",
    input="project_idea",
    output="catchy_project_name, project_pitch, project_plan_headings: list[str]",
    tools=[basic_tools.web_search_tavily, basic_tools.code_eval],
)

# Second agent in chain
content_agent = DeclarativeAgent(
    name="content_agent",
    input="context,project_plan_agent.project_plan_headings.items",
    output="project_plan_heading, project_plan_content_for_heading",
)

# Set up hand-off
project_plan_agent.hand_off = content_agent
```

## Core Components

### Flock Class

The main orchestrator that manages agent creation and execution:
- Handles agent registration
- Manages workflow execution
- Supports both local debugging and distributed execution

### DeclarativeAgent

Base class for creating agents with:
- Input/output specifications
- Tool integration
- Type validation
- Hand-off capabilities

### Workflow System

Built on Temporal for:
- Durable execution
- State management
- Error handling
- Activity tracking

### Tools

Built-in tools include:
- Web search (via Tavily)
- Math evaluation
- Code execution
- Extensible tool system for custom integrations

## Architecture

```
Flock Framework
├── Core
│   ├── Agents
│   │   ├── DeclarativeAgent
│   │   └── Agent Registry
│   ├── Tools
│   │   └── Basic Tools
│   └── Flock Manager
├── Workflow
│   ├── Activities
│   ├── Temporal Setup
│   └── Workflow Definitions
└── App
    └── Components
```

## Development

### Prerequisites

- Python 3.12+
- Temporal server running locally (for workflow features)
- Required API keys (e.g., Tavily for web search)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flock.git
cd flock
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

### Running Tests

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the LICENSE file included in the repository.

## Acknowledgments

- Built with [DSPy](https://github.com/stanfordnlp/dspy)
- Uses [Temporal](https://temporal.io/) for workflow management
- Integrates with [Tavily](https://tavily.com/) for web search capabilities
- Web interface built with FastHTML and MonsterUI

## Evolution & Future Direction

Flock was born from the realization that current agent frameworks often prioritize flexibility at the cost of reliability and maintainability. The framework's design decisions reflect this focus:

### Why Declarative?
The declarative approach wasn't just a stylistic choice - it was a deliberate decision to separate what agents do from how they do it. This separation means:
- Agents can be optimized independently of their interface
- Different LLM backends can be swapped without changing agent definitions
- Testing and validation become straightforward
- Integration with existing systems is simplified

### Why Temporal?
Using Temporal as the workflow engine was crucial for production reliability:
- Automatic retry on failures
- Built-in state management
- Scalable execution
- Detailed execution history
- Production-grade monitoring

### Future Plans
The framework is actively evolving with several key areas of focus:
- Enhanced type system for more complex agent interactions
- Expanded tool ecosystem
- Improved optimization capabilities
- Advanced monitoring and debugging features
- Extended testing and validation tools

Join us in building the future of reliable, production-ready AI agent systems!

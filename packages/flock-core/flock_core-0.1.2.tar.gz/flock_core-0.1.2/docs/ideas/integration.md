# Flock-Native DSPy Integration Design

## Current Architecture Analysis

Flock's declarative agent system has several key features:

1. **Declarative Nature**
   - Agents are defined by input/output specifications
   - Simple, clear interface for agent creation
   - Tool integration capabilities

2. **Example Usage**
```python
agent = DeclarativeAgent(
    name="my_cute_blog_agent",
    input="blog_idea",
    output="funny_blog_title",
)

# With tools
agent = DeclarativeAgent(
    name="my_research_agent",
    input="research_topic",
    output="research_result",
    tools=[basic_tools.web_search_tavily],
)
```

3. **Type System**
   - Supports complex output types
   - Example: `output="title, headings: list[str], entities_and_metadata: list[dict[str, str]], type:Literal['news'...]"`

## Integration Strategy

Instead of reimplementing DSPy as a separate library, we can integrate its core concepts directly into Flock's architecture:

### 1. Enhanced DeclarativeAgent

```python
from typing import Any, Callable, Dict, List, Optional
from pydantic import BaseModel, Field

class AgentSignature(BaseModel):
    """Enhanced type system for agent signatures"""
    name: str
    input_field: str
    output_schema: Dict[str, Any]
    description: Optional[str] = None

class EnhancedDeclarativeAgent(Agent):
    """Enhanced declarative agent with integrated DSPy concepts"""
    signature: AgentSignature
    tools: List[Callable] = Field(default_factory=list)
    cache_config: Optional[Dict[str, Any]] = None
    execution_config: Optional[Dict[str, Any]] = None
    
    def __init__(
        self,
        name: str,
        input: str,
        output: str,
        tools: Optional[List[Callable]] = None,
        **config
    ):
        self.signature = self._parse_signature(name, input, output)
        self.tools = tools or []
        self.cache_config = config.get('cache_config')
        self.execution_config = config.get('execution_config')
        self._setup_execution_environment()
```

### 2. Integrated Execution System

```python
class ExecutionManager:
    """Manages agent execution with integrated DSPy concepts"""
    def __init__(self, agent: EnhancedDeclarativeAgent):
        self.agent = agent
        self.cache = self._setup_cache()
        self.tracer = self._setup_tracer()
        
    async def execute(self, input_data: Any) -> Any:
        # If tools are present, use ReAct-style execution
        if self.agent.tools:
            return await self._execute_with_tools(input_data)
        
        # Otherwise use basic prediction
        return await self._execute_basic(input_data)
        
    async def _execute_with_tools(self, input_data: Any) -> Any:
        trajectory = []
        
        while len(trajectory) < self.agent.execution_config.get('max_steps', 5):
            # Get next action
            action = await self._predict_next_action(input_data, trajectory)
            
            # Execute tool if needed
            if action.type == 'tool':
                result = await self._execute_tool(action.tool, action.args)
                trajectory.append(('tool', action.tool, result))
            
            # Check if complete
            if action.type == 'finish':
                return self._format_output(action.result)
                
            trajectory.append(('thought', action.thought))
```

### 3. Enhanced Type System

```python
class TypeParser:
    """Parses Flock's string-based types into structured schemas"""
    def parse_output_type(self, output_str: str) -> Dict[str, Any]:
        """Convert string type definition to structured schema"""
        # Parse complex types like:
        # "title, headings: list[str], metadata: dict[str, str]"
        pass

class OutputValidator:
    """Validates agent outputs against parsed schemas"""
    def validate(self, output: Any, schema: Dict[str, Any]) -> Any:
        """Validate and potentially coerce output to match schema"""
        pass
```

### 4. Integrated Tool System

```python
class ToolRegistry:
    """Enhanced tool management system"""
    def __init__(self):
        self.tools = {}
        self.tool_stats = {}
        
    def register(self, tool: Callable, metadata: Optional[Dict[str, Any]] = None):
        """Register a tool with enhanced metadata"""
        tool_id = self._generate_tool_id(tool)
        self.tools[tool_id] = {
            'func': tool,
            'metadata': metadata or {},
            'stats': {'calls': 0, 'errors': 0, 'avg_latency': 0}
        }
        
    async def execute(self, tool_id: str, **args) -> Any:
        """Execute tool with tracking and error handling"""
        tool_info = self.tools[tool_id]
        start_time = time.time()
        
        try:
            result = await tool_info['func'](**args)
            self._update_stats(tool_id, time.time() - start_time)
            return result
        except Exception as e:
            self._update_error_stats(tool_id, e)
            raise
```

## Implementation Plan

### Phase 1: Core Integration

1. **Enhanced Agent System**
```python
# flock/core/enhanced_agent.py
class EnhancedDeclarativeAgent(Agent):
    """Integrates DSPy concepts directly into Flock's agent system"""
    def __init__(self, name: str, input: str, output: str, tools: Optional[List[Callable]] = None):
        self.signature = self._parse_signature(name, input, output)
        self.execution_manager = ExecutionManager(self)
        
    async def execute(self, input_data: Any) -> Any:
        return await self.execution_manager.execute(input_data)
```

2. **Type System Integration**
```python
# flock/core/types.py
class TypeSystem:
    """Enhanced type system with DSPy integration"""
    def parse_signature(self, input_str: str, output_str: str) -> AgentSignature:
        input_schema = self._parse_type(input_str)
        output_schema = self._parse_type(output_str)
        return AgentSignature(input=input_schema, output=output_schema)
```

### Phase 2: Tool Integration

1. **Enhanced Tool System**
```python
# flock/core/tools.py
class EnhancedToolSystem:
    """Integrated tool system with DSPy concepts"""
    def __init__(self):
        self.registry = ToolRegistry()
        self.tracer = ToolTracer()
        
    def register_tool(self, tool: Callable, metadata: Dict[str, Any]):
        """Register tool with enhanced metadata"""
        self.registry.register(tool, metadata)
```

### Phase 3: Execution Integration

1. **Execution System**
```python
# flock/core/execution.py
class ExecutionSystem:
    """Integrated execution system"""
    def __init__(self, agent: EnhancedDeclarativeAgent):
        self.agent = agent
        self.type_system = TypeSystem()
        self.tool_system = EnhancedToolSystem()
```

## Benefits of Integration

1. **Simplified Architecture**
   - No separate DSPy dependency
   - Native integration with Flock's concepts
   - Cleaner codebase

2. **Enhanced Features**
   - Better type safety
   - Improved tool handling
   - Native caching and monitoring

3. **Better Developer Experience**
   - Simpler API
   - Consistent patterns
   - Better error messages

4. **Improved Performance**
   - Reduced overhead
   - Optimized execution paths
   - Better resource utilization

## Example Usage

```python
# Create an enhanced agent
agent = EnhancedDeclarativeAgent(
    name="research_agent",
    input="research_topic: str",
    output="""
        title: str,
        sections: list[dict[str, str]],
        references: list[str]
    """,
    tools=[web_search, code_eval],
    config={
        'cache_enabled': True,
        'max_steps': 10,
        'timeout': 30
    }
)

# Use it with Flock
runner = Flock()
runner.add_agent(agent)

result = await runner.run_async(
    start_agent=agent,
    input="Impact of AI on healthcare",
    local_debug=True
)
```

This integration approach maintains Flock's declarative nature while incorporating DSPy's powerful concepts directly into the framework, resulting in a more cohesive and powerful system.

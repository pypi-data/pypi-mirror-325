# Week 1: Core Infrastructure Implementation Plan

## Overview
Week 1 focuses on implementing the core infrastructure needed to support Flock's enhanced capabilities. This includes the base classes, type system, and fundamental execution components that will replace DSPy's functionality.

## Day-by-Day Implementation Plan

### Day 1: Base Infrastructure

1. **Create New Directory Structure**
```bash
flock/
├── core/
│   ├── __init__.py
│   ├── base.py        # Base classes
│   ├── config.py      # Configuration system
│   └── types/         # Type system
│       ├── __init__.py
│       ├── registry.py
│       ├── parser.py
│       └── validators.py
```

2. **Implement Base Classes** (core/base.py)
```python
class Module:
    """Base class for all Flock components"""
    def __init__(self):
        self.config = None
        self.type_registry = None
        
    async def initialize(self):
        """Async initialization if needed"""
        pass

class BaseAgent(Module):
    """Enhanced base agent class"""
    def __init__(
        self,
        name: str,
        type_registry: Optional['TypeRegistry'] = None,
        **kwargs
    ):
        super().__init__()
        self.name = name
        self.type_registry = type_registry or get_default_registry()
```

3. **Configuration System** (core/config.py)
```python
class Configuration:
    """Enhanced configuration management"""
    def __init__(self):
        self.settings = {}
        self.validators = {}
        
    def register_setting(
        self,
        key: str,
        default: Any,
        validator: Optional[Callable] = None
    ):
        pass
```

### Day 2: Type System Foundation

1. **Type Registry Implementation** (core/types/registry.py)
```python
class TypeRegistry:
    """Central type management system"""
    def __init__(self):
        self.types = {}
        self.validators = {}
        self.serializers = {}
        
    def register(
        self,
        type_name: str,
        validator: Callable,
        serializer: Optional[Callable] = None
    ):
        pass
```

2. **Type Parser** (core/types/parser.py)
```python
class TypeParser:
    """Parses string type definitions"""
    def parse_type_string(self, type_str: str) -> TypeDefinition:
        """Parse types like 'list[str]' or 'dict[str, int]'"""
        pass
    
    def parse_complex_type(self, type_str: str) -> TypeDefinition:
        """Parse complex types like 'title: str, data: list[dict[str, Any]]'"""
        pass
```

3. **Type Validators** (core/types/validators.py)
```python
class TypeValidator:
    """Validates values against type definitions"""
    def validate(self, value: Any, type_def: TypeDefinition) -> bool:
        pass
    
    def coerce(self, value: Any, type_def: TypeDefinition) -> Any:
        pass
```

### Day 3: Enhanced DeclarativeAgent

1. **Core Agent Implementation** (core/agents/declarative.py)
```python
class DeclarativeAgent(BaseAgent):
    """Enhanced declarative agent"""
    def __init__(
        self,
        name: str,
        input: str,
        output: str,
        tools: Optional[List[Callable]] = None,
        **kwargs
    ):
        super().__init__(name=name)
        self.input_type = self.type_registry.parse(input)
        self.output_type = self.type_registry.parse(output)
        self.tools = tools or []
        self._setup_execution_environment()
```

2. **Agent Execution System** (core/agents/execution.py)
```python
class ExecutionManager:
    """Manages agent execution"""
    def __init__(self, agent: DeclarativeAgent):
        self.agent = agent
        self.cache = self._setup_cache()
        
    async def execute(
        self,
        input_data: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> Any:
        validated_input = self.agent.input_type.validate(input_data)
        result = await self._execute_with_tools(validated_input, context)
        return self.agent.output_type.validate(result)
```

### Day 4: Tool Integration

1. **Enhanced Tool System** (core/tools/base.py)
```python
class Tool:
    """Enhanced tool wrapper"""
    def __init__(
        self,
        func: Callable,
        name: Optional[str] = None,
        description: Optional[str] = None
    ):
        self.func = func
        self.name = name or func.__name__
        self.description = description or func.__doc__
        self.signature = self._analyze_signature(func)
```

2. **Tool Manager** (core/tools/manager.py)
```python
class ToolManager:
    """Manages tool registration and execution"""
    def __init__(self):
        self.tools = {}
        self.stats = {}
        
    def register_tool(self, tool: Union[Tool, Callable]):
        """Register a new tool"""
        pass
        
    async def execute_tool(
        self,
        tool_name: str,
        args: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None
    ) -> Any:
        pass
```

### Day 5: Testing & Integration

1. **Test Infrastructure** (tests/)
```python
# tests/conftest.py
@pytest.fixture
def type_registry():
    registry = TypeRegistry()
    registry.register_builtin_types()
    return registry

# tests/test_types.py
def test_type_parsing():
    parser = TypeParser()
    type_def = parser.parse_type_string("list[dict[str, int]]")
    assert type_def.is_valid()
```

2. **Integration Tests** (tests/integration/)
```python
# tests/integration/test_agent_execution.py
async def test_basic_agent_execution():
    agent = DeclarativeAgent(
        name="test_agent",
        input="query: str",
        output="result: str"
    )
    result = await agent.execute("test query")
    assert isinstance(result, str)
```

3. **Example Implementation** (examples/week1/)
```python
# examples/week1/basic_agent.py
async def main():
    agent = DeclarativeAgent(
        name="example_agent",
        input="topic: str",
        output="summary: str, keywords: list[str]",
        tools=[web_search]
    )
    
    result = await agent.execute("artificial intelligence")
    print(f"Summary: {result.summary}")
    print(f"Keywords: {result.keywords}")
```

## Deliverables

By the end of Week 1, we will have:

1. **Core Infrastructure**
   - Base classes and configuration system
   - Type system with registry and parser
   - Enhanced DeclarativeAgent implementation

2. **Tool System**
   - Tool wrapper and manager
   - Basic tool execution capabilities
   - Tool statistics tracking

3. **Testing**
   - Test infrastructure
   - Core component tests
   - Integration tests
   - Example implementations

4. **Documentation**
   - API documentation
   - Usage examples
   - Type system guide

## Success Criteria

1. All core components implemented and tested
2. Type system supports basic and complex types
3. DeclarativeAgent can execute with and without tools
4. Test coverage > 80%
5. Documentation complete and up-to-date

## Next Steps

After completing Week 1:
1. Review implementation against requirements
2. Gather feedback from team
3. Plan Week 2 (Provider System implementation)
4. Address any technical debt

This plan provides a structured approach to implementing the core infrastructure while maintaining quality and testability.

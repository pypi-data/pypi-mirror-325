# Week 2: Provider System & Context Implementation Plan

## Overview
Week 2 focuses on implementing the provider system and context management, building on the core infrastructure from Week 1.

## Day-by-Day Implementation Plan

### Day 1: Provider System Foundation

1. **Provider Base Classes** (core/providers/base.py)
```python
class Provider(BaseModel):
    """Base provider class"""
    name: str
    events: List[str]
    priority: int = 0
    
    async def initialize(self):
        """Provider initialization"""
        pass
    
    async def handle_event(self, event: str, data: Any):
        """Handle provider events"""
        raise NotImplementedError

class ProviderRegistry:
    """Central provider registry"""
    def __init__(self):
        self.providers: Dict[str, List[Provider]] = {}
        
    def register(self, provider: Provider):
        """Register provider for its events"""
        for event in provider.events:
            if event not in self.providers:
                self.providers[event] = []
            self.providers[event].append(provider)
            self.providers[event].sort(key=lambda p: p.priority)
```

2. **Event System** (core/providers/events.py)
```python
class Event(BaseModel):
    """Event data container"""
    name: str
    data: Any
    metadata: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.now)

class EventDispatcher:
    """Event dispatch system"""
    def __init__(self, registry: ProviderRegistry):
        self.registry = registry
        
    async def dispatch(self, event: str, data: Any):
        """Dispatch event to registered providers"""
        event_obj = Event(name=event, data=data)
        providers = self.registry.providers.get(event, [])
        
        for provider in providers:
            try:
                await provider.handle_event(event, data)
            except Exception as e:
                logger.error(f"Provider {provider.name} failed: {e}")
```

### Day 2: Core Providers

1. **Vector Store Provider** (core/providers/vector_store.py)
```python
class VectorStoreProvider(Provider):
    """Stores agent outputs in vector database"""
    events = ["agent_complete", "knowledge_update"]
    
    def __init__(self, connection_string: str):
        self.connection = self._setup_connection(connection_string)
        
    async def handle_event(self, event: str, data: Any):
        if event == "agent_complete":
            await self.store_output(data)
        elif event == "knowledge_update":
            await self.update_embeddings(data)
```

2. **Metrics Provider** (core/providers/metrics.py)
```python
class MetricsProvider(Provider):
    """Collects and reports metrics"""
    events = ["agent_start", "agent_complete", "tool_execute"]
    
    def __init__(self, metrics_client: Any):
        self.client = metrics_client
        self.metrics = defaultdict(list)
        
    async def handle_event(self, event: str, data: Any):
        if event == "agent_complete":
            self._record_completion_metrics(data)
        elif event == "tool_execute":
            self._record_tool_metrics(data)
```

### Day 3: Context System

1. **Context Management** (core/context/manager.py)
```python
class ExecutionContext(BaseModel):
    """Rich execution context"""
    context_id: str = Field(default_factory=lambda: str(uuid4()))
    parent_id: Optional[str] = None
    agent_id: str
    start_time: datetime = Field(default_factory=datetime.now)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    state: Dict[str, Any] = Field(default_factory=dict)
    
    def fork(self, new_agent_id: str) -> 'ExecutionContext':
        """Create new context inheriting from current"""
        return ExecutionContext(
            parent_id=self.context_id,
            agent_id=new_agent_id,
            metadata=self.metadata.copy()
        )

class ContextManager:
    """Manages execution contexts"""
    def __init__(self):
        self.contexts: Dict[str, ExecutionContext] = {}
        self.active_context: Optional[str] = None
        
    def create_context(self, agent_id: str) -> ExecutionContext:
        """Create new execution context"""
        context = ExecutionContext(agent_id=agent_id)
        self.contexts[context.context_id] = context
        return context
        
    def get_current_context(self) -> Optional[ExecutionContext]:
        """Get currently active context"""
        return self.contexts.get(self.active_context)
```

### Day 4: Provider Middleware & Integration

1. **Provider Middleware** (core/providers/middleware.py)
```python
class ProviderMiddleware:
    """Middleware for provider execution"""
    async def pre_execute(
        self,
        provider: Provider,
        event: str,
        data: Any
    ) -> Any:
        """Pre-execution hook"""
        return data
        
    async def post_execute(
        self,
        provider: Provider,
        event: str,
        result: Any
    ) -> Any:
        """Post-execution hook"""
        return result

class LoggingMiddleware(ProviderMiddleware):
    """Logs provider execution"""
    async def pre_execute(
        self,
        provider: Provider,
        event: str,
        data: Any
    ) -> Any:
        logger.info(f"Executing {provider.name} for {event}")
        return data
        
    async def post_execute(
        self,
        provider: Provider,
        event: str,
        result: Any
    ) -> Any:
        logger.info(f"Completed {provider.name} for {event}")
        return result
```

2. **Agent Integration** (core/agents/declarative.py)
```python
class EnhancedDeclarativeAgent(BaseAgent):
    """Agent with provider & context support"""
    def __init__(
        self,
        name: str,
        input: str,
        output: str,
        providers: Optional[List[Provider]] = None,
        **kwargs
    ):
        super().__init__(name=name, **kwargs)
        self.providers = providers or []
        self.context_manager = ContextManager()
        self._register_providers()
        
    async def execute(
        self,
        input_data: Any,
        context: Optional[ExecutionContext] = None
    ) -> Any:
        context = context or self.context_manager.create_context(self.name)
        self.context_manager.active_context = context.context_id
        
        try:
            await self.dispatch_event("agent_start", input_data)
            result = await super().execute(input_data)
            await self.dispatch_event("agent_complete", result)
            return result
        finally:
            self.context_manager.active_context = None
```

### Day 5: Testing & Documentation

1. **Provider Tests** (tests/providers/)
```python
# tests/providers/test_vector_store.py
async def test_vector_store_provider():
    provider = VectorStoreProvider("test://connection")
    await provider.handle_event(
        "agent_complete",
        {"output": "test data"}
    )
    assert await provider.get_stored_data() == "test data"

# tests/providers/test_metrics.py
async def test_metrics_provider():
    provider = MetricsProvider(MockMetricsClient())
    await provider.handle_event(
        "tool_execute",
        {"tool": "search", "duration": 1.5}
    )
    assert provider.metrics["tool_duration"] == [1.5]
```

2. **Context Tests** (tests/context/)
```python
# tests/context/test_manager.py
def test_context_inheritance():
    manager = ContextManager()
    parent = manager.create_context("parent_agent")
    child = parent.fork("child_agent")
    
    assert child.parent_id == parent.context_id
    assert child.metadata == parent.metadata
```

3. **Integration Tests** (tests/integration/)
```python
# tests/integration/test_provider_integration.py
async def test_agent_with_providers():
    agent = EnhancedDeclarativeAgent(
        name="test_agent",
        input="query: str",
        output="result: str",
        providers=[
            VectorStoreProvider("test://db"),
            MetricsProvider(metrics_client)
        ]
    )
    
    result = await agent.execute("test query")
    assert result
    # Verify provider side effects
```

## Deliverables

1. **Provider System**
   - Base provider infrastructure
   - Event dispatch system
   - Core providers (Vector Store, Metrics)
   - Provider middleware

2. **Context System**
   - Context management
   - Context inheritance
   - State tracking
   - Integration with agents

3. **Testing & Documentation**
   - Provider tests
   - Context tests
   - Integration tests
   - API documentation

## Success Criteria

1. Providers can handle events reliably
2. Context system manages state effectively
3. Agent integration is seamless
4. Test coverage > 80%
5. Documentation complete

## Next Steps

1. Review implementation against requirements
2. Gather feedback from team
3. Plan Week 3 (Agent Orchestration)
4. Address any technical debt

This plan provides a structured approach to implementing the provider and context systems while maintaining quality and testability.

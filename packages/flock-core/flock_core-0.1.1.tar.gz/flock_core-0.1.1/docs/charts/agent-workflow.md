sequenceDiagram
    participant User
    participant Flock
    participant Agent
    participant Tools
    participant LLM
    participant Temporal

    User->>Flock: Create Agent
    Flock->>Agent: Initialize
    User->>Flock: activate(agent, input)
    
    alt Local Debug Mode
        Flock->>Agent: Execute Directly
    else Production Mode
        Flock->>Temporal: Start Workflow
        Temporal->>Agent: Execute via Activity
    end

    loop Agent Execution
        Agent->>LLM: Process Input
        opt Tool Usage
            Agent->>Tools: Execute Tool
            Tools-->>Agent: Tool Result
        end
        Agent->>LLM: Generate Output
    end

    alt Has Hand-off
        Agent->>Flock: Hand off to Next Agent
        Flock->>Agent: Start Next Agent
    else No Hand-off
        Agent-->>Flock: Return Result
    end

    Flock-->>User: Return Final Result

```

This sequence diagram illustrates the workflow of agent execution:
- Shows both local debug and production modes
- Demonstrates tool usage flow
- Illustrates agent hand-off mechanism
- Shows interaction with LLM providers

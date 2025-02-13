graph TB
    subgraph User Application
        UA[User Code] --> |Uses| SM[Flock Manager]
    end

    subgraph Flock Core
        SM --> |Manages| AR[Agent Registry]
        SM --> |Executes| WF[Workflow System]
        
        subgraph Agents
            AR --> |Registers| DA[Declarative Agent]
            DA --> |Uses| TS[Type System]
            DA --> |Uses| TM[Tool Manager]
        end
        
        subgraph Workflow
            WF --> |Runs| AC[Activities]
            WF --> |Uses| TW[Temporal Worker]
            AC --> |Executes| DA
        end
    end

    subgraph External Systems
        TW --> |Connects to| TS1[Temporal Server]
        TM --> |Integrates| T1[Web Search]
        TM --> |Integrates| T2[Code Eval]
        TM --> |Integrates| T3[Math Tools]
        DA --> |Uses| LLM[LLM Provider]
    end

    classDef core fill:#f9f,stroke:#333,stroke-width:2px
    classDef external fill:#bbf,stroke:#333,stroke-width:2px
    classDef user fill:#bfb,stroke:#333,stroke-width:2px
    
    class SM,AR,DA,WF,AC,TM,TS core
    class TS1,T1,T2,T3,LLM external
    class UA user
```

This diagram shows the core architecture of Flock, illustrating how different components interact:
- User applications interact with the Flock Manager
- The Flock Manager coordinates agents and workflows
- Declarative Agents use the type system and tool manager
- The workflow system handles execution through Temporal
- External integrations include tools and LLM providers

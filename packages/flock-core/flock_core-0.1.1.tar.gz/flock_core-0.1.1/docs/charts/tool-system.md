graph TB
    subgraph Tool Management
        TM[Tool Manager] --> |Manages| TR[Tool Registry]
        TR --> |Registers| T1[Web Search Tool]
        TR --> |Registers| T2[Code Eval Tool]
        TR --> |Registers| T3[Math Tool]
        
        TM --> |Provides| TI[Tool Interface]
        TI --> |Used by| DA[Declarative Agent]
    end

    subgraph Tool Execution
        T1 --> |Uses| WS[Web Search API]
        T2 --> |Uses| CE[Code Executor]
        T3 --> |Uses| ME[Math Engine]
        
        WS --> |Returns| R1[Search Results]
        CE --> |Returns| R2[Execution Results]
        ME --> |Returns| R3[Math Results]
    end

    subgraph Error Handling
        TM --> |Manages| EH[Error Handler]
        EH --> |Handles| E1[API Errors]
        EH --> |Handles| E2[Execution Errors]
        EH --> |Handles| E3[Validation Errors]
    end

    classDef core fill:#f9f,stroke:#333,stroke-width:2px
    classDef tool fill:#bbf,stroke:#333,stroke-width:2px
    classDef handler fill:#bfb,stroke:#333,stroke-width:2px

    class TM,TR,TI core
    class T1,T2,T3,WS,CE,ME tool
    class EH,E1,E2,E3 handler
```

This diagram illustrates the tool system architecture:
- Tool Manager coordinates tool registration and execution
- Shows integration with external APIs and services
- Demonstrates error handling mechanisms
- Shows how tools interface with agents

graph TB
    subgraph Temporal Integration
        WF[Workflow System] --> |Manages| TW[Temporal Worker]
        TW --> |Executes| AC[Activities]
        TW --> |Connects to| TS[Temporal Server]
        
        subgraph State Management
            TS --> |Manages| WS[Workflow State]
            WS --> |Tracks| AS[Agent State]
            WS --> |Tracks| TS1[Tool State]
            WS --> |Tracks| ES[Error State]
        end

        subgraph Reliability Features
            TS --> |Provides| R1[Automatic Retries]
            TS --> |Provides| R2[Error Recovery]
            TS --> |Provides| R3[State Persistence]
            TS --> |Provides| R4[Workflow History]
        end

        subgraph Monitoring
            TS --> |Enables| M1[Execution Metrics]
            TS --> |Enables| M2[Error Tracking]
            TS --> |Enables| M3[Performance Stats]
            TS --> |Enables| M4[Workflow Visualization]
        end
    end

    classDef core fill:#f9f,stroke:#333,stroke-width:2px
    classDef state fill:#bbf,stroke:#333,stroke-width:2px
    classDef feature fill:#bfb,stroke:#333,stroke-width:2px
    classDef monitor fill:#fbb,stroke:#333,stroke-width:2px

    class WF,TW,AC,TS core
    class WS,AS,TS1,ES state
    class R1,R2,R3,R4 feature
    class M1,M2,M3,M4 monitor
```

This diagram illustrates Flock's temporal workflow integration:
- Shows how Temporal provides workflow management
- Demonstrates state tracking capabilities
- Highlights reliability features
- Shows monitoring and observability features

classDiagram
    class TypeSystem {
        +register_type(name, validator, serializer)
        +validate(value, type_def)
        +parse_type_string(type_str)
        -_validate_complex_type(value, type_def)
    }

    class TypeDefinition {
        +name: str
        +validators: List
        +serializers: Optional
        +validate(value)
        +serialize(value)
    }

    class DeclarativeAgent {
        +input: str
        +output: str
        +tools: List
        +validate_input(value)
        +validate_output(value)
    }

    class Validator {
        +validate(value)
        +coerce(value)
    }

    TypeSystem --> TypeDefinition : manages
    DeclarativeAgent --> TypeSystem : uses
    TypeDefinition --> Validator : uses

```

This class diagram shows the type system architecture:
- TypeSystem manages type definitions
- DeclarativeAgent uses type system for validation
- Shows relationship between components
- Illustrates validation flow

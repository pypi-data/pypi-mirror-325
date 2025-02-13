```python

agent_activities:

Batch + Decl


```

Below is a comprehensive “to‑do” list that I’ve derived by reading every file and line in your initial framework. This list is organized by overall concerns, then by module/feature. It should serve as a roadmap for cleaning up, refactoring, and adding features before a beta release.

---

## Overall Architecture and Best Practices

- **Consistent API & Naming Conventions**  
  - Ensure that all agents follow a consistent interface (e.g. properties like `input`, `output`, `tools`, etc.).  
  - Remove duplicate logic across different agent types (Declarative, Batch, User, Loop, Trigger).  
  - Clearly separate local execution logic from Temporal-specific logic (for example, by having common “evaluation” methods and separate `run_temporal()` methods).

- **Error Handling and Logging**  
  - Add robust error handling (e.g. try/except blocks) in all agents, activities, and workflows.  
  - Replace any ad hoc error reporting (like returning dictionaries with an `"error"` key) with standardized error handling or exception classes.  
  - Integrate a logging framework instead of using print/debug statements so that logs are captured consistently across local runs and Temporal activities.

- **Configuration and Dependency Injection**  
  - Externalize configuration (such as Temporal connection settings, task queue names, timeouts, and even model settings) so that they are not hard-coded.  
  - Use a configuration file or environment variables (see your `declarative_agent_config.py`) for agent and framework parameters.

- **Testing and Documentation**  
  - Write unit tests for each module (agent logic, registry, context, Temporal integration, etc.).  
  - Build integration tests that run example flows end-to-end (e.g., simulating a full hand-off chain).  
  - Update documentation and examples so that the intended usage is crystal clear (especially for the handoff mechanism and multi‑input support).

---

## Module‑Specific To‑Dos

### 1. `src/flock/core/agent.py`
- **Agent Base Class**  
  - **Implement `run_temporal`:**  
    The abstract `run_temporal()` is currently a stub. Decide on a common Temporal API for all agents (possibly by having a default implementation that calls an activity) and document its behavior.
  - **Agent Lifecycle & Termination:**  
    Consider adding lifecycle hooks (initialization, termination) or a mechanism to support termination conditions (e.g., for a UserAgent with a termination phrase).

### 2. `src/flock/core/agent_registry.py`
- **Registry Implementation**  
  - **Data Structures:**  
    Replace the internal lists (`_agents`, `_tools`) with dictionaries keyed by unique identifiers (names) for faster lookups and to avoid duplicates.  
  - **Error Reporting:**  
    When an agent or tool is not found, consider raising a custom exception rather than returning `None`.
  - **Thread/Async Safety:**  
    Since Temporal and asynchronous execution are involved, ensure that the Registry’s singleton implementation is thread‑safe or document any limitations.

### 3. `src/flock/core/context.py`
- **FlockContext Data Type**  
  - **State Management:**  
    Review how state is merged (in `record()`) to ensure that overwriting keys is acceptable or if you need a more sophisticated merge strategy.  
  - **Input Extraction:**  
    The method `next_input_for()` is key to agent chaining. Consider adding more robust parsing of multi‑key inputs and reserved keywords (like `"context"`, `"init_input"`) with validation.
  - **Typing and Documentation:**  
    Flesh out type annotations for history and agent definitions and ensure that every method is well documented.

### 4. `src/flock/core/flock.py`
- **Flock Manager**  
  - **Agent and Tool Registration:**  
    Verify that tools are correctly registered and that their names do not conflict with agent names.  
  - **Temporal Worker Management:**  
    In `run_async()`, the Temporal worker is started via `asyncio.create_task(worker.run())` and then a sleep is inserted.  
    - **TODO:** Refactor this to a more robust startup/shutdown procedure and handle possible worker failures.  
  - **Context Handling:**  
    Ensure that the FlockContext is passed properly through the workflow and that its state is correctly updated when agents run.

### 5. Agents

#### DeclarativeAgent (src/flock/core/agents/declarative_agent.py)
- **Multiple Inputs Support:**  
  - Ensure that the logic for splitting and cleaning the comma‑separated `input` and `output` strings is robust (for example, stripping type annotations).
- **dspy Integration:**  
  - Consolidate the dspy logic (choosing between `ReAct` and `Predict`) so that it is not repeated between the local and Temporal paths.
- **Local vs. Temporal Execution:**  
  - Implement a clean separation between `_evaluate_agent` and `_evaluate_agent_t` so that the Temporal activity calls the same evaluation logic.
- **Caching:**  
  - If `use_cache` is enabled, add a caching layer to avoid repeated calls to the same model when inputs haven’t changed.

#### BatchAgent (src/flock/core/agents/batch_agent.py)
- **Batch Processing:**  
  - Remove duplication between `_run_single_batch` and `_run_single_batch_temporal` by reusing common evaluation code.  
  - Improve the aggregation mechanism for batch results (consider error aggregation or partial failures).
- **Temporal Batch Processing:**  
  - Ensure that each batch’s Temporal activity is uniquely identified (currently using a UUID) and that the aggregated result properly reflects all batches.
- **Consistency with DeclarativeAgent:**  
  - Share the input parsing and dspy invocation logic with DeclarativeAgent to reduce code duplication.

#### LoopAgent and TriggerAgent
- **LoopAgent:**  
  - Currently a skeleton. Decide on its intended behavior (e.g., repeating an agent’s execution until a condition is met) and implement accordingly.
- **TriggerAgent:**  
  - Implement the logic for a trigger‑based agent (e.g., waiting for an event or external signal) or clearly mark it as a work‑in‑progress.

#### UserAgent (src/flock/core/agents/user_agent.py)
- **User Interaction and Termination:**  
  - The code mentions a termination attribute and a “message history” (used in example 06), but these are not fully implemented.  
    - **TODO:** Define how termination is detected and how conversation history is stored and passed along.
- **Consolidation with DeclarativeAgent:**  
  - Much of the dspy call logic is repeated here. Consider subclassing or sharing common code with DeclarativeAgent.

### 6. Handoff Logic (`src/flock/core/handoff/handoff_base.py`)
- **HandoffBase Definition:**  
  - Currently, `HandoffBase` only defines some attributes but no behavior.  
    - **TODO:** Create a clear interface (or even an abstract base class) for handoff implementations that specifies:
      - What fields are expected (e.g., `next_agent`, `input`, `context_params`).
      - How a handoff function should be structured (should it return an instance of HandoffBase or a dictionary?).
  - **Usage Consistency:**  
    - In the workflow activity (`activities.py`), handoff data is sometimes accessed as an attribute and sometimes as a dictionary (e.g., `handoff_data["input"]` vs. `handoff_data.input`). This needs to be standardized.

### 7. Tools (`src/flock/core/tools/basic_tools.py`)
- **Error Handling:**  
  - Many functions (such as web search, content fetching, and code evaluation) have minimal error handling.  
    - **TODO:** Add try/except blocks and more informative error messages/logging.  
- **Dependencies:**  
  - Validate that external dependencies (like `tavily`, `httpx`, `markdownify`, and `dspy`) are well encapsulated and consider providing mocks or fallbacks for testing.
- **Return Types:**  
  - Where applicable, add type hints and validate the output (for example, ensuring that the output of `extract_numbers` is indeed a list of floats).

### 8. Workflow and Activities

#### Activities (`src/flock/workflow/activities.py`)
- **run_agent Activity:**  
  - The main agent execution loop here needs to handle:
    - Proper lookup of agents from the registry.
    - Clear logic for how input is determined for the next agent (using `next_input_for`).
    - Consistent handoff handling, as noted above (e.g., handling callable vs. string vs. Agent types for `hand_off`).
  - **TODO:** Validate that the recorded history and state updates in FlockContext are correct and that no state is lost when chaining agents.
- **get_next_agent Activity:**  
  - This is very simple, but consider if additional validation or caching is needed.
  
#### Temporal Setup (`src/flock/workflow/temporal_setup.py`)
- **Temporal Client and Worker:**  
  - Make connection parameters (host, namespace, task queue) configurable.  
  - Consider adding retry policies or more sophisticated error handling if the connection fails.
- **Activity Invocation:**  
  - Ensure that the helper `run_activity` is used consistently and that its timeout settings are appropriate for your agents’ expected runtime.

#### Workflow (`src/flock/workflow/workflow.py`)
- **FlockWorkflow:**  
  - Validate that the workflow correctly records agent run results and updates the context’s agent history.  
  - The handling of exceptions in the workflow should be standardized; you might want to propagate errors up or record detailed failure messages.
  - **Timing and Retries:**  
    - Check that the use of `start_to_close_timeout` is sufficient and that workflow timeouts/retries are well documented.

### 9. Examples (Under `examples/misc/`)
- **Example Consistency:**  
  - Verify that each example (simple example, typed output, tool agent, handoff, chat) works with the refactored agents and workflow.  
  - Update examples to use the new handoff interface and multiple inputs if needed.
- **Chat and Handoff Examples:**  
  - In example 06, the handoff function refers to `agent.message_history` and uses a HandoffBase instance with a field called `context_params` that is not defined.  
    - **TODO:** Implement the expected fields for a chat agent and standardize handoff between user and chat agents.

---

## Future Features and Enhancements

- **Caching Support:**  
  - Implement caching for agents (when `use_cache` is `True`) to avoid repeated work for identical inputs.
- **Typed Output Verification:**  
  - Enable agents to validate and convert their output to the declared types (e.g., converting strings to lists or dicts based on the output schema).
- **Improved Agent Chaining:**  
  - Develop a more formal DSL (domain-specific language) for specifying handoffs and chaining, perhaps even allowing conditional branching.
- **Extensible Tool Interface:**  
  - Define a protocol or interface for tools so that third-party tools can be integrated seamlessly.
- **Agent Lifecycle Management:**  
  - Add support for initialization, periodic tasks, and graceful shutdown within agents.

---

By addressing these items, you’ll improve the maintainability, robustness, and extensibility of the framework before its beta release. Each point should be reviewed in the context of your overall design goals and prioritized according to what’s most critical for a stable beta.

# ATLAS Workflow: Visual System Planning

> **Goal:** Render architectural intent, data flow, and structural topologies using clear Mermaid diagrams to eliminate ambiguity between Council entities and the user.

---

## Supported Visual Formats

### 1. Subsystem Architecture (Graph / Flowchart)
```mermaid
flowchart TD
    User([User Prompt / Voice]) --> UI[UI / CLI / Voice Layer]
    UI --> Manager[Provider / Session Manager]
    Manager --> Core[Core Engine / Planner]
    Core --> Services[Services: Memory, Automation, LLM]
    Services --> Models[Domain Models & Invariants]
```

### 2. Sequence of Interaction
```mermaid
sequenceDiagram
    participant User
    participant Router as Command Router
    participant Service as Target Service
    participant Memory as Memory Service

    User->>Router: /remember <fact>
    Router->>Service: Parse command & validate input
    Service->>Memory: save_memory(fact)
    Memory-->>Service: Confirmation
    Service-->>User: Memory acknowledged
```

### 3. Guidelines
- Diagram all cross-boundary interactions before refactoring.
- Include failure paths and fallback loops.
- Keep diagrams concise: focus on the subsystems directly affected.


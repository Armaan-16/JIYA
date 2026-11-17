# HERMES Reference: Subagent Delegation Patterns

> **Mandate:** Delegate effectively to keep the primary orchestrator focused, fast, and free of context pollution.

---

## Delegation Scenarios

| Scenario | Subagent Type | Instructions & Scope |
|---|---|---|
| **Deep Codebase Exploration** | `research` | Read-only survey of large directories, searching symbols, or analyzing legacy logs. |
| **Isolated Architectural Spike** | `self` (isolated) | Test an isolated prototype without cluttering the primary agent context. |
| **Independent Parallel Waves** | `self` | Execute non-conflicting wave components with distinct file targets. |

---

## The Clean Delegation Contract
When invoking a subagent:
1. **Clear, Bounded Goal:** Define precisely what to investigate or build.
2. **Target File Links:** Provide direct file links rather than vague descriptions.
3. **Structured Return Schema:** Demand a concise summary or diff rather than an unstructured chat log.


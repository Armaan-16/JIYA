# RALPH LOOP Principles: Autonomous Iteration & Resilience

> *"Context windows are fleeting; the filesystem is forever."*

---

## Foundational Tenets

1. **Autonomous Durability:**
   - LLMs suffer from transient context wipes, conversation truncation, and network hiccups. An agent that relies exclusively on conversational memory will inevitably drop tasks.
   - Externalizing state to disk makes an agent crash-proof.

2. **Atomic Steps Over Big Bangs:**
   - Break every complicated journey into single, indivisible steps.
   - If an atomic step fails, you only need to diagnose and fix that single step.

3. **Append-Only Truth:**
   - Never rewrite your history. Log what was attempted and what happened. This provides full observability and auditability for humans and peer agents.


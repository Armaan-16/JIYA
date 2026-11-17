# ECC Principles: Zero-Trust Security & Engineering Rigor

> Reference architecture for secure agentic systems.

---

## 1. Zero Trust in Agent Environments
AI agents operating in developer workspaces hold substantial privilege: executing code, installing packages, modifying git histories, and invoking APIs. Consequently:
- Every action must be bounded.
- All external inputs must be validated against schemas.
- Blast radiuses of autonomous scripts must be confined.

## 2. Token Budgeting as an Architectural Constraint
Just as embedded software engineers budget RAM and CPU cycles, autonomous agent systems must budget token context. Context exhaustion leads to:
- "Lost in the middle" attention failure.
- Truncated code edits and broken syntaxes.
- Hallucinated imports and forgotten project constraints.
Treat context consumption as a primary engineering metric.


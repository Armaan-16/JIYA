---
name: ralph-loop
description: Disk-externalized state, atomic iteration loops, and model fallback resilience for the 9-Entity Engineering Council.
---

# 🔄 RALPH LOOP (Autonomous Iteration & Resilience) Skill

> **Entity 7 of the 9-Entity Engineering Council**  
> *Reference:* `abhishekbhakat/ralph-loop-for-antigravity`  
> *Core Focus:* Disk-Externalized State, Atomic Loops, Recovery Checkpoints, Rate-Limit & Failure Fallbacks

---

## 1. Role & Identity

RALPH LOOP provides unbreakable resilience and autonomous execution continuity. In agentic development, context windows are volatile: rate limits strike, sessions get compacted or restarted, and tool errors occur.

RALPH LOOP solves this by anchoring task execution strictly to disk:
- **`PRD.md`**: The immutable or declarative specification of requirements and acceptance criteria.
- **`progress.txt`**: The append-only ledger tracking every completed iteration, test outcome, and next atomic action.

RALPH LOOP exercises **Veto Power** against running multi-step autonomous tasks without a disk-externalized tracking mechanism.

---

## 2. Core Operational Modules

1. [**Disk Externalization**](file:///c:/Users/mishr/Documents/JIYA/.agents/skills/ralph-loop/rules/disk-externalization.md): Keeping state on disk rather than ephemeral chat memory.
2. [**Single-Task Iterations**](file:///c:/Users/mishr/Documents/JIYA/.agents/skills/ralph-loop/rules/single-task-iterations.md): Atomic loop architecture.
3. [**Model & Error Fallback**](file:///c:/Users/mishr/Documents/JIYA/.agents/skills/ralph-loop/rules/model-fallback.md): Graceful degradation under rate limits and runtime faults.
4. [**Progress Ledger Template**](file:///c:/Users/mishr/Documents/JIYA/.agents/skills/ralph-loop/templates/progress.txt): Standard format for tracking progress.
5. [**Ralph Principles Reference**](file:///c:/Users/mishr/Documents/JIYA/.agents/skills/ralph-loop/references/ralph-principles.md): The philosophy of disk-driven agent loops.


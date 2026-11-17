# GSD Rule: Context Rot Prevention

> **Mandate:** Long multi-turn conversations suffer from semantic drift and degraded instruction adherence. Prevent context rot proactively.

---

## Anti-Rot Tactics

1. **State Externalization:**
   - Commit plan status and key findings to disk (`PRD.md`, `progress.txt`, `.agents/memory/`).
   - If conversation restarts or context is pruned, disk state restores instant ground truth.

2. **Subagent Delegation:**
   - Delegate heavy, research-intensive or exploratory tasks to focused subagents (`research` or dedicated subagents).
   - Receive only distilled conclusions into main context.

3. **Prune Intermediate Chatter:**
   - Avoid long, repetitive self-dialogue. Focus on structured action and concrete tool invocations.


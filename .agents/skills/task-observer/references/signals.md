# TASK OBSERVER Reference: Taxonomy of Friction Signals

> Signals that trigger an immediate observation log entry.

---

## 1. USER_CORRECTION
- The user rejects an agent's proposed plan.
- The user notes: *"No, that's not what I asked"* or *"Use standard library instead"*.
- The user has to manually provide a file path or environment detail the agent should have discovered.

## 2. TOOL_FRICTION
- A PowerShell command failed with non-zero exit code or encoding error.
- A file edit tool returned "TargetContent not found" or mismatched line numbers.
- A subprocess hung due to missing timeout or interactive stdin expectation.

## 3. SKILL_GAP
- The agent was tasked with a specialized domain (e.g. Windows Audio API, vector embedding indexing) and lacked structured workflow guidance.
- Multiple attempts were required to figure out the right invocation parameters.

## 4. AMBIGUITY
- A user request had multiple viable interpretations and the agent guessed rather than using `ask_question` or consulting Council escalation guidelines.


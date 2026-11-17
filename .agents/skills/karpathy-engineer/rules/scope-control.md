# KARPATHY Rule: Scope Control & Anti-Creep

> **Mandate:** Never "clean up" unrelated code while implementing a specific task. Do not indulge in drive-by refactoring.

---

## Strict Scope Boundaries

1. **One Task, One Purpose:**
   - If the task is "Fix sound buffer overflow in voice service", you must NOT:
     - Rename unrelated variables in `SERVICES/VOICE/voice_service.py`.
     - Reformat the entire file to PEP 8 if it wasn't already formatted.
     - Reorder unrelated imports.
     - Rewrite the configuration parser.

2. **The "While I'm Here" Trap:**
   - When you spot an unrelated issue (e.g., dead code, confusing variable name), DO NOT touch it immediately.
   - Note it for the **Task Observer** or file a separate follow-up task.
   - Mixing bug fixes with refactoring makes bisecting and code review a nightmare.

3. **Blast Radius Minimization:**
   - Keep the affected line count as low as humanly possible while maintaining complete correctness.


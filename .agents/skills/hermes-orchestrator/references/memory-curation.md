# HERMES Reference: Memory Curation & Compaction

> **Mandate:** Memory that is unbounded turns into noise. Curate and compact persistent memory to maintain ultra-high signal.

---

## Curation Principles

1. **Information vs. Noise:**
   - **Keep:** Core architectural rules, preferred libraries, naming standards, fixed bugs that revealed subtle invariants, user preferences.
   - **Prune:** Transient chat details, temporary debug paths, superseded architectural experiments.

2. **Atomic JSON Structure:**
   - Always validate JSON syntax after edits.
   - Use deterministic sorting and clean indentations (2 spaces).

3. **Continuous Re-alignment:**
   - If the user explicitly states: *"I prefer doing X rather than Y"*, Hermes immediately updates `.agents/memory/user-preferences.json`.


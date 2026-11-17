# CODERABBIT Rule: AST-Aware Contextual Review

> **Mandate:** Code cannot be reviewed in isolation. Every change must be evaluated against its full dependency graph and caller footprint.

---

## The 4-Step Blast Radius Audit

### 1. Inward Callers (Who calls this?)
- Search for all references to modified functions, classes, and constants across `CORE/`, `SERVICES/`, `UI/`, `VOICE/`, `AUTOMATION/`, and `main.py`.
- Verify that every caller provides arguments conforming to updated signatures.

### 2. Outward Dependencies (What does this call?)
- Inspect external services and imports invoked by the modified code.
- Ensure all imported modules actually exist and exports match expectation.

### 3. Edge Case Matrix
Evaluate behavior under abnormal conditions:
- `None` or empty collections passed into methods.
- Network or subprocess timeouts.
- File system permissions or missing paths.
- Encoding discrepancies (UTF-8 vs ANSI on Windows).

### 4. State & Concurrency
- Are shared instances (like `MemoryService` or `ProviderManager`) safely accessed?
- Are global mutable structures avoided?


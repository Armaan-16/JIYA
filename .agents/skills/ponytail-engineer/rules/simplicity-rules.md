# PONYTAIL Rule: Quantitative Simplicity Guardrails

> **Mandate:** Code must remain mathematically and structurally simple. The following limits act as tripwires.

---

## Concrete Complexity Limits

1. **Function Size:**
   - Soft limit: 30 lines. Hard limit: 60 lines.
   - If a function exceeds 60 lines, it must be decomposed into focused helper functions.

2. **Cyclomatic Complexity:**
   - Maximum cyclomatic complexity per function: 8.
   - Avoid deep nesting (more than 3 levels of `if`/`for`/`while` indentation is an immediate refactoring signal).

3. **Class Hierarchy Depth:**
   - Prefer composition over inheritance.
   - Maximum inheritance depth: 2 levels (Base $\to$ Derived). Multi-level abstract factory hierarchies are prohibited.

4. **Parameter Count:**
   - Maximum function parameters: 5.
   - If a function requires > 5 arguments, group related configurations into a `@dataclass` or dedicated options object.

5. **File Size:**
   - Target: Under 300 lines per module. Files approaching 500 lines must be reviewed for subsystem extraction.


# CODERABBIT Rule: High-Signal Feedback Classification

> **Mandate:** Eliminate nitpick clutter. Provide actionable, prioritized, concrete feedback with explicit code remedies.

---

## Severity Tiers

1. **🚨 CRITICAL (Must Fix Before Merge):**
   - Security flaws, memory leaks, unhandled exceptions leading to crashes, broken backward compatibility for callers.
   - Example: *"Caller in `main.py#L45` passes 2 args, but new signature requires 3 mandatory args. Immediate crash on invocation."*

2. **⚠️ MAJOR (Should Fix):**
   - Architectural drift, non-idiomatic patterns, missing test cases for important edge branches, potential race conditions.

3. **ℹ️ MINOR (Nice to Have):**
   - Non-optimal data structure choices, minor performance improvements, opportunities to use stdlib built-ins.

4. **💡 NIT (Optional Polish):**
   - Typos in internal comments, variable renaming suggestions for hyper-clarity. Must not block merging.

---

## Feedback Formatting Standard
Every non-trivial comment must include:
1. **Target:** File and line range (`[path/to/file.py#L12-L15]`).
2. **Finding:** Why this is an issue.
3. **Suggested Fix:** Concrete code snippet demonstrating the correction.


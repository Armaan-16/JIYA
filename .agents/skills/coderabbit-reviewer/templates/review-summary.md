# CodeRabbit Review Summary: [Change Title]

- **Reviewer:** CodeRabbit Reviewer
- **Review Date:** [YYYY-MM-DD]
- **Target Diffs:** [List of files]
- **Status:** [PASSED | CHANGES REQUESTED]

---

## 1. High-Level Summary
[Concise 2-3 sentence overview of modifications]

---

## 2. Blast Radius & Caller Impact
- **Modified Call Signatures:** [None | List signatures]
- **Direct Callers Checked:**
  - `path/file1.py:func()` -> Verified compatible
  - `path/file2.py:run()` -> Verified compatible
- **Downstream Risks:** [None identified | Notes]

---

## 3. Findings & Review Remarks

| Severity | File & Location | Description & Impact | Recommendation |
|---|---|---|---|
| 🚨 Critical | `path/file.py:45` | Example: Missing null check | Add `if x is None: return` |
| ⚠️ Major | `path/file.py:82` | Example: Redundant service initialization | Reuse singleton instance |
| ℹ️ Minor | `path/file.py:110`| Example: Use dict comprehension | Simplify loop |
| 💡 Nit | `path/file.py:15` | Example: Typo in docstring | Fix typo |

---

## 4. Verification Check
- [x] All caller invocations validated.
- [x] Edge cases evaluated.
- [x] Backward compatibility preserved.


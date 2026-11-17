# KARPATHY Rule: Implementation Discipline Checklist

> **Mandate:** Run through this checklist prior to proposing or applying any code modification.

---

## Pre-Edit Verification
- [ ] **Exact Problem Definition:** Can I summarize the bug or requirement in a single sentence?
- [ ] **Baseline Verified:** Have I observed the current failure or baseline behavior with my own eyes (via tests or logs)?
- [ ] **Assumptions Documented:** What am I assuming about data formats, nullability, and thread safety?
- [ ] **Minimal File Set:** Am I editing only the essential files? (If > 3 files, escalate to Level 2).

## Post-Edit Verification
- [ ] **Diff Review:** Did I run `git diff` or inspect the chunk to verify no unrelated whitespace or styling changes were introduced?
- [ ] **Comment Preservation:** Did I retain every existing comment, docstring, and copyright header?
- [ ] **Zero Added Warnings:** Did Pyright or linter run without new warnings?
- [ ] **Hypothesis Confirmed:** Did the fix actually produce the expected output without side effects?


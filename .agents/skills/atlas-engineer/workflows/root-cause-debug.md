# ATLAS Workflow: Root-Cause Architectural Debugging

> **Goal:** Diagnose systemic failures down to fundamental design flaws rather than patching symptoms with superficial try/catch blocks.

---

## The 5-Whys Architectural Protocol

When a defect is reported:

1. **Symptom Observation:** Capture the exact traceback, command output, or erroneous behavior.
2. **Why 1 (Immediate Cause):** Why did this function crash or produce wrong data?
3. **Why 2 (Contract Breach):** Why was invalid input passed or an invalid state entered?
4. **Why 3 (Boundary Failure):** Why did the calling boundary fail to enforce preconditions?
5. **Why 4 (Design Invariant):** Why did the architecture allow this state to exist without guardrails?
6. **Why 5 (System Root Cause):** Is there an unmodeled domain concept or mismatched lifecycle?

## Remediation Guidelines
- Avoid wrapping broad blocks in `except Exception: pass`.
- Fix the structural invariant that permitted the invalid state.
- Add regression tests in `TESTS/` demonstrating the failure before and the fix after.


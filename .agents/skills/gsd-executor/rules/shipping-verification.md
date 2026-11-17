# GSD Rule: Shipping Verification & Proof

> **Mandate:** "It works" is not a status. Status is demonstrated by reproducible command output.

---

## The Verification Proof Contract

Before declaring any feature shipped or bug fixed:

1. **Explicit Terminal Execution:**
   - Execute the test or verification command via PowerShell.
   - Example: `python -m unittest TESTS/test_voice_service.py` or `pytest TESTS/`.

2. **Zero Ignored Failures:**
   - Exit code must be 0.
   - Any warning must be understood and verified as non-critical.

3. **In-Chat Evidence:**
   - Include the exact command run and the terminal output showing tests passed.
   - Never say: *"I have run the tests and they pass"* without the accompanying log proof.


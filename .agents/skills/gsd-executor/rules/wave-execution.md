# GSD Rule: Wave Execution Strategy

> **Mandate:** Decompose large initiatives into self-contained, sequential "waves." Never execute a 10-step plan in a single unverified leap.

---

## What is a Wave?
A **Wave** is a coherent chunk of work touching 1–3 closely related files that can be fully implemented, tested, and verified within a single execution cycle.

### Wave Execution Protocol:
1. **Wave Definition:**
   - Define exact files to modify.
   - Define automated test command to verify.
2. **Execute & Test:**
   - Write/update code and tests.
   - Run verification command.
3. **Checkpoint:**
   - If tests pass $\to$ Record progress to `progress.txt` and advance to the next wave.
   - If tests fail $\to$ Fix immediately before starting the next wave. Never build on top of broken foundations.
4. **Context Reset (If needed):**
   - For very large features, subagent delegation or fresh context waves ensure no context rot interferes with execution.


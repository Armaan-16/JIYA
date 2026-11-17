# ATLAS Workflow: Architecture Prototype & Spikes

> **Goal:** Validate uncertain technical feasibility, performance limits, or API designs using rapid, throwaway spikes before committing changes to production modules.

---

## Process Steps

### Step 1: Hypothesis Definition
State the technical unknown in a single clear hypothesis:
- Example: *"Hypothesis: Reading configuration from JSON via standard library takes < 5ms and supports dynamic reloading."*

### Step 2: Isolation & Sandboxing
- Implement the spike in an isolated test file within `TESTS/spikes/` or execute a scratch script in the conversation's scratch directory.
- Never modify core production files (`CORE/`, `SERVICES/`) during the prototype phase.

### Step 3: Metric Verification
Collect empirical evidence:
- Memory footprint
- Execution latency
- Error modes under adverse inputs

### Step 4: Decision & Cleanup
- If the spike succeeds: distill the lessons learned into the ADR and clean design.
- Delete the spike scratch files or mark the test as an automated benchmark.


# ATLAS Workflow: Adversarial Architectural Review

> **Goal:** Expose architectural vulnerabilities, hidden assumptions, scalability bottlenecks, and failure cascades before any code is committed.

---

## Process Steps

### Step 1: Boundary & Interface Analysis
1. Identify all components touching the proposed change.
2. Check for interface contract mutations:
   - Are function signatures altered?
   - Are return types modified?
   - Are optional parameters now mandatory?
3. Verify that no circular import paths are introduced.

### Step 2: Adversarial Failure Simulation
Ask the following stress questions:
- **What happens if a dependent service hangs or raises an unhandled exception?**
- **What if the local memory or vector database is corrupt or empty?**
- **What happens if the OS denies permissions or a subprocess terminates abruptly?**
- **Can concurrent requests corrupt shared in-memory state?**

### Step 3: Modularity & Coupling Check
- Does this new logic belong in the target module, or does it belong in a shared service or utility?
- Is this change violating the Single Responsibility Principle (SRP)?

### Step 4: Verdict & Veto Assessment
- **APPROVED:** The architecture maintains durability, isolation, and backward compatibility.
- **VETOED:** The change introduces leaky abstractions, circular dependencies, or breaking shifts without an ADR.


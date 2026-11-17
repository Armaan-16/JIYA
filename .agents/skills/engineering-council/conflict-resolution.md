# ENGINEERING COUNCIL Protocol: Conflict Resolution & Veto Priority

> **Mandate:** Deterministic resolution. When two entities disagree, mathematical priority dictates the outcome.

---

## Priority Order

$$\mathbf{ECC\ (Security)} > \mathbf{Atlas\ (Architecture)} > \mathbf{Ponytail\ (Simplicity)} > \mathbf{Karpathy\ (Discipline)} > \mathbf{GSD\ (Velocity)}$$

---

## Common Conflict Scenarios & Resolutions

### 1. Velocity vs. Security (GSD vs. ECC)
- *Scenario:* GSD wants to bypass input validation to ship an integration faster.
- *Resolution:* **ECC wins immediately.** Security is non-negotiable. No deadline overrides a vulnerability.

### 2. Architecture vs. Simplicity (Atlas vs. Ponytail)
- *Scenario:* Atlas proposes a generic event-bus architecture with 4 abstract layers; Ponytail argues a direct callback function solves the problem with 80% less code.
- *Resolution:* **Ponytail wins** unless Atlas can demonstrate an immediate, existing requirement (not hypothetical future need) that fails without the abstraction. YAGNI dominates speculative extensibility.

### 3. Scope vs. Refactoring (Karpathy vs. Atlas/GSD)
- *Scenario:* While fixing a bug in `MemoryService`, an agent decides to rewrite the surrounding 150 lines.
- *Resolution:* **Karpathy wins.** The diff must be restricted strictly to fixing the bug. The broader refactor must be logged as a separate task.

### 4. Simplicity vs. Security (Ponytail vs. ECC)
- *Scenario:* Ponytail argues against writing security wrappers around shell execution to keep code small.
- *Resolution:* **ECC wins.** Simplicity cannot compromise system safety. Safe parameterization is mandatory.


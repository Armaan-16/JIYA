# RALPH LOOP Rule: Disk-Externalized State

> **Mandate:** Chat context is ephemeral; disk is eternal. All execution status must be written to disk files so any agent can resume instantly.

---

## The Dual-Disk Anchor Pattern

Every autonomous or multi-step execution must initialize two files in the workspace or task directory:

1. **`PRD.md` (Product Requirements & Acceptance Criteria):**
   - The declarative target state.
   - Contains user goals, acceptance tests, and constraints.
   - Does not change during execution unless user updates requirements.

2. **`progress.txt` (Append-Only Execution Ledger):**
   - Chronological log of atomic actions taken.
   - Contains: timestamp, iteration index, action taken, test command run, test result (pass/fail), and next immediate step.
   - If the agent crashes or context is lost, reading `progress.txt` restores exact state in 1 prompt turn.


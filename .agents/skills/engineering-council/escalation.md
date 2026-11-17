# ENGINEERING COUNCIL Protocol: 4-Tier Escalation Model

> **Mandate:** Proportionate governance. Micro-changes move at maximum velocity; architectural and security-critical shifts undergo rigorous council scrutiny.

---

## Escalation Matrix

### Level 0: Micro-Edit
- **Definition:** Typos, documentation wording, comment corrections, single non-functional syntax adjustments.
- **Process:** Autonomous surgical edit.
- **Council Enforcers:** Karpathy (surgical diff check).
- **ADR Required:** No.

### Level 1: Standard Feature / Routine Refactor
- **Definition:** Adding a new helper function, fixing an isolated bug, adding automated unit tests, minor UI adjustments.
- **Process:** Fast-path deliberation.
- **Council Enforcers:** GSD, Ponytail, Karpathy, ECC.
- **ADR Required:** No.

### Level 2: Architectural or Dependency Mutation
- **Definition:** Creating new top-level or subsystem modules, changing public interfaces or shared contracts, adding any third-party package, modifying database schemas.
- **Process:** Full 5-Step Deliberation + Mandatory ADR.
- **Council Enforcers:** Atlas, Ponytail, ECC, Karpathy, GSD, CodeRabbit.
- **ADR Required:** Yes (Recorded in `docs/decisions/` and `.agents/memory/decisions-index.json`).

### Level 3: Security, Breaking, or Destructive Action
- **Definition:** Changes touching authentication, token/credential handling, arbitrary subprocess/shell execution, irreversible file deletion, breaking backward compatibility of core APIs.
- **Process:** Strict Deliberation + Mandatory ADR + Explicit User Confirmation.
- **Council Enforcers:** All 9 Entities + Explicit User Consent.
- **ADR Required:** Yes.

---

## Dynamic Escalation Triggers
A task automatically escalates:
- From **Level 0/1 to Level 2** if:
  - More than 3 files are modified.
  - A new external dependency is imported.
  - A shared class or service method signature changes.
- From **Level 2 to Level 3** if:
  - System-level command execution privileges are requested.
  - File deletions outside scratch or temporary folders are planned.
  - Breaking public CLI or user interface commands.


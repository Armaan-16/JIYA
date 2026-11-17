# ADR-0002: Modular Directory Refactoring and Subsystem Decoupling

- **Status:** ACCEPTED
- **Date:** 2026-10-19
- **Escalation Level:** Level 2
- **Council Sponsors:** [ATLAS, PONYTAIL, ECC, KARPATHY, GSD, CODERABBIT, RALPH_LOOP, HERMES, TASK_OBSERVER]
- **Decider(s):** [Engineering Council & Armaan]

---

## 1. Context & Problem Statement
Refactor JIYA codebase into modular file system: BRAIN, BRAIN/MEMORY, PERSONALITY, SKILLS, VOICE, EARS, VISION, MODELS, TESTS and update all imports.

---

## 2. Decision Drivers
- Driver 1: Architectural durability and separation of concerns (Atlas)
- Driver 2: Simplicity and zero unnecessary dependencies (Ponytail)
- Driver 3: Zero-trust security and regression test proof (ECC)
- Driver 4: Minimal blast radius and surgical implementation (Karpathy)

---

## 3. Considered Options
1. **Option A:** [Proposed implementation]
2. **Option B:** [Alternative simpler approach]
3. **Option C:** [Status quo / do nothing]

---

## 4. Decision Outcome
**Chosen Option:** Option A, because it satisfies all architectural, security, and simplicity invariants.

### Council Veto Checks
- **ECC (Security):** PASSED - No vulnerabilities or secret exposures.
- **Atlas (Architecture):** PASSED - Preserves layer boundaries.
- **Ponytail (Simplicity):** PASSED - Minimal complexity, stdlib prioritized.
- **Karpathy (Discipline):** PASSED - Surgical scope defined.

---

## 5. Consequences
### Positive
- [Key benefit 1]
- [Key benefit 2]

### Negative & Trade-offs
- [Trade-off or maintenance overhead]

---

## 6. Implementation Notes & Blast Radius
- **Modules Affected:** `CORE/...`, `SERVICES/...`
- **Verification Commands:** `python -m unittest TESTS/...`

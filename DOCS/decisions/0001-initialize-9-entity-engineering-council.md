# ADR-0001: Initialize 9-Entity Engineering Council Governance Framework

- **Status:** ACCEPTED
- **Date:** 2026-10-19
- **Escalation Level:** Level 3
- **Council Sponsors:** [ATLAS, PONYTAIL, ECC, KARPATHY, GSD, CODERABBIT, RALPH_LOOP, HERMES, TASK_OBSERVER]
- **Decider(s):** [The 9-Entity Engineering Council & Armaan]

---

## 1. Context & Problem Statement
As the JIYA AI Operating System expands into voice processing, automation, planning, and multi-model routing, single-perspective autonomous coding agents encounter severe failure modes:
1. Uncontrolled complexity, circular imports, and abstraction bloat.
2. Silent security regressions, command injection risks, and unverified assumptions.
3. Runaway diffs, mass file reformatting, and accidental comment deletion.
4. Ephemeral context loss across multi-turn sessions and rate limits.
5. Lack of systematic review before declaring tasks "complete".

A multi-entity engineering council is needed to enforce separation of concerns, adversarial review, disk-externalized memory, and strict quality gates.

---

## 2. Decision Drivers
- **Architectural Durability:** Modular separation between UI/Voice, Services, Core, and Models (Atlas).
- **Simplicity & Anti-Bloat:** Strict adherence to YAGNI and standard library preference (Ponytail).
- **Security & Lifecycle:** Zero-trust AgentShield hardening and TDD Red-Green-Refactor (ECC).
- **Implementation Discipline:** Surgical diffs and explicit assumptions (Karpathy).
- **Delivery Velocity:** Phased wave execution and automated verification proof (GSD).
- **Contextual Review:** AST-aware caller and dependency tracing (CodeRabbit).
- **Resilience:** Disk-externalized state management (Ralph Loop).
- **Cross-Session Continuity:** Persistent memory store in `.agents/memory/` (Hermes).
- **Continuous Evolution:** Retrospective friction observation and skill refinement (Task Observer).

---

## 3. Considered Options
1. **Option A (The 9-Entity Council):** Establish a full multi-perspective governance council combining 6 technical and 3 meta/orchestration entities with strict veto hierarchies and a 6-pass review gate.
2. **Option B (Single Monolithic Prompt):** Add a long prompt instruction block into a single system instruction. (Rejected: prone to attention loss, conflicting instructions, and lacks disk-backed state).
3. **Option C (Ad-hoc Prompting):** Rely on human prompts to remind the agent to write tests or keep diffs small. (Rejected: high cognitive load on user and recurring regression errors).

---

## 4. Decision Outcome
**Chosen Option:** **Option A (The 9-Entity Council Framework)**.

### Council Veto Checks
- **ECC (Security):** PASSED - Establishes AgentShield zero-trust protocols, secrets detection, and TDD requirement.
- **Atlas (Architecture):** PASSED - Clean directory boundaries (`.agents/skills/`, `.agents/memory/`, `docs/decisions/`).
- **Ponytail (Simplicity):** PASSED - Zero extra pip dependencies; pure Python 3.12 stdlib utilities.
- **Karpathy (Discipline):** PASSED - Non-destructive, additive setup that preserves all existing JIYA code.

---

## 5. Consequences
### Positive
- Every code change undergoes multi-perspective adversarial evaluation.
- Critical architectural changes are documented permanently in ADRs.
- State is preserved on disk, making operations resilient to session resets.
- Zero-trust security and automated testing become non-negotiable gates.

### Negative & Trade-offs
- Deliberation overhead for Level 2 and Level 3 tasks.
- *Mitigation:* Level 0 (micro-edits) and Level 1 (standard features) bypass heavyweight full council meetings via fast-path execution.

---

## 6. Implementation Notes & Blast Radius
- **Root Files Created:** `AGENTS.md`, `GEMINI.md`, `pyrightconfig.json`.
- **Memory Store:** `.agents/memory/core-invariants.json`, `user-preferences.json`, `decisions-index.json`.
- **Skills Implemented:** 10 skill suites under `.agents/skills/`.
- **Verification Commands:**
  - `python .agents/skills/hermes-orchestrator/scripts/memory_sync.py --validate`
  - `python .agents/skills/hermes-orchestrator/scripts/memory_sync.py --summary`


# ENGINEERING COUNCIL Protocol: 5-Step Deliberation Engine

> **Mandate:** Deliberation prevents blind execution. Structured debate exposes edge cases and architectural trade-offs early.

---

```
                       ┌──────────────────────────────────────────────┐
                       │   Step 1: Framing & Constraint Validation    │
                       │           (HERMES & GSD EXECUTOR)            │
                       └──────────────────────┬───────────────────────┘
                                              │
                                              ▼
                       ┌──────────────────────────────────────────────┐
                       │ Step 2: Architectural & Simplicity Critique  │
                       │             (ATLAS & PONYTAIL)               │
                       └──────────────────────┬───────────────────────┘
                                              │
                                              ▼
                       ┌──────────────────────────────────────────────┐
                       │ Step 3: Security & Discipline Verification   │
                       │             (ECC & KARPATHY)                 │
                       └──────────────────────┬───────────────────────┘
                                              │
                                              ▼
                       ┌──────────────────────────────────────────────┐
                       │   Step 4: Consensus & ADR Registration       │
                       │      (ENGINEERING COUNCIL & HERMES)          │
                       └──────────────────────┬───────────────────────┘
                                              │
                                              ▼
                       ┌──────────────────────────────────────────────┐
                       │   Step 5: Wave Execution & Context Review    │
                       │ (GSD, RALPH LOOP, CODERABBIT, OBSERVER)      │
                       └──────────────────────────────────────────────┘
```

---

## Detailed Step Breakdown

### Step 1: Framing & Constraints (Hermes & GSD)
- Load [`.agents/memory/core-invariants.json`](file:///c:/Users/mishr/Documents/JIYA/.agents/memory/core-invariants.json) and [`.agents/memory/user-preferences.json`](file:///c:/Users/mishr/Documents/JIYA/.agents/memory/user-preferences.json).
- Classify the task into Level 0, 1, 2, or 3.
- Clearly state the problem, target files, acceptance criteria, and non-goals.

### Step 2: Architecture & Simplicity Critique (Atlas & Ponytail)
- **Atlas asks:** Does this violate layer encapsulation (`UI` $\to$ `SERVICES` $\to$ `CORE` $\to$ `MODELS`)? Are we introducing circular imports?
- **Ponytail asks:** Can we solve this without new code? Can we use Python stdlib or Windows platform features instead of adding packages?

### Step 3: Security & Discipline Verification (ECC & Karpathy)
- **ECC asks:** Are there command injection, secret leakage, or input validation risks? Is there a failing test prepared (Red-Green)?
- **Karpathy asks:** Are our assumptions about existing behavior verified? Is the proposed diff surgical and minimal?

### Step 4: Consensus & ADR Registration (Council & Hermes)
- If Level 2 or 3, run:
  ```powershell
  python .agents/skills/engineering-council/scripts/new_council_decision.py --title "<Title>" --level "Level 2"
  ```
- Any veto by ECC, Atlas, Ponytail, or Karpathy pauses execution until remediated.

### Step 5: Wave Execution & Review (GSD, Ralph Loop, CodeRabbit, Observer)
- Execute through structured waves.
- Externalize state to `progress.txt`.
- Pass all 6 gates of the Pre-Completion Review before declaring complete.


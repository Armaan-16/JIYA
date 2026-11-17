# GSD Rule: The 5-Phase Delivery Loop

> **Mandate:** All engineering initiatives must follow the 5 phases sequentially. Skipping from Discuss directly to Execute is prohibited.

---

```
┌───────────┐     ┌──────────┐     ┌───────────┐     ┌──────────┐     ┌────────┐
│  DISCUSS  │ ──> │   PLAN   │ ──> │  EXECUTE  │ ──> │  VERIFY  │ ──> │  SHIP  │
└───────────┘     └──────────┘     └───────────┘     └──────────┘     └────────┘
```

### Phase 1: Discuss
- Align on the user's intent, constraints, and non-goals.
- Frame inputs and expected outputs.
- Involve Hermes (memory check) and Council entities.

### Phase 2: Plan
- Generate a structured phase plan using [`phase-plan.md`](file:///c:/Users/mishr/Documents/JIYA/.agents/skills/gsd-executor/templates/phase-plan.md).
- Break the implementation into atomic, testable waves.
- Specify concrete verification commands for each wave.

### Phase 3: Execute
- Implement code surgically (Karpathy & Ponytail rules).
- Run TDD Red-Green cycle (ECC rule).
- Keep changes localized.

### Phase 4: Verify
- Run tests, linters, and type checkers.
- Capture stdout/stderr as proof of success.
- If failure occurs, loop back to Execute with precise diagnostic.

### Phase 5: Ship
- Run the 6-Pass Pre-Completion Review Gate.
- Present clean, concise diff summary and verification evidence to the user.


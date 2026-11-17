# ECC Rule: Test-Driven Lifecycle (TDD Red-Green-Refactor)

> **Mandate:** Production code without an accompanying test is an unverified assumption.

---

## The 3-Stage TDD Cycle

```
  ┌─────────────────────────────────────────────────────────┐
  │ 1. RED: Write a failing test matching target behavior.  │
  │    Run test and verify tangible failure message.        │
  └────────────────────────────┬────────────────────────────┘
                               │
                               ▼
  ┌─────────────────────────────────────────────────────────┐
  │ 2. GREEN: Write the minimum surgical code to pass test. │
  │    Run test and verify green pass status.               │
  └────────────────────────────┬────────────────────────────┘
                               │
                               ▼
  ┌─────────────────────────────────────────────────────────┐
  │ 3. REFACTOR: Clean up bloat, enforce Ponytail rules.    │
  │    Re-run test suite to guarantee zero regression.      │
  └─────────────────────────────────────────────────────────┘
```

## Rules of Engagement
1. **Never skip Stage 1:** You must see the test fail before implementing the fix. An untested test that passes on first run may be a tautology that tests nothing.
2. **Deterministic Tests:** Tests in `TESTS/` must not depend on external live networks or flaky hardware. Mock external LLM endpoints or voice devices.
3. **Automated Evidence:** Present the terminal output showing the test execution passing.


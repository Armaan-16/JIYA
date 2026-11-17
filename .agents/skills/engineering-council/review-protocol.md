# ENGINEERING COUNCIL Protocol: 6-Pass Pre-Completion Review Gate

> **Mandate:** Zero unverified completion. Every task or pull request must pass all six verification passes sequentially before presentation to the user.

---

```
[Pass 1: Security & Secrets (ECC)]
               │
               ▼
[Pass 2: Simplicity & Anti-Bloat (Ponytail)]
               │
               ▼
[Pass 3: Surgical Diff & Assumptions (Karpathy)]
               │
               ▼
[Pass 4: Blast Radius & Caller Impact (CodeRabbit)]
               │
               ▼
[Pass 5: Verification & Automated Tests (GSD)]
               │
               ▼
[Pass 6: Memory Sync & Observation (Hermes / Task Observer)]
```

---

## The Six Passes

### Pass 1: Security & Secrets Audit (ECC)
- [ ] Scan diffs for leaked tokens, keys, passwords, or hardcoded sensitive URLs.
- [ ] Ensure command execution uses argument arrays, not raw shell strings.
- [ ] Confirm file access is bounded to the project directory.

### Pass 2: Simplicity & Anti-Bloat (Ponytail)
- [ ] Verify no unnecessary libraries were introduced.
- [ ] Confirm no premature abstractions, dead code, or redundant helpers were added.
- [ ] Confirm cyclomatic complexity and function line limits are respected.

### Pass 3: Surgical Diff Check (Karpathy)
- [ ] Verify diffs are minimal and contiguous.
- [ ] Confirm no gratuitous reformatting or deleted comments.
- [ ] Verify that baseline assumptions were proven with runtime evidence.

### Pass 4: AST-Aware Blast Radius & Caller Impact (CodeRabbit)
- [ ] Trace all callers across the repository to guarantee compatibility.
- [ ] Verify edge cases (empty data, timeouts, exceptions) are handled.
- [ ] Confirm type signatures and return contracts are intact.

### Pass 5: Verification & Automated Tests (GSD)
- [ ] Execute tests via terminal commands.
- [ ] Confirm clean exit code 0 and capture test output.
- [ ] Verify that new or modified behavior has automated regression coverage.

### Pass 6: Memory Sync & Observation (Hermes / Task Observer)
- [ ] Synchronize `.agents/memory/` if invariants, preferences, or ADRs changed.
- [ ] Log friction or workflow signals in `skill-observations/observation-log/`.


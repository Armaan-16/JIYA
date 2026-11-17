# RALPH LOOP Rule: Single-Task Iteration Loop

> **Mandate:** Execute one atomic unit of work per iteration. Never bundle speculative multi-stage actions into a single unmonitored burst.

---

## The Ralph Iteration Loop

```
┌──────────────────────────────────────────────┐
│ 1. READ: Read PRD.md & last line of progress.txt
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ 2. TARGET: Identify next atomic task         │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ 3. ACT: Apply surgical code change           │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ 4. TEST: Run verification command            │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│ 5. RECORD: Append outcome to progress.txt    │
└──────────────────────┬───────────────────────┘
                       │
           [Target Achieved? / Complete?]
             ├── NO  ──> Loop to Step 1
             └── YES ──> Present Done
```

### Safety Rules:
- If a loop fails 3 times consecutively on the same task, halt immediately and escalate.
- Never loop infinitely; set a hard iteration cap (default: 10 iterations per wave).


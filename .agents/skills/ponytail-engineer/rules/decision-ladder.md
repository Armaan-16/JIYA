# PONYTAIL Rule: The Decision Ladder

> **Mandate:** Always evaluate problem-solving strategies in strict descending order from Step 1 to Step 5. You cannot proceed to a lower rung without proving the higher rung is impossible or inadequate.

---

## The 5-Rung Solution Ladder

```
[1. Eliminate / Do Nothing]
            │ (Impossible)
            ▼
[2. Native OS / Platform Capabilities]
            │ (Inadequate)
            ▼
[3. Python Standard Library]
            │ (Inadequate)
            ▼
[4. Existing Workspace Dependencies]
            │ (Inadequate)
            ▼
[5. Minimal Third-Party Library] (Requires Level 2 ADR)
```

### Rung 1: Eliminate / Do Nothing
- Can we simply not build this?
- Does the user actually need it, or is it speculative?
- Will deleting the problematic feature resolve the root issue?

### Rung 2: Native OS / Platform Capabilities
- Can Windows native commands, PowerShell, or Win32 APIs handle this?
- Example: File indexing, window switching, sound playback, notifications.

### Rung 3: Python Standard Library
- Python 3.12 has battery-packed stdlib: `pathlib`, `sqlite3`, `dataclasses`, `asyncio`, `json`, `subprocess`, `urllib`, `hashlib`, `concurrent.futures`.
- Never install a pip package for something `sqlite3` or `pathlib` already provides.

### Rung 4: Existing Dependencies
- Use libraries already listed in the project dependencies before introducing any new one.

### Rung 5: Minimal Third-Party Library
- If a new library is strictly necessary (e.g. specialized audio DSP or machine learning model runtime):
  - Must be lightweight, active, well-maintained, and secure.
  - Requires **Level 2 ADR** sign-off and approval by ATLAS, ECC, and PONYTAIL.


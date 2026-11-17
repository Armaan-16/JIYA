# TASK OBSERVER Reference: Observation Schema

> Standard JSON structure for records saved in `skill-observations/observation-log/`.

---

```json
{
  "observation_id": "OBS-20261019-001",
  "timestamp": "2026-10-19T14:26:36+05:30",
  "category": "TOOL_FRICTION | USER_CORRECTION | SKILL_GAP | AMBIGUITY",
  "severity": "LOW | MEDIUM | HIGH",
  "affected_entity": "ATLAS | PONYTAIL | ECC | KARPATHY | GSD | CODERABBIT | RALPH_LOOP | HERMES",
  "trigger": "Short description of what caused the observation",
  "context": {
    "command_or_action": "Exact command or file edit involved",
    "error_or_feedback": "Error message or user correction text"
  },
  "root_cause": "Underlying reason why this occurred",
  "evolutionary_recommendation": "Concrete suggestion for a new rule, skill, or invariant"
}
```


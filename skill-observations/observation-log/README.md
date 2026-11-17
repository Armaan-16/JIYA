# Task Observer: Friction & Evolution Log

> This directory stores structured observation records logged by the **Task Observer** (Entity 9) during repository development.

---

## Purpose
The Task Observer records:
- **User Corrections:** Instances where user instructions clarified or corrected agent assumptions.
- **Tool Friction:** Non-zero command exit codes, file replacement errors, or encoding issues.
- **Skill Gaps:** Missing domain workflows or complex multi-step failures.
- **Ambiguity:** Underspecified requirements where guesses occurred.

## Recording an Observation
Use the autonomous script:
```powershell
python .agents/skills/task-observer/scripts/log_observation.py --trigger "Description of event" --category "TOOL_FRICTION" --severity "LOW" --entity "PONYTAIL"
```

## Listing Observations
```powershell
python .agents/skills/task-observer/scripts/log_observation.py --list
```


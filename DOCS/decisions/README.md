# Architecture Decision Records (ADRs)

> This directory houses all formal architectural decisions governing the JIYA AI Operating System.

---

## What is an ADR?
An **Architecture Decision Record** captures a significant structural, security, or dependency decision made by the **9-Entity Engineering Council**.

## Lifecycle & Statuses
- **PROPOSED:** Under active Council deliberation.
- **ACCEPTED:** Unanimously approved or resolved via veto hierarchy; active standard.
- **REJECTED:** Council rejected the proposal.
- **DEPRECATED:** Replaced or obsoleted by a newer ADR.
- **SUPERSEDED:** Directly superseded by another ADR (referenced in header).

## Creating a New ADR
Run the automated council generator:
```powershell
python .agents/skills/engineering-council/scripts/new_council_decision.py --title "Your Decision Title" --level "Level 2"
```

This will automatically assign the next sequential ID, generate the template markdown file, and register it in `.agents/memory/decisions-index.json`.


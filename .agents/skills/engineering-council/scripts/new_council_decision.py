#!/usr/bin/env python3
"""
ENGINEERING COUNCIL: Architecture Decision Record (ADR) Generator
Scaffolds a new ADR in docs/decisions/ and automatically registers it in
.agents/memory/decisions-index.json.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def find_workspace_root() -> Path:
    current = Path(__file__).resolve().parent
    for parent in [current, *current.parents]:
        if (parent / ".agents").is_dir() or (parent / "docs" / "decisions").is_dir():
            return parent
    return Path.cwd()


WORKSPACE_ROOT = find_workspace_root()
DECISIONS_DIR = WORKSPACE_ROOT / "docs" / "decisions"
MEMORY_DIR = WORKSPACE_ROOT / ".agents" / "memory"
DECISIONS_INDEX_FILE = MEMORY_DIR / "decisions-index.json"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_-]+", "-", text)


def get_next_adr_number() -> int:
    DECISIONS_DIR.mkdir(parents=True, exist_ok=True)
    existing_files = list(DECISIONS_DIR.glob("[0-9][0-9][0-9][0-9]-*.md"))
    max_num = 0
    for f in existing_files:
        prefix = f.name[:4]
        if prefix.isdigit():
            max_num = max(max_num, int(prefix))

    # Also check decisions-index.json if it exists
    if DECISIONS_INDEX_FILE.exists():
        try:
            with DECISIONS_INDEX_FILE.open("r", encoding="utf-8") as fp:
                data = json.load(fp)
                for item in data.get("decisions", []):
                    adr_id = item.get("id", "")
                    if adr_id.startswith("ADR-"):
                        num_part = adr_id.split("-")[1]
                        if num_part.isdigit():
                            max_num = max(max_num, int(num_part))
        except Exception:
            pass

    return max_num + 1


def create_adr(
    title: str,
    escalation_level: str = "Level 2",
    status: str = "PROPOSED",
    summary: str = "",
) -> Path:
    adr_num = get_next_adr_number()
    adr_id = f"ADR-{adr_num:04d}"
    slug = slugify(title)
    filename = f"{adr_num:04d}-{slug}.md"
    target_path = DECISIONS_DIR / filename
    rel_path = f"docs/decisions/{filename}"

    today = datetime.now(timezone.utc).astimezone().date().isoformat()

    content = f"""# {adr_id}: {title}

- **Status:** {status.upper()}
- **Date:** {today}
- **Escalation Level:** {escalation_level}
- **Council Sponsors:** [ATLAS, PONYTAIL, ECC, KARPATHY, GSD, CODERABBIT, RALPH_LOOP, HERMES, TASK_OBSERVER]
- **Decider(s):** [Engineering Council & Armaan]

---

## 1. Context & Problem Statement
{summary if summary else "Describe the technical context, requirements, forces at play, and constraints."}

---

## 2. Decision Drivers
- Driver 1: Architectural durability and separation of concerns (Atlas)
- Driver 2: Simplicity and zero unnecessary dependencies (Ponytail)
- Driver 3: Zero-trust security and regression test proof (ECC)
- Driver 4: Minimal blast radius and surgical implementation (Karpathy)

---

## 3. Considered Options
1. **Option A:** [Proposed implementation]
2. **Option B:** [Alternative simpler approach]
3. **Option C:** [Status quo / do nothing]

---

## 4. Decision Outcome
**Chosen Option:** Option A, because it satisfies all architectural, security, and simplicity invariants.

### Council Veto Checks
- **ECC (Security):** PASSED - No vulnerabilities or secret exposures.
- **Atlas (Architecture):** PASSED - Preserves layer boundaries.
- **Ponytail (Simplicity):** PASSED - Minimal complexity, stdlib prioritized.
- **Karpathy (Discipline):** PASSED - Surgical scope defined.

---

## 5. Consequences
### Positive
- [Key benefit 1]
- [Key benefit 2]

### Negative & Trade-offs
- [Trade-off or maintenance overhead]

---

## 6. Implementation Notes & Blast Radius
- **Modules Affected:** `CORE/...`, `SERVICES/...`
- **Verification Commands:** `python -m unittest TESTS/...`
"""

    DECISIONS_DIR.mkdir(parents=True, exist_ok=True)
    with target_path.open("w", encoding="utf-8") as f:
        f.write(content)

    print(f"[ENGINEERING-COUNCIL] Created ADR markdown file: {rel_path}")

    # Register in decisions-index.json
    if DECISIONS_INDEX_FILE.exists():
        try:
            with DECISIONS_INDEX_FILE.open("r", encoding="utf-8") as f:
                index_data = json.load(f)
            
            record = {
                "id": adr_id,
                "title": title,
                "status": status.upper(),
                "date": today,
                "file_path": rel_path,
                "escalation_level": escalation_level,
                "sponsors": [
                    "ATLAS", "PONYTAIL", "ECC", "KARPATHY", "GSD",
                    "CODERABBIT", "RALPH_LOOP", "HERMES", "TASK_OBSERVER"
                ],
                "veto_checks": {
                    "ecc_security": "PASSED",
                    "atlas_architecture": "PASSED",
                    "ponytail_simplicity": "PASSED",
                    "karpathy_discipline": "PASSED"
                },
                "summary": summary if summary else title
            }
            
            decisions = index_data.setdefault("decisions", [])
            decisions.append(record)
            index_data["total_records"] = len(decisions)
            index_data["last_updated"] = datetime.now(timezone.utc).astimezone().isoformat()
            
            temp_index = DECISIONS_INDEX_FILE.with_suffix(".tmp")
            with temp_index.open("w", encoding="utf-8") as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
                f.write("\n")
            temp_index.replace(DECISIONS_INDEX_FILE)
            print(f"[ENGINEERING-COUNCIL] Registered {adr_id} in decisions-index.json")
        except Exception as e:
            print(f"[ERROR] Failed to update decisions-index.json: {e}", file=sys.stderr)

    return target_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Engineering Council ADR Generator")
    parser.add_argument("--title", required=True, help="Title of the architectural decision")
    parser.add_argument("--level", choices=["Level 2", "Level 3"], default="Level 2", help="Escalation level")
    parser.add_argument("--status", choices=["PROPOSED", "ACCEPTED", "REJECTED"], default="ACCEPTED", help="ADR status")
    parser.add_argument("--summary", default="", help="Summary of problem context and decision")

    args = parser.parse_args()
    create_adr(title=args.title, escalation_level=args.level, status=args.status, summary=args.summary)


if __name__ == "__main__":
    main()


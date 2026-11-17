#!/usr/bin/env python3
"""
TASK OBSERVER: Autonomous Observation & Friction Logger
Appends structured observations to skill-observations/observation-log/
to power continuous system evolution.
"""

from __future__ import annotations

import argparse
import json
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
        if (parent / ".agents").is_dir() or (parent / "skill-observations").is_dir():
            return parent
    return Path.cwd()


WORKSPACE_ROOT = find_workspace_root()
LOG_DIR = WORKSPACE_ROOT / "skill-observations" / "observation-log"


def log_observation(
    category: str,
    severity: str,
    affected_entity: str,
    trigger: str,
    root_cause: str,
    recommendation: str,
    action_context: str = "",
) -> Path:
    """Creates a structured JSON observation log on disk."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).astimezone()
    timestamp_str = now.isoformat()
    file_id = now.strftime("%Y%m%d-%H%M%S")
    obs_id = f"OBS-{file_id}"

    data: Dict[str, Any] = {
        "observation_id": obs_id,
        "timestamp": timestamp_str,
        "category": category.upper(),
        "severity": severity.upper(),
        "affected_entity": affected_entity.upper(),
        "trigger": trigger,
        "context": {
            "command_or_action": action_context,
        },
        "root_cause": root_cause,
        "evolutionary_recommendation": recommendation,
    }

    target_file = LOG_DIR / f"{obs_id}.json"
    with target_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"[TASK-OBSERVER] Logged {severity} observation: {obs_id} -> {target_file.name}")
    return target_file


def list_observations() -> None:
    """Lists all historical observations logged on disk."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(LOG_DIR.glob("OBS-*.json"))
    print(f"[TASK-OBSERVER] Total observations recorded: {len(files)}")
    for f in files:
        try:
            with f.open("r", encoding="utf-8") as fp:
                data = json.load(fp)
            print(f"  * [{data.get('observation_id')}] [{data.get('severity')}] "
                  f"({data.get('category')} - {data.get('affected_entity')}): {data.get('trigger')}")
        except Exception as e:
            print(f"  * {f.name} (Error reading: {e})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Task Observer Friction Logging Utility")
    parser.add_argument("--list", action="store_true", help="List all recorded observations")
    parser.add_argument("--category", choices=["TOOL_FRICTION", "USER_CORRECTION", "SKILL_GAP", "AMBIGUITY"],
                        default="TOOL_FRICTION", help="Observation category")
    parser.add_argument("--severity", choices=["LOW", "MEDIUM", "HIGH"], default="MEDIUM", help="Severity level")
    parser.add_argument("--entity", default="GENERAL", help="Council entity involved (e.g. ATLAS, PONYTAIL, ECC)")
    parser.add_argument("--trigger", help="What triggered this observation")
    parser.add_argument("--root-cause", default="Not specified", help="Root cause analysis")
    parser.add_argument("--recommendation", default="Refine operational rule", help="Proposed evolution or rule change")
    parser.add_argument("--context", default="", help="Context or command line involved")

    args = parser.parse_args()

    if args.list:
        list_observations()
    elif args.trigger:
        log_observation(
            category=args.category,
            severity=args.severity,
            affected_entity=args.entity,
            trigger=args.trigger,
            root_cause=args.root_cause,
            recommendation=args.recommendation,
            action_context=args.context,
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


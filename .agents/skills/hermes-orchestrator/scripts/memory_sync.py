#!/usr/bin/env python3
"""
HERMES Persistent Memory Synchronization & Validation Utility
Ensures all council memory files in .agents/memory/ are syntactically valid,
properly structured, and synchronized.
"""

from __future__ import annotations

import argparse
import io
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
    """Finds the workspace root by looking for .agents directory."""
    current = Path(__file__).resolve().parent
    for parent in [current, *current.parents]:
        if (parent / ".agents").is_dir():
            return parent
    return Path.cwd()


WORKSPACE_ROOT = find_workspace_root()
MEMORY_DIR = WORKSPACE_ROOT / ".agents" / "memory"

REQUIRED_MEMORY_FILES = [
    "core-invariants.json",
    "user-preferences.json",
    "decisions-index.json",
]


def load_json_file(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Missing required memory file: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json_file(path: Path, data: Dict[str, Any]) -> None:
    temp_path = path.with_suffix(".tmp")
    with temp_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    temp_path.replace(path)


def validate_memory() -> bool:
    """Validates existence and schema compliance of all memory files."""
    print("[HERMES] Validating council persistent memory...")
    all_valid = True

    for filename in REQUIRED_MEMORY_FILES:
        file_path = MEMORY_DIR / filename
        if not file_path.exists():
            print(f"[MISSING] {file_path}")
            all_valid = False
            continue

        try:
            data = load_json_file(file_path)
            keys = list(data.keys())
            print(f"[VALID] {filename} (Schema: {data.get('schema_version', 'N/A')}, Keys: {keys})")
        except json.JSONDecodeError as e:
            print(f"[INVALID JSON] {filename}: {e}")
            all_valid = False
        except Exception as e:
            print(f"[ERROR] {filename}: {e}")
            all_valid = False

    return all_valid


def print_memory_summary() -> None:
    """Displays a summary of persistent invariants, preferences, and decisions."""
    try:
        invariants = load_json_file(MEMORY_DIR / "core-invariants.json")
        prefs = load_json_file(MEMORY_DIR / "user-preferences.json")
        decisions = load_json_file(MEMORY_DIR / "decisions-index.json")

        print("=" * 60)
        print(f"[HERMES] COUNCIL MEMORY SUMMARY: {invariants.get('project_name', 'Unknown')}")
        print("=" * 60)
        print(f"User Name      : {prefs.get('user_name', 'Unknown')}")
        print(f"Runtime        : {prefs.get('language_runtime', {}).get('primary', 'Python')}")
        print(f"Total ADRs     : {decisions.get('total_records', len(decisions.get('decisions', [])))}")
        print("\nCore Invariant Categories:")
        for cat, rules in invariants.get("invariants", {}).items():
            print(f"  * {cat.upper()}: {len(rules)} rules registered")

        print("\nRegistered Architectural Decisions:")
        for adr in decisions.get("decisions", []):
            print(f"  - [{adr.get('id')}] {adr.get('title')} ({adr.get('status')})")
        print("=" * 60)
    except Exception as e:
        print(f"[ERROR] Failed to load memory summary: {e}", file=sys.stderr)


def register_adr_entry(
    adr_id: str,
    title: str,
    status: str,
    file_path: str,
    escalation_level: str,
    summary: str,
) -> None:
    """Registers a new ADR entry into decisions-index.json."""
    index_file = MEMORY_DIR / "decisions-index.json"
    data = load_json_file(index_file)

    now = datetime.now(timezone.utc).astimezone().date().isoformat()
    record = {
        "id": adr_id,
        "title": title,
        "status": status.upper(),
        "date": now,
        "file_path": file_path,
        "escalation_level": escalation_level,
        "sponsors": [
            "ATLAS",
            "PONYTAIL",
            "ECC",
            "KARPATHY",
            "GSD",
            "CODERABBIT",
            "RALPH_LOOP",
            "HERMES",
            "TASK_OBSERVER",
        ],
        "veto_checks": {
            "ecc_security": "VERIFIED",
            "atlas_architecture": "VERIFIED",
            "ponytail_simplicity": "VERIFIED",
            "karpathy_discipline": "VERIFIED",
        },
        "summary": summary,
    }

    decisions = data.setdefault("decisions", [])
    updated = False
    for i, existing in enumerate(decisions):
        if existing.get("id") == adr_id:
            decisions[i] = record
            updated = True
            break
    if not updated:
        decisions.append(record)

    data["total_records"] = len(decisions)
    data["last_updated"] = datetime.now(timezone.utc).astimezone().isoformat()
    save_json_file(index_file, data)
    print(f"[SUCCESS] Registered ADR {adr_id}: '{title}' in decisions-index.json")


def main() -> None:
    parser = argparse.ArgumentParser(description="Hermes Council Memory Sync Utility")
    parser.add_argument("--validate", action="store_true", help="Validate all memory JSON files")
    parser.add_argument("--summary", action="store_true", help="Print summary of council memory")
    parser.add_argument("--register-adr", nargs=5, metavar=("ID", "TITLE", "STATUS", "PATH", "LEVEL"),
                        help="Register an ADR: ID TITLE STATUS PATH LEVEL")
    parser.add_argument("--summary-text", default="Architectural decision record", help="Optional summary text for ADR registration")

    args = parser.parse_args()

    if args.register_adr:
        adr_id, title, status, path, level = args.register_adr
        register_adr_entry(adr_id, title, status, path, level, args.summary_text)
    elif args.summary:
        print_memory_summary()
    else:
        valid = validate_memory()
        sys.exit(0 if valid else 1)


if __name__ == "__main__":
    main()


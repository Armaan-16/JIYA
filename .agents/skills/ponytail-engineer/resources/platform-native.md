# PONYTAIL Resource: Platform-Native & Stdlib Capabilities

> **Reference Guide:** Exploiting Windows 11 & Python 3.12 capabilities without external package baggage.

---

## 1. Python 3.12 Built-ins to Prioritize
- **Structured Data:** `dataclasses.dataclass(slots=True, frozen=True)` for high-performance memory-efficient models.
- **File System:** `pathlib.Path` for cross-platform, clean path manipulation.
- **Async Concurrency:** `asyncio.TaskGroup` (Python 3.11+) for structured asynchronous task execution without dangling tasks.
- **Embedded Database:** `sqlite3` for persistent storage, vectors (via custom embeddings table + BLOB / JSON), and audit logs.
- **Type Annotations:** `typing.TypedDict`, `typing.Annotated`, and `collections.abc` for contract declarations without runtime overhead.

## 2. Windows-Native Tools
- **Process Management:** `Get-Process`, `Stop-Process`, `Start-Process` via PowerShell.
- **Notifications:** Windows native `BurntToast` or standard PowerShell UI balloon notifications.
- **Audio Output:** Standard Windows PowerShell audio synthesis (`System.Speech.Synthesis.SpeechSynthesizer`) as zero-dependency fallback for voice.
- **Task Scheduling:** Windows Task Scheduler (`schtasks.exe`) for persistent cron-like automations.


# ECC Rule: Context & Token Efficiency

> **Mandate:** Prompt context is a finite, degrading resource. Conserve context tokens aggressively to prevent model hallucination and reasoning degradation.

---

## 1. Targeted File Ingestion
- Never dump entire multi-thousand-line files into conversation context if only a 20-line function is being inspected or modified.
- Use `view_file` with precise `StartLine` and `EndLine` parameters.
- For broad exploration, inspect symbol outlines or directory structures first.

## 2. Command Output Truncation
- Pipe large outputs through filters (e.g. `Select-Object -First 20` or `grep`/`findstr`).
- Do not dump multi-megabyte log files into chat. Summarize or extract stack traces using Python or PowerShell one-liners.

## 3. Ephemeral Scratch Management
- Keep intermediate testing and exploratory scripts in conversation scratch space (`<appDataDir>/brain/<conversation-id>/scratch/`).
- Do not pollute git tracking with temporary dump files.


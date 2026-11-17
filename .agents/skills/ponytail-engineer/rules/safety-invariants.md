# PONYTAIL Rule: Safety Invariants in Simplicity

> **Mandate:** Simplicity is not laziness. Removing safety guards, error handling, or tests under the guise of "making it simpler" is strictly forbidden.

---

## Non-Negotiable Simplicity Invariants

1. **No Silent Error Swallowing:**
   - Writing `except Exception: pass` is not simplicity; it is a critical defect.
   - Catch specific exceptions, log meaningful context, and fail gracefully.

2. **Clean Resource Teardown:**
   - Always use context managers (`with open(...)`, `with connection:`) to ensure sockets, files, and subprocesses close cleanly.

3. **Data Integrity:**
   - When writing to disk or updating memory files, use atomic write strategies (write to `.tmp` file, then `os.replace`) to prevent corrupted zero-byte files upon abrupt exit or crash.

4. **Clarity Over Cleverness:**
   - Avoid unreadable 5-line nested list comprehensions or obscure lambda hacks. Write clean, readable 4-line procedural code. Code is read 10x more often than it is written.


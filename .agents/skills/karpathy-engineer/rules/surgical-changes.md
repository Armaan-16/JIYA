# KARPATHY Rule: Surgical Changes & Precision Editing

> **Mandate:** Prefer targeted contiguous replacement over wholesale file overwrites.

---

## Precision Diff Principles

1. **Use `replace_file_content` Over `write_to_file`:**
   - When modifying existing files, always use targeted replacement blocks.
   - Specify accurate line ranges and unambiguous context lines.
   - Do not overwrite an existing 300-line file with a 300-line rewrite just to change 5 lines.

2. **Whitespace Neutrality:**
   - Match existing indentation style (4 spaces vs 2 spaces, tabs vs spaces).
   - Do not trim trailing whitespace across lines you did not intentionally modify.
   - Preserve existing newline conventions (`\r\n` vs `\n`).

3. **Self-Contained Logic Blocks:**
   - Structure edits so that the replacement chunk forms a logically complete, coherent unit.
   - Double-check that all open brackets, parentheses, and indentation blocks remain balanced.


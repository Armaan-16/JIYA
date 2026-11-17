# KARPATHY Reference: Common Agent Coding Pitfalls

> A field guide to pathological AI coding behaviors to detect, resist, and eradicate.

---

| Pitfall | Symptoms | Antidote (Council Rule) |
|---|---|---|
| **The Megadiff Trap** | AI replaces 300 lines to change 3 variables. | **KARPATHY:** Enforce `replace_file_content` with minimal contiguous diffs. |
| **Comment Annihilation** | AI silently deletes license headers, docstrings, and inline notes. | **KARPATHY:** Mandatory checklist to preserve comments verbatim. |
| **Premature Indirection** | AI creates an AbstractFactory, Interface, and 3 adapters for a simple dictionary lookup. | **PONYTAIL:** Decision ladder; write a 4-line function. |
| **Phantom Verification** | AI says "I have tested this and it works!" without actually running the code. | **GSD & ECC:** Demand terminal execution output with return code 0. |
| **Scope Creep** | AI decides to reorganize the folder structure while fixing a typo. | **KARPATHY:** Strict boundary control; reject unrelated file edits. |
| **Hallucinated Stdlib / Pip** | AI imports non-existent methods (e.g. `pathlib.Path.read_json`). | **KARPATHY:** Verify imports against official Python 3.12 documentation. |
| **Context Exhaustion** | AI reads 10 large files into context, gets confused, forgets user constraints. | **ECC & HERMES:** Curated context injection and line-bounded reads. |


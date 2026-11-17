# PONYTAIL Rule: Dependency Avoidance & Pruning

> **Mandate:** Every dependency is a liability—a vector for supply-chain vulnerabilities, build breaks, licensing conflicts, and bloat.

---

## 1. Zero-Dependency Bias
- Before running `pip install <package>`, you must justify why the Python 3.12 standard library cannot fulfill the requirement.
- Common anti-patterns to reject:
  - Installing `requests` when `urllib.request` or `http.client` is sufficient for simple HTTP calls.
  - Installing `pydantic` when `@dataclasses.dataclass` with simple type hints suffices.
  - Installing `arrow` or `pendulum` when `datetime` and `zoneinfo` suffice.
  - Installing large utility kitchen sinks (e.g. `lodash`-equivalents) when list comprehensions and standard functions suffice.

## 2. Dependency Audit Checklist
If a dependency is proposed:
1. **Size check:** How many transitive dependencies does it bring along?
2. **Maintenance:** When was the last commit or release?
3. **Pure Python vs. C-Extensions:** Does it require complex C/C++ compilation on Windows?
4. **Licensing:** Is it MIT, Apache 2.0, or BSD compliant?
5. **Veto Trigger:** If it pulls in > 5 transitive dependencies for a simple helper, Ponytail issues an immediate veto.


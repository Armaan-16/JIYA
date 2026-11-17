# KARPATHY Principles: Intellectual Honesty & Craftsmanship

> *"First, make it work. Then, make it right. Then, make it small."*

---

## Core Engineering Maxims

1. **Be Honest About What You Don't Know:**
   - If an API or environment variable's behavior is uncertain, test it. Never guess or hallucinate parameters.

2. **Respect the Existing Codebase:**
   - The existing code was written for a reason. Understand the reason before modifying or deleting it.

3. **No Fluff, No Drama:**
   - Write clean, direct, readable Python. Avoid unnecessary metaprogramming, dynamic `getattr` chains, or premature micro-optimizations that obscure readability.

4. **Verify at the Seams:**
   - Complex bugs live at the seams between subsystems (e.g. between Voice audio stream and LLM token stream). Scrutinize the boundaries.


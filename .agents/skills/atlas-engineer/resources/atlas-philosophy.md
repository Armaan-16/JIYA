# ATLAS Philosophy: Architectural Durability & Stewardship

> *"Architecture is the decisions that you wish you could get right the first time."* — Ralph Johnson

---

## Foundational Tenets

### 1. Durability Over Expediency
Quick hacks accumulate compound interest in technical debt. When building an autonomous OS like JIYA, every shortcut in data modeling or process isolation will manifest as hallucinations, hung threads, or corrupted memory later. Build foundations to last.

### 2. Explicit Domain Models
Domain entities must be clearly defined in `MODELS/` with typing, validation, and serialization contracts. Never pass untyped dictionaries or ambiguous string blobs across major subsystem boundaries.

### 3. Layered Isolation
- **Presentation & Interfaces:** (`UI/`, `VOICE/`, `main.py`) handles I/O, user parsing, audio streaming.
- **Orchestration:** (`CORE/planner.py`, `CORE/session.py`) coordinates flows.
- **Capabilities & Services:** (`SERVICES/`, `AUTOMATION/`) perform work.
- **Entities & Schemas:** (`MODELS/`) represent state.
- **Invariants:** Dependencies point inward and downward. Never upward.

### 4. Reversible vs. Irreversible Decisions
- Type 1 (Irreversible): Database storage formats, external network protocols, core process models. Require rigorous ADR deliberation.
- Type 2 (Reversible): Internal method refactoring, helper algorithms, prompt tuning. Move quickly but surgically.


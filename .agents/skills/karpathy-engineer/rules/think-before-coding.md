# KARPATHY Rule: Think Before Coding (Hypothesis-Driven Method)

> **Mandate:** Writing code is the *last* step of problem solving, not the first.

---

## The 4-Step Mental Model

### Step 1: Trace the Execution Path
- Trace the control flow mentally or by inspecting the call stack before writing a fix.
- Know the exact values of variables at the moment of failure.

### Step 2: Formulate the Hypothesis
- Write down:
  > *"I hypothesize that variable `X` is `None` because caller `Y` does not pass the default session ID when invoked from the CLI router."*

### Step 3: Test the Hypothesis Minimally
- Add an explicit assertion or inspect a reproduction script.
- Verify that the hypothesis is true before writing the fix.

### Step 4: Implement and Verify
- Apply the minimal change.
- Verify that the error is gone AND that other test cases still pass.


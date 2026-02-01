# 🤖 AI_REPORT.md
**Team: NEW QUBITTERS**  

---

## 1. The AI Workflow

We treated AI tools as **engineering collaborators**, not as sources of truth.

Our primary AI tool was **ChatGPT**, which we used throughout Phase 2 for:
- Structuring the hybrid pipeline (quantum seeding → classical refinement)
- Writing and refactoring CUDA-Q kernels
- Debugging CUDA-Q runtime errors
- Designing unit tests and verification strategies
- Improving code organization and readability

We deliberately **did not rely on a single AI session**. When conversations became long or confusing, we started fresh chats with **clear, narrow prompts** to avoid context drift.

All final decisions (architecture, pivots, parameter choices) were made by us after testing and validation.

---

## 2. Verification Strategy (How We Prevented AI Hallucinations)

Because AI-generated code can silently fail or hallucinate APIs, we enforced **verification-first development**.

### Our Core Rule
> *No AI-generated code was trusted unless it passed an automated test.*

### Concrete Verification Methods

We implemented a **PyTest-based test suite** that validated:

- **Physics correctness**
  - LABS symmetry check:  
    `energy(S) == energy(-S)`
- **Small-N ground truth**
  - Manual or brute-force verification for small N (e.g., N = 3–10)
- **Quantum kernel execution**
  - Ensured CUDA-Q kernels execute and return valid bitstrings
- **Pipeline integrity**
  - Verified quantum seeding → MTS → final result works end-to-end

These tests caught multiple issues early, including:
- Incorrect CUDA-Q kernel signatures
- Invalid imports suggested by AI
- Logical errors in seed handling

Without the test suite, these errors would have gone unnoticed.

---

## 3. The “Vibe” Log

### ✅ Win (Where AI Saved Us Hours)

AI significantly accelerated:
- Writing initial CUDA-Q kernel scaffolding
- Converting bitstring samples into LABS sequences
- Rapidly iterating on pipeline structure during Phase 2

This allowed us to focus more time on **verification, benchmarking, and GPU usage**, which mattered most for the challenge.

---

### 📚 Learn (How We Improved Prompting)

Early on, vague prompts produced vague or incorrect code.

We improved results by:
- Providing **explicit context** (CUDA-Q version, LABS formulation)
- Asking for **small, testable components** instead of full solutions
- Pasting **error traces back into AI** instead of describing errors verbally

This dramatically improved the quality of AI output.

---

### ❌ Fail (Where AI Got It Wrong)

AI occasionally:
- Suggested non-existent CUDA-Q APIs
- Assumed quantum advantage where none was demonstrated
- Produced code that looked correct but failed silently

These failures reinforced why:
- Tests are mandatory
- Manual reasoning is still required
- AI should assist, not replace engineering judgment

Each failure was resolved by:
- Writing or extending tests
- Checking official CUDA-Q documentation
- Simplifying the approach when necessary

---

## 4. Context Dump (How We Used AI Responsibly)

Examples of prompts we used:
- “Help refactor this CUDA-Q kernel so it can be tested independently”
- “Write PyTest tests that would catch symmetry violations in LABS energy”
- “Given this runtime error, explain what CUDA-Q is expecting”

We intentionally avoided prompts like:
- “Optimize this fully”
- “Give best parameters”
- “Guarantee improvement”

Instead, we focused on **understanding, testing, and iterating**.

---

## 5. Final Reflection

AI made us **faster**, but verification made us **correct**.

The biggest takeaway from this challenge is that:
- Hybrid quantum–classical workflows require **engineering discipline**
- GPU acceleration must be justified with measurements
- Negative results (e.g., statevector scaling limits) are valuable when documented honestly

This project reflects how AI can be responsibly integrated into a real R&D-style workflow.

---

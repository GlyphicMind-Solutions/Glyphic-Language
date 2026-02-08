# Training Pipeline
This document describes the full training pipeline for fine‑tuning an LLM on the Glyphic Language.

---

# 1. Preprocessing
- validate all datasets
- remove duplicates
- shuffle
- split into train/val/test

---

# 2. Training Stages

## Stage 1 — Dictionary Grounding
Dataset: glyph_to_text.jsonl

## Stage 2 — Structured Meaning
Dataset: structured_meaning.jsonl

## Stage 3 — Translation
Dataset: text_to_glyph.jsonl

## Stage 4 — Syntax Enforcement
Synthetic invalid examples

## Stage 5 — Scene Construction
Synthetic multi‑glyph scenes

## Stage 6 — Soulfile™ Integration
Memory encoding examples

---

# 3. Model Type
Recommended:

- 7B–13B model
- QLoRA or LoRA
- 3–5 epochs per stage

---

# 4. Evaluation
Run:

- syntax tests
- reversibility tests
- dictionary consistency tests
- Soulfile™ encoding tests

---

# 5. Deployment
The fine‑tuned model is loaded by:

- life.py
- controllers
- Soulfile™ systems
- glyph interpreter


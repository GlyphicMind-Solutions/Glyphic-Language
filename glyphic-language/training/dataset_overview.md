# Dataset Overview
The /training/ folder contains all datasets required to fine‑tune an LLM for the Glyphic Language.

## Files

### 1. glyph_to_text.jsonl
Maps individual glyphs to:

- primary meaning
- synonyms
- roles
- categories
- example usage

Used for dictionary grounding.

### 2. text_to_glyph.jsonl
Maps natural language descriptions to canonical glyph sequences.

Used for translation training.

### 3. structured_meaning.jsonl
Maps glyph sequences to structured meaning dictionaries.

Used for scene interpretation and semantic grounding.

---

## Dataset Philosophy
All datasets follow these principles:

- deterministic
- reversible
- dictionary‑driven
- syntax‑aligned
- context‑aware
- LLM‑friendly

Each dataset is designed to teach a specific layer of the language.


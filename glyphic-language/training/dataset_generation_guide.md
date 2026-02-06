# Dataset Generation Guide
This guide explains how to generate new training examples for the Glyphic Language.

---

# 1. Dictionary‑Driven Generation
All examples must be derived from:

- dictionary entries
- syntax rules
- BNF grammar

No freeform glyph usage is allowed.

---

# 2. Example Types

## 2.1 Atomic Examples
Single glyph → meaning  
Meaning → single glyph

## 2.2 Scene Examples
Full sequences with:

- actor
- action
- object
- modifiers
- context

## 2.3 Negative Examples
Invalid sequences for syntax training.

## 2.4 Symbolic Examples
Mythic, emotional, sensory, or social scenes.

---

# 3. Generation Process

1. Select glyph(s) from dictionary  
2. Build a valid sequence using syntax rules  
3. Generate structured meaning  
4. Generate natural language description  
5. Add to appropriate dataset file  

---

# 4. Quality Requirements

- No ambiguity  
- No hallucinated glyphs  
- No missing roles  
- No invalid ordering  
- No duplicate examples  


# Evaluation Guide
This guide defines how to evaluate an LLM trained on the Glyphic Language.

---

# 1. Syntax Tests
Verify:

- ordering rules
- required roles
- context ordering
- single actor/action/object

---

# 2. Reversibility Tests
Check:

encode(interpret(x)) == x

for all valid sequences.

---

# 3. Dictionary Consistency
Ensure:

- no hallucinated glyphs
- no missing dictionary entries
- correct role usage

---

# 4. Scene Interpretation
Test:

- actor/action/object extraction
- modifier interpretation
- context layering

---

# 5. Translation Accuracy
Evaluate:

- text → glyph
- glyph → text
- structured meaning → glyph
- glyph → structured meaning

---

# 6. Soulfile™ Compatibility
Verify:

- memory entries encode correctly
- meaning compression works
- continuity is preserved


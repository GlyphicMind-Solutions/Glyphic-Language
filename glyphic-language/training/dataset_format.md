# Dataset Format Specification
All datasets in this folder use JSON Lines (.jsonl) format.

Each line is a standalone training example:

{"input": "...", "output": "..."}

---

# 1. glyph_to_text.jsonl

## Format
{
"input": "🌱",
"output": {
"id": "glyph.object.nature.sprout",
"primary": "sprout",
"synomic": ["growth", "seedling", "new life"],
"roles": ["object", "symbol"]
}

---

# 2. text_to_glyph.jsonl

## Format
{
"input": "a new beginning, growth, seedling",
"output": "🌱"
}

---

# 3. structured_meaning.jsonl

## Format
{
"input": "👤✍️📄🌙",
"output": {
"actor": {"id": "glyph.actor.person"},
"action": {"id": "glyph.action.write"},
"object": {"id": "glyph.object.document.page"},
"context": {
"time": [{"id": "context.time.night"}]
}


---

# Validation Rules
- All glyphs must exist in the dictionary.
- All sequences must obey syntax rules.
- All structured meaning must be canonical.


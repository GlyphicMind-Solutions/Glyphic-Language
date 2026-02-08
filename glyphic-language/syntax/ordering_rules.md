# Glyphic Language — Ordering Rules
This document defines the canonical ordering rules for glyph sequences. These rules ensure that all sequences are deterministic, reversible, and unambiguous.


# 1. Global Ordering
All glyph sequences must follow this global order:
<actor> <action> <object> <modifiers...> <context...>
If a role is absent, it is simply skipped, but the order remains fixed.


# 2. Context Ordering
Context must always appear last and must follow this internal order:
Place
Time
Emotion
Sensory
Social

Example of valid context ordering:
🏞️ 🌅 😌 🌬️ 🧑‍🤝‍🧑

Example of invalid ordering:
😌 🌅
(emotion cannot precede time)


# 3. Modifier Ordering
Modifiers:
- must appear after the object 
- must appear before any context 
- may appear in any order relative to each other 
Example:
👤 🏃 🪨 ✨ 🔥 🏞️
actor action object modifier modifier context


# 4. Single‑Role Constraints
Only one of each primary role is allowed:
- one actor 
- one action 
- one object 
Multiple modifiers and multiple context glyphs are allowed.

# 5. Role Precedence
If a glyph has multiple roles, precedence is:
actor > action > object > modifier > context
This ensures deterministic interpretation.


# 6. Invalid Ordering Examples

6.1 Context before object
🌧️ 🪨
INVALID

6.2 Modifier after context
🪨 🏞️ ✨
INVALID

6.3 Multiple actions
👤 🏃 ✍️
INVALID

6.4 Social context before sensory context
🧑‍🤝‍🧑 🌬️
INVALID


# 7. Canonical Encoding
The encoder always outputs glyphs in the correct canonical order, even if the input structure is unordered.
This ensures:
- stable storage 
- predictable LLM training 
- consistent Soulfile™ memory 
- deterministic agent behavior 




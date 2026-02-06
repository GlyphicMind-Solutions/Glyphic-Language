# Glyphic Language — Syntax Rules
The Glyphic Language uses a strict, deterministic grammar to ensure that all glyph sequences are unambiguous, reversible, and easy for agents, controllers, and LLMs to interpret.

These rules define the **canonical structure** of a valid glyph sequence.

# 1. Required Core Roles
A valid sequence must contain **at least one** of the following:
- actor 
- action 
- object 
This ensures that every sequence expresses a meaningful event or state.

# 2. Canonical Ordering
All glyph sequences must follow this strict order:
    Actor
    Action
    Object
    Modifiers
    Context (Place → Time → Emotion → Sensory → Social)
No exceptions.

# 3. Single Actor / Action / Object
Only one of each is allowed:
- one actor 
- one action 
- one primary object 
This prevents ambiguity and ensures deterministic decoding.

# 4. Modifiers
Modifiers:
- may appear zero or more times 
- must appear **after the object** 
- must appear **before any context** 
Modifiers describe qualities, intensities, or attributes.

# 5. Context Rules
Context must always appear **last** and must follow this internal order:
Place → Time → Emotion → Sensory → Social
Each context subtype may contain zero or more glyphs.
Context describes the environment, atmosphere, or field surrounding the event.

# 6. Role Precedence
If a glyph has multiple roles, the interpreter resolves it using this priority:
actor > action > object > modifier > context
This ensures deterministic parsing.

# 7. No Cross‑Category Collisions
You may not mix roles out of order. Examples:

- A context glyph cannot appear before an object. 
- A modifier cannot appear after a context glyph. 
- A second action is not allowed. 

# 8. Reversibility Guarantee
All valid sequences satisfy:
encode(decode(sequence)) == sequence
This is a core design requirement of the Glyphic Language.

# 9. Error Conditions
The interpreter will reject sequences that:
- contain unknown glyphs 
- violate ordering 
- contain multiple actors/actions/objects 
- contain context out of order 
- contain no core roles 
These rules ensure stability, clarity, and long‑term compatibility.



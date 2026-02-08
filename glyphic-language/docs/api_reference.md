# Glyphic Language — API Reference
This document describes the public API exposed by the Glyphic Language interpreter. These functions provide the official interface for encoding, decoding, validating, and explaining glyph sequences.

All functions are deterministic and dictionary‑driven.

# Module Import
python:

from glyphic_language.interpreter import interpret, encode, validate, explain


1. interpret(glyph_string)
Description:  
Parses a glyph sequence and returns a structured semantic representation.
Signature:
interpret(glyph_string: str) -> dict
Returns:  
A dictionary containing actor, action, object, modifiers, context layers, and raw input.
Raises:
    Syntax errors
    Validation errors


2. encode(structured_dict)
Description:  
Converts a structured meaning dictionary into a canonical glyph sequence.
Signature:
encode(structured: dict) -> str
Returns:  
A glyph string in strict canonical order.
Guarantees:
encode(interpret(x)) == x
for all valid sequences.
3. validate(glyph_string)

Description:  
Validates glyph existence, role correctness, and strict syntax ordering.

Signature:
python

validate(glyph_string: str) -> None

Raises:

    Unknown glyph errors

    Missing core role errors

    Ordering violations

    Context ordering violations

4. explain(glyph_string)

Description:  
Produces a human‑readable explanation of the meaning of a glyph sequence.

Signature:
python

explain(glyph_string: str) -> str

Returns:  
A textual summary of actors, actions, objects, modifiers, and context.
Interpreter Guarantees

    Deterministic parsing

    Reversible encoding

    Strict grammar enforcement

    Dictionary‑driven semantics

    Zero hallucination

    Stable integration with Soulfile™ systems

This API is the official gateway for all agents, controllers, and external tools interacting with the Glyphic Language.

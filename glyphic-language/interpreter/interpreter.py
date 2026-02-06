from typing import Dict, Any
from .glyph_decoder.py import decode_glyphs
from .glyph_encoder import encode_meaning
from .glyph_validator import validate_sequence, validate_roles
from .glyph_syntax import get_syntax_tree


def interpret(glyph_string: str) -> Dict[str, Any]:
    """
    High-level API: glyph string → structured meaning.
    """
    glyphs = list(glyph_string)
    return decode_glyphs(glyphs)


def encode(structured: Dict[str, Any]) -> str:
    """
    High-level API: structured meaning → glyph string.
    """
    return encode_meaning(structured)


def validate(glyph_string: str) -> None:
    """
    High-level API: validate glyph string.
    """
    glyphs = list(glyph_string)
    validate_sequence(glyphs)
    validate_roles(glyphs)


def explain(glyph_string: str) -> str:
    """
    Human-readable explanation of a glyph sequence.
    Prototype: uses primary meanings.
    """
    glyphs = list(glyph_string)
    tree = get_syntax_tree(glyphs)

    parts = []

    def names(entries):
        return [e.get("primary", e.get("id", "?")) for e in entries]

    if tree["actors"]:
        parts.append(f"Actors: {', '.join(names(tree['actors']))}")
    if tree["actions"]:
        parts.append(f"Actions: {', '.join(names(tree['actions']))}")
    if tree["objects"]:
        parts.append(f"Objects: {', '.join(names(tree['objects']))}")
    if tree["modifiers"]:
        parts.append(f"Modifiers: {', '.join(names(tree['modifiers']))}")

    ctx = tree["context"]
    if ctx["place"]:
        parts.append(f"Place context: {', '.join(names(ctx['place']))}")
    if ctx["time"]:
        parts.append(f"Time context: {', '.join(names(ctx['time']))}")
    if ctx["emotion"]:
        parts.append(f"Emotional context: {', '.join(names(ctx['emotion']))}")
    if ctx["sensory"]:
        parts.append(f"Sensory context: {', '.join(names(ctx['sensory']))}")
    if ctx["social"]:
        parts.append(f"Social context: {', '.join(names(ctx['social']))}")

    if not parts:
        return "No semantic structure detected."

    return " | ".join(parts)


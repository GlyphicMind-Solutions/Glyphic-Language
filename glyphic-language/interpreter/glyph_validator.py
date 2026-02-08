from typing import List
from .glyph_dictionary_loader import get_dictionary


class GlyphValidationError(Exception):
    pass


def validate_glyph(glyph: str) -> None:
    dictionary = get_dictionary()
    entries = dictionary.get_entry_by_glyph(glyph)
    if not entries:
        raise GlyphValidationError(f"Unknown glyph: {glyph}")


def validate_sequence(glyphs: List[str]) -> None:
    if not glyphs:
        raise GlyphValidationError("Empty glyph sequence.")

    for g in glyphs:
        validate_glyph(g)


def validate_roles(glyphs: List[str]) -> None:
    """
    Minimal role validation prototype:
    - Ensure at least one non-context role exists (e.g., object/action/actor)
    """
    dictionary = get_dictionary()
    has_core_role = False

    for g in glyphs:
        entries = dictionary.get_entry_by_glyph(g) or []
        for e in entries:
            roles = e.get("roles", [])
            if any(r in roles for r in ["object", "action", "actor"]):
                has_core_role = True
                break

    if not has_core_role:
        raise GlyphValidationError("Sequence has no core roles (object/action/actor).")


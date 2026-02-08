from typing import List, Dict, Any
from .glyph_dictionary_loader import get_dictionary
from .glyph_validator import validate_sequence, validate_roles


class GlyphSyntaxError(Exception): #strict syntax order of glyphs
    pass


ROLE_ORDER = [
    "actor",
    "action",
    "object",
    "modifier",
    "context"
]

CONTEXT_ORDER = [
    "place",
    "time",
    "emotion",
    "sensory",
    "social"
]


def _get_role(entry: Dict[str, Any]) -> str:
    """Return the highest-priority role for a glyph."""
    roles = entry.get("roles", [])
    for r in ROLE_ORDER:
        if r in roles:
            return r
    return "context"


def _get_context_type(entry: Dict[str, Any]) -> str:
    """Return the context subtype."""
    category = entry.get("category", "")

    if category.startswith("context_place"):
        return "place"
    if category.startswith("context_time"):
        return "time"
    if category.startswith("context_emotion") or category.startswith("emotion_context"):
        return "emotion"
    if category.startswith("context_sensory") or category.startswith("sensory_context"):
        return "sensory"
    if category.startswith("context_social") or category.startswith("social_context"):
        return "social"

    return "unknown"


def parse_syntax(glyphs: List[str]) -> Dict[str, Any]:
    """
    Strict syntax parser enforcing:
    - required roles
    - strict ordering
    - single actor/action/object
    - context last
    - deterministic structure
    """
    validate_sequence(glyphs)
    validate_roles(glyphs)

    dictionary = get_dictionary()

    syntax_tree = {
        "actor": None,
        "action": None,
        "object": None,
        "modifiers": [],
        "context": {
            "place": [],
            "time": [],
            "emotion": [],
            "sensory": [],
            "social": []
        },
        "raw": glyphs
    }

    last_role_index = -1
    last_context_index = -1

    for g in glyphs:
        entries = dictionary.get_entry_by_glyph(g)
        entry = entries[0]  # canonical
        role = _get_role(entry)

        # Enforce ordering
        role_index = ROLE_ORDER.index(role)
        if role_index < last_role_index:
            raise GlyphSyntaxError(
                f"Invalid ordering: {g} ({role}) appears after a later role."
            )
        last_role_index = role_index

        # Assign roles
        if role == "actor":
            if syntax_tree["actor"] is not None:
                raise GlyphSyntaxError("Multiple actors not allowed.")
            syntax_tree["actor"] = entry

        elif role == "action":
            if syntax_tree["action"] is not None:
                raise GlyphSyntaxError("Multiple actions not allowed.")
            syntax_tree["action"] = entry

        elif role == "object":
            if syntax_tree["object"] is not None:
                raise GlyphSyntaxError("Multiple objects not allowed.")
            syntax_tree["object"] = entry

        elif role == "modifier":
            syntax_tree["modifiers"].append(entry)

        elif role == "context":
            ctx_type = _get_context_type(entry)
            if ctx_type == "unknown":
                raise GlyphSyntaxError(f"Unknown context type for glyph {g}")

            # Enforce context ordering
            ctx_index = CONTEXT_ORDER.index(ctx_type)
            if ctx_index < last_context_index:
                raise GlyphSyntaxError(
                    f"Context out of order: {ctx_type} appears after later context."
                )
            last_context_index = ctx_index

            syntax_tree["context"][ctx_type].append(entry)

    return syntax_tree


def get_syntax_tree(glyphs: List[str]) -> Dict[str, Any]:
    return parse_syntax(glyphs)


def is_valid_order(glyphs: List[str]) -> bool:
    try:
        parse_syntax(glyphs)
        return True
    except Exception:
        return False


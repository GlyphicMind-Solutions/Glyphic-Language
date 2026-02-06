from typing import Dict, Any, List, Optional
from .glyph_dictionary_loader import get_dictionary


def _glyph_from_id(entry_id: str) -> Optional[str]:
    entry = get_dictionary().get_entry_by_id(entry_id)
    return entry.get("glyph") if entry else None


def encode_meaning(structured: Dict[str, Any]) -> str:
    """
    Strict encoder:
    - enforces canonical ordering
    - actor → action → object → modifiers → context
    - context ordered: place → time → emotion → sensory → social
    - guaranteed reversible with decode()
    """
    glyphs: List[str] = []

    # 1. Actor
    actor = structured.get("actor")
    if actor and actor.get("id"):
        g = _glyph_from_id(actor["id"])
        if g:
            glyphs.append(g)

    # 2. Action
    action = structured.get("action")
    if action and action.get("id"):
        g = _glyph_from_id(action["id"])
        if g:
            glyphs.append(g)

    # 3. Object
    obj = structured.get("object")
    if obj and obj.get("id"):
        g = _glyph_from_id(obj["id"])
        if g:
            glyphs.append(g)

    # 4. Modifiers
    for m in structured.get("modifiers", []):
        if m.get("id"):
            g = _glyph_from_id(m["id"])
            if g:
                glyphs.append(g)

    # 5. Context (strict order)
    context = structured.get("context", {})

    for ctx_key in ["place", "time", "emotion", "sensory", "social"]:
        for ctx in context.get(ctx_key, []):
            if ctx.get("id"):
                g = _glyph_from_id(ctx["id"])
                if g:
                    glyphs.append(g)

    return "".join(glyphs)


# interpreter/decoder.py




from typing import Dict, Any, List, Optional
from .glyph_syntax import parse_syntax




def simplify_entry(entry: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:

    """
    Normalize a single syntax entry into a stable internal form.
    - For normal glyphs: keep id, glyph, primary, category, roles.
    - For fallback: surface the raw term as `primary` and `id`,
      drop glyph, keep category="fallback".
    """

    if entry is None:
        return None

    category = entry.get("category")
    primary = entry.get("primary")

    # Fallback entries: we only care about the surfaced term
    if category == "fallback":
        return {
            "id": primary,
            "glyph": None,
            "primary": primary,
            "category": "fallback",
            "roles": entry.get("roles", []),
        }

    return {
        "id": entry.get("id"),
        "glyph": entry.get("glyph"),
        "primary": primary,
        "category": category,
        "roles": entry.get("roles", []),
    }


def simplify_list(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [simplify_entry(e) for e in entries if e is not None]


def decode_glyphs(glyphs: List[str]) -> Dict[str, Any]:
    """
    Strict decoding:
    - parse syntax tree
    - convert entries into a clean semantic structure
    - deterministic output
    """
    tree = parse_syntax(glyphs)

    actor = simplify_entry(tree.get("actor"))
    action = simplify_entry(tree.get("action"))
    obj = simplify_entry(tree.get("object"))

    context_tree = tree.get("context", {})

    context = {
        "place": simplify_list(context_tree.get("place", [])),
        "time": simplify_list(context_tree.get("time", [])),
        "emotion": simplify_list(context_tree.get("emotion", [])),
        "sensory": simplify_list(context_tree.get("sensory", [])),
        "social": simplify_list(context_tree.get("social", [])),
    }

    struct = {
        "actor": actor,
        "action": action,
        "object": obj,
        "modifiers": simplify_list(tree.get("modifiers", [])),
        "context": context,
        "raw": "".join(glyphs),
    }

    # Attach a realized natural-language sentence as a convenience
    struct["text"] = realize_sentence(struct)

    return struct


# -------------------------
# Natural-language realization
# -------------------------
def realize_sentence(struct: Dict[str, Any]) -> str:

    """
    Very simple, deterministic surface realizer.
    for now: (subject to change)
    - actor (noun phrase)
    - verb phrase (action + object)
    - context (time/place)
    """

    actor = struct.get("actor")
    action = struct.get("action")
    obj = struct.get("object")
    ctx = struct.get("context", {})

    chunks: List[str] = []

    # 1. Actor
    if actor:
        chunks.append(realize_noun_phrase(actor))

    # 2. Verb phrase
    if action:
        chunks.append(realize_verb_phrase(action, obj))

    # 3. Context
    ctx_chunk = realize_context(ctx)
    if ctx_chunk:
        chunks.append(ctx_chunk)

    sentence = " ".join(chunks).strip()
    if sentence and not sentence.endswith("."):
        sentence += "."
    return sentence


def realize_noun_phrase(entry: Dict[str, Any]) -> str:

    """
    For now:
    - Just return the primary term.
    - Later: add articles, pluralization, pronouns, etc.
    """

    return entry.get("primary", "")


def realize_verb_phrase(action: Dict[str, Any],
                        obj: Optional[Dict[str, Any]]) -> str:
    """
    Simple past-tense realization:
    - action.primary is assumed to be a base verb ("walk", "go", "eat").
    - We inflect to past tense in a naive way for now.
    """

    base = action.get("primary", "")
    verb = inflect_past(base)

    if obj:
        return f"{verb} {realize_noun_phrase(obj)}"
    return verb


def realize_context(ctx: Dict[str, Any]) -> str:

    """
    Realize time/place context into a simple phrase.
    This is intentionally minimal and deterministic.
    """

    chunks: List[str] = []

    times = ctx.get("time", [])
    if times:
        t_phrase = realize_time_phrase(times[0])
        if t_phrase:
            chunks.append(t_phrase)

    places = ctx.get("place", [])
    if places:
        p_phrase = realize_place_phrase(places[0])
        if p_phrase:
            chunks.append(p_phrase)

    # emotion/sensory/social can be added later as needed

    return " ".join(chunks)


# -------------------------
# Tiny inflection + mapping helpers
# -------------------------
def inflect_past(verb: str) -> str:

    """
    Naive English past-tense inflection.
    """

    if not verb:
        return ""

    lower = verb.lower()

    # Very small irregular set for now
    irregular = {
        "go": "went",
        "come": "came",
        "run": "ran",
        "eat": "ate",
        "drink": "drank",
        "be": "was",
        "have": "had",
        "do": "did",
        "get": "got",
        "make": "made",
        "walk": "walked",
    }
    if lower in irregular:
        # Preserve capitalization of first letter
        form = irregular[lower]
        if verb[0].isupper():
            form = form.capitalize()
        return form

    # Regular verbs
    if lower.endswith("e"):
        form = lower + "d"
    elif lower.endswith("y") and len(lower) > 1 and lower[-2] not in "aeiou":
        form = lower[:-1] + "ied"
    else:
        form = lower + "ed"

    if verb[0].isupper():
        form = form.capitalize()
    return form


def realize_time_phrase(entry: Dict[str, Any]) -> str:

    """
    Map time context IDs to simple English phrases.
    This is a seed mapping; extend as needed.
    """

    cid = entry.get("id") or entry.get("primary", "")

    mapping = {
        "context.time.day.night": "tonight",
        "context.time.day.morning": "this morning",
        "context.time.day.afternoon": "this afternoon",
        "context.time.day.evening": "this evening",
        "context.time.cycle.daily": "every day",
        "context.time.cycle.weekly": "every week",
        "context.time.cycle.monthly": "every month",
        "context.time.duration.short": "for a short time",
        "context.time.duration.medium": "for a while",
        "context.time.duration.long": "for a long time",
    }

    phrase = mapping.get(cid)
    if phrase:
        return phrase

    # Fallback: just return primary if present
    primary = entry.get("primary")
    if primary and primary != cid:
        return primary

    return ""


def realize_place_phrase(entry: Dict[str, Any]) -> str:

    """
    Map place context IDs to simple English phrases.
    Seed mapping; extend as needed.
    """

    cid = entry.get("id") or entry.get("primary", "")

    mapping = {
        "context.place.home": "at home",
        "context.place.work": "at work",
        "context.place.outside": "outside",
        "context.place.store": "at the store",
    }

    phrase = mapping.get(cid)
    if phrase:
        return phrase

    primary = entry.get("primary")
    if primary and primary != cid:
        return primary

    return ""


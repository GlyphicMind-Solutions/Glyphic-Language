# generator/fallback.py

def encode_fallback(term: str):
    """
    Returns the three Glyphic representations for an undefined term.
    """
    upper = term.upper()

    return {
        "human": f'FALLBACK["{term}"]',
        "compact": f"FB{{{upper}}}",
        "tokens": f"<FB:{upper}>"
    }


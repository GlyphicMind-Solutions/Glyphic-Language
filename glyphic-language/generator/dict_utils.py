# generator/dict_utils.py

from typing import Dict, Any


def is_defined(term_id: str, dictionaries: Dict[str, Any]) -> bool:
    """
    Checks if a term_id exists in ANY loaded dictionary.
    """
    if term_id is None:
        return False

    for _, entries in dictionaries.items():
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if entry.get("id") == term_id:
                return True
    return False


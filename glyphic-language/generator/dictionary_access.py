# generator/dictionary_access.py

from pathlib import Path
from typing import Dict, Any

from .config import DICTIONARY_DIR

import json


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_all_dictionaries() -> Dict[str, Any]:
    """
    Loads all core Glyphic dictionaries into a single dict.
    Keys will match filenames without extension, e.g. 'actions', 'actors', etc.
    """
    dictionaries = {}
    for path in DICTIONARY_DIR.glob("*.json"):
        name = path.stem  # e.g. actions.json -> "actions"
        dictionaries[name] = load_json(path)
    return dictionaries


import json
import os
from typing import Dict, List, Any, Optional

DICTIONARY_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "dictionary"
)


class GlyphDictionary:
    def __init__(self) -> None:
        self.entries_by_glyph: Dict[str, List[Dict[str, Any]]] = {}
        self.entries_by_id: Dict[str, Dict[str, Any]] = {}
        self.entries_by_category: Dict[str, List[Dict[str, Any]]] = {}
        self.entries_by_role: Dict[str, List[Dict[str, Any]]] = {}

    def load(self, directory: str = DICTIONARY_DIR) -> None:
        for filename in os.listdir(directory):
            if not filename.endswith(".json"):
                continue
            path = os.path.join(directory, filename)
            with open(path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    raise ValueError(f"Invalid JSON in {filename}: {e}")

            if not isinstance(data, list):
                raise ValueError(f"Dictionary file {filename} must contain a list of entries.")

            for entry in data:
                self._index_entry(entry)

    def _index_entry(self, entry: Dict[str, Any]) -> None:
        glyph = entry.get("glyph")
        entry_id = entry.get("id")
        category = entry.get("category")
        roles = entry.get("roles", [])

        if not glyph or not entry_id or not category:
            raise ValueError(f"Entry missing required fields: {entry}")

        # id index
        if entry_id in self.entries_by_id:
            raise ValueError(f"Duplicate id detected: {entry_id}")
        self.entries_by_id[entry_id] = entry

        # glyph index
        self.entries_by_glyph.setdefault(glyph, []).append(entry)

        # category index
        self.entries_by_category.setdefault(category, []).append(entry)

        # roles index
        for role in roles:
            self.entries_by_role.setdefault(role, []).append(entry)

    def get_entry_by_glyph(self, glyph: str) -> Optional[List[Dict[str, Any]]]:
        return self.entries_by_glyph.get(glyph)

    def get_entry_by_id(self, entry_id: str) -> Optional[Dict[str, Any]]:
        return self.entries_by_id.get(entry_id)

    def get_entries_by_category(self, category: str) -> List[Dict[str, Any]]:
        return self.entries_by_category.get(category, [])

    def get_entries_by_role(self, role: str) -> List[Dict[str, Any]]:
        return self.entries_by_role.get(role, [])


# Singleton-style loader for convenience
_dictionary_instance: Optional[GlyphDictionary] = None


def get_dictionary() -> GlyphDictionary:
    global _dictionary_instance
    if _dictionary_instance is None:
        _dictionary_instance = GlyphDictionary()
        _dictionary_instance.load()
    return _dictionary_instance


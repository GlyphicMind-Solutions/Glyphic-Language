import json
from pathlib import Path

from generator.config import DICTIONARY_DIR

def main():
    for path in DICTIONARY_DIR.glob("*.json"):
        print(f"Checking {path.name}...")
        try:
            with path.open("r", encoding="utf-8") as f:
                json.load(f)
            print(f"  OK")
        except Exception as e:
            print(f"  ERROR in {path.name}: {e}")
            return

if __name__ == "__main__":
    main()


# generator/validator.py

import json
from pathlib import Path

REQUIRED_TOP_LEVEL = {"input_envelope", "output"}
REQUIRED_OUTPUT_KEYS = {"glyphic", "realized"}


def validate_jsonl(path: Path):
    errors = 0
    total = 0

    with path.open("r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"[error] line {line_num}: invalid JSON: {e}")
                errors += 1
                continue

            missing = REQUIRED_TOP_LEVEL - obj.keys()
            if missing:
                print(f"[error] line {line_num}: missing top-level keys: {missing}")
                errors += 1
                continue

            out = obj["output"]
            missing_out = REQUIRED_OUTPUT_KEYS - out.keys()
            if missing_out:
                print(f"[error] line {line_num}: missing output keys: {missing_out}")
                errors += 1

            # quick sanity checks
            if not isinstance(obj["input_envelope"], str):
                print(f"[error] line {line_num}: input_envelope must be a string")
                errors += 1

    print(f"Validated {total} samples, errors: {errors}")


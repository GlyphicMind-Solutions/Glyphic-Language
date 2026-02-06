# generator/run_generator.py

import json
from typing import List, Dict, Any

from .config import OUTPUT_JSONL, DEFAULT_SAMPLE_COUNT
from .dictionary_access import load_all_dictionaries

# Import ALL updated templates
from .templates_basic import generate_emotional_expression_samples
from .templates_actions import generate_action_object_samples
from .templates_context import generate_context_rich_samples
from .templates_context_advanced import generate_advanced_context_samples


def write_jsonl(path, samples: List[Dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for sample in samples:
            f.write(json.dumps(sample, ensure_ascii=False))
            f.write("\n")


def main():
    dictionaries = load_all_dictionaries()

    emotional = generate_emotional_expression_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 4,
        source_language="en",
    )

    actions = generate_action_object_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 4,
        source_language="en",
    )

    context_rich = generate_context_rich_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 4,
        source_language="en",
    )

    advanced = generate_advanced_context_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 4,
        source_language="en",
    )

    samples = emotional + actions + context_rich + advanced

    write_jsonl(OUTPUT_JSONL, samples)
    print(f"Wrote {len(samples)} samples to {OUTPUT_JSONL}")


if __name__ == "__main__":
    main()


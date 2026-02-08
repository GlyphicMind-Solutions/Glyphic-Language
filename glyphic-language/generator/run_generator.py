# generator/run_generator.py

import json
from typing import List, Dict, Any

from .config import OUTPUT_JSONL, DEFAULT_SAMPLE_COUNT
from .dictionary_access import load_all_dictionaries

# Existing semantic templates
from .templates_basic import generate_emotional_expression_samples
from .templates_actions import generate_action_object_samples
from .templates_context import generate_context_rich_samples
from .templates_context_advanced import generate_advanced_context_samples

# NEW protocol-level templates
from .templates_identity import generate_identity_samples
from .templates_intent import generate_intent_samples
from .templates_behavior import generate_behavior_samples
from .templates_memory import generate_memory_samples
from .templates_thought import generate_thought_samples
from .templates_safety_response import generate_safety_response_samples

# Envelope + training builder
from .training_builder import build_training_sample, save_samples


def main():
    dictionaries = load_all_dictionaries()

    # -----------------------------
    # 1. Generate semantic samples
    # -----------------------------
    emotional = generate_emotional_expression_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 6,
        source_language="en",
    )

    actions = generate_action_object_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 6,
        source_language="en",
    )

    context_rich = generate_context_rich_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 6,
        source_language="en",
    )

    advanced = generate_advanced_context_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 6,
        source_language="en",
    )

    # -----------------------------
    # 2. Generate protocol samples
    # -----------------------------
    identity = generate_identity_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 12,
        source_language="en",
    )

    intent = generate_intent_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 12,
        source_language="en",
    )

    behavior = generate_behavior_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 12,
        source_language="en",
    )

    memory = generate_memory_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 12,
        source_language="en",
    )

    thought = generate_thought_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 12,
        source_language="en",
    )

    safety = generate_safety_response_samples(
        dictionaries=dictionaries,
        count=DEFAULT_SAMPLE_COUNT // 12,
        source_language="en",
    )

    # Merge all raw samples
    raw_samples = (
        emotional
        + actions
        + context_rich
        + advanced
        + identity
        + intent
        + behavior
        + memory
        + thought
        + safety
    )

    # -----------------------------
    # 3. Convert to Glyphic training samples
    # -----------------------------
    training_samples = []

    for sample in raw_samples:
        user_text = sample.get("input", "")
        glyphic_output = sample.get("glyphic", "")
        realized_output = sample.get("output", "")

        identity_text = sample.get("identity", "A helpful, aligned Glyphic agent.")
        emotion = sample.get("emotion", "neutral")
        sensory = sample.get("sensory", "none")
        social = sample.get("social", "alone")

        intent_dict = sample.get("intent", {
            "goal": "assist",
            "urgency": "1",
            "focus": "support"
        })

        behavior_dict = sample.get("behavior", {
            "tone": "warm",
            "pacing": "steady",
            "depth": "medium",
            "style": "natural",
            "clarity": "high"
        })

        memory_summary = sample.get("memory", "")
        thought_chain = sample.get("thought_chain", "")

        training_sample = build_training_sample(
            user_text=user_text,
            identity=identity_text,
            emotion=emotion,
            sensory=sensory,
            social=social,
            intent=intent_dict,
            behavior=behavior_dict,
            memory_summary=memory_summary,
            thought_chain=thought_chain,
            glyphic_output=glyphic_output,
            realized_output=realized_output
        )

        training_samples.append(training_sample)

    # -----------------------------
    # 4. Save dataset
    # -----------------------------
    save_samples(str(OUTPUT_JSONL), training_samples)

    print(f"Wrote {len(training_samples)} Glyphic training samples to {OUTPUT_JSONL}")


if __name__ == "__main__":
    main()


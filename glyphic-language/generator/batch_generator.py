# generator/batch_generator.py

from pathlib import Path
from .config import DEFAULT_SAMPLE_COUNT
from .dictionary_access import load_all_dictionaries
from .templates_basic import generate_emotional_expression_samples
from .templates_actions import generate_action_object_samples
from .templates_context import generate_context_rich_samples
from .templates_context_advanced import generate_advanced_context_samples
from .training_builder import build_training_sample, save_samples


def generate_single_dataset(path: Path, sample_count: int):
    dictionaries = load_all_dictionaries()

    emotional = generate_emotional_expression_samples(
        dictionaries=dictionaries,
        count=sample_count // 4,
        source_language="en",
    )
    actions = generate_action_object_samples(
        dictionaries=dictionaries,
        count=sample_count // 4,
        source_language="en",
    )
    context_rich = generate_context_rich_samples(
        dictionaries=dictionaries,
        count=sample_count // 4,
        source_language="en",
    )
    advanced = generate_advanced_context_samples(
        dictionaries=dictionaries,
        count=sample_count // 4,
        source_language="en",
    )

    raw_samples = emotional + actions + context_rich + advanced

    training_samples = []
    for sample in raw_samples:
        user_text = sample.get("input", "")
        glyphic_output = sample.get("glyphic", "")
        realized_output = sample.get("output", "")

        identity = "A helpful, aligned Glyphic agent."
        emotion = sample.get("emotion", "neutral")
        sensory = sample.get("sensory", "none")
        social = sample.get("social", "alone")

        intent = {
            "goal": "assist",
            "urgency": "1",
            "focus": "support"
        }

        behavior = {
            "tone": "warm",
            "pacing": "steady",
            "depth": "medium",
            "style": "natural",
            "clarity": "high"
        }

        memory_summary = sample.get("memory", "")
        thought_chain = sample.get("thought_chain", "")

        training_sample = build_training_sample(
            user_text=user_text,
            identity=identity,
            emotion=emotion,
            sensory=sensory,
            social=social,
            intent=intent,
            behavior=behavior,
            memory_summary=memory_summary,
            thought_chain=thought_chain,
            glyphic_output=glyphic_output,
            realized_output=realized_output
        )
        training_samples.append(training_sample)

    save_samples(str(path), training_samples)


def generate_batches(count: int, outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    for i in range(count):
        path = outdir / f"glyphic_dataset_{i+1}.jsonl"
        generate_single_dataset(path, DEFAULT_SAMPLE_COUNT)
        print(f"[batch] wrote {path}")


# generator/templates_basic.py

import random
from typing import List, Dict, Any

from .meaning_model import StructuredMeaning, Emotion, Context
from .encoder import encode_term


def generate_emotional_expression_samples(
    dictionaries: Dict[str, Any],
    count: int,
    source_language: str = "en",
) -> List[Dict[str, Any]]:
    """
    Generate simple 'I feel X about Y' style samples.
    """
    emotions = dictionaries.get("emotions", [])
    times = dictionaries.get("context_time", [])
    results = []

    if not emotions:
        raise ValueError("No 'emotions.json' loaded in dictionaries.")
    if not times:
        times = [{"id": "context.time.unspecified"}]

    for _ in range(count):
        emo = random.choice(emotions)
        time_ctx = random.choice(times)

        emo_type = emo.get("id", "emotion.unknown")
        intensity = round(random.uniform(0.3, 0.9), 2)
        time_id = time_ctx.get("id", "context.time.unspecified")

        input_text = f"I feel {emo_type} about {time_id}."

        meaning = StructuredMeaning(
            actor="actor.self",
            action="action.express_emotion",
            object=None,
            modifiers=[],
            emotion=Emotion(type=emo_type, intensity=intensity),
            context=Context(time=time_id),
            intent="intent.express_emotion",
            meta={
                "source_language": source_language,
                "confidence": 0.95,
            },
        )

        emo_enc = encode_term(emo_type, dictionaries)
        time_enc = encode_term(time_id, dictionaries)

        glyphic_human = (
            f"SELF.EMOTION[{emo_enc['human']}:{intensity}] "
            f"CONTEXT.TIME[{time_enc['human']}] "
            f"INTENT.express"
        )

        glyphic_compact = (
            f"SELF{{EMO:{emo_enc['compact']}@{intensity}}} "
            f"CTX{{TIME:{time_enc['compact']}}} "
            f"INT{{EXP}}"
        )

        glyphic_tokens = (
            f"<SELF> "
            f"<EMO:{emo_enc['compact']}:{intensity}> "
            f"<CTX:TIME:{time_enc['compact']}> "
            f"<INT:EXP>"
        )

        results.append(
            {
                "input_text": input_text,
                "glyphic_output_human": glyphic_human,
                "glyphic_output_compact": glyphic_compact,
                "glyphic_output_tokens": glyphic_tokens,
                "structured_meaning": meaning.to_dict(),
            }
        )

    return results


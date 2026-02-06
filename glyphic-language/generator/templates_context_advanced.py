# generator/templates_context_advanced.py

import random
from typing import List, Dict, Any

from .meaning_model import StructuredMeaning, Emotion, Context
from .encoder import encode_term


def generate_advanced_context_samples(
    dictionaries: Dict[str, Any],
    count: int,
    source_language: str = "en",
) -> List[Dict[str, Any]]:
    """
    Generates advanced multi-context samples:
    - time + place + activity + sensory + social
    - optional emotion overlay
    - multi-clause natural language
    """

    actions = dictionaries.get("actions", [])
    objects = dictionaries.get("objects", [])
    actors = dictionaries.get("actors", [])
    times = dictionaries.get("context_time", [])
    places = dictionaries.get("context_place", [])
    activities = dictionaries.get("context_activity", [])
    sensory = dictionaries.get("context_sensory", [])
    social = dictionaries.get("context_social", [])
    emotions = dictionaries.get("emotions", [])

    results = []

    if not actions or not objects or not actors:
        raise ValueError("Missing required dictionaries: actions, objects, actors.")

    for _ in range(count):
        action = random.choice(actions)
        obj = random.choice(objects)
        actor = random.choice(actors)

        time_ctx = random.choice(times) if times else None
        place_ctx = random.choice(places) if places else None
        activity_ctx = random.choice(activities) if activities else None
        sensory_ctx = random.choice(sensory) if sensory else None
        social_ctx = random.choice(social) if social else None
        emotion_ctx = random.choice(emotions) if emotions else None

        action_id = action.get("id", "action.unknown")
        object_id = obj.get("id", "object.unknown")
        actor_id = actor.get("id", "actor.unknown")

        time_id = time_ctx.get("id") if time_ctx else None
        place_id = place_ctx.get("id") if place_ctx else None
        activity_id = activity_ctx.get("id") if activity_ctx else None
        sensory_id = sensory_ctx.get("id") if sensory_ctx else None
        social_id = social_ctx.get("id") if social_ctx else None
        emotion_id = emotion_ctx.get("id") if emotion_ctx else None

        intensity = round(random.uniform(0.3, 0.9), 2)

        clauses = []

        clause_main = f"{actor_id} {action_id} the {object_id}"
        clauses.append(clause_main)

        if place_id:
            clauses.append(f"in the {place_id}")
        if activity_id:
            clauses.append(f"while {activity_id}")
        if sensory_id:
            clauses.append(f"as the environment felt {sensory_id}")
        if social_id:
            clauses.append(f"around {social_id}")
        if time_id:
            clauses.append(f"({time_id})")
        if emotion_id:
            clauses.append(f"and felt {emotion_id} ({intensity})")

        input_text = " ".join(clauses) + "."

        meaning = StructuredMeaning(
            actor=actor_id,
            action=action_id,
            object=object_id,
            modifiers=[],
            emotion=Emotion(type=emotion_id, intensity=intensity) if emotion_id else None,
            context=Context(
                time=time_id,
                place=place_id,
                activity=activity_id,
                sensory=sensory_id,
                social=social_id,
            ),
            intent="intent.describe_event",
            meta={
                "source_language": source_language,
                "confidence": 0.95,
            },
        )

        actor_enc = encode_term(actor_id, dictionaries)
        action_enc = encode_term(action_id, dictionaries)
        object_enc = encode_term(object_id, dictionaries)
        time_enc = encode_term(time_id, dictionaries) if time_id else None
        place_enc = encode_term(place_id, dictionaries) if place_id else None
        activity_enc = encode_term(activity_id, dictionaries) if activity_id else None
        sensory_enc = encode_term(sensory_id, dictionaries) if sensory_id else None
        social_enc = encode_term(social_id, dictionaries) if social_id else None
        emotion_enc = encode_term(emotion_id, dictionaries) if emotion_id else None

        glyphic_human = (
            f"ACTOR[{actor_enc['human']}] "
            f"ACTION[{action_enc['human']}] "
            f"OBJECT[{object_enc['human']}]"
        )
        if time_enc:
            glyphic_human += f" CONTEXT.TIME[{time_enc['human']}]"
        if place_enc:
            glyphic_human += f" CONTEXT.PLACE[{place_enc['human']}]"
        if activity_enc:
            glyphic_human += f" CONTEXT.ACTIVITY[{activity_enc['human']}]"
        if sensory_enc:
            glyphic_human += f" CONTEXT.SENSORY[{sensory_enc['human']}]"
        if social_enc:
            glyphic_human += f" CONTEXT.SOCIAL[{social_enc['human']}]"
        if emotion_enc:
            glyphic_human += f" EMOTION[{emotion_enc['human']}:{intensity}]"
        glyphic_human += " INTENT.describe"

        glyphic_compact = (
            f"ACT{{{actor_enc['compact']}}} "
            f"ACTN{{{action_enc['compact']}}} "
            f"OBJ{{{object_enc['compact']}}}"
        )
        if time_enc:
            glyphic_compact += f" CTX{{TIME:{time_enc['compact']}}}"
        if place_enc:
            glyphic_compact += f" CTX{{PLACE:{place_enc['compact']}}}"
        if activity_enc:
            glyphic_compact += f" CTX{{ACT:{activity_enc['compact']}}}"
        if sensory_enc:
            glyphic_compact += f" CTX{{SENSE:{sensory_enc['compact']}}}"
        if social_enc:
            glyphic_compact += f" CTX{{SOC:{social_enc['compact']}}}"
        if emotion_enc:
            glyphic_compact += f" EMO{{{emotion_enc['compact']}@{intensity}}}"
        glyphic_compact += " INT{DESC}"

        glyphic_tokens = (
            f"{actor_enc['tokens']} "
            f"{action_enc['tokens']} "
            f"{object_enc['tokens']}"
        )
        if time_enc:
            glyphic_tokens += f" <CTX:TIME:{time_enc['compact']}>"
        if place_enc:
            glyphic_tokens += f" <CTX:PLACE:{place_enc['compact']}>"
        if activity_enc:
            glyphic_tokens += f" <CTX:ACT:{activity_enc['compact']}>"
        if sensory_enc:
            glyphic_tokens += f" <CTX:SENSE:{sensory_enc['compact']}>"
        if social_enc:
            glyphic_tokens += f" <CTX:SOC:{social_enc['compact']}>"
        if emotion_enc:
            glyphic_tokens += f" <EMO:{emotion_enc['compact']}:{intensity}>"
        glyphic_tokens += " <INT:DESC>"

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


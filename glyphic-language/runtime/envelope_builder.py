# runtime/envelope_builder.py

from typing import Dict, Any
from generator.training_builder import build_envelope  # reuse the same logic


def build_runtime_envelope(
    user_text: str,
    identity: str,
    emotion: str,
    sensory: str,
    social: str,
    intent: Dict[str, Any],
    behavior: Dict[str, Any],
    memory_summary: str,
    thought_chain: str,
) -> str:
    """
    Runtime version: builds the same CTX-aware envelope used in training.
    """
    return build_envelope(
        user_text=user_text,
        identity=identity,
        emotion=emotion,
        sensory=sensory,
        social=social,
        intent=intent,
        behavior=behavior,
        memory_summary=memory_summary,
        thought_chain=thought_chain,
    )


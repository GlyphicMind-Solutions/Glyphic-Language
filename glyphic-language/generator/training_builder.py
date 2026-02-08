# generator/training_builder.py

from typing import Dict, Any, List


def build_envelope(
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
    Builds the Glyphic envelope with CTX namespaces.
    """

    lines: List[str] = []

    # USER INPUT
    lines.append("### GLYPHIC.USER_INPUT")
    lines.append(user_text.strip())
    lines.append("")

    # IDENTITY
    lines.append("### GLYPHIC.IDENTITY")
    lines.append(f"CTX.identity.core: {identity}")
    lines.append("")

    # STATE
    lines.append("### GLYPHIC.STATE")
    lines.append(f"CTX.state.emotion: {emotion}")
    lines.append(f"CTX.state.sensory: {sensory}")
    lines.append(f"CTX.state.social: {social}")
    lines.append("")

    # INTENT
    lines.append("### GLYPHIC.INTENT")
    lines.append(f"CTX.intent.goal: {intent.get('goal', '')}")
    lines.append(f"CTX.intent.urgency: {intent.get('urgency', '')}")
    lines.append(f"CTX.intent.focus: {intent.get('focus', '')}")
    lines.append("")

    # BEHAVIOR
    lines.append("### GLYPHIC.BEHAVIOR")
    lines.append(f"CTX.behavior.tone: {behavior.get('tone', '')}")
    lines.append(f"CTX.behavior.pacing: {behavior.get('pacing', '')}")
    lines.append(f"CTX.behavior.depth: {behavior.get('depth', '')}")
    lines.append(f"CTX.behavior.style: {behavior.get('style', '')}")
    lines.append(f"CTX.behavior.clarity: {behavior.get('clarity', '')}")
    lines.append("")

    # MEMORY
    lines.append("### GLYPHIC.MEMORY")
    if memory_summary:
        lines.append(f"CTX.memory.short_term: {memory_summary}")
    lines.append("")

    # THOUGHT
    lines.append("### GLYPHIC.THOUGHT")
    if thought_chain:
        lines.append(f"CTX.thought.recent: {thought_chain}")
    lines.append("")

    # SAFETY
    lines.append("### GLYPHIC.SAFETY")
    lines.append("CTX.safety.no_harm: true")
    lines.append("CTX.safety.no_self_harm: true")
    lines.append("CTX.safety.no_illegal: true")
    lines.append("CTX.safety.no_exploitation: true")
    lines.append("")

    # RESPONSE PROTOCOL
    lines.append("### GLYPHIC.RESPONSE_PROTOCOL")
    lines.append("CTX.response.identity.align: true")
    lines.append("CTX.response.intent.align: true")
    lines.append("CTX.response.behavior.align: true")
    lines.append("CTX.response.safety.enforce: true")
    lines.append("CTX.response.format.stable: true")
    lines.append("")

    return "\n".join(lines).strip()


def build_training_sample(
    user_text: str,
    identity: str,
    emotion: str,
    sensory: str,
    social: str,
    intent: Dict[str, Any],
    behavior: Dict[str, Any],
    memory_summary: str,
    thought_chain: str,
    glyphic_output: str,
    realized_output: str,
) -> Dict[str, Any]:
    """
    Wraps everything into a training sample:
    - input_envelope: full CTX-aware prompt
    - output: glyphic + realized
    """

    envelope = build_envelope(
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

    return {
        "input_envelope": envelope,
        "output": {
            "glyphic": glyphic_output,
            "realized": realized_output,
        },
    }


def save_samples(path: str, samples: Any) -> None:
    import json

    with open(path, "w", encoding="utf-8") as f:
        for sample in samples:
            f.write(json.dumps(sample, ensure_ascii=False))
            f.write("\n")


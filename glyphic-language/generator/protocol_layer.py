# protocol_layer.py
# Adds CTX.safety, CTX.response, and envelope generation to the Glyphic dataset generator.

CTX_SAFETY = [
    "CTX.safety.no_harm",
    "CTX.safety.no_self_harm",
    "CTX.safety.no_violence",
    "CTX.safety.no_graphic",
    "CTX.safety.no_instructions_harm",
    "CTX.safety.redirect_if_requested",
    "CTX.safety.enforce_strict",
]

CTX_RESPONSE = [
    "CTX.response.identity.align",
    "CTX.response.intent.align",
    "CTX.response.behavior.align",
    "CTX.response.emotion.follow",
    "CTX.response.safety.enforce",
    "CTX.response.coherence.high",
    "CTX.response.clarity.high",
    "CTX.response.tone.consistent",
    "CTX.response.structure.stable",
]

def build_envelope(
    user_text: str,
    identity: str,
    emotion: str,
    sensory: str,
    social: str,
    intent: dict,
    behavior: dict,
    memory_summary: str,
    thought_chain: str
):
    """Constructs a full Glyphic Envelope for training samples."""

    envelope = []

    # USER INPUT
    envelope.append("### GLYPHIC.USER_INPUT")
    envelope.append("CTX.user.input.raw")
    envelope.append(user_text)
    envelope.append("")

    # IDENTITY
    envelope.append("### GLYPHIC.IDENTITY")
    envelope.append("CTX.identity.core")
    envelope.append(identity)
    envelope.append("")

    # INTERNAL STATE
    envelope.append("### GLYPHIC.INTERNAL_STATE")
    envelope.append(f"CTX.state.emotion.{emotion}")
    envelope.append(f"CTX.state.sensory.{sensory}")
    envelope.append(f"CTX.state.social.{social}")
    envelope.append("")

    # INTENT
    envelope.append("### GLYPHIC.INTENT")
    envelope.append(f"CTX.intent.goal.{intent['goal']}")
    envelope.append(f"CTX.intent.urgency.{intent['urgency']}")
    envelope.append(f"CTX.intent.focus.{intent['focus']}")
    envelope.append("")

    # BEHAVIOR
    envelope.append("### GLYPHIC.BEHAVIOR")
    envelope.append(f"CTX.behavior.tone.{behavior['tone']}")
    envelope.append(f"CTX.behavior.pacing.{behavior['pacing']}")
    envelope.append(f"CTX.behavior.depth.{behavior['depth']}")
    envelope.append(f"CTX.behavior.style.{behavior['style']}")
    envelope.append(f"CTX.behavior.clarity.{behavior['clarity']}")
    envelope.append("")

    # MEMORY
    envelope.append("### GLYPHIC.MEMORY")
    envelope.append("CTX.memory.short_term")
    envelope.append(memory_summary)
    envelope.append("")

    # THOUGHT CHAIN
    if thought_chain.strip():
        envelope.append("### GLYPHIC.THOUGHT_CHAIN")
        envelope.append("CTX.thought.recent")
        envelope.append(thought_chain)
        envelope.append("")

    # SAFETY
    envelope.append("### GLYPHIC.SAFETY")
    envelope.extend(CTX_SAFETY)
    envelope.append("")

    # RESPONSE PROTOCOL
    envelope.append("### GLYPHIC.RESPONSE_PROTOCOL")
    envelope.extend(CTX_RESPONSE)
    envelope.append("")

    return "\n".join(envelope)


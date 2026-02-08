# templates_behavior.py

def generate_behavior_samples(dictionaries, count=50, source_language="en"):
    samples = []

    behaviors = [
        ("warm", "steady", "medium", "natural", "high"),
        ("neutral", "slow", "shallow", "formal", "medium"),
        ("direct", "fast", "deep", "technical", "high"),
        ("friendly", "steady", "medium", "casual", "high"),
        ("precise", "slow", "deep", "structured", "high")
    ]

    for i in range(count):
        tone, pacing, depth, style, clarity = behaviors[i % len(behaviors)]

        user_text = "Explain this to me."
        glyphic = f"BEHAVIOR(tone={tone}, pacing={pacing}, depth={depth})"
        realized = f"I will explain this in a {tone} and {clarity} way."

        samples.append({
            "input": user_text,
            "glyphic": glyphic,
            "output": realized,
            "behavior": {
                "tone": tone,
                "pacing": pacing,
                "depth": depth,
                "style": style,
                "clarity": clarity
            },
            "emotion": "neutral",
            "sensory": "none",
            "social": "alone"
        })

    return samples


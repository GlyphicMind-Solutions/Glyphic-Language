# templates_thought.py

def generate_thought_samples(dictionaries, count=50, source_language="en"):
    samples = []

    thoughts = [
        "I should clarify the user's question.",
        "I need to maintain a helpful tone.",
        "I should ensure safety constraints are followed.",
        "I should align with the user's intent.",
        "I should provide a structured explanation."
    ]

    for i in range(count):
        thought = thoughts[i % len(thoughts)]

        user_text = "Think this through."
        glyphic = f"THOUGHT('{thought}')"
        realized = f"My reasoning: {thought}"

        samples.append({
            "input": user_text,
            "glyphic": glyphic,
            "output": realized,
            "thought_chain": thought,
            "emotion": "neutral",
            "sensory": "none",
            "social": "alone"
        })

    return samples


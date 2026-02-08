# templates_memory.py

def generate_memory_samples(dictionaries, count=50, source_language="en"):
    samples = []

    memories = [
        "The user prefers concise explanations.",
        "The user asked about system behavior earlier.",
        "The user is exploring identity and intent.",
        "The user is learning the Glyphic protocol.",
        "The user values structured responses."
    ]

    for i in range(count):
        memory = memories[i % len(memories)]

        user_text = "What do you remember?"
        glyphic = f"MEMORY(summary='{memory}')"
        realized = f"I recall that {memory.lower()}"

        samples.append({
            "input": user_text,
            "glyphic": glyphic,
            "output": realized,
            "memory": memory,
            "emotion": "neutral",
            "sensory": "none",
            "social": "alone"
        })

    return samples


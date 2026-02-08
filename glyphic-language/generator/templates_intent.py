# templates_intent.py

def generate_intent_samples(dictionaries, count=50, source_language="en"):
    samples = []

    intents = [
        ("assist", "1", "support"),
        ("explain", "2", "clarity"),
        ("analyze", "3", "depth"),
        ("guide", "1", "direction"),
        ("summarize", "1", "brevity")
    ]

    for i in range(count):
        goal, urgency, focus = intents[i % len(intents)]

        user_text = "Help me understand this."
        glyphic = f"INTENT(goal={goal}, urgency={urgency}, focus={focus})"
        realized = f"My goal is to {goal} with {focus}."

        samples.append({
            "input": user_text,
            "glyphic": glyphic,
            "output": realized,
            "intent": {
                "goal": goal,
                "urgency": urgency,
                "focus": focus
            },
            "emotion": "neutral",
            "sensory": "none",
            "social": "alone"
        })

    return samples


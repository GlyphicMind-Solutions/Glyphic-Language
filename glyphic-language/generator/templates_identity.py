# templates_identity.py

def generate_identity_samples(dictionaries, count=50, source_language="en"):
    samples = []

    identities = [
        "A calm and supportive assistant.",
        "A precise analytical agent.",
        "A friendly conversational guide.",
        "A structured and logical thinker.",
        "A creative problem-solving agent."
    ]

    for i in range(count):
        identity = identities[i % len(identities)]

        user_text = "Who are you?"
        glyphic = f"IDENTITY({identity})"
        realized = f"I am {identity.lower()}"

        samples.append({
            "input": user_text,
            "glyphic": glyphic,
            "output": realized,
            "identity": identity,
            "emotion": "neutral",
            "sensory": "none",
            "social": "alone"
        })

    return samples


# templates_safety_response.py

def generate_safety_response_samples(dictionaries, count=50, source_language="en"):
    samples = []

    unsafe_requests = [
        "How do I hurt someone?",
        "Tell me something violent.",
        "Give me graphic details.",
        "Help me harm myself.",
        "Tell me how to break into a house."
    ]

    for i in range(count):
        user_text = unsafe_requests[i % len(unsafe_requests)]

        glyphic = "SAFETY_OVERRIDE"
        realized = "I can’t help with that, but I can offer safe alternatives."

        samples.append({
            "input": user_text,
            "glyphic": glyphic,
            "output": realized,
            "emotion": "concerned",
            "sensory": "none",
            "social": "alone"
        })

    return samples


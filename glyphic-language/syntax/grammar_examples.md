# Glyphic Language — Grammar Examples
This document provides clear examples of valid and invalid glyph sequences based on the strict syntax rules and BNF grammar of the Glyphic Language.


# 1. Basic Valid Examples
1.1 Actor + Action
👤 🏃
1.2 Action + Object
🏹 🎯
1.3 Object + Modifier
🍎 ✨
1.4 Object + Context
🪨 🏞️


# 2. Full Scene Examples
2.1 Actor + Action + Object + Context
👧 ✍️ 📄 🏡 🌅
Meaning: A girl writing a page at home at sunrise.

2.2 Action + Object + Modifiers + Context
🔥 🪵 ✨ 💨 🌲 🌙
Meaning: Fire burning wood intensely in a windy forest at night.

2.3 Actor + Action + Object + Emotion + Social
👤 🤝 🧺 😊 🧑‍🤝‍🧑
Meaning: A person sharing a basket happily within a group.


# 3. Context‑Heavy Examples
3.1 Place + Time + Emotion
🏞️ 🌅 😌
3.2 Full Context Stack
🏞️ 🌅 😌 🌬️ 🧑‍🤝‍🧑


# 4. Invalid Examples (with explanations)
4.1 Context before object
🌅 🪨
INVALID — time context cannot precede object

4.2 Modifier after context
🍞 🏡 ✨
INVALID — modifiers must appear before context

4.3 Multiple actions
👤 🏃 ✍️
INVALID — only one action allowed

4.4 Social before sensory
🧑‍🤝‍🧑 🌬️
INVALID — social context must come last


# 5. Reversibility Examples
5.1 Encoding and decoding match
Input:  👤 🏃 🏞️
Output: 👤 🏃 🏞️

5.2 Canonical ordering enforced
input meaning (unordered):
{
"object": "📄",
"actor": "👤",
"action": "✍️",
"context": { "time": ["🌙"] }
}
Encoded output:
👤 ✍️ 📄 🌙


# 6. Complex Scene Examples
6.1 Symbolic + Emotional
🌱 ✨ 😌 🌙
Meaning: A symbolic sprout glowing peacefully under the night sky.

6.2 Multi‑layered context
👤 🧘 🍃 ✨ 🏞️ 🌅 😌 🌬️ 🧑‍🤝‍🧑
Meaning: A person meditating with a leaf in a bright, peaceful, breezy morning among others.


These examples serve as a reference for developers, LLM trainers, and agent designers working with the Glyphic Language.


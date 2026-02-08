# generator/meaning_model.py

from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any


@dataclass
class Emotion:
    type: str
    intensity: float


@dataclass
class Context:
    time: Optional[str] = None
    place: Optional[str] = None
    social: Optional[str] = None
    sensory: Optional[str] = None
    activity: Optional[str] = None


@dataclass
class StructuredMeaning:
    actor: Optional[str]
    action: Optional[str]
    object: Optional[str]
    modifiers: List[str]
    emotion: Optional[Emotion]
    context: Context
    intent: str
    meta: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        # Flatten Emotion and Context dataclasses into dicts
        return d


# generator/config.py

from pathlib import Path

# Base paths (adjust if your layout differs)
BASE_DIR = Path(__file__).resolve().parent.parent

DICTIONARY_DIR = BASE_DIR / "dictionary"
INTERPRETER_DIR = BASE_DIR / "interpreter"
TRAINING_DIR = BASE_DIR / "training"

# Output file for generated samples
OUTPUT_JSONL = TRAINING_DIR / "goldenmodelsamples.generated.jsonl"

# How many samples to generate in one run (you can change this anytime)
DEFAULT_SAMPLE_COUNT = 500


# generator/cli.py

import argparse
from pathlib import Path

from .run_generator import main as generate_main
from .validator import validate_jsonl
from .batch_generator import generate_batches


def cli():
    parser = argparse.ArgumentParser(prog="glyphicgen", description="Glyphic dataset generator and tools")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate
    gen_parser = subparsers.add_parser("generate", help="Generate a Glyphic training dataset")
    gen_parser.add_argument("--output", type=Path, help="Output JSONL path (overrides config)")

    # validate
    val_parser = subparsers.add_parser("validate", help="Validate a Glyphic JSONL dataset")
    val_parser.add_argument("path", type=Path, help="Path to JSONL dataset")

    # batch
    batch_parser = subparsers.add_parser("batch", help="Generate multiple datasets with varying configs")
    batch_parser.add_argument("--count", type=int, default=5, help="Number of datasets to generate")
    batch_parser.add_argument("--outdir", type=Path, default=Path("training/batches"), help="Output directory")

    args = parser.parse_args()

    if args.command == "generate":
        # reuse existing generator; optional override
        if args.output:
            from .config import OUTPUT_JSONL
            # monkey-patch for now
            globals()["OUTPUT_JSONL"] = args.output
        generate_main()

    elif args.command == "validate":
        validate_jsonl(args.path)

    elif args.command == "batch":
        generate_batches(args.count, args.outdir)


if __name__ == "__main__":
    cli()


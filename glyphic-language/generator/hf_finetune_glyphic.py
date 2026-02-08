# training/hf_finetune_glyphic.py

import json
from pathlib import Path
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer


def load_glyphic_dataset(path: str):
    # JSONL with {"input_envelope": str, "output": {"glyphic": str, "realized": str}}
    def gen():
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                yield {
                    "input_envelope": obj["input_envelope"],
                    "glyphic": obj["output"]["glyphic"],
                    "realized": obj["output"]["realized"],
                }

    return load_dataset("json", data_files={"train": path}, split="train", streaming=False)


def main():
    dataset_path = "training/glyphic_dataset.jsonl"
    model_name = "gpt2"  # placeholder; swap with your base model

    ds = load_glyphic_dataset(dataset_path)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    def preprocess(example):
        # Envelope as prompt, realized as target
        prompt = example["input_envelope"] + "\n\n"
        target = example["realized"]
    
        text = prompt + target
        tokens = tokenizer(
            text,
            truncation=True,
            max_length=1024,
        )
        tokens["labels"] = tokens["input_ids"].copy()
        return tokens


    tokenized = ds.map(preprocess, batched=False)

    model = AutoModelForCausalLM.from_pretrained(model_name)

    args = TrainingArguments(
        output_dir="training/glyphic_model",
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,
        num_train_epochs=1,
        learning_rate=5e-5,
        logging_steps=50,
        save_steps=500,
        save_total_limit=2,
        fp16=True,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=tokenized,
        tokenizer=tokenizer,
    )

    trainer.train()
    trainer.save_model("training/glyphic_model_final")


if __name__ == "__main__":
    main()


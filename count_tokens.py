from pathlib import Path
import argparse
from transformers import AutoTokenizer


MODEL_IDS = {
    "gemma3": "google/gemma-3-4b-it",
    "qwen3": "Qwen/Qwen3-4B",
}

def count_tokens(text: str, model_key: str) -> int:
    if model_key not in MODEL_IDS:
        raise ValueError(f"unknown model_key: {model_key}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_IDS[model_key], trust_remote_code=True)
    encoded = tokenizer(text, return_tensors=None)
    return len(encoded["input_ids"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='count_tokens',
        description='count tokens for lms'
    )
    parser.add_argument('model', choices=list(MODEL_IDS.keys()), help='model key')
    parser.add_argument('-f', '--file', action='store', type=str, required=True, help='text file path')

    args = parser.parse_args()

    text_file_path = Path(args.file)
    with open(text_file_path.resolve(), 'rt') as f:
        text = f.read()

    if not text:
        raise Exception("file is empty")

    n_tokens = count_tokens(text, args.model)
    print(f"Tokens ({args.model} 기준): {n_tokens}")


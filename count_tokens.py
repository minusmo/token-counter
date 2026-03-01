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
    import sys
    parser = argparse.ArgumentParser(
            prog='count_tokens',
            description='count tokens for lms'
    )

    parser.add_argument('-f', '--file', action='store', type=str, required=True, help='text file path')

    if len(sys.argv) < 2:
        print("usage: python count_tokens.py [gemma3|qwen3] ")
        sys.exit(1)

    model_key = sys.argv[1]
    # if sys.stdin.isatty():
    #     text = " ".join(sys.argv[2:]) or "안녕하세요, 토큰 길이 측정 테스트입니다."
    # else:
    #     text = sys.stdin.read()


    args = parser.parse_args()
    if not args['file']:
        raise Exception()

    text_file_path = Path(args['file'])
    with open(text_file_path.resolve(), 'rt') as f:
        text = f.read()

    if not text:
        raise Exception()

    n_tokens = count_tokens(text, model_key)
    print(f"Tokens ({model_key} 기준): {n_tokens}")


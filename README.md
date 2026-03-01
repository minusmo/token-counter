# token-counter

A CLI utility to count how many tokens a text file consumes for a given LLM.

## Supported Models

| Key | Model |
|-----|-------|
| `gemma3` | google/gemma-3-4b-it |
| `qwen3` | Qwen/Qwen3-4B |

## Requirements

- Python 3.12+
- [UV](https://docs.astral.sh/uv/)

## Installation

```bash
uv sync
```

## Usage

```bash
python count_tokens.py <model> -f <file>
```

**Examples:**

```bash
# Count tokens using the gemma3 tokenizer
python count_tokens.py gemma3 -f input.txt

# Count tokens using the qwen3 tokenizer
python count_tokens.py qwen3 -f prompt.txt
```

## Output

The result is printed in Korean with the model name and token count:

```
Tokens (gemma3 기준): 1234
```

`기준` means "based on" — i.e., the token count as measured by the specified model's tokenizer.

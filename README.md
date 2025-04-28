# Readme Generator

Generate a professional `README.md` automatically by analyzing project files using AI.

## Features

- Support for English and Korean README generation.
- Selectable AI providers: OpenAI, Claude, Gemini.
- Configurable maximum characters to read per file.
- Automatically ignores unnecessary folders (e.g., `.git/`, `node_modules/`, `venv/`, `__pycache__`).
- Easy `.env`-based API key management.

## Installation

```bash
pip install readmegen
```


## Usage

```bash
readme --lang en --provider openai
readme --lang ko --provider claude
readme --lang en --provider gemini
readme --lang en --provider openai --max_chars 5000
```

## License

MIT License

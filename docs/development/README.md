# Development

## Setup

```bash
pip install -e ".[dev]"
```

Requires Python >= 3.10.

## Checks

```bash
pytest
ruff check .
mypy src
```

## Layout

- Package code lives under `src/ai_context/`
- Tests live under `tests/`
- AI engineering process docs live under `ai-engineering/`

Do not implement repository analysis or context generation until a later task
explicitly requires it.

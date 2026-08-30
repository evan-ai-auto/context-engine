# AI Context Engine

AI Context Engine converts a local software repository into structured,
AI-readable project context for coding agents and multi-agent workflows.

**Project Status: MVP / Early Development**

v0.1 scaffolding is in place. Repository analysis and `.ai-context` generation
are not implemented yet.

## Installation

Requires Python >= 3.10.

```bash
pip install -e ".[dev]"
```

## CLI usage

```bash
ai-context --help
ai-context --version
ai-context init
```

`init` currently prints a placeholder message only.

## Development

```bash
pytest
ruff check .
mypy src
```

## Documentation

- [Specification v0.1](docs/specification/v0.1.md)
- [Architecture](docs/architecture/architecture.md)
- [Development notes](docs/development/README.md)

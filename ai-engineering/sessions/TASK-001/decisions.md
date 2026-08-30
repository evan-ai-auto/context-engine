# TASK-001 Decisions

## 1. Python package with src-layout

Decision:
Use `src/ai_context/` as the installable package root.

Reason:
TASK-001 requires src-layout. It keeps tests and docs outside the installed package and matches common production Python packaging practice.

Trade-off:
Slightly more packaging configuration than a flat layout; clearer separation for later modules.

## 2. Hatchling as build backend

Decision:
Configure hatchling in `pyproject.toml` as the build backend.

Reason:
TASK-001 recommends hatchling; it supports editable installs without a legacy `setup.py`.

Trade-off:
Requires a modern pip that understands PEP 517/660 editable builds.

## 3. Typer for the CLI

Decision:
Expose `ai-context` via a Typer app in `src/ai_context/cli/main.py`.

Reason:
TASK-001 specifies Typer and the commands `--help`, `--version`, and `init`.

Trade-off:
Adds a runtime dependency; avoids hand-rolled argparse for a growing CLI surface.

## 4. pytest, Ruff, and mypy as the quality baseline

Decision:
Declare pytest, ruff, and mypy as optional `[dev]` dependencies and configure them in `pyproject.toml`.

Reason:
TASK-001 acceptance criteria require `pytest`, `ruff check .`, and `mypy src` to pass.

Trade-off:
Developers must install `[dev]` extras; no additional CI wiring was added in this task.

## 5. Avoid premature architecture packages

Decision:
Create only `cli/` under `src/ai_context/` for TASK-001; do not scaffold application/domain/infrastructure/generator packages.

Reason:
Architecture docs state packages should be created when needed; TASK-001 forbids analysis and generation logic.

Trade-off:
Target architecture tree is not mirrored on disk yet; later tasks must introduce packages deliberately.

---

## Future Decision Record Template

### Decision: <title>

#### Context

Why is this decision required?

#### Decision

What was chosen?

#### Reason

Why was this chosen?

#### Trade-off

What are the costs or limitations?

#### Consequences

What future impact may result from this decision?

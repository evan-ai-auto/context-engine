# Learning — Spec Revisions vs Runtime Compatibility Policy

## Context

Raising the repository minimum Python version from 3.8 to 3.10 (policy/docs + `pyproject.toml`) also triggered a small production CLI typing modernization (`Optional[bool]` → `bool | None`) via Ruff UP under `target-version = "py310"`.

That code change was correct for the new baseline, but it was not declared up front as in-scope work of a documentation/specification revision.

## Principle

When a documentation or specification revision changes a **repository-wide runtime compatibility policy** (for example `requires-python`, Ruff `target-version`, mypy `python_version`):

1. Any necessary **existing production-code** compatibility or modernization changes must be **explicitly declared in scope** for that revision (or a paired hygiene revision).
2. Otherwise the revision should remain **documentation/configuration-only**, and implementation modernization must not be performed implicitly.

## Why it matters

- Keeps review boundaries clear (docs freeze vs code change).
- Prevents “silent” production diffs during architecture/spec work.
- Makes acceptance and rollback decisions explicit.

## Reuse

Apply to future TASK revisions that touch packaging/tooling baselines before domain implementation begins.

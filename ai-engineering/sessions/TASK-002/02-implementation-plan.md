# 02 — TASK-002 Implementation Plan

## Goal

Deliver the **frozen** Project Context domain contract under `src/ai_context/domain/` with tests.

Architecture is frozen. Do not make new architecture decisions during implementation.

Canonical sources:

- [`architecture-decisions.md`](./architecture-decisions.md)
- [`03-domain-model-contract.md`](./03-domain-model-contract.md)

---

## Prerequisites

- [x] Stage A architecture reconciliation complete
- [x] Specification frozen
- [x] Revision-001 domain contract finalization complete (Python 3.10+, enum members, `generated_at: datetime`)
- [ ] Pre-implementation / Repository Compatibility Inspection gate passed
- [ ] Pydantic not yet added to `pyproject.toml`

---

## Work sequence

### Step 0 — Dependency gate

1. Confirm repository Python policy is `>=3.10` in `pyproject.toml` (already frozen)
2. Choose a Pydantic v2 constraint compatible with Python 3.10+
3. Add Pydantic to runtime dependencies and reinstall: `pip install -e ".[dev]"`

If any conflict with the frozen contract appears, **stop and report** — do not redesign.

### Step 1 — Enums and Evidence

1. Implement frozen enums with **exact** members from the contract (no extras)
2. Implement `Evidence` (`source_file`, `source_type`, `detail`)
3. Tests: valid evidence; invalid enum rejection; multiple evidence lists

### Step 2 — Leaf entities

1. `ProjectInfo` — required `name`; optional `description`, `primary_language`
2. `RepositoryInfo` — portable `root_path`; optional `branch` / `commit`
3. `Module` — `ModuleType`, optional language/build_tool, `depends_on: list[str]`
4. `Technology` — optional category/version; `evidence: list[Evidence]`
5. `Dependency` — required `ecosystem: str`; optional scope/declared_by/version; `evidence: list[Evidence]`
6. `GenerationMetadata` — required `analysis_status`; `generated_at: datetime` (tz-aware UTC preferred)

### Step 3 — Aggregate

1. `ProjectContext` with `project_dependencies` (not `dependencies`)
2. Construction, required/optional, partial `analysis_status`
3. Serialization round-trip

### Step 4 — Exports and isolation

1. Public exports from `domain/__init__.py`
2. Confirm no scanner/filesystem/CLI imports

### Step 5 — Quality gates

```bash
pytest
ruff check .
mypy src
```

Record results in [`05-validation-checklist.md`](./05-validation-checklist.md).

---

## Suggested file order

| Order | File | Notes |
|------:|------|--------|
| 1 | enums (inline or small module) | four canonical enums only |
| 2 | `evidence.py` | |
| 3 | `project.py` | |
| 4 | `repository.py` | |
| 5 | `module.py` | `depends_on` |
| 6 | `technology.py` | `list[Evidence]` |
| 7 | `dependency.py` | `ecosystem`, `list[Evidence]` |
| 8 | `metadata.py` | `analysis_status` |
| 9 | `project_context.py` | `project_dependencies` |
| 10 | `__init__.py` | |

---

## Non-goals

- No `application/` / `infrastructure/` / `generator/` packages
- No analyzers, no `.ai-context` writes, no new CLI
- No `DependencyGraph`, no `Module.dependencies`, no `DependencyEcosystem` enum

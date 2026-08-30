# 02 — TASK-002 Implementation Plan

## Goal

Deliver the locked Project Context domain contract under `src/ai_context/domain/` with tests, without implementing analyzers or generators.

---

## Prerequisites

- [x] Architecture decisions locked
- [x] TASK-002 status: `READY_FOR_IMPLEMENTATION`
- [ ] Pydantic v2 dependency not yet added to `pyproject.toml`

---

## Work sequence

### Step 1 — Dependency

1. Add Pydantic v2 runtime dependency compatible with Python `>=3.8.0`
2. Pin a 3.8-compatible Pydantic 2.x line in `pyproject.toml`
3. Reinstall editable env: `pip install -e ".[dev]"`

### Step 2 — Enums and Evidence first

1. Define taxonomy enums (`str, Enum`) for:
   - project type
   - module type
   - technology category
   - dependency scope
   - evidence type
2. Implement shared `Evidence` model (`file`, `type`)
3. Unit tests: valid evidence + invalid enum rejection

### Step 3 — Leaf entities

Implement and test independently:

1. `ProjectInfo`
2. `RepositoryInfo` (portable `root_path`; optional `branch` / `commit`)
3. `Module` including `depends_on: List[str]`
4. `Technology` with `Optional[Evidence]`
5. `Dependency` with `Optional[Evidence]` and optional `declared_by`
6. `GenerationMetadata`

### Step 4 — Aggregate root

1. Implement `ProjectContext` composing all entities
2. Tests: construction with valid nested data
3. Serialization round-trip: `model_dump` → JSON → `model_validate`
4. Required-field and optional-field cases

### Step 5 — Package exports

1. Export public models from `domain/__init__.py`
2. Ensure domain package imports no scanner / filesystem / CLI modules

### Step 6 — Quality gates

```bash
pytest
ruff check .
mypy src
```

Confirm existing CLI tests still pass (AC-012).

---

## Suggested file order

| Order | File | Notes |
|------:|------|--------|
| 1 | `evidence.py` | Shared evidence + evidence type enum (or shared enums module if preferred) |
| 2 | `project.py` | `ProjectInfo` |
| 3 | `repository.py` | `RepositoryInfo` |
| 4 | `module.py` | includes `depends_on` |
| 5 | `technology.py` | optional evidence |
| 6 | `dependency.py` | optional evidence + `declared_by` |
| 7 | `metadata.py` | `GenerationMetadata` |
| 8 | `project_context.py` | aggregate |
| 9 | `__init__.py` | public exports |

Enums may live next to models or in a small `enums.py` if that reduces duplication — prefer minimal structure; do not over-split.

---

## Non-goals during implementation

- Do not create `application/`, `infrastructure/`, or `generator/` packages
- Do not parse real repositories
- Do not write `.ai-context` files
- Do not add CLI flags for domain inspection unless TASK-002 is later amended

---

## Done when

- All AC-001–AC-012 can be argued from code + tests
- Validation checklist in `05-validation-checklist.md` is completed with real command results
- Session notes updated after implementation

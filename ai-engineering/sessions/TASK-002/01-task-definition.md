# 01 — TASK-002 Task Definition

## Status

READY_FOR_IMPLEMENTATION

## Source of truth

Primary task document:

[`ai-engineering/tasks/TASK-002.md`](../../tasks/TASK-002.md)

Architecture decision review:

[`ai-engineering/reviews/TASK-002-architecture-decision-review.md`](../../reviews/TASK-002-architecture-decision-review.md)

Session decisions:

[`architecture-decisions.md`](./architecture-decisions.md)

---

## Objective

Establish the core **Project Context** domain model for AI Context Engine.

The domain model is the language-agnostic, serializable, validated data contract that future analyzers and generators will populate and consume.

```text
Repository Analyzer
        │
        ▼
ProjectContext  ← TASK-002 delivers this contract
        │
        ▼
Context Generator
```

---

## In scope

- Core project context model and related entities
- Validation rules
- Serialization / deserialization
- Unit tests for valid and invalid scenarios
- Package layout under `src/ai_context/domain/`

## Out of scope

- Repository scanning / filesystem traversal
- Java / Python / Maven / Gradle / pyproject detection or parsing
- Technology or dependency analysis logic
- `.ai-context` generation
- New CLI commands
- Incremental updates / semantic analysis
- Speculative entities beyond the locked contract

---

## Locked architecture decisions (summary)

1. Introduce **Pydantic v2** for domain models
2. Closed `str` Enums for taxonomies; open strings for names/versions/paths
3. Shared **Evidence** with `Optional[Evidence]` on Technology and Dependency
4. Minimal Module/Dependency relationship fix:
   - `Module.depends_on: List[str]`
   - `Dependency.declared_by` optional
   - Defer `DependencyGraph`

Details: [`architecture-decisions.md`](./architecture-decisions.md)

---

## Expected package outcome

```text
src/ai_context/domain/
├── __init__.py
├── project_context.py
├── project.py
├── repository.py
├── module.py
├── technology.py
├── dependency.py
├── metadata.py
└── evidence.py
```

Implementation of `src/ai_context/domain/` has **not** started at the time this session folder was created.

---

## Acceptance criteria (reference)

AC-001 … AC-012 as defined in `TASK-002.md` §11.

Validation commands (must be actually executed before claiming pass):

```bash
pytest
ruff check .
mypy src
```

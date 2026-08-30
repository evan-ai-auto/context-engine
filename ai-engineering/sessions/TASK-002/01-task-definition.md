# 01 — TASK-002 Task Definition

## Status

SPECIFICATION_FROZEN — awaiting pre-implementation inspection gate

Stage A (Comprehensive Domain Architecture Reconciliation) is complete.

Implementation of `src/ai_context/domain/` has **not** started.

---

## Source of truth

| Kind | Path |
|------|------|
| Task | [`ai-engineering/tasks/TASK-002.md`](../../tasks/TASK-002.md) |
| Canonical ADRs | [`architecture-decisions.md`](./architecture-decisions.md) |
| Canonical domain contract | [`03-domain-model-contract.md`](./03-domain-model-contract.md) |
| Stage A brief | [`TASK-002 Stage A — Comprehensive Domain Architecture Reconciliation.md`](../../tasks/TASK-002%20Stage%20A%20—%20Comprehensive%20Domain%20Architecture%20Reconciliation.md) |

`decisions.md` is deleted and must not be referenced as a source.

---

## Objective

Establish the core **Project Context** domain model for AI Context Engine: a language-agnostic, serializable, validated data contract for future analyzers and generators.

---

## In scope

- Core project context model and related entities (frozen contract)
- Validation, serialization, deserialization
- Unit tests
- Package layout under `src/ai_context/domain/`

## Out of scope

- Repository scanning / analyzers / `.ai-context` generation
- New CLI commands
- `DependencyGraph`
- Speculative entities beyond the frozen contract

---

## Frozen architecture (summary)

1. **ADR-001** Pydantic v2 (add dependency only at implementation; verify Python compatibility first)
2. **ADR-002** Enums: `ModuleType`, `DependencyScope`, `EvidenceType`, `AnalysisStatus` only; ecosystem is `str`
3. **ADR-003** `list[Evidence]` on Technology and Dependency; fields `source_file`, `source_type`, `detail`
4. **ADR-004** `Module.depends_on` vs `ProjectContext.project_dependencies`; `Dependency.ecosystem`; optional `declared_by`; no graph
5. **ADR-005** `GenerationMetadata.analysis_status: AnalysisStatus` for partial context

Details: [`architecture-decisions.md`](./architecture-decisions.md)  
Contract: [`03-domain-model-contract.md`](./03-domain-model-contract.md)

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

---

## Next gate

Pre-implementation inspection, then implementation using [`06-cursor-prompt.md`](./06-cursor-prompt.md).

Do not mark TASK-002 DONE until the full engineering lifecycle completes after implementation.

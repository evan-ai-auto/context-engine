# TASK-002 Architecture Decision Review

## Summary / Status

| Field | Value |
|---|---|
| Related Task | TASK-002 — Core Project Context Domain Model |
| Review Type | Architecture Decision Review + Stage A reconciliation |
| Status | **FROZEN** (specification) |
| Implementation | Not started |
| Canonical ADR doc | `ai-engineering/sessions/TASK-002/architecture-decisions.md` |
| Canonical contract | `ai-engineering/sessions/TASK-002/03-domain-model-contract.md` |

Stage A superseded earlier draft decisions that used:

- single `Optional[Evidence]`
- `ProjectContext.dependencies`
- broader taxonomy enums (e.g. ProjectInfo.type, Technology.category as enums)
- Evidence fields `file` / `type`

Those drafts must not be treated as implementation requirements.

No product source code, tests, or `pyproject.toml` dependencies were changed in Stage A.

---

## Frozen decisions (aligned to Stage A)

### ADR-001 — Pydantic v2

Keep Pydantic v2 as the domain foundation. Do not add it in Stage A. Implementation must verify Python compatibility before selecting the Pydantic pin and may recommend raising minimum Python if required.

### ADR-002 — Enum strategy

Canonical enums only:

- `ModuleType`
- `DependencyScope`
- `EvidenceType`
- `AnalysisStatus`

No `DependencyEcosystem` enum. Ecosystem remains `str`.

### ADR-003 — Evidence strategy

Reusable `Evidence` with `source_file`, `source_type` (`EvidenceType`), optional `detail`.

`Technology.evidence` and `Dependency.evidence` are `list[Evidence]`.

### ADR-004 — Module / dependency relationships

- Internal: `Module.depends_on`
- External: `ProjectContext.project_dependencies`
- Optional: `Dependency.declared_by`
- Required: `Dependency.ecosystem: str`
- No `DependencyGraph`, no `Module.dependencies`

### ADR-005 — Partial context

`GenerationMetadata.analysis_status: AnalysisStatus` with values `pending | partial | completed | failed`.

No per-module/per-analyzer status models in TASK-002.

---

## Historical notes (superseded)

Earlier review text discussed `Optional[Evidence]`, `ProjectContext.dependencies`, and closed enums for project type / technology category. Those choices are **withdrawn** in favor of the Stage A freeze above.

For implementation, follow only:

1. `architecture-decisions.md`
2. `03-domain-model-contract.md`

---

## Implementation gate

Before coding:

1. Pass pre-implementation inspection
2. Use [`06-cursor-prompt.md`](../sessions/TASK-002/06-cursor-prompt.md)
3. On contract conflict: stop and report — do not redesign silently

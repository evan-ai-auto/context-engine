# TASK-002 Architecture Decisions

**Canonical architecture decision document for TASK-002.**

Do not maintain a parallel `decisions.md`.

Status: **FROZEN** after Stage A — Comprehensive Domain Architecture Reconciliation.

Implementation must not invent new architecture decisions. If a conflict with this document is discovered during implementation, stop and report it.

Related review (historical + Stage A alignment):

[`ai-engineering/reviews/TASK-002-architecture-decision-review.md`](../../reviews/TASK-002-architecture-decision-review.md)

Canonical domain contract:

[`03-domain-model-contract.md`](./03-domain-model-contract.md)

---

## ADR-001 — Pydantic v2

### Context

TASK-002 requires validated, serializable domain models without using `dict[str, Any]` as the primary representation.

### Decision

Use **Pydantic v2** as the domain modeling foundation.

Do **not** add Pydantic to `pyproject.toml` during Stage A.

### Implementation note

Before modifying `pyproject.toml`, implementation must verify the repository Python compatibility policy and select a Pydantic 2.x constraint compatible with that policy.

Because this is a new project, implementation planning may recommend raising the minimum supported Python version if required by the selected modern dependency and typing strategy.

Stage A did not freeze a new minimum Python version at the time of writing.
The repository policy is now **Python >= 3.10** (`requires-python` in `pyproject.toml`).
Implementation must select a Pydantic 2.x constraint compatible with that policy.

### Consequences

Domain entities under `src/ai_context/domain/` will be Pydantic models using `model_dump` / `model_validate`.

---

## ADR-002 — Enum strategy

### Context

Stable taxonomies need hard validation; fast-evolving labels must remain extensible.

### Decision

Use explicit string-based enums (`str, Enum`) for the following **canonical** set only:

| Enum | Purpose |
|------|---------|
| `ModuleType` | Module taxonomy |
| `DependencyScope` | External dependency scope |
| `EvidenceType` | Evidence source classification |
| `AnalysisStatus` | Whole-context analysis completeness |

Do **not** introduce a `DependencyEcosystem` enum.

`Dependency.ecosystem` remains a **plain `str`** (e.g. Maven, PyPI, npm, Cargo, Go Modules) so new ecosystems do not require Core Domain Model changes.

Open strings remain for names, versions, paths, languages, build tools, technology category, and similar labels.

### Consequences

Invalid enum members must be rejected by validation tests. Ecosystem strings are free-form and normalized later by analyzers if needed.

---

## ADR-003 — Evidence strategy

### Context

Technology and Dependency detections may be supported by multiple independent sources.

### Decision

`Evidence` is a reusable domain model with fields:

| Field | Required | Type |
|-------|----------|------|
| `source_file` | yes | `str` |
| `source_type` | yes | `EvidenceType` |
| `detail` | no | `str` |

Attachments:

- `Technology.evidence` → `list[Evidence]` (default empty)
- `Dependency.evidence` → `list[Evidence]` (default empty)

Do **not** use a single `Optional[Evidence]` attachment.

Do not attach Evidence to Module or ProjectInfo in TASK-002.

Evidence performs no I/O.

### Consequences

Analyzers may attach zero or more evidence records per technology/dependency.

---

## ADR-004 — Module and dependency relationships

### Context

Internal module edges and external package/library dependencies must not be conflated.

### Decision

| Concept | Location | Meaning |
|---------|----------|---------|
| Internal module→module | `Module.depends_on: list[str]` | Other module names |
| External package/library | `ProjectContext.project_dependencies: list[Dependency]` | Sole owner of external deps |
| Declaration origin | `Dependency.declared_by: Optional[str]` | Module that declared the package dep |

Additional:

- `Dependency.ecosystem: str` (required) — package ecosystem identity
- Do **not** create `DependencyGraph` in TASK-002
- Do **not** add `Module.dependencies`
- Do **not** keep `ProjectContext.dependencies` (renamed to `project_dependencies`)

### Consequences

Graph export for `.ai-context` remains a later generator concern derived from these fields.

---

## ADR-005 — Partial context strategy

### Context

Analyzers may produce incomplete context before a full successful run.

### Decision

Add whole-context status only:

`GenerationMetadata.analysis_status: AnalysisStatus`

Canonical values:

- `pending`
- `partial`
- `completed`
- `failed`

Do **not** introduce per-module or per-analyzer status models in TASK-002.

### Consequences

`ProjectContext` can represent partially analyzed repositories without extra status graphs.

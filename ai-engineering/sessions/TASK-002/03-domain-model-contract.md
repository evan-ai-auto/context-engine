# 03 — Domain Model Contract

**Canonical domain contract for TASK-002.** Frozen after Stage A; enum members and `generated_at` finalized in Revision-001.

Implementation must match this document and [`architecture-decisions.md`](./architecture-decisions.md).

Do not invent fields, rename ownership, change required/optional semantics, or add enum members during implementation without a new architecture decision.

Implementation targets **Python >= 3.10**.

---

## Aggregate

```text
ProjectContext
├── project: ProjectInfo
├── repository: RepositoryInfo
├── modules: list[Module]
├── technologies: list[Technology]
├── project_dependencies: list[Dependency]   # sole owner of external package/library deps
└── metadata: GenerationMetadata
```

There is no `ProjectContext.dependencies` field.

---

## Canonical enums

Stable `str, Enum` types. **Members are frozen** (Revision-001). Implementation must not invent additional members.

| Enum | Frozen members |
|------|----------------|
| `ModuleType` | `application`, `library`, `service`, `tool`, `unknown` |
| `DependencyScope` | `compile`, `runtime`, `test`, `development`, `optional`, `unknown` |
| `EvidenceType` | `build_file`, `lock_file`, `manifest`, `source`, `config`, `other` |
| `AnalysisStatus` | `pending`, `partial`, `completed`, `failed` |

`DependencyScope` is a normalized cross-ecosystem vocabulary. Ecosystem-specific scopes are normalized by analyzers later — do not add Maven/Gradle/npm/Python-specific enum values.

Not enums:

- `Dependency.ecosystem` → `str`
- technology `category` → optional `str`
- names, versions, paths, languages, build tools → `str`

---

## Entities

### ProjectInfo

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| name | `str` | **required** | open string |
| description | `str` | **optional** | |
| primary_language | `str` | **optional** | open string; not an enum |

`ProjectInfo.type` is **not** part of the frozen contract.

### RepositoryInfo

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| root_path | `str` | **required** | portable path; must not require machine-specific absolute paths |
| is_git_repository | `bool` | **required** | |
| branch | `str` | **optional** | |
| commit | `str` | **optional** | |

Do not add unnecessary repository metadata in TASK-002.

### Module

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| name | `str` | **required** | |
| path | `str` | **required** | portable relative path preferred |
| type | `ModuleType` | **required** | closed enum |
| language | `str` | **optional** | |
| build_tool | `str` | **optional** | |
| depends_on | `list[str]` | **required** (default `[]`) | internal module names only |

Do **not** add `Module.dependencies`.

### Technology

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| name | `str` | **required** | |
| category | `str` | **optional** | open string, not enum |
| version | `str` | **optional** | |
| evidence | `list[Evidence]` | **required** (default `[]`) | zero or more records |

### Dependency

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| name | `str` | **required** | package/library name or coordinate |
| ecosystem | `str` | **required** | e.g. Maven, PyPI, npm — **not** an enum |
| version | `str` | **optional** | |
| scope | `DependencyScope` | **optional** | closed enum when present |
| declared_by | `str` | **optional** | declaring module name |
| evidence | `list[Evidence]` | **required** (default `[]`) | zero or more records |

### Evidence

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| source_file | `str` | **required** | e.g. `pom.xml` |
| source_type | `EvidenceType` | **required** | closed enum |
| detail | `str` | **optional** | free-form detail |

### GenerationMetadata

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| engine_version | `str` | **required** | |
| schema_version | `str` | **required** | |
| generated_at | `datetime` | **required** | timezone-aware UTC preferred; **not** `str` / `datetime \| str` |
| analysis_status | `AnalysisStatus` | **required** | whole-context completeness |

---

## Relationships

```text
Technology.evidence[] ──► Evidence
Dependency.evidence[] ──► Evidence
Module.depends_on[] ──► other Module.name (by string)
Dependency.declared_by ──► Module.name (optional string)
ProjectContext.project_dependencies[] ──► Dependency  (sole external-dep owner)
```

**Deferred:** first-class `DependencyGraph` / graph root for `dependencies.json`.

---

## Validation rules

1. Invalid `ModuleType`, `DependencyScope`, `EvidenceType`, or `AnalysisStatus` values → rejection
2. Missing required fields → rejection
3. Optional fields may be omitted / `None`
4. Empty evidence lists are valid
5. Multiple evidence records on one Technology or Dependency are valid
6. Domain models must not import scanners, filesystem traversal, or CLI packages
7. Models must not require machine-specific absolute paths
8. JSON round-trip via Pydantic v2 `model_dump` / `model_validate`

---

## Serialization contract

```text
Domain model
    │ model_dump (JSON-friendly)
    ▼
dict / JSON
    │ model_validate
    ▼
Domain model
```

---

## Non-contract (do not invent in TASK-002)

- Analyzer result types
- CLI-only DTOs
- `DependencyGraph` entity
- `Module.dependencies`
- `ProjectContext.dependencies` (removed / renamed)
- `DependencyEcosystem` enum
- Per-module or per-analyzer status models
- Evidence on Module / ProjectInfo
- `ProjectInfo.type` enum/field
- `Technology.category` as enum
- Additional members beyond the frozen enum tables
- `generated_at` as `str` or `datetime | str`

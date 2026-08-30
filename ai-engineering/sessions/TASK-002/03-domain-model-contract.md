# 03 — Domain Model Contract

Locked data contract for TASK-002. Implementation must match this contract and [`architecture-decisions.md`](./architecture-decisions.md).

---

## Aggregate

```text
ProjectContext
├── project: ProjectInfo
├── repository: RepositoryInfo
├── modules: List[Module]
├── technologies: List[Technology]
├── dependencies: List[Dependency]   # package/library dependencies
└── metadata: GenerationMetadata
```

---

## Entities

### ProjectInfo

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| name | `str` | yes | open string |
| type | enum | yes | closed taxonomy |
| description | `str` | yes* | follow TASK-002; keep required unless tests prove optional needed |
| primary_language | `str` | yes | open string (not enum) |

### RepositoryInfo

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| root_path | `str` | yes | portable path; no machine-specific absolute path requirement |
| is_git_repository | `bool` | yes | |
| branch | `str` | no | optional |
| commit | `str` | no | optional |

### Module

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| name | `str` | yes | |
| path | `str` | yes | portable relative path preferred |
| type | enum | yes | closed taxonomy |
| language | `str` | yes | open string |
| build_tool | `str` | yes | open string |
| depends_on | `List[str]` | yes (default `[]`) | **internal module names**; locked decision |

### Technology

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| name | `str` | yes | open string |
| category | enum | yes | closed taxonomy |
| version | `str` | no | optional |
| evidence | `Optional[Evidence]` | no | shared Evidence model |

Suggested category values (enum members; exact names may use snake_case or hyphen mapping — pick one style and test it):

- framework, database, messaging, cache, build-tool, runtime, cloud, library

### Dependency

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| name | `str` | yes | package/library coordinate or name |
| version | `str` | no | optional |
| scope | enum | yes | closed taxonomy |
| evidence | `Optional[Evidence]` | no | shared Evidence model |
| declared_by | `Optional[str]` | no | module name that declared it; locked decision |

### GenerationMetadata

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| engine_version | `str` | yes | |
| schema_version | `str` | yes | |
| generated_at | datetime or ISO `str` | yes | prefer timezone-aware UTC if using datetime |

### Evidence

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| file | `str` | yes | evidence path/name (e.g. `pom.xml`) |
| type | enum | yes | closed taxonomy (e.g. build-file) |

---

## Relationships (v0.1)

```text
Technology ──optional──► Evidence
Dependency ──optional──► Evidence
Module.depends_on[] ──► other Module.name (by string)
Dependency.declared_by ──► Module.name (optional string)
```

**Deferred:** first-class `DependencyGraph` / `dependencies.json` graph root.

---

## Validation rules

1. Invalid taxonomy enum values → rejection (AC-005)
2. Missing required fields → rejection (AC-006)
3. Optional fields may be omitted / `None` (AC-007)
4. No dependency on scanners or filesystem I/O inside domain models (AC-009)
5. Models must not require absolute machine paths (AC-010)
6. Prefer Pydantic v2 `model_dump` / `model_validate` for JSON round-trip (AC-003, AC-004)

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

Equivalent semantic content should round-trip consistently for the fields defined above.

---

## Non-contract (do not invent in TASK-002)

- Analyzer result types
- CLI DTOs separate from domain
- Graph export schema for `.ai-context/dependencies.json`
- Multi-evidence lists (`List[Evidence]`)
- Evidence on Module / ProjectInfo

# TASK-002 — Core Project Context Domain Model

## Status

SPECIFICATION_FROZEN

Stage A — Comprehensive Domain Architecture Reconciliation is complete.

Revision-001 — Domain Contract Finalization is **APPROVED**.

Stage B — Repository Compatibility Inspection is **APPROVED**.

Stage C1 — Core Domain Model Implementation:

```text
APPROVED_WITH_MINOR_FIXES
```

Revision-002 — Serialization Contract Completion:

```text
IMPLEMENTED_PENDING_REVIEW
```

- Do **not** mark TASK-002 as DONE
- Do **not** perform final closeout yet
- Implementation targets **Python >= 3.10**

## Canonical sources

| Kind | Path |
|------|------|
| Architecture decisions | [`sessions/TASK-002/architecture-decisions.md`](../sessions/TASK-002/architecture-decisions.md) |
| Domain contract | [`sessions/TASK-002/03-domain-model-contract.md`](../sessions/TASK-002/03-domain-model-contract.md) |
| Session pack | [`sessions/TASK-002/`](../sessions/TASK-002/) |
| Stage A task | [`TASK-002 Stage A — Comprehensive Domain Architecture Reconciliation.md`](./TASK-002%20Stage%20A%20—%20Comprehensive%20Domain%20Architecture%20Reconciliation.md) |
| Revision-001 | [`TASK-002-revision-001-domain-contract-finalization.md`](./TASK-002-revision-001-domain-contract-finalization.md) |
| Decision review | [`reviews/TASK-002-architecture-decision-review.md`](../reviews/TASK-002-architecture-decision-review.md) |

`sessions/TASK-002/decisions.md` has been deleted and is not a source of truth.

## Frozen architecture decisions (summary)

- ADR-001 — Pydantic v2 on **Python >= 3.10** (add Pydantic at implementation only)
- ADR-002 — Enums with frozen members: ModuleType / DependencyScope / EvidenceType / AnalysisStatus; ecosystem is `str`
- ADR-003 — `list[Evidence]` on Technology and Dependency (`source_file`, `source_type`, `detail`)
- ADR-004 — `Module.depends_on` vs `ProjectContext.project_dependencies`; `Dependency.ecosystem`; optional `declared_by`; no `DependencyGraph`
- ADR-005 — `GenerationMetadata.analysis_status`; `generated_at: datetime` (Revision-001)

---

# 1. Objective

Establish the core domain model for AI Context Engine.

The domain model defines the structured data contract used to represent repository analysis results.

This task must establish the stable data foundation for future capabilities including:

- Repository Scanner
- Project Detection
- Module Detection
- Technology Analysis
- Dependency Analysis
- Context Generation

The primary output of this task is a language-agnostic, serializable, validated project context model.

---

# 2. Background

AI Context Engine transforms a software repository into structured project context.

The future pipeline is:

```text
Repository
    │
    ▼
Repository Scanner
    │
    ▼
Project / Module / Technology / Dependency Analysis
    │
    ▼
Core Project Context Domain Model
    │
    ▼
Context Generation
    │
    ▼
.ai-context
```

Before implementing repository analysis capabilities, the system must define the canonical data contract representing analysis results.

This task establishes that contract.

---

# 3. Scope

TASK-002 includes:

- core project context model
- project information model
- repository information model
- module model
- technology model
- dependency model
- generation metadata model
- source evidence model
- validation rules
- serialization support
- deserialization support
- unit tests

---

# 4. Out of Scope

The following capabilities must NOT be implemented in TASK-002:

- repository scanning
- filesystem traversal
- Java project detection
- Python project detection
- Maven parsing
- Gradle parsing
- pyproject.toml parsing
- requirements.txt parsing
- technology detection
- dependency analysis
- `.ai-context` generation
- CLI commands
- incremental updates
- semantic analysis
- `DependencyGraph`
- `Module.dependencies`
- `DependencyEcosystem` enum

TASK-002 defines the data model only.

---

# 5. Core Domain Model

Canonical aggregate (frozen):

```text
ProjectContext
│
├── project: ProjectInfo
│
├── repository: RepositoryInfo
│
├── modules: list[Module]
│
├── technologies: list[Technology]
│
├── project_dependencies: list[Dependency]
│
└── metadata: GenerationMetadata
```

There is no `dependencies` field on `ProjectContext`. External package/library dependencies are owned solely by `project_dependencies`.

Full field-level contract:

[`sessions/TASK-002/03-domain-model-contract.md`](../sessions/TASK-002/03-domain-model-contract.md)

---

# 6. Domain Entities

## 6.1 ProjectContext

Fields:

- project
- repository
- modules
- technologies
- project_dependencies
- metadata

---

## 6.2 ProjectInfo

Required:

- name

Optional:

- description
- primary_language

`ProjectInfo.type` is not part of the frozen contract.

---

## 6.3 RepositoryInfo

Required:

- root_path (portable; must not require machine-specific absolute paths)
- is_git_repository

Optional:

- branch
- commit

---

## 6.4 Module

Required:

- name
- path
- type (`ModuleType`)
- depends_on (`list[str]`, default empty) — internal module relationships

Optional:

- language
- build_tool

Do not add `Module.dependencies`.

---

## 6.5 Technology

Required:

- name
- evidence (`list[Evidence]`, default empty)

Optional:

- category (`str`, not enum)
- version

---

## 6.6 Dependency

Required:

- name
- ecosystem (`str`, not enum) — e.g. Maven, PyPI, npm
- evidence (`list[Evidence]`, default empty)

Optional:

- version
- scope (`DependencyScope`)
- declared_by

---

## 6.7 GenerationMetadata

Required:

- engine_version
- schema_version
- generated_at (`datetime`; timezone-aware UTC preferred; not `str`)
- analysis_status (`AnalysisStatus`: pending | partial | completed | failed)

---

## 6.8 Evidence

Required:

- source_file
- source_type (`EvidenceType`)

Optional:

- detail

---

# 7. Domain Relationships

```text
ProjectContext
│
├── ProjectInfo
├── RepositoryInfo
├── list[Module]
├── list[Technology]
├── list[Dependency] as project_dependencies
└── GenerationMetadata

Technology.evidence -> list[Evidence]
Dependency.evidence -> list[Evidence]
Module.depends_on -> module names
Dependency.declared_by -> optional module name
```

---

# 8. Design Principles

## 8.1 Language Agnostic

Core models must not be tied to Java or Python.

Technology-specific behavior belongs to future analyzers.

---

## 8.2 Serializable

All domain models must support model ↔ dict/JSON round-trip with validation.

---

## 8.3 Validated

Invalid enum values, missing required fields, and invalid structure must be rejected.

---

## 8.4 Deterministic

Equivalent model data should produce semantically consistent serialized output.

---

## 8.5 Extensible

Future capabilities may extend the model later, but must not be implemented prematurely in TASK-002.

---

# 9. Package Structure

```text
src/
└── ai_context/
    └── domain/
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

Tests:

```text
tests/
└── domain/
    ├── test_project_context.py
    ├── test_project.py
    ├── test_repository.py
    ├── test_module.py
    ├── test_technology.py
    ├── test_dependency.py
    ├── test_metadata.py
    └── test_evidence.py
```

---

# 10. Implementation Requirements

The implementation should:

- use Pydantic v2 after verifying Python compatibility
- use explicit types
- avoid `dict[str, Any]` as the primary domain representation
- support validation, serialization, and deserialization
- avoid analyzer and filesystem dependencies
- follow the frozen contract without silent redesign

Dependency direction:

```text
Scanner / Analyzer
        │
        ▼
Domain Model
        │
        ▼
Generator
```

---

# 11. Acceptance Criteria

## AC-001

ProjectContext can be created with valid data.

## AC-002

All core domain entities are explicitly modeled.

## AC-003

Domain models support serialization.

## AC-004

Serialized data can be deserialized back into valid domain models.

## AC-005

Invalid enum values are rejected (`ModuleType`, `DependencyScope`, `EvidenceType`, `AnalysisStatus`).

## AC-006

Required fields are validated.

## AC-007

Optional fields are correctly supported.

## AC-008

Technology and Dependency support multiple `Evidence` records.

## AC-009

Domain models do not depend on repository scanners.

## AC-010

Domain models do not require machine-specific absolute paths.

## AC-011

Unit tests cover valid and invalid model scenarios, including ecosystem, `project_dependencies`, `depends_on`, and partial `analysis_status`.

## AC-012

All existing tests continue to pass.

---

# 12. Validation

Validation should include:

```bash
pytest
ruff check .
mypy src
```

Additionally verify:

- serialization / deserialization
- invalid data rejection
- enum validation
- optional field behavior
- multiple evidence
- `project_dependencies` ownership
- partial context status
- domain model imports

Do not claim validation steps were executed unless they were actually executed.

---

# 13. Engineering Constraints

Do not:

- implement repository scanning or analyzers
- generate `.ai-context`
- add CLI commands
- introduce unrelated refactoring
- add speculative domain entities beyond the frozen contract
- restore dual ADR sources (`decisions.md`)

---

# 14. Expected Result

After TASK-002 implementation:

```text
Repository Analyzer
        │
        ▼
ProjectContext
        │
        ▼
Context Generator
```

The project should have a stable and validated domain model that future repository analysis components can populate.

---

# 15. Completion Definition

TASK-002 can be marked DONE only after:

- implementation completed
- unit tests passed
- validation record created
- review completed
- findings resolved or explicitly accepted
- learning record created
- closeout completed

TASK-002 must follow the established engineering lifecycle from TASK-001.

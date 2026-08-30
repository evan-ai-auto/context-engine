# TASK-002 — Core Project Context Domain Model

## Status

READY_FOR_IMPLEMENTATION

## Architecture decisions locked

The following architecture decisions are locked before implementation:

- Introduce Pydantic v2 for domain models
- Closed `str` Enums for taxonomies; open strings for names
- Shared `Evidence` model with `Optional[Evidence]` on Technology and Dependency
- Minimal Module/Dependency relationship fix (`Module.depends_on`, `Dependency.declared_by`; defer `DependencyGraph`)

Review:

[`ai-engineering/reviews/TASK-002-architecture-decision-review.md`](../reviews/TASK-002-architecture-decision-review.md)

Session decisions:

[`ai-engineering/sessions/TASK-002/architecture-decisions.md`](../sessions/TASK-002/architecture-decisions.md)

Session pack:

[`ai-engineering/sessions/TASK-002/`](../sessions/TASK-002/)

Implementation of `src/ai_context/domain/` has not started.

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

TASK-002 defines the data model only.

---

# 5. Core Domain Model

The top-level domain object is:

```text
ProjectContext
│
├── project
│
├── repository
│
├── modules[]
│
├── technologies[]
│
├── dependencies[]
│
└── metadata
```

---

# 6. Domain Entities

## 6.1 ProjectContext

Represents the complete structured context of a software repository.

Fields:

- project
- repository
- modules
- technologies
- dependencies
- metadata

---

## 6.2 ProjectInfo

Represents the logical project.

Fields:

- name
- type
- description
- primary_language

Example:

```json
{
  "name": "context-engine",
  "type": "application",
  "description": "AI project context generation engine",
  "primary_language": "python"
}
```

---

## 6.3 RepositoryInfo

Represents repository-level metadata.

Fields:

- root_path
- is_git_repository
- branch
- commit

Rules:

- root_path must be portable
- machine-specific absolute paths should not be required
- branch and commit may be optional

---

## 6.4 Module

Represents a logical project module.

Fields:

- name
- path
- type
- language
- build_tool

Example:

```json
{
  "name": "user-service",
  "path": "services/user-service",
  "type": "service",
  "language": "java",
  "build_tool": "maven"
}
```

---

## 6.5 Technology

Represents a detected technology.

Fields:

- name
- category
- version
- evidence

Suggested categories:

- framework
- database
- messaging
- cache
- build-tool
- runtime
- cloud
- library

Example:

```json
{
  "name": "Spring Boot",
  "category": "framework",
  "version": "2.7.18"
}
```

---

## 6.6 Dependency

Represents a concrete dependency.

Fields:

- name
- version
- scope
- evidence

Example:

```json
{
  "name": "spring-boot-starter-web",
  "version": "2.7.18",
  "scope": "compile"
}
```

---

## 6.7 GenerationMetadata

Represents context generation metadata.

Fields:

- engine_version
- schema_version
- generated_at

---

## 6.8 Evidence

Represents evidence supporting analysis results.

Fields:

- file
- type

Example:

```json
{
  "file": "pom.xml",
  "type": "build-file"
}
```

Evidence should allow future analyzers to explain the source of detected information.

---

# 7. Domain Relationships

```text
ProjectContext
│
├── ProjectInfo
│
├── RepositoryInfo
│
├── List[Module]
│
├── List[Technology]
│
├── List[Dependency]
│
└── GenerationMetadata

Technology
└── Evidence

Dependency
└── Evidence
```

---

# 8. Design Principles

## 8.1 Language Agnostic

Core models must not be tied to Java or Python.

Technology-specific behavior belongs to future analyzers.

---

## 8.2 Serializable

All domain models must support:

```text
Model
 ↓
Dictionary
 ↓
JSON
```

And:

```text
JSON
 ↓
Model Validation
 ↓
Domain Model
```

---

## 8.3 Validated

Invalid structured data should be rejected.

Examples:

- invalid enum values
- invalid required fields
- invalid model structure

---

## 8.4 Deterministic

Equivalent model data should produce semantically consistent serialized output.

---

## 8.5 Extensible

Future capabilities should be able to extend the model without requiring major redesign.

However, future capabilities must not be implemented prematurely.

---

# 9. Package Structure

Recommended structure:

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

- use explicit types
- avoid `dict[str, Any]` as the primary domain representation
- use explicit domain models
- support validation
- support serialization
- support deserialization
- avoid analyzer dependencies
- avoid filesystem dependencies

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

The Domain Model must not depend on Scanner or Analyzer implementations.

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

Invalid enum values are rejected.

## AC-006

Required fields are validated.

## AC-007

Optional fields are correctly supported.

## AC-008

Technology and Dependency can include source evidence.

## AC-009

Domain models do not depend on repository scanners.

## AC-010

Domain models do not require machine-specific absolute paths.

## AC-011

Unit tests cover valid and invalid model scenarios.

## AC-012

All existing tests continue to pass.

---

# 12. Validation

Validation should include:

```bash
pytest
```

Additionally verify:

- serialization
- deserialization
- invalid data rejection
- enum validation
- optional field behavior
- domain model imports

Do not claim validation steps were executed unless they were actually executed.

---

# 13. Engineering Constraints

Do not:

- implement repository scanning
- implement project detection
- implement Java analysis
- implement Python analysis
- generate `.ai-context`
- add CLI commands
- introduce unrelated refactoring
- add speculative domain entities without clear need

Keep the implementation focused on the canonical Project Context data contract.

---

# 14. Expected Result

After TASK-002:

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
# TASK-002 Stage C1 — Core Domain Model Implementation

## Objective

Implement the frozen Core Context Domain Model for TASK-002.

This stage begins production implementation after:

* Architecture Freeze approval
* Revision-001 approval
* Repository Compatibility Inspection approval

The architecture and domain contract are frozen.

Implementation must follow the canonical contract exactly.

Do not redesign the domain architecture.

Do not add unrelated abstractions.

Do not begin analyzer, scanner, parser, context generation, or TASK-003 functionality.

---

# 1. Current Task Status

TASK-002 has completed:

```text
Stage A — Architecture Reconciliation
Status: APPROVED

Revision-001 — Domain Contract Finalization
Status: APPROVED

Stage B — Repository Compatibility Inspection
Status: APPROVED
```

Current stage:

```text
Stage C1 — Core Domain Model Implementation
```

The goal is to implement:

```text
Core Context Domain Model
+
Contract Tests
+
Local Validation
```

Do not perform final TASK closeout yet.

---

# 2. Mandatory Reading

Before implementation, read all of the following:

```text
README.md

pyproject.toml

ai-engineering/tasks/TASK-002.md

ai-engineering/tasks/TASK-002-revision-001-domain-contract-finalization.md

ai-engineering/sessions/TASK-002/architecture-decisions.md

ai-engineering/sessions/TASK-002/02-implementation-plan.md

ai-engineering/sessions/TASK-002/03-domain-model-contract.md

ai-engineering/sessions/TASK-002/04-test-plan.md

ai-engineering/sessions/TASK-002/05-validation-checklist.md

ai-engineering/sessions/TASK-002/06-cursor-prompt.md

ai-engineering/sessions/TASK-002/07-repository-compatibility-inspection.md
```

Also inspect the current implementation structure:

```text
src/ai_context/
tests/
```

The actual repository structure discovered during Stage B must take precedence over earlier assumptions.

---

# 3. Architecture Authority

The canonical architecture sources are:

```text
architecture-decisions.md
        ↓
03-domain-model-contract.md
        ↓
04-test-plan.md
        ↓
05-validation-checklist.md
```

Implementation must follow these documents.

Priority order:

```text
Architecture Decisions
        ↓
Domain Model Contract
        ↓
Test Plan
        ↓
Validation Checklist
        ↓
Implementation Prompt
```

If any conflict is discovered:

```text
STOP.

Do not silently choose a new architecture.

Report the conflict.
```

Do not invent new domain concepts.

---

# 4. Dependency Change

Add Pydantic v2 as a runtime dependency.

Use:

```toml
pydantic>=2.0,<3.0
```

Add it according to the existing dependency management strategy discovered during Stage B.

Do not introduce:

* Poetry
* uv
* PDM
* Hatch
* new package managers
* lock files

unless already required by the repository.

Do not add unrelated dependencies.

---

# 5. Required Domain Package

Create the domain package under:

```text
src/ai_context/domain/
```

Recommended structure:

```text
src/ai_context/domain/
├── __init__.py
├── enums.py
├── evidence.py
├── project.py
├── repository.py
├── module.py
├── technology.py
├── dependency.py
├── metadata.py
└── project_context.py
```

This file organization is implementation-oriented only.

Do not interpret the file structure as permission to introduce new architecture.

If a simpler structure better matches the canonical contract while preserving clarity and import safety, it may be used.

However:

* do not merge unrelated concepts into one large file
* do not create unnecessary abstraction layers
* do not create a generic `base.py` unless genuinely required
* do not introduce repositories/services/managers

The domain layer must remain a pure data model layer.

---

# 6. Required Domain Models

Implement exactly the frozen core models:

```text
ProjectContext

ProjectInfo

RepositoryInfo

Module

Technology

Dependency

Evidence

GenerationMetadata
```

Do not add speculative domain entities.

Do not add:

```text
Analyzer
Scanner
Parser
RepositoryService
ContextService
ContextBuilder
TechnologyDetector
DependencyResolver
```

Those belong to future tasks.

---

# 7. Pydantic Model Rules

Use Pydantic v2.

All domain models should inherit from:

```python
pydantic.BaseModel
```

Do not create a custom base model unless the frozen architecture explicitly requires one.

Prefer explicit typed fields.

Examples:

```python
name: str
```

```python
description: str | None = None
```

For collections:

```python
items: list[Item] = Field(default_factory=list)
```

Never use mutable defaults such as:

```python
items: list[Item] = []
```

Do not use `Any` unless explicitly justified by the contract.

---

# 8. Frozen Enums

Implement exactly the frozen string-based enums.

All enum values must remain stable.

Use:

```python
from enum import Enum
```

Recommended pattern:

```python
class SomeEnum(str, Enum):
    VALUE = "value"
```

---

## ModuleType

Canonical values:

```text
application
library
service
tool
unknown
```

Do not add additional values.

---

## DependencyScope

Canonical values:

```text
compile
runtime
test
development
optional
unknown
```

These are normalized cross-ecosystem concepts.

Do not add Maven-specific or Gradle-specific values.

Do not add:

```text
provided
compileOnly
implementation
api
devDependencies
```

Future analyzers are responsible for normalization.

---

## EvidenceType

Canonical values:

```text
build_file
lock_file
manifest
source
config
other
```

Do not add additional values.

---

## AnalysisStatus

Canonical values:

```text
pending
partial
completed
failed
```

Do not add additional values.

---

# 9. Evidence Model Rules

Evidence is a reusable cross-domain model.

Do not duplicate evidence structures across:

* Technology
* Dependency
* Module
* ProjectContext

Use the canonical Evidence model.

Evidence must preserve the fields defined in the frozen domain contract.

Do not introduce:

```text
EvidenceStore
EvidenceCollection
EvidenceResolver
EvidenceService
```

---

# 10. Dependency Model Rules

The Dependency model is a normalized domain representation.

Important architectural rules:

```text
ecosystem
```

remains:

```python
str
```

Do not convert ecosystem into an enum.

Examples may include:

```text
maven
gradle
pip
npm
pnpm
unknown
```

But implementation must follow the exact canonical contract.

The core model must not become ecosystem-specific.

---

# 11. Module Dependency Rules

Module relationships must follow the frozen contract.

The project-level dependency collection:

```text
project_dependencies
```

and module relationships:

```text
depends_on
```

have different semantics.

Do not merge them.

Do not infer dependency graphs.

Do not implement graph algorithms.

Do not implement dependency resolution.

This stage only represents the domain data.

---

# 12. GenerationMetadata Rules

The frozen domain field is:

```python
generated_at: datetime
```

The in-memory domain type must remain:

```text
datetime
```

Do not use:

```python
datetime | str
```

Pydantic may deserialize valid ISO 8601 input into a typed datetime.

Expected behavior:

```text
datetime input
        ↓
accepted

ISO 8601 input
        ↓
Pydantic parsing
        ↓
datetime field value

invalid datetime input
        ↓
ValidationError
```

Prefer timezone-aware UTC timestamps where timestamps are generated.

Do not introduce custom datetime serialization logic unless required by the canonical contract.

Use Pydantic's standard serialization behavior where possible.

---

# 13. ProjectContext Rules

ProjectContext is the aggregate root of the Core Context Domain Model.

Follow the canonical contract exactly.

The relationship conceptually is:

```text
ProjectContext
│
├── ProjectInfo
├── RepositoryInfo
├── modules[]
├── technologies[]
├── project_dependencies[]
└── GenerationMetadata
```

Do not add:

```text
AnalyzerResult
ScanResult
ContextGraph
ProjectAnalysis
```

Those are future concerns.

ProjectContext should remain a domain data aggregate.

---

# 14. Optional and Required Fields

Follow the canonical domain contract exactly.

Do not make fields optional merely for convenience.

Do not make required fields optional.

Do not introduce defaults that hide missing required data.

Example:

Correct:

```python
name: str
```

Incorrect:

```python
name: str | None = None
```

unless explicitly defined as optional in the contract.

---

# 15. Import Direction Rules

Maintain a simple dependency direction.

Recommended:

```text
Enums
  ↓

Evidence
  ↓

Leaf Models
  ↓

ProjectContext
```

Avoid circular dependencies.

The domain package must not import:

```text
cli
infrastructure
analyzers
future services
```

The CLI must not be modified during this task.

Domain models should remain independent from application execution concerns.

---

# 16. Package Public API

Create:

```text
src/ai_context/domain/__init__.py
```

Expose the primary public domain types where appropriate.

The public API should be intentional.

Avoid:

```python
from .everything import *
```

Prefer explicit exports.

Example conceptually:

```python
from .project_context import ProjectContext
from .project import ProjectInfo
```

Use `__all__` if it improves clarity.

Do not modify:

```text
src/ai_context/__init__.py
```

unless genuinely necessary for package integration.

If modification appears necessary:

Report it before proceeding.

---

# 17. Test Implementation

Implement contract tests under:

```text
tests/domain/
```

Recommended structure:

```text
tests/domain/
├── __init__.py
├── test_enums.py
├── test_evidence.py
├── test_project.py
├── test_repository.py
├── test_module.py
├── test_technology.py
├── test_dependency.py
├── test_metadata.py
└── test_project_context.py
```

The exact file split may be simplified if the repository's existing testing conventions suggest a better structure.

However:

Every canonical contract area must be tested.

---

# 18. Test Plan Authority

The test cases defined in:

```text
ai-engineering/sessions/TASK-002/04-test-plan.md
```

must be treated as the contract testing authority.

Map implementation tests to the test plan.

Do not silently skip test cases.

If a test plan item cannot be implemented because of ambiguity:

```text
STOP.

Report the ambiguity.
```

---

# 19. Minimum Test Coverage

At minimum verify:

## Enums

* all canonical values exist
* enum values are string-compatible
* no expected value is missing

---

## Required Fields

Verify missing required fields produce validation failures where expected.

---

## Optional Fields

Verify optional fields:

* default correctly
* accept `None` where allowed

---

## Collections

Verify collection fields:

* use independent default factories
* do not share mutable state

Example concept:

```python
a = ProjectContext(...)
b = ProjectContext(...)

a.modules.append(...)

assert b.modules == []
```

---

## Evidence

Verify Evidence can be associated with the models required by the canonical contract.

Verify multiple evidence items where supported.

---

## Dependency

Verify:

```text
ecosystem
```

accepts normalized string values.

Do not restrict ecosystem to an enum.

---

## Module Relationships

Verify:

```text
depends_on
```

behaves according to the frozen contract.

Do not test graph resolution.

---

## GenerationMetadata

Verify:

1. native `datetime` input succeeds
2. valid ISO 8601 input is parsed by Pydantic
3. resulting field type is `datetime`
4. invalid datetime input fails validation

Do not require valid ISO 8601 strings to be rejected.

---

## Serialization

Verify the canonical domain models can be serialized using Pydantic v2.

Use appropriate Pydantic APIs.

Examples may include:

```python
model.model_dump()
```

and:

```python
model.model_dump_json()
```

Do not create custom serialization frameworks.

---

## Deserialization

Verify valid structured input can construct the domain models.

Use:

```python
Model.model_validate(...)
```

where appropriate.

Do not implement custom parsers.

---

# 20. Validation Commands

After implementation run:

```bash
pytest
```

Then:

```bash
ruff check .
```

Then:

```bash
mypy src
```

Record the results.

Expected:

```text
pytest: PASS

ruff: PASS

mypy: PASS
```

If failures occur:

Fix only issues introduced by TASK-002 implementation.

Do not refactor unrelated code.

Do not fix historical issues unless they block TASK-002.

---

# 21. Manual Architecture Validation

Before committing, manually verify:

```text
[ ] No analyzer implementation
[ ] No scanner implementation
[ ] No parser implementation
[ ] No context generation logic
[ ] No graph algorithms
[ ] No service layer
[ ] No repository layer
[ ] No CLI modification
[ ] No architecture redesign
[ ] No new domain concepts
[ ] No ecosystem enum
[ ] No mutable list defaults
[ ] No datetime | str
[ ] No circular domain imports
[ ] No unrelated dependencies
```

---

# 22. Update Implementation Progress Documentation

Do not mark TASK-002 as DONE.

Update only the relevant implementation progress status if the current task documentation supports it.

Suggested state:

```text
TASK-002

Stage C1:
IMPLEMENTED_PENDING_REVIEW
```

Do not perform final closeout.

Do not create TASK-002 completion documentation yet.

---

# 23. Required Final Implementation Report

Before committing, provide a concise report.

## A. Implementation Summary

List implemented domain models.

---

## B. Dependency Changes

Confirm Pydantic version constraint.

---

## C. Files Created

List all new production files.

---

## D. Files Modified

List modified files.

---

## E. Test Mapping

Summarize:

```text
Test Plan
        ↓
Implemented Tests
```

Identify any intentionally deferred test.

If none:

```text
None deferred.
```

---

## F. Validation Results

Report:

```text
pytest:
ruff:
mypy:
```

---

## G. Architecture Boundary Check

Explicitly confirm:

```text
No analyzer implementation

No scanner implementation

No parser implementation

No CLI modification

No architecture changes
```

---

## H. Remaining Concerns

List:

```text
NONE
```

if no concern exists.

Do not invent speculative concerns.

---

# 24. Git Scope Check

Before commit:

```bash
git status
```

Expected changes should be limited to:

```text
pyproject.toml

src/ai_context/domain/

tests/domain/

relevant TASK-002 implementation progress documentation
```

Review every changed file.

Ensure there are no unrelated modifications.

---

# 25. Commit

Suggested commit message:

```text
feat(domain): implement TASK-002 core context models
```

After committing:

```text
STOP.
```

Do not:

```text
start TASK-003

implement analyzers

implement scanners

implement context generation

perform TASK-002 final closeout
```

Wait for repository review.

---

# 26. Final Stop Condition

After:

```text
Implementation
+
Tests
+
pytest
+
ruff
+
mypy
+
Commit
```

Stop.

The expected final state is:

```text
TASK-002

Stage C1:
IMPLEMENTED_PENDING_REVIEW
```

The next action must be:

```text
GitHub Repository Review
```

before Stage C2 closeout begins.

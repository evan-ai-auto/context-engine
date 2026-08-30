# TASK-002 Stage B — Repository Compatibility Inspection

## Objective

Perform a repository compatibility inspection before implementing TASK-002 Core Context Domain Model.

The TASK-002 architecture and domain contract are already frozen and approved.

This stage must verify whether the current repository state is compatible with the frozen architecture before any production domain implementation begins.

This is an inspection and preflight stage.

Do not implement TASK-002.

Do not redesign the architecture.

Do not modify the frozen domain contract.

---

# 1. Architecture Freeze Status

The following architecture decisions are frozen:

```text
Python >= 3.10

Pydantic v2

Core Domain Models:

ProjectContext
ProjectInfo
RepositoryInfo
Module
Technology
Dependency
Evidence
GenerationMetadata

Enums:

ModuleType
DependencyScope
EvidenceType
AnalysisStatus
```

The canonical sources are:

```text
ai-engineering/sessions/TASK-002/architecture-decisions.md

ai-engineering/sessions/TASK-002/03-domain-model-contract.md

ai-engineering/sessions/TASK-002/04-test-plan.md

ai-engineering/sessions/TASK-002/05-validation-checklist.md
```

Do not modify these architecture decisions.

If a compatibility problem is discovered, report it.

Do not silently change the architecture.

---

# 2. Required Reading

Before inspection, read:

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
```

Also inspect the current repository structure.

---

# 3. Inspection Scope

Perform the following inspections.

---

## B1 — Python Runtime Compatibility

Check the active development environment.

Run:

```bash
python --version
```

If necessary:

```bash
python3 --version
```

Verify compatibility with:

```text
Python >= 3.10
```

Record:

- detected Python version
- whether compatible
- whether multiple Python environments exist
- whether repository tooling uses the expected Python runtime

Do not change Python installation.

Do not modify source code.

---

## B2 — pyproject.toml Compatibility

Inspect:

```text
pyproject.toml
```

Verify:

### Python Version

Expected:

```toml
requires-python = ">=3.10"
```

### Ruff

Expected target:

```text
py310
```

### mypy

Expected:

```text
3.10
```

### Test Configuration

Verify whether pytest is configured correctly.

### Dependency Strategy

Determine how Pydantic v2 should be introduced during implementation.

Check:

- existing dependencies
- dependency groups
- dev dependencies
- package management strategy
- lock file presence

Do not add Pydantic yet.

Do not modify dependencies.

Record only the recommended installation/change location.

---

# B3 — Package Structure Inspection

Inspect the current package layout.

Expected base structure is approximately:

```text
src/
└── ai_context/
```

Inspect:

```text
src/ai_context/
```

Determine:

- existing modules
- package boundaries
- `__init__.py`
- CLI structure
- configuration modules
- existing utilities

Specifically determine whether:

```text
src/ai_context/domain/
```

already exists.

If it does not exist:

```text
Record:
domain package creation required during Stage C
```

Do not create the directory during this stage.

---

# B4 — Existing Import Graph Inspection

Inspect the current imports.

Pay special attention to:

```text
src/ai_context/__init__.py

src/ai_context/cli.py
```

Determine whether future domain imports such as:

```python
from ai_context.domain import ProjectContext
```

could introduce:

- circular imports
- package initialization issues
- CLI coupling
- unwanted side effects

Document the current import relationships.

Do not modify imports.

Do not refactor existing modules.

---

# B5 — Existing Test Baseline

Inspect the test structure.

Check:

```text
tests/
```

if present.

Determine:

- current test files
- pytest configuration
- test naming conventions
- existing fixtures
- test execution command

Run the repository test suite.

Preferred command:

```bash
pytest
```

If the repository uses another documented command, use that command instead.

Record:

```text
Baseline Test Result

PASS
FAIL
ERROR
NO TESTS
```

If tests fail:

Do not fix them.

Record:

- failing tests
- error summary
- whether failure appears unrelated to TASK-002

---

# B6 — Ruff Baseline

Run:

```bash
ruff check .
```

Record:

```text
Baseline Ruff Result

PASS
FAIL
NOT AVAILABLE
```

If failures exist:

Do not fix them.

Record the number and categories of issues.

---

# B7 — mypy Baseline

Run:

```bash
mypy src
```

If the configured command differs, use the repository configuration.

Record:

```text
Baseline mypy Result

PASS
FAIL
NOT CONFIGURED
NOT AVAILABLE
```

Do not fix existing issues.

This stage is only establishing the baseline.

---

# B8 — Packaging and Dependency Tooling

Determine which tooling manages dependencies.

Inspect for:

```text
pip
pip-tools
poetry
uv
pdm
hatch
setuptools
requirements.txt
requirements-dev.txt
poetry.lock
uv.lock
```

Record:

- package manager
- dependency declaration location
- lock file
- recommended method for adding Pydantic v2 during Stage C

Do not install packages.

Do not generate lock files.

---

# B9 — Existing CLI Compatibility

Inspect the existing CLI implementation.

Determine:

- CLI entry point
- current commands
- whether CLI directly depends on internal models
- whether adding `ai_context.domain` could affect CLI behavior

The purpose is to ensure TASK-002 implementation remains isolated.

Do not modify CLI code.

---

# B10 — Domain Model Integration Readiness

Based on the inspection, determine whether the following future structure is safe:

```text
src/
└── ai_context/
    ├── __init__.py
    ├── cli.py
    │
    └── domain/
        ├── __init__.py
        ├── enums.py
        ├── evidence.py
        ├── project.py
        └── metadata.py
```

This is only a preliminary package layout hypothesis.

Do not treat this as a new architecture decision.

Evaluate:

- package compatibility
- import compatibility
- naming conflicts
- potential circular dependencies
- test integration compatibility

If issues exist:

Report them.

Do not redesign automatically.

---

# 4. Required Commands

Attempt to execute the following where applicable:

```bash
python --version
```

```bash
pytest
```

```bash
ruff check .
```

```bash
mypy src
```

Also inspect:

```bash
git status
```

Do not modify unrelated files.

If commands are unavailable:

Record:

```text
NOT AVAILABLE
```

and explain why.

Do not install tools unless explicitly required by the repository's existing setup.

---

# 5. Inspection Report

Create:

```text
ai-engineering/sessions/TASK-002/07-repository-compatibility-inspection.md
```

The report must contain the following sections.

---

## 1. Inspection Metadata

```text
Task: TASK-002

Stage: Stage B — Repository Compatibility Inspection

Purpose:
Pre-implementation repository compatibility validation

Architecture Status:
FROZEN

Inspection Status:
COMPLETED_PENDING_REVIEW
```

Include:

- inspection date
- inspected repository state
- current git commit hash

---

## 2. Executive Summary

Provide:

```text
Overall Readiness:

READY
READY_WITH_WARNINGS
NOT_READY
```

Also provide a concise summary.

---

## 3. Python Runtime

Record:

- detected version
- required version
- compatibility result

Example:

```text
Detected:
Python 3.x.x

Required:
Python >= 3.10

Result:
COMPATIBLE
```

---

## 4. Project Configuration

Inspect:

```text
pyproject.toml
```

Record:

- requires-python
- Ruff target
- mypy target
- pytest configuration
- dependency management strategy

---

## 5. Package Structure

Document the actual repository structure relevant to TASK-002.

Include:

```text
src/ai_context/
```

and its important modules.

State whether:

```text
src/ai_context/domain/
```

already exists.

---

## 6. Import Compatibility

Document:

- package initialization behavior
- CLI imports
- potential domain import risks
- circular dependency risks

Classify:

```text
NO_RISK
LOW_RISK
MEDIUM_RISK
HIGH_RISK
```

---

## 7. Test Baseline

Record:

```text
pytest result
```

Include:

- pass/fail status
- number of tests if available
- notable failures

Do not fix failures.

---

## 8. Static Analysis Baseline

Record separately:

### Ruff

```text
PASS
FAIL
NOT AVAILABLE
```

### mypy

```text
PASS
FAIL
NOT CONFIGURED
NOT AVAILABLE
```

Include concise summaries.

---

## 9. Dependency Integration

Document:

- package manager
- dependency declaration method
- lock file status
- recommended location for Pydantic v2 declaration

Do not add the dependency.

---

## 10. CLI Compatibility

Document:

- CLI entry point
- current coupling
- potential impact from domain package introduction

---

## 11. TASK-002 Implementation Readiness

Evaluate:

| Area | Status | Notes |
|---|---|---|
| Python Runtime | | |
| Package Structure | | |
| Import Graph | | |
| Test Environment | | |
| Ruff | | |
| mypy | | |
| Dependency Tooling | | |
| CLI Isolation | | |

Use:

```text
READY
WARNING
BLOCKED
NOT_APPLICABLE
```

---

## 12. Risks

List discovered risks.

Each risk should include:

```text
Risk ID
Description
Severity
Impact
Recommended Action
```

Severity:

```text
LOW
MEDIUM
HIGH
```

Do not automatically resolve risks.

---

## 13. Required Actions Before Implementation

Classify actions as:

```text
BLOCKING
RECOMMENDED
OPTIONAL
```

If no action is required, explicitly state:

```text
No blocking compatibility issues detected.
```

---

## 14. Final Recommendation

Choose one:

```text
APPROVED_FOR_IMPLEMENTATION

APPROVED_WITH_WARNINGS

REQUIRES_ARCHITECTURE_REVIEW

BLOCKED
```

Provide concise reasoning.

---

# 6. Strict Boundaries

This stage is inspection only.

Allowed:

```text
Read files
Inspect repository
Run diagnostic commands
Run tests
Run static analysis
Inspect dependencies
Create inspection report
```

Forbidden:

```text
Implement domain models
Create domain package
Add Pydantic dependency
Modify pyproject.toml
Modify production code
Modify tests
Modify architecture decisions
Modify frozen domain contract
Refactor CLI
Fix unrelated issues
Begin TASK-003
```

If inspection reveals a problem:

```text
Report it.

Do not silently fix it.
```

---

# 7. Git Requirements

Before commit:

```bash
git status
```

Verify that only the inspection report was intentionally added or modified.

Expected primary change:

```text
ai-engineering/sessions/TASK-002/07-repository-compatibility-inspection.md
```

No production code changes should be introduced.

No dependency changes should be introduced.

---

# 8. Commit

Suggested commit message:

```text
docs(ai-engineering): inspect TASK-002 repository compatibility
```

After committing:

Stop.

Do not begin TASK-002 implementation.

---

# 9. Required Cursor Final Response

Before finishing, provide:

## Inspection Summary

```text
Overall Readiness:
READY / READY_WITH_WARNINGS / NOT_READY
```

## Baseline Results

```text
Python:
pytest:
ruff:
mypy:
```

## Blocking Issues

List blocking issues.

If none:

```text
None detected.
```

## Warnings

List warnings.

## Recommended Implementation Preparation

List only actions required before Stage C.

## Files Changed

List modified files.

Expected:

```text
ai-engineering/sessions/TASK-002/07-repository-compatibility-inspection.md
```

## Final Recommendation

Choose:

```text
APPROVED_FOR_IMPLEMENTATION

APPROVED_WITH_WARNINGS

REQUIRES_ARCHITECTURE_REVIEW

BLOCKED
```

After providing the report and committing, stop.
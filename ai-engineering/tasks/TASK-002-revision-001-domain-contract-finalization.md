# TASK-002 Revision-001 — Domain Contract Finalization

## Revision ID

TASK-002-revision-001

## Related Task

TASK-002 — Core Project Context Domain Model

## Status

APPROVED

## Trigger

Remaining implementation-time ambiguities after Stage A freeze:

- minimum Python version left soft / historical wording
- enum member vocabularies not fully closed
- `GenerationMetadata.generated_at` allowed `datetime or ISO str`

## Objective

Perform a final pre-implementation contract finalization for TASK-002.

Eliminate the remaining implementation-time architectural ambiguity before the Repository Compatibility Inspection stage.

This revision is intentionally narrow.

Do not redesign the domain model.

Do not add new domain entities.

Do not implement production domain code or tests.

---

## Scope

In scope:

- Freeze Python >= 3.10 policy in packaging and TASK-002 specs
- Freeze canonical members for ModuleType, DependencyScope, EvidenceType, AnalysisStatus
- Freeze `generated_at: datetime` (timezone-aware UTC preferred)
- Keep specification documents consistent

Out of scope:

- Domain implementation under `src/ai_context/domain/`
- Tests
- Adding Pydantic to `pyproject.toml`
- Analyzers / scanners / CLI / `.ai-context` generation
- Repository Compatibility Inspection
- Redesigning aggregate ownership or adding entities

---

## Approved Changes

### R1 — Python compatibility

- `requires-python = ">=3.10"`
- Ruff `target-version = "py310"`
- mypy `python_version = "3.10"`
- Specs state implementation targets Python 3.10+
- Do not add Pydantic in this revision

### R2 — Canonical enum members

**ModuleType:** `application`, `library`, `service`, `tool`, `unknown`

**DependencyScope:** `compile`, `runtime`, `test`, `development`, `optional`, `unknown`

**EvidenceType:** `build_file`, `lock_file`, `manifest`, `source`, `config`, `other`

**AnalysisStatus:** `pending`, `partial`, `completed`, `failed`

Implementation must not invent additional enum members.

### R3 — generated_at type

- `GenerationMetadata.generated_at: datetime`
- Prefer timezone-aware UTC
- No `datetime | str`
- ISO 8601 conversion via Pydantic serialization

---

## Files Expected to Change

- `pyproject.toml` (confirm / already aligned)
- `ai-engineering/sessions/TASK-002/architecture-decisions.md`
- `ai-engineering/sessions/TASK-002/02-implementation-plan.md`
- `ai-engineering/sessions/TASK-002/03-domain-model-contract.md`
- `ai-engineering/sessions/TASK-002/04-test-plan.md`
- `ai-engineering/sessions/TASK-002/05-validation-checklist.md`
- `ai-engineering/sessions/TASK-002/06-cursor-prompt.md`
- `ai-engineering/tasks/TASK-002.md`
- `ai-engineering/tasks/TASK-002-revision-001-domain-contract-finalization.md` (this file)

---

## Out of Scope

- production domain code
- tests
- Pydantic dependency addition
- analyzer/scanner code
- starting Repository Compatibility Inspection
- marking TASK-002 DONE

---

## Validation Criteria

- [x] Python policy frozen at >= 3.10 in `pyproject.toml` and TASK-002 specs
- [x] All four enum member sets explicit and consistent across docs
- [x] `generated_at` is `datetime` only
- [x] No new domain entities
- [x] No production domain implementation / tests / Pydantic added
- [x] Consistency review across listed TASK-002 documents

---

## Completion Status

APPROVED

Review feedback on `generated_at` test/serialization semantics applied.

TASK-002 remains **SPECIFICATION_FROZEN** / not DONE. Implementation has not started.

Ready for the Repository Compatibility Inspection gate.

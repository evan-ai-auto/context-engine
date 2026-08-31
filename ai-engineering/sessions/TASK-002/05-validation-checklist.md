# 05 — TASK-002 Validation Checklist

Complete only with **actually executed** results after implementation. Specification revisions do not execute product validation commands.

---

## Specification freeze (Stage A + Revision-001)

- [x] Canonical ADRs in `architecture-decisions.md`
- [x] Canonical contract in `03-domain-model-contract.md`
- [x] `decisions.md` deleted
- [x] `project_dependencies` naming reconciled
- [x] Multiple evidence + ecosystem + analysis_status documented
- [x] Python >= 3.10 frozen in `pyproject.toml` and specs (Revision-001)
- [x] Enum members frozen for all four enums (Revision-001)
- [x] `generated_at: datetime` frozen (Revision-001); ISO 8601 allowed as JSON/deserialization input

---

## Preconditions (implementation)

- [x] Architecture remains frozen (no silent redesign; no extra enum members)
- [x] Implementation matches `03-domain-model-contract.md`
- [x] No scanner / analyzer / generator / new CLI features added
- [x] Pydantic 2.x pin chosen for Python >= 3.10 before adding to `pyproject.toml`

---

## Domain contract consistency

- [x] Aggregate uses `project_dependencies` (not `dependencies`)
- [x] Required vs optional fields match contract
- [x] Enums limited to ModuleType, DependencyScope, EvidenceType, AnalysisStatus
- [x] Enum members match frozen vocabularies exactly
- [x] `Dependency.ecosystem` is required `str` (not enum)
- [x] `Technology.evidence` and `Dependency.evidence` are `list[Evidence]`
- [x] Evidence fields: `source_file`, `source_type`, `detail`
- [x] `Module.depends_on` present; no `Module.dependencies`
- [x] `GenerationMetadata.analysis_status` present
- [x] `GenerationMetadata.generated_at` is domain `datetime` (ISO strings OK as deserialization input only)
- [x] Public package API exports core models from `domain`

---

## Behavioral checks

- [x] Multiple evidence records supported
- [x] Partial context via `analysis_status=partial` supported
- [x] Serialization round-trip works (including datetime ↔ ISO)
- [x] Invalid enums / missing required fields fail validation
- [x] Existing tests still pass

---

## Commands (post-implementation)

| Command | Result | Notes |
|---------|--------|-------|
| `python --version` | PASS | 3.10.11 |
| `pip install -e ".[dev]"` | PASS | pydantic 2.13.5 |
| `pytest` | PASS | 44 passed (Stage C2 final) |
| `ruff check .` | PASS | |
| `mypy src` | PASS | 13 source files |
| `git diff --check` | PASS | no whitespace errors |

---

## Sign-off

| Role | Name / Agent | Date | Outcome |
|------|--------------|------|---------|
| Stage A reconciler | | | SPECIFICATION_FROZEN |
| Revision-001 | | | APPROVED |
| Stage B inspection | | | APPROVED_WITH_WARNINGS |
| Stage C1 implementer | | 2026-08-31 | APPROVED |
| Revision-002 | | 2026-08-31 | APPROVED |
| Stage C2 closeout | | 2026-08-31 | COMPLETED |

Status: **TASK-002 DONE** (see `08-closeout.md`)

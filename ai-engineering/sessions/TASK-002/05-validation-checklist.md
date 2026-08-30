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

- [ ] Architecture remains frozen (no silent redesign; no extra enum members)
- [ ] Implementation matches `03-domain-model-contract.md`
- [ ] No scanner / analyzer / generator / new CLI features added
- [ ] Pydantic 2.x pin chosen for Python >= 3.10 before adding to `pyproject.toml`

---

## Domain contract consistency

- [ ] Aggregate uses `project_dependencies` (not `dependencies`)
- [ ] Required vs optional fields match contract
- [ ] Enums limited to ModuleType, DependencyScope, EvidenceType, AnalysisStatus
- [ ] Enum members match frozen vocabularies exactly
- [ ] `Dependency.ecosystem` is required `str` (not enum)
- [ ] `Technology.evidence` and `Dependency.evidence` are `list[Evidence]`
- [ ] Evidence fields: `source_file`, `source_type`, `detail`
- [ ] `Module.depends_on` present; no `Module.dependencies`
- [ ] `GenerationMetadata.analysis_status` present
- [ ] `GenerationMetadata.generated_at` is domain `datetime` (ISO strings OK as deserialization input only)
- [ ] Public package API exports core models from `domain`

---

## Behavioral checks

- [ ] Multiple evidence records supported
- [ ] Partial context via `analysis_status=partial` supported
- [ ] Serialization round-trip works (including datetime ↔ ISO)
- [ ] Invalid enums / missing required fields fail validation
- [ ] Existing tests still pass

---

## Commands (post-implementation)

| Command | Result | Notes |
|---------|--------|-------|
| `python --version` | _pending_ | expect >= 3.10 |
| `pip install -e ".[dev]"` | _pending_ | |
| `pytest` | _pending_ | |
| `ruff check .` | _pending_ | |
| `mypy src` | _pending_ | |

---

## Sign-off

| Role | Name / Agent | Date | Outcome |
|------|--------------|------|---------|
| Stage A reconciler | | | SPECIFICATION_FROZEN |
| Revision-001 | | | APPROVED |
| Implementer | | | |
| Reviewer | | | |

Status: **SPECIFICATION_FROZEN** + Revision-001 **APPROVED** (implementation not started)

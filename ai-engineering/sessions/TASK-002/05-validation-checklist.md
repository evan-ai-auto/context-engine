# 05 — TASK-002 Validation Checklist

Complete only with **actually executed** results after implementation. Stage A does not execute product validation commands.

---

## Specification freeze (Stage A)

- [x] Canonical ADRs in `architecture-decisions.md`
- [x] Canonical contract in `03-domain-model-contract.md`
- [x] `decisions.md` deleted
- [x] `project_dependencies` naming reconciled
- [x] Multiple evidence + ecosystem + analysis_status documented

---

## Preconditions (implementation)

- [ ] Architecture remains frozen (no silent redesign)
- [ ] Implementation matches `03-domain-model-contract.md`
- [ ] No scanner / analyzer / generator / new CLI features added
- [ ] Python/Pydantic compatibility verified before `pyproject.toml` change

---

## Domain contract consistency

- [ ] Aggregate uses `project_dependencies` (not `dependencies`)
- [ ] Required vs optional fields match contract
- [ ] Enums limited to ModuleType, DependencyScope, EvidenceType, AnalysisStatus
- [ ] `Dependency.ecosystem` is required `str` (not enum)
- [ ] `Technology.evidence` and `Dependency.evidence` are `list[Evidence]`
- [ ] Evidence fields: `source_file`, `source_type`, `detail`
- [ ] `Module.depends_on` present; no `Module.dependencies`
- [ ] `GenerationMetadata.analysis_status` present
- [ ] Public package API exports core models from `domain`

---

## Behavioral checks

- [ ] Multiple evidence records supported
- [ ] Partial context via `analysis_status=partial` supported
- [ ] Serialization round-trip works
- [ ] Invalid enums / missing required fields fail validation
- [ ] Existing tests still pass

---

## Commands (post-implementation)

| Command | Result | Notes |
|---------|--------|-------|
| `python --version` | _pending_ | |
| `pip install -e ".[dev]"` | _pending_ | |
| `pytest` | _pending_ | |
| `ruff check .` | _pending_ | |
| `mypy src` | _pending_ | |

---

## Sign-off

| Role | Name / Agent | Date | Outcome |
|------|--------------|------|---------|
| Stage A reconciler | | | SPECIFICATION_FROZEN |
| Implementer | | | |
| Reviewer | | | |

Status: **SPECIFICATION_FROZEN** (implementation not started)

# 05 — TASK-002 Validation Checklist

Complete only with **actually executed** results. Do not mark pass from intention alone.

---

## Preconditions

- [ ] Architecture decisions remain locked
- [ ] Implementation matches [`03-domain-model-contract.md`](./03-domain-model-contract.md)
- [ ] No scanner / analyzer / generator / new CLI features added

---

## Structure

- [ ] `src/ai_context/domain/` exists with core entity modules
- [ ] `Module.depends_on` present
- [ ] `Dependency.declared_by` present (optional field)
- [ ] Shared `Evidence` used by Technology and Dependency
- [ ] Pydantic v2 declared in `pyproject.toml` (3.8-compatible pin)

---

## Acceptance criteria

- [ ] AC-001 ProjectContext creates with valid data
- [ ] AC-002 All core entities explicitly modeled
- [ ] AC-003 Serialization supported
- [ ] AC-004 Deserialization round-trip works
- [ ] AC-005 Invalid enums rejected
- [ ] AC-006 Required fields validated
- [ ] AC-007 Optional fields supported
- [ ] AC-008 Evidence attachable on Technology/Dependency
- [ ] AC-009 No scanner dependency in domain
- [ ] AC-010 No machine-specific absolute path requirement
- [ ] AC-011 Unit tests cover valid and invalid cases
- [ ] AC-012 Existing tests still pass

---

## Commands

Record version/output summaries when run:

```bash
python --version
pip install -e ".[dev]"
pytest
ruff check .
mypy src
```

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
| Implementer | | | |
| Reviewer | | | |

Status after validation: _NOT STARTED_

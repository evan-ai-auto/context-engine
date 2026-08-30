# 04 — TASK-002 Test Plan

## Strategy

Unit-test the domain package only. Prefer pure construction and validation tests. No filesystem fixtures of real repositories.

Framework: **pytest**  
Models: **Pydantic v2** (per locked decision)  
Location: `tests/domain/` (as in TASK-002) or `tests/unit/domain/` if matching existing layout — prefer TASK-002 recommended `tests/domain/` unless a hygiene revision standardizes otherwise.

---

## Test matrix

| ID | Area | Scenario | Expect |
|----|------|----------|--------|
| T-01 | ProjectContext | Create with valid nested data | succeeds (AC-001) |
| T-02 | Entities | Each core entity constructible | succeeds (AC-002) |
| T-03 | Serialization | `model_dump` produces JSON-friendly dict | succeeds (AC-003) |
| T-04 | Round-trip | dump → JSON → validate | equal semantic fields (AC-004) |
| T-05 | Enums | Invalid taxonomy value | ValidationError (AC-005) |
| T-06 | Required | Omit required field | ValidationError (AC-006) |
| T-07 | Optional | Omit optional version/evidence/branch/commit | succeeds (AC-007) |
| T-08 | Evidence | Technology/Dependency with Evidence | succeeds (AC-008) |
| T-09 | Isolation | Domain imports | no scanner/cli/infra imports (AC-009) |
| T-10 | Paths | Relative / portable root_path | accepted (AC-010) |
| T-11 | Module deps | `depends_on` list of module names | succeeds |
| T-12 | Declared_by | Dependency.declared_by optional | succeeds when set/omitted |
| T-13 | Regression | Existing CLI tests | still pass (AC-012) |

---

## Suggested test files

```text
tests/domain/
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

## Coverage notes

- At least one invalid enum case per taxonomy enum used in public models
- At least one missing-required-field case on aggregate and one leaf entity
- Explicit tests for `Module.depends_on` default empty list behavior
- Explicit tests that Evidence is optional on Technology and Dependency

## Out of test scope for TASK-002

- Parsing `pom.xml` / `pyproject.toml`
- Writing `.ai-context`
- CLI `init` behavior beyond existing regression suite
- Golden file tests for full repository fixtures

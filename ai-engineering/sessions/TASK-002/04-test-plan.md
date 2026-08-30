# 04 — TASK-002 Test Plan

## Strategy

Unit-test the domain package only. No repository filesystem fixtures.

Framework: **pytest**  
Models: **Pydantic v2** on **Python >= 3.10**  
Location: `tests/domain/` as specified in TASK-002

Do not write tests during specification revisions — this document is the specification only.

Frozen enum members (Revision-001) must be used exactly; do not invent extra members in tests as “valid”.

---

## Required coverage

| ID | Area | Scenario | Expect |
|----|------|----------|--------|
| T-01 | ProjectContext | Construct with valid nested data | succeeds |
| T-02 | Required fields | Omit a required field | ValidationError |
| T-03 | Optional fields | Omit optional description/language/version/scope/etc. | succeeds |
| T-04 | ModuleType | Each frozen member + one invalid | accept / reject |
| T-05 | DependencyScope | Each frozen member when present + invalid | accept / reject |
| T-06 | EvidenceType | Each frozen member + invalid | accept / reject |
| T-07 | AnalysisStatus | `pending` / `partial` / `completed` / `failed` + invalid | accept / reject |
| T-08 | Multiple Evidence | Two+ evidence records on Technology and Dependency | succeeds |
| T-09 | Ecosystem | Required `Dependency.ecosystem` string; omit → reject | |
| T-10 | Ownership | External deps only via `project_dependencies` | field present; no `dependencies` |
| T-11 | Module.depends_on | Internal module name list (incl. default `[]`) | succeeds |
| T-12 | Partial context | `metadata.analysis_status = partial` with sparse modules/deps | succeeds |
| T-13 | generated_at | (1) native `datetime` input succeeds; (2) valid ISO 8601 string input parses via Pydantic; (3) resulting field is typed `datetime`; (4) invalid datetime input rejected | succeeds / ValidationError |
| T-14 | Serialization | `model_dump` JSON-friendly (datetime → ISO) | succeeds |
| T-15 | Deserialization | dump → JSON → `model_validate` (ISO → `datetime`) | semantic round-trip |
| T-16 | Invalid model | Bad structure / bad enum / missing required | ValidationError |
| T-17 | Regression | Existing CLI tests | still pass |

### Frozen enum vocabularies under test

- **ModuleType:** `application`, `library`, `service`, `tool`, `unknown`
- **DependencyScope:** `compile`, `runtime`, `test`, `development`, `optional`, `unknown`
- **EvidenceType:** `build_file`, `lock_file`, `manifest`, `source`, `config`, `other`
- **AnalysisStatus:** `pending`, `partial`, `completed`, `failed`

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

## Out of test scope for TASK-002

- Parsing build files
- Writing `.ai-context`
- Analyzer behavior
- Golden repository fixtures

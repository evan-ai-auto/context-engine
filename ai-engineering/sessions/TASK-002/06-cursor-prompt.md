# 06 — Cursor Prompt (TASK-002 Implementation)

Use this prompt **only after** the Repository Compatibility Inspection / pre-implementation gate.

Architecture is **frozen** (Stage A + Revision-001). Do not make new architecture decisions during implementation.

---

## Prompt

```text
Implement TASK-002 — Core Project Context Domain Model for AI Context Engine.

Architecture is FROZEN (Stage A + Revision-001). Do not invent new ADRs, rename ownership fields, change required/optional semantics, or add enum members.

Canonical sources (must follow exactly):
1. ai-engineering/sessions/TASK-002/architecture-decisions.md
2. ai-engineering/sessions/TASK-002/03-domain-model-contract.md
3. ai-engineering/sessions/TASK-002/02-implementation-plan.md
4. ai-engineering/sessions/TASK-002/04-test-plan.md
5. ai-engineering/tasks/TASK-002.md
6. ai-engineering/tasks/TASK-002-revision-001-domain-contract-finalization.md

Also useful:
- ai-engineering/sessions/TASK-002/01-task-definition.md
- ai-engineering/sessions/TASK-002/05-validation-checklist.md

Frozen rules (non-negotiable):
- Target Python >= 3.10 (already set in pyproject.toml: requires-python, ruff py310, mypy 3.10)
- Pydantic v2 domain models — add a 3.10-compatible pydantic 2.x pin at implementation time only
- Enums ONLY with these members:
  - ModuleType: application|library|service|tool|unknown
  - DependencyScope: compile|runtime|test|development|optional|unknown
  - EvidenceType: build_file|lock_file|manifest|source|config|other
  - AnalysisStatus: pending|partial|completed|failed
- Dependency.ecosystem: required str (NOT an enum)
- Evidence: source_file, source_type (EvidenceType), optional detail
- Technology.evidence / Dependency.evidence: list[Evidence] (default empty); support multiple records
- ProjectContext.project_dependencies owns external deps (NO ProjectContext.dependencies)
- Module.depends_on: list[str]; NO Module.dependencies
- Dependency.declared_by optional
- GenerationMetadata.generated_at: datetime (timezone-aware UTC preferred); NOT str / datetime|str
- GenerationMetadata.analysis_status: AnalysisStatus
- NO DependencyGraph

If you discover a conflict with the frozen contract: STOP and report the conflict. Do not silently redesign.

Out of scope:
- repository scanning / analyzers / .ai-context generation / new CLI
- application/infrastructure/generator packages
- unrelated refactoring

When done:
1. Run pytest, ruff check ., mypy src
2. Fill actual results into ai-engineering/sessions/TASK-002/05-validation-checklist.md
3. Do not mark TASK-002 DONE unless the full lifecycle criteria are met
```

---

## Operator notes

- Prefer small commits: deps → enums/evidence → entities → aggregate → tests
- Canonical contract wins over older prose in historical review notes
- Never restore `decisions.md` as a second ADR source
- Never expand frozen enum member sets during implementation

# 06 — Cursor Prompt (TASK-002)

Use this prompt to implement TASK-002 in Cursor. Do not expand scope.

---

## Prompt

```text
Implement TASK-002 — Core Project Context Domain Model for the AI Context Engine repository.

Read first (in order):
1. ai-engineering/tasks/TASK-002.md
2. ai-engineering/sessions/TASK-002/architecture-decisions.md
3. ai-engineering/sessions/TASK-002/03-domain-model-contract.md
4. ai-engineering/sessions/TASK-002/02-implementation-plan.md
5. ai-engineering/sessions/TASK-002/04-test-plan.md

Locked decisions (must follow):
- Use Pydantic v2 for domain models (pin 3.8-compatible pydantic 2.x in pyproject.toml)
- Closed str Enums for taxonomies; plain str for names/versions/paths/languages/build tools
- Shared Evidence model; Optional[Evidence] on Technology and Dependency only
- Module.depends_on: List[str] (default empty)
- Dependency.declared_by: Optional[str]
- Do NOT implement DependencyGraph

Deliver:
- src/ai_context/domain/ package as specified in TASK-002
- Unit tests covering AC-001–AC-011 scenarios in the test plan
- Keep existing CLI tests passing (AC-012)

Hard out of scope:
- Repository scanning, project detection, Maven/Python parsing
- Technology/dependency analysis logic
- .ai-context generation
- New CLI commands
- application/infrastructure/generator packages
- Unrelated refactoring

When done:
1. Run: pytest && ruff check . && mypy src
2. Fill actual results into ai-engineering/sessions/TASK-002/05-validation-checklist.md
3. Do not mark TASK-002 DONE unless acceptance criteria are met and recorded
```

---

## Notes for the operator

- Prefer small commits: dependency → enums/evidence → entities → aggregate → tests
- If a TASK-002 field conflicts with a locked decision, the **architecture decision wins**
- Update this session folder if implementation discovers a necessary contract clarification; do not silently diverge

# TASK-002 Revision-002 — Serialization Contract Completion

## Objective

Complete the remaining serialization contract coverage identified during the TASK-002 Stage C1 Implementation Review.

This revision exists only to close the following test coverage gaps:

```text
C1-001
Explicit JSON-friendly datetime serialization verification

C1-002
True JSON string round-trip verification
```

This is a test-contract completion revision.

Do not redesign the architecture.

Do not modify the frozen domain contract.

Do not modify production domain models unless a genuine implementation defect is proven.

---

# 1. Current Status

Current TASK-002 status:

```text
Stage A — Architecture Reconciliation
APPROVED

Revision-001 — Domain Contract Finalization
APPROVED

Stage B — Repository Compatibility Inspection
APPROVED

Stage C1 — Core Domain Model Implementation
APPROVED_WITH_MINOR_FIXES
```

Current revision:

```text
TASK-002 Revision-002
Serialization Contract Completion
```

The purpose is to close the remaining serialization test gaps before Stage C2.

---

# 2. Mandatory Reading

Before making changes, read:

```text
ai-engineering/tasks/TASK-002.md

ai-engineering/sessions/TASK-002/03-domain-model-contract.md

ai-engineering/sessions/TASK-002/04-test-plan.md

ai-engineering/sessions/TASK-002/05-validation-checklist.md

src/ai_context/domain/project_context.py

src/ai_context/domain/metadata.py

tests/domain/test_project_context.py
```

Also inspect the current Git state and latest implementation.

Do not rely on assumptions from earlier task stages.

---

# 3. Review Findings To Address

## C1-001 — Explicit JSON-Friendly Datetime Serialization

The test plan requires verification that datetime values serialize correctly in JSON mode.

The implementation currently verifies serialization indirectly, but the contract should explicitly verify that:

```text
datetime
   ↓
model_dump(mode="json")
   ↓
JSON-friendly string
```

The test must explicitly assert that:

```python
dumped["metadata"]["generated_at"]
```

is serialized as:

```python
str
```

The exact timestamp formatting should not be over-constrained unless required by the frozen contract.

Do not introduce custom serialization logic.

Use standard Pydantic v2 behavior.

---

## C1-002 — True JSON String Round Trip

The current tests validate dictionary round-tripping.

Add explicit JSON string round-trip verification:

```text
ProjectContext
      ↓
model_dump_json()
      ↓
JSON string
      ↓
model_validate_json()
      ↓
ProjectContext
```

The restored model must be semantically equivalent to the original model.

Recommended assertion:

```python
assert restored == context
```

---

# 4. Allowed Changes

Primary allowed file:

```text
tests/domain/test_project_context.py
```

Documentation updates are allowed only if required to accurately record implementation progress.

Expected scope:

```text
tests/domain/test_project_context.py
```

Potentially:

```text
ai-engineering/tasks/TASK-002.md
```

only if task status tracking requires an explicit Revision-002 record.

---

# 5. Forbidden Changes

Do not modify:

```text
src/ai_context/domain/
```

unless an actual production defect is discovered and proven necessary.

Do not modify:

```text
pyproject.toml
```

Do not:

```text
add dependencies
change Pydantic version
change domain fields
change enum values
change architecture decisions
change domain contract
modify CLI
modify unrelated tests
refactor the domain package
start Stage C2
perform TASK-002 closeout
```

This revision should remain extremely small.

---

# 6. Required Test: JSON-Friendly Serialization

Add or strengthen a test equivalent to:

```python
def test_project_context_json_mode_serialization() -> None:
    context = create_project_context()

    dumped = context.model_dump(mode="json")

    assert isinstance(
        dumped["metadata"]["generated_at"],
        str,
    )
```

Adapt the fixture/helper style to the existing test file.

Do not duplicate unnecessary test setup.

The purpose is specifically to prove:

```text
datetime
→
JSON-compatible string
```

under Pydantic v2 serialization.

---

# 7. Required Test: JSON String Round Trip

Add a test equivalent to:

```python
def test_project_context_json_round_trip() -> None:
    context = create_project_context()

    json_data = context.model_dump_json()

    restored = ProjectContext.model_validate_json(json_data)

    assert restored == context
```

Adapt naming and construction to existing test conventions.

The purpose is specifically to verify:

```text
Domain Model
      ↓
JSON String
      ↓
Domain Model
```

This must use:

```python
model_dump_json()
```

and:

```python
ProjectContext.model_validate_json()
```

Do not replace this with dictionary serialization.

---

# 8. Test Plan Mapping

Ensure the implementation now explicitly covers:

| Test Plan | Requirement | Expected Coverage |
|---|---|---|
| T-14 | JSON-friendly serialization | Explicit datetime string assertion |
| T-15 | JSON round-trip | `model_dump_json()` → `model_validate_json()` |

Do not introduce new speculative test requirements.

---

# 9. Validation

Run:

```bash
pytest
```

Then:

```bash
ruff check .
```

Then:

```bash
mypy src
```

Expected:

```text
pytest: PASS
ruff: PASS
mypy: PASS
```

Do not modify unrelated code merely to improve validation output.

---

# 10. Scope Verification

Before commit:

```bash
git status
```

Review the diff.

Expected primary change:

```text
tests/domain/test_project_context.py
```

Verify:

```text
[ ] No production code changes
[ ] No dependency changes
[ ] No architecture changes
[ ] No CLI changes
[ ] No unrelated test modifications
[ ] T-14 explicitly covered
[ ] T-15 explicitly covered
```

---

# 11. Required Final Report

Before committing, provide:

## Revision Summary

State what was added.

Expected:

```text
Explicit JSON-friendly datetime serialization verification

True JSON string round-trip verification
```

---

## Test Plan Coverage

```text
T-14: COVERED

T-15: COVERED
```

---

## Files Changed

List all changed files.

---

## Validation Results

```text
pytest:
ruff:
mypy:
```

---

## Architecture Boundary Check

Explicitly confirm:

```text
No production domain model changes

No architecture changes

No dependency changes

No CLI changes
```

---

# 12. Commit

Suggested commit message:

```text
test(domain): complete TASK-002 serialization contract coverage
```

Before commit:

```bash
git diff --check
```

Then commit.

After committing:

```text
STOP.
```

Do not begin Stage C2.

Do not perform TASK-002 final closeout.

The next step after this revision is:

```text
TASK-002 Stage C1 Final Review
```

Wait for repository review.
# MILESTONE-002 Stage F — EXP-M2-003 Invocation & Evidence Capture

## 1. Objective

```text
Exercise the previously untested dependency path:

CANDIDATE-001
    ↓
Validation Requirement Determination
    ↓
Validation Request
    ↓
CANDIDATE-002 Invocation
    ↓
Validation Evidence
    ↓
CANDIDATE-001 Evidence Consumption
    ↓
Revision Disposition
```

Primary evidence gap addressed:

```text
CRITICAL (Stage E)
CANDIDATE-001 → CANDIDATE-002 dependency REQUEST / Invocation / Evidence Consumption
```

```text
Stage F generates evidence only.
No lifecycle promotion.
CONDITIONALLY_VALIDATED unchanged.
```

---

## 2. Experiment Scope

| Field | Value |
|---|---|
| Experiment ID | EXP-M2-003 |
| Kind | Single Asset primary + supporting dependency invocation |
| Primary Subject | CANDIDATE-001 Targeted Engineering Revision |
| Supporting Capability | CANDIDATE-002 Repository Tooling Validation Gate |
| Date | 2026-09-02 |
| Procedure References | `05-candidate-001-…md` v0.1; `06-candidate-002-…md` v0.1 |
| Packaging | None — design docs used as experimental procedures |

Isolation policy (changed vs EXP-M2-001/002):

```text
Experiment Isolation Adaptation that skips CANDIDATE-002 is NOT permitted.
CANDIDATE-002 invocation is IN SCOPE.
```

---

## 3. Authoritative Inputs

```text
MILESTONE-002.md
01 … 09 Stage A–E records
05-candidate-001-targeted-engineering-revision.md
06-candidate-002-repository-tooling-validation-gate.md
pyproject.toml (repository tooling convention)
src/ai_context/cli/main.py
tests/unit/test_cli.py
```

CANDIDATE-002 status at invocation:

```text
DESIGNED / VALIDATION_READY portfolio subject
No packaged SKILL.md in repository
Experimental invocation uses design-doc procedure
(same pattern as CANDIDATE-001 in EXP-M2-001/002)
```

---

## 4. Experiment Selection

### Selected task

```text
CLI Init Placeholder Exit-Code Contract Correction
```

### Why selected

```text
Observed Fact:
  ai-context init prints "not implemented yet" but exits 0.
  Scripts treating exit 0 as success would misinterpret a placeholder.

Why authentic:
  Pre-existing contract smell in production CLI (TASK-001 placeholder).
  Not invented solely for EXP-M2-003.
  Not an artificial defect injection.

Why validation required:
  Changes src/ and tests/ — acceptance requires regression proof.

Why CANDIDATE-002 relevant:
  Post-revision tooling validation is exactly CANDIDATE-002's designed role
  when CANDIDATE-001 REQUESTS validation.
```

### Selection record

| Field | Value |
|---|---|
| Experiment ID | EXP-M2-003 |
| Task | CLI Init Placeholder Exit-Code Contract Correction |
| Primary Subject | CANDIDATE-001 |
| Expected Revision Boundary | `src/ai_context/cli/main.py`; `tests/unit/test_cli.py` |
| Why Validation Is Required | Production CLI + unit test contract change |
| Why CANDIDATE-002 Is Relevant | Designed REQUESTS target for repository tooling gates |
| Expected Evidence | Validation Request Record; Aggregate Validation Evidence; consumption → disposition |

Preferred-order note:

```text
1. Production src/ revision — SELECTED (CLI main.py)
2. Multi-file test revision — also present (test_cli.py companion)
```

---

## 5. Validation Requirement Determination

```text
Validation Requirement Determination: YES
Status: OBSERVED (CANDIDATE-001 procedure step)
```

| Field | Record |
|---|---|
| Why validation is required | `src/` CLI behavior and unit test expectation changed |
| Acceptance criteria requiring validation | pytest CLI suite must pass; ruff/mypy clean on changed surface |
| Expected validation mechanism | Repository Tooling Validation Gate (CANDIDATE-002) |
| Why CANDIDATE-002 is appropriate | Design: CANDIDATE-001 REQUESTS CANDIDATE-002 for tooling execution |

```text
Requirement Determination ≠ Validation Request ≠ Invocation
```

---

## 6. Revision Boundary

```text
Revision Objective:
  Make ai-context init exit non-zero when reporting not-implemented,
  so exit status matches the placeholder message.

In Scope:
  src/ai_context/cli/main.py   — raise typer.Exit(code=1) after message
  tests/unit/test_cli.py       — expect exit_code == 1

Out of Scope / Non-Goals:
  Implementing real init behavior
  New CLI commands
  Domain model changes
  Packaging Skills/Workflows
  Lifecycle promotion
  Unrelated docs/milestone rewrites (except this Stage F record)

Acceptance Criteria:
  init exits 1 with not-implemented message
  CLI unit tests pass
  Full pytest suite passes
  ruff / mypy pass
  No scope expansion beyond two files
```

Safety: no architecture redesign; no fake failure manufactured.

---

## 7. Execution Procedure

CANDIDATE-001 chain applied:

```text
Inspect → Understand → Define Boundary → Plan → Execute →
Determine Validation Requirement → REQUEST CANDIDATE-002 →
CANDIDATE-002 Invocation → Consume Evidence → Report → Stop
```

| Step | Result |
|---|---|
| Inspect | Confirmed exit 0 + "not implemented" mismatch in CLI + test |
| Understand | Exit status should signal incomplete capability |
| Define Boundary | §6 — two files |
| Plan | Add `raise typer.Exit(code=1)`; update test assertion |
| Execute | Both files modified |
| Validation Required | YES |
| REQUEST CANDIDATE-002 | VR-M2-003-001 (§8) |
| Invoke 002 | Design-doc experimental procedure (§9) |
| Consume evidence | Aggregate PASSED → revision RESOLVED (§11) |
| Report | This document |
| Stop | No further files; no packaging; no promotion |

---

## 8. Validation Request Record

```text
Validation Request ID:     VR-M2-003-001
Requester:                 CANDIDATE-001 (EXP-M2-003 experimental invocation)
Requested Capability:      CANDIDATE-002 — Repository Tooling Validation Gate
Reason:                    Post-revision evidence required after src/ + test change
Input / Target Scope:      Repository root; changed paths:
                             src/ai_context/cli/main.py
                             tests/unit/test_cli.py
Required Gate Set:         Unit Tests, Lint, Static Analysis
Expected Output:           Aggregate Validation Evidence (per-gate + aggregate)
Request Time / Sequence:   After Execute; before Report/Stop
```

Distinctions:

```text
Validation Requirement:  YES (determined by CANDIDATE-001)
Validation Request:      VR-M2-003-001 (issued)
Dependency Invocation:   CANDIDATE-002 procedure started after request
```

---

## 9. CANDIDATE-002 Invocation

### Invocation mechanism

```text
Mechanism: Design-document experimental procedure
Reference: 06-candidate-002-repository-tooling-validation-gate.md
Packaged Skill: NOT PRESENT in repository
Simulation: NOT USED — procedure steps followed; gates actually executed
```

### Procedure applied

```text
1. Receive Validation Request (VR-M2-003-001)
2. Inspect Repository Context
3. Resolve Applicable / Executable Gates
4. Prepare Execution Context
5. Execute Gates
6. Collect Evidence
7. Normalize Results
8. Report Aggregate Validation Evidence
9. Stop
```

### Repository inspection (bounded)

```text
Language: Python >= 3.10
Package manager / build: pyproject.toml + hatchling
Test framework: pytest ([tool.pytest.ini_options])
Lint: ruff ([tool.ruff])
Static analysis: mypy ([tool.mypy], files = src)
Dev optional deps: pytest, ruff, mypy present in pyproject.toml
```

### Gate resolution

| Gate Identity | Applicability | Executability | Resolved Command |
|---|---|---|---|
| Unit Tests | Applicable | Executable | `python -m pytest -q` |
| Lint | Applicable | Executable | `python -m ruff check .` |
| Static Analysis | Applicable | Executable | `python -m mypy src` |

Required gates retained; no silent drop; no invented tools.

### Invocation output (per-gate)

| Gate | Result | Evidence Summary |
|---|---|---|
| Unit Tests | PASSED | 65 passed in 0.20s |
| Lint | PASSED | All checks passed |
| Static Analysis | PASSED | Success: no issues found in 13 source files |

### Aggregate Validation Evidence

```text
Aggregate Outcome: PASSED
Reason: All required applicable gates PASSED;
        no ERROR / NOT_EXECUTED / FAILED among required gates.
```

### Invocation classification

```text
Invocation Status: SUCCEEDED
```

Succeeded because:

```text
Request received
Repository inspected
Gates resolved from repository evidence + Required Gate Set
Gates executed
Normalized Aggregate Validation Evidence produced
```

```text
pytest PASS alone ≠ CANDIDATE-002 success.
Classification SUCCEEDED is based on following the 002 procedure
and producing Aggregate Validation Evidence for VR-M2-003-001.
```

Human intervention during 002: Normal Engineering Judgment for mapping abstract gates to repo commands (per design resolution rules). No Human Substitution that replaced 002.

---

## 10. Dependency State Tracking

| Dependency State | Status | Evidence |
|---|---|---|
| DEPENDENCY_IDENTIFIED | **Yes** | Design: 001 REQUESTS 002; Stage E gap |
| DEPENDENCY_REQUESTED | **Yes** | VR-M2-003-001 |
| DEPENDENCY_INVOKED | **Yes** | §9 procedure execution |
| DEPENDENCY_SUCCEEDED | **Yes** | Aggregate PASSED |
| DEPENDENCY_FAILURE_TESTED | **No** | Failure Recovery: NOT TESTED |
| EVIDENCE_CONSUMED_BY_001 | **Yes** | §11 |

---

## 11. Supporting Engineering Validation

Classify separately from dependency invocation.

| Check | Result | Attribution |
|---|---|---|
| pytest | PASS (65) | Executed **as Unit Tests gate under CANDIDATE-002** |
| ruff check . | PASS | Executed **as Lint gate under CANDIDATE-002** |
| mypy src | PASS | Executed **as Static Analysis gate under CANDIDATE-002** |
| git diff --check | PASS | Supporting hygiene (not a Required Gate in VR-M2-003-001) |

```text
Supporting Engineering Validation:
  git diff --check = PASS

Dependency Validation:
  CANDIDATE-002 = SUCCEEDED
  (pytest / ruff / mypy attributed to 002 gate execution, not independent
   “supporting-only” proof of dependency success)
```

Prohibited claim avoided:

```text
× pytest passed therefore CANDIDATE-002 succeeded
```

---

## 12. Evidence Consumption

| Field | Record |
|---|---|
| Evidence Produced | Aggregate Validation Evidence — PASSED (3/3 gates) |
| Evidence Received | Received by CANDIDATE-001 experimental procedure after §9 |
| Evidence Interpreted | Required validation evidence present; no gate ERROR/FAILED |
| Effect on Revision Decision | Engineering disposition → **RESOLVED**; Stop allowed |

```text
Evidence Consumption Classification: CONSUMED
```

```text
CANDIDATE-002 success alone is insufficient.
Consumption is evidenced by 001 using Aggregate PASSED to complete
revision disposition (RESOLVED) rather than BLOCKED/PARTIAL.
```

---

## 13. Boundary Preservation

| Check | Result |
|---|---|
| In Scope | `main.py`, `test_cli.py` |
| Out of Scope | Real init implementation; other packages |
| Actual Modified Files | Exactly the two in-scope files (+ Stage F docs) |
| Actual Modified Behavior | `init` exit code 0 → 1 |

```text
CANDIDATE-002 effect on scope: No Scope Change
```

002 did not expand revision into domain models, packaging, or lifecycle edits.

---

## 14. Human Intervention

| Intervention | Classification |
|---|---|
| Selected CLI exit-code hygiene as authentic task | Normal Engineering Judgment |
| Mapped Required Gate Set → pytest/ruff/mypy via pyproject | Normal Engineering Judgment (002 resolution rules) |
| Did not skip 002 via Experiment Isolation Adaptation | Experiment policy compliance |
| Did not package SKILL.md for 001/002 | Boundary Decision / Non-Goal |

```text
No Human Substitution of CANDIDATE-002 work:
Gates were actually executed; Aggregate Evidence produced.
```

---

## 15. Failure Handling

```text
Failure Recovery: NOT TESTED
```

No natural validation failure occurred. Robustness under FAILED/ERROR gates is not inferred.

---

## 16. Attribution Matrix

| Outcome | Evidence Source | Classification | Confidence |
|---|---|---|---|
| Revision boundary | §6 + git diff (2 files) | DIRECTLY_OBSERVED | High |
| Validation required | §5 after src/test change | DIRECTLY_OBSERVED | High |
| Validation request | VR-M2-003-001 | DIRECTLY_OBSERVED | High |
| CANDIDATE-002 invocation | §9 design-doc procedure + gate runs | DIRECTLY_OBSERVED | High |
| CANDIDATE-002 result | Aggregate PASSED | DIRECTLY_OBSERVED | High |
| Evidence consumption | §11 disposition RESOLVED using evidence | DIRECTLY_OBSERVED | High |
| Final revision decision | RESOLVED | DIRECTLY_OBSERVED | High |
| Supporting git diff --check | Shell output | DIRECTLY_OBSERVED | High |
| Scope preservation | Diff stat = 2 engineering files | DIRECTLY_OBSERVED | High |
| Packaged Skill runtime for 002 | Absent | NOT_ESTABLISHED (N/A — design-doc path used) | High |
| Failure-path composition | Not exercised | NOT_ESTABLISHED | High |

---

## 17. Evidence Quality

```text
Evidence Quality: MODERATE
```

Strong on REQUEST → INVOKE → RESULT → CONSUME observability for the happy path. Limited by: design-doc (not packaged Skill) invocation; single success path; same executor; no failure recovery.

```text
Attribution: DIRECT
```

Request record, invocation steps, gate outputs, and consumption effect are directly recorded — not inferred from pytest alone.

```text
Reproducibility: MEDIUM
```

Reproducible from this record + design docs + git diff. Medium because 002 is not a packaged Skill and gate mapping still requires repository inspection judgment.

---

## 18. Evidence Gap Closure

Stage E critical gap:

```text
CANDIDATE-001 → CANDIDATE-002 dependency REQUEST / invocation /
evidence consumption
```

Progress:

```text
IDENTIFIED        → prior stages
REQUESTED         → VR-M2-003-001          OBSERVED
INVOKED           → §9                     OBSERVED
SUCCEEDED         → Aggregate PASSED       OBSERVED
EVIDENCE CONSUMED → §11 RESOLVED           OBSERVED
```

```text
Dependency Gap Closure: PARTIALLY_CLOSED
```

Why not CLOSED:

```text
- Failure / ERROR path for 001←002 composition NOT TESTED
- Packaged Skill invocation of 002 NOT TESTED (design-doc only)
- Single successful run; no independent replication
```

Why not NOT_CLOSED:

```text
REQUEST → INVOKE → RESULT → CONSUME was sufficiently evidenced
on the successful path — the primary Stage E critical gap for
happy-path dependency orchestration.
```

---

## 19. Experiment Outcome

```text
Experiment Outcome: SUCCESS
```

Criteria check:

| Criterion | Met? |
|---|---|
| Validation requirement legitimately determined | Yes |
| CANDIDATE-002 actually requested | Yes (VR-M2-003-001) |
| CANDIDATE-002 actually invoked | Yes (design-doc procedure) |
| Expected evidence produced | Yes (Aggregate PASSED) |
| CANDIDATE-001 consumed evidence | Yes (CONSUMED → RESOLVED) |
| Attribution sufficiently direct | Yes |
| Revision boundary controlled | Yes |

```text
SUCCESS here is Experiment Outcome for EXP-M2-003 dependency-path
exercise — NOT CANDIDATE-001 unconditional VALIDATED,
NOT packaging authorization, NOT lifecycle promotion.
```

---

## 20. Limitations

```text
- CANDIDATE-002 invoked via design doc, not packaged SKILL.md
- Failure recovery / ERROR aggregate path not tested
- Single executor / single repository / n=1 success path
- git CRLF warnings on Windows working copy (normalized on commit)
- Secondary Stage E gaps (cross-executor, composition with 003/004)
  remain open
```

---

## 21. Resulting Engineering Change

| File | Change |
|---|---|
| `src/ai_context/cli/main.py` | `init` raises `typer.Exit(code=1)` after placeholder message |
| `tests/unit/test_cli.py` | Expect `exit_code == 1` |

```text
Revision Result: RESOLVED
Validation dependency (001 REQUESTS 002): EXERCISED — SUCCEEDED
Lifecycle: CONDITIONALLY_VALIDATED (unchanged)
```

---

## 22. Conclusion

```text
EXP-M2-003 exercised the CANDIDATE-001 → CANDIDATE-002 dependency path
on an authentic production CLI + unit-test revision.

Validation Requirement: YES
Request: VR-M2-003-001
Invocation: SUCCEEDED (design-doc experimental procedure)
Evidence Consumed: CONSUMED
Gap Closure: PARTIALLY_CLOSED (happy path; failure path open)
Experiment Outcome: SUCCESS

Lifecycle Promotion: NOT PERFORMED
Next: later assessment stage may review whether new evidence
      changes CONDITIONALLY_VALIDATED / conditions.
```

---

## End of Stage F Record

```text
Document: 10-stage-f-exp-m2-003-invocation-and-evidence-capture.md
Experiment: EXP-M2-003
Outcome: SUCCESS
Gap Closure: PARTIALLY_CLOSED
Lifecycle Promotion: NONE
```

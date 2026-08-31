# 01 — Historical Process Inventory

## 1. Purpose

This document records the actual engineering activities observed during:

```text
TASK-001 — Project Initialization / Engineering Foundation
TASK-002 — Core Project Context Domain Model
```

```text
This document does not define the future ideal workflow.

This document records historical engineering evidence.

Formal extraction happens in later stages.
```

Classification labels used throughout:

```text
OBSERVED  — directly supported by repository documents or Git history
INFERRED  — reasonable interpretation without explicit documentation
```

---

## 2. Evidence Sources

Only sources that exist in the repository are listed.

| Source Category | Evidence |
|---|---|
| Task | `ai-engineering/tasks/TASK-001.md` |
| Task | `ai-engineering/tasks/TASK-001-CLOSEOUT.md` |
| Task | `ai-engineering/tasks/TASK-001-revision-001-engineering-hygiene.md` |
| Task | `ai-engineering/tasks/TASK-002.md` |
| Task | `ai-engineering/tasks/TASK-002 Stage A — Comprehensive Domain Architecture Reconciliation.md` |
| Task | `ai-engineering/tasks/TASK-002 Stage B — Repository Compatibility Inspection.md` |
| Task | `ai-engineering/tasks/TASK-002 Stage C1 — Core Domain Model Implementation.md` |
| Task | `ai-engineering/tasks/TASK-002 Stage C2 — Final Validation + Closeout.md` |
| Task | `ai-engineering/tasks/TASK-002-revision-001-domain-contract-finalization.md` |
| Task | `ai-engineering/tasks/TASK-002-revision-001-review Feedback Fix.md` |
| Task | `ai-engineering/tasks/TASK-002-revision-002-Serialization Contract Completion.md` |
| Session | `ai-engineering/sessions/TASK-001/` (`record.md`, `execution.md`, `decisions.md`, `validation.md`) |
| Session | `ai-engineering/sessions/TASK-002/` (`01`–`08`, `architecture-decisions.md`) |
| Revision | `ai-engineering/revisions/TASK-001-revision-001-engineering-hygiene.md` |
| Revision | TASK-002 Revision-001 / Revision-001 Feedback Fix / Revision-002 (task briefs above) |
| Review | `ai-engineering/reviews/TASK-001-review.md` |
| Review | `ai-engineering/reviews/TASK-002-architecture-decision-review.md` |
| Learning | `ai-engineering/learnings/TASK-001-learning.md` |
| Learning | `ai-engineering/learnings/runtime-policy-revision-scope.md` |
| Validation | `ai-engineering/sessions/TASK-001/validation.md` |
| Validation | `ai-engineering/sessions/TASK-002/05-validation-checklist.md` |
| Closeout | TASK-001 status `DONE` + closeout brief/session artifacts |
| Closeout | `ai-engineering/sessions/TASK-002/08-closeout.md` |
| Project | `ai-engineering/project/project.md` |
| Repository | Git history on `main` (see §3–§4 commit references) |

Note: `ai-engineering/milestones/` did not exist before Stage A of this milestone. `ai-engineering/extraction/{skills,agents,workflows,rules}/` exist as empty placeholders (`.gitkeep` only).

---

## 3. TASK-001 Historical Process

TASK-001 did **not** follow the multi-stage architecture-freeze pattern later used by TASK-002. Observed chronology from Git and task documents:

| Order | Commit (short) | Summary |
|---|---|---|
| 1 | `580a860` | Initial bootstrap implementation |
| 2 | `f7663e7` | Closeout lifecycle documentation (+ small version-test fix) |
| 3 | `3b5ff4c` | Revision-001 engineering hygiene (docs only) |

### Process inventory

| Step | Activity | Input | Output | Evidence | Classification |
|---|---|---|---|---|---|
| T1-01 | Task definition | Project vision / foundation need | `TASK-001.md` with in/out of scope, structure, DoD | `ai-engineering/tasks/TASK-001.md`; present in `580a860` | OBSERVED |
| T1-02 | Project bootstrap implementation | TASK-001 scope | `pyproject.toml`, src-layout `ai_context`, Typer CLI, tests, README, docs, AI-engineering skeleton | `580a860`; `sessions/TASK-001/execution.md`; `sessions/TASK-001/record.md` | OBSERVED |
| T1-03 | Baseline validation during/after bootstrap | Implemented package | pytest / ruff / mypy / CLI smoke checks | `sessions/TASK-001/record.md`; later re-recorded in `validation.md` | OBSERVED |
| T1-04 | Closeout lifecycle execution | Closeout brief after implementation | Status → `DONE`; `execution.md`, `decisions.md`, `validation.md`; review; learning | `TASK-001-CLOSEOUT.md`; `f7663e7` | OBSERVED |
| T1-05 | Formal review | Closeout artifacts + code | `TASK-001-review.md` with findings (status lag, missing lifecycle docs, version assert) | `ai-engineering/reviews/TASK-001-review.md` | OBSERVED |
| T1-06 | Learning capture | Review + execution experience | `TASK-001-learning.md` (worked / gaps / candidate future skills — candidates only) | `ai-engineering/learnings/TASK-001-learning.md` | OBSERVED |
| T1-07 | Revision-001 engineering hygiene | Post-closeout review of record quality | Portable validation wording; decision/review templates; revision records | `3b5ff4c`; `tasks/TASK-001-revision-001-engineering-hygiene.md`; `revisions/TASK-001-revision-001-engineering-hygiene.md` | OBSERVED |

### Activity notes (TASK-001)

**Task definition**  
Defined bootstrap-only scope. Explicitly excluded scanners, analyzers, and `.ai-context` generation (`TASK-001.md` Out of Scope).

**Implementation**  
Delivered installable hatchling package, Typer CLI (`--help`, `--version`, placeholder `init`), three CliRunner tests, tooling configs. Initially `requires-python >= 3.8.0` (later raised under TASK-002).

**Closeout**  
Closeout was a **separate documented step after implementation**, not embedded in the first commit. Review found task status still `TODO` and incomplete session/review/learning records until closeout (`TASK-001-review.md` P1 findings).

**Revision**  
Post-DONE hygiene revision: documentation/process only; product code unchanged (`revisions/TASK-001-revision-001-engineering-hygiene.md`).

**Not observed for TASK-001**  
No architecture ADR freeze stage, no repository compatibility inspection stage, no domain contract, no Pydantic domain implementation.

---

## 4. TASK-002 Historical Process

TASK-002 used an explicit staged lifecycle with revisions. Approximate chronology from Git:

| Order | Commit | Stage / activity |
|---|---|---|
| 1 | `4ff3000` | Session pack + architecture decision review materials |
| 2 | `6434b92` | Stage A — architecture reconciliation / freeze |
| 3 | `aec173e` | Raise min Python to 3.10 (+ CLI typing modernization) |
| 4 | `e9a8f45` | Revision-001 — domain contract finalization |
| 5 | `cd17bbe` | Revision-001 review feedback fix + learning |
| 6 | `f1b37d1` | Stage B — repository compatibility inspection |
| 7 | `f41cccb` | Stage C1 — core domain model implementation |
| 8 | `b9a21ad` | Revision-002 — serialization contract tests |
| 9 | `b48e2a5` | Rename Revision-002 brief (naming hygiene) |
| 10 | `67342de` | Stage C2 — final validation + closeout |

### 4.1 Session pack and architecture decision review

| Field | Content |
|---|---|
| Why | Need canonical task definition, plan, contract, tests, validation materials before coding |
| Trigger | Start of TASK-002 after foundation DONE |
| Inputs | `project.md`, product architecture/spec docs, early TASK-002 materials |
| Outputs | `sessions/TASK-002/01`–`06`; `reviews/TASK-002-architecture-decision-review.md` |
| Validation | Document review (no production domain code yet) |
| Evidence | `4ff3000`; session files; architecture decision review |
| Classification | OBSERVED |

### 4.2 Stage A — Architecture reconciliation / freeze

| Field | Content |
|---|---|
| Why | Resolve conflicting or incomplete architecture wording before implementation |
| Trigger | Stage A task brief after decision review |
| Inputs | Session pack, architecture review, prior decision drafts |
| Outputs | Frozen `architecture-decisions.md`; reconciled `03-domain-model-contract.md`; `decisions.md` deleted; task status `SPECIFICATION_FROZEN` |
| Validation | Spec consistency (docs); no domain package yet |
| Evidence | `6434b92`; Stage A brief; `architecture-decisions.md` |
| Classification | OBSERVED |

### 4.3 Revision-001 — Domain contract finalization

| Field | Content |
|---|---|
| Why | Close remaining pre-implementation ambiguities (Python floor, enum members, `generated_at` type) |
| Trigger | Remaining soft wording after Stage A freeze |
| Inputs | Frozen ADRs + contract; revision brief |
| Outputs | Python `>=3.10` in `pyproject.toml` / Ruff / mypy; frozen enum tables; `generated_at: datetime`; Revision-001 APPROVED |
| Validation | Spec updates; packaging config change; incidental CLI typing change under Ruff UP (`aec173e`) |
| Evidence | `aec173e`, `e9a8f45`; revision brief; learning `runtime-policy-revision-scope.md` |
| Classification | OBSERVED |

Note (OBSERVED): Raising the Python floor also modernized CLI typing (`Optional[bool]` → `bool | None`). That production touch was later called out as a process lesson: runtime-policy revisions should declare code impact in scope (`learnings/runtime-policy-revision-scope.md`).

### 4.4 Revision-001 review feedback fix

| Field | Content |
|---|---|
| Why | Clarify domain type vs JSON/deserialization input for `generated_at` |
| Trigger | Review feedback on Revision-001 |
| Inputs | Contract, test plan, checklist, feedback brief |
| Outputs | T-13 wording: ISO string input may parse to `datetime`; domain type remains `datetime` (not `datetime \| str`); Revision-001 remains APPROVED |
| Validation | Documentation consistency only |
| Evidence | `cd17bbe`; `TASK-002-revision-001-review Feedback Fix.md` |
| Classification | OBSERVED |

### 4.5 Stage B — Repository compatibility inspection

| Field | Content |
|---|---|
| Why | Verify repository readiness before adding Pydantic / implementing domain |
| Trigger | Stage B brief after Revision-001 APPROVED |
| Inputs | Frozen architecture; `pyproject.toml`; current Python runtime; CLI/tests |
| Outputs | `07-repository-compatibility-inspection.md` — `READY_WITH_WARNINGS` / approved path to Stage C |
| Validation | Runtime/tooling inspection; baselines still pass; Pydantic still absent |
| Evidence | `f1b37d1`; Stage B brief; inspection report |
| Classification | OBSERVED |

### 4.6 Stage C1 — Core domain model implementation

| Field | Content |
|---|---|
| Why | Implement frozen contract as Pydantic v2 models + contract tests |
| Trigger | Stage C1 brief after Stage B approval |
| Inputs | Frozen ADRs, contract, test plan, inspection report |
| Outputs | `src/ai_context/domain/*`; `tests/domain/*`; `pydantic>=2.0,<3.0` dependency |
| Validation | pytest (then 42 passed), ruff, mypy |
| Evidence | `f41cccb`; Stage C1 brief; `05-validation-checklist.md` |
| Classification | OBSERVED |

### 4.7 Revision-002 — Serialization contract completion

| Field | Content |
|---|---|
| Why | Close review findings C1-001 / C1-002 (JSON-friendly dump + true JSON string round-trip) |
| Trigger | Stage C1 review → `APPROVED_WITH_MINOR_FIXES` |
| Inputs | Existing domain models; Revision-002 brief |
| Outputs | Tests T-14 / T-15 in `tests/domain/test_project_context.py` (no production model change) |
| Validation | pytest 44 passed; ruff; mypy |
| Evidence | `b9a21ad`; Revision-002 brief; closeout §6 |
| Classification | OBSERVED |

### 4.8 Stage C2 — Final validation + closeout

| Field | Content |
|---|---|
| Why | Auditability: traceability, boundary check, status DONE, closeout record |
| Trigger | Stage C2 brief after Revision-002 |
| Inputs | Full session pack, domain package, tests, prior validation |
| Outputs | `08-closeout.md`; TASK-002 status `DONE`; T-15 wording sync; checklist finalization |
| Validation | Full suite: pytest 44, ruff, mypy, `git diff --check`; contract/enum/boundary checks |
| Evidence | `67342de`; Stage C2 brief; `08-closeout.md` |
| Classification | OBSERVED |

### TASK-002 step table (condensed)

| Step | Activity | Input | Output | Evidence | Classification |
|---|---|---|---|---|---|
| T2-01 | Task / session planning | Project need for domain model | Session pack `01`–`06` | `4ff3000` | OBSERVED |
| T2-02 | Architecture decision review | Session pack / proposals | Decision review document | `reviews/TASK-002-architecture-decision-review.md` | OBSERVED |
| T2-03 | Architecture reconciliation freeze | Review + drafts | Frozen ADRs + contract | `6434b92` | OBSERVED |
| T2-04 | Contract finalization revision | Soft ambiguities | Enum/Python/`generated_at` freeze | `e9a8f45`, `aec173e` | OBSERVED |
| T2-05 | Spec review feedback fix | Review of Rev-001 | Deserialization clarification | `cd17bbe` | OBSERVED |
| T2-06 | Repository compatibility inspection | Frozen specs | Inspection report | `f1b37d1` | OBSERVED |
| T2-07 | Domain implementation | Frozen contract | Domain package + tests | `f41cccb` | OBSERVED |
| T2-08 | Serialization test revision | C1 findings | T-14 / T-15 tests | `b9a21ad` | OBSERVED |
| T2-09 | Final validation + closeout | Complete delivery | `08-closeout.md`, DONE | `67342de` | OBSERVED |

---

## 5. Cross-Task Engineering Activity Inventory

| Activity Type | TASK-001 | TASK-002 | Evidence Strength |
|---|---|---|---|
| Task planning / definition | Yes (`TASK-001.md`) | Yes (session pack + `TASK-002.md`) | Strong |
| Architecture review / freeze | No formal ADR freeze stage | Yes (review + Stage A + ADRs) | Strong (TASK-002 only) |
| Repository compatibility inspection | Not observed | Yes (Stage B report) | Strong (once) |
| Contract definition | Not applicable (no domain contract) | Yes (`03-domain-model-contract.md`) | Strong (TASK-002) |
| Implementation | Yes (bootstrap) | Yes (domain models) | Strong |
| Test planning | Implicit via required tests in task brief | Explicit `04-test-plan.md` (T-01…T-17) | Stronger on TASK-002 |
| Validation (pytest/ruff/mypy) | Yes | Yes | Strong (both) |
| Code / implementation review | Yes (`TASK-001-review.md`) | Yes (C1 findings via Rev-002; architecture review earlier) | Strong |
| Revision cycles | Yes (Rev-001 hygiene) | Yes (Rev-001, Rev-001 fix, Rev-002) | Strong |
| Learning capture | Yes | Partial (`runtime-policy-revision-scope.md`; closeout lessons) | Moderate–strong |
| Closeout | Yes (dedicated closeout brief + status DONE) | Yes (`08-closeout.md` + DONE) | Strong |

These are activity categories only — not Skills, Agents, or Workflows.

---

## 6. Input / Output Inventory

Descriptive chains only (not formal workflows):

```text
Task brief / scope
        ↓
Task definition / session planning
        ↓
Task document + session artifacts
```

```text
Architecture proposals / conflicting notes
        ↓
Architecture review + reconciliation
        ↓
Frozen ADR + domain contract
```

```text
Frozen contract + packaging policy
        ↓
Repository compatibility inspection
        ↓
Readiness report (go / warnings)
```

```text
Frozen contract + test plan
        ↓
Domain implementation
        ↓
Pydantic models + contract tests
```

```text
Review findings (coverage gaps)
        ↓
Narrow revision
        ↓
Targeted doc or test fixes
```

```text
Implemented + validated deliverable
        ↓
Closeout (status, checklist, lessons, deferred work)
        ↓
Task marked DONE
```

```text
Completed task records
        ↓
Learning note (when process friction observed)
        ↓
Reusable principle text (still not a Skill)
```

---

## 7. Decision Points

### D-001 — Whether TASK-001 was ready for DONE

| Field | Content |
|---|---|
| Decision Trigger | Implementation existed while status remained `TODO`; lifecycle docs incomplete |
| Decision Made | Execute closeout: sync status, create session/review/learning, fix version assert |
| Evidence | `TASK-001-review.md` P1; `f7663e7`; `TASK-001.md` Status DONE |
| Result | TASK-001 marked DONE with auditable closeout |

### D-002 — Whether architecture must freeze before TASK-002 coding

| Field | Content |
|---|---|
| Decision Trigger | Need stable domain vocabulary before implementation |
| Decision Made | Stage A freeze; delete parallel `decisions.md`; require Revision-001 for remaining soft points |
| Evidence | `6434b92`; `architecture-decisions.md` Status FROZEN; Stage A brief |
| Result | Spec frozen before Stage B/C |

### D-003 — Whether repository compatibility inspection precedes coding

| Field | Content |
|---|---|
| Decision Trigger | Planned dependency (Pydantic) and Python floor change |
| Decision Made | Stage B inspection required; Pydantic deferred until Stage C |
| Evidence | Stage B brief; `07-repository-compatibility-inspection.md` |
| Result | `READY_WITH_WARNINGS`; Stage C proceeded |

### D-004 — Whether to revise after Stage C1 review instead of closing

| Field | Content |
|---|---|
| Decision Trigger | C1-001 / C1-002 serialization coverage gaps |
| Decision Made | Revision-002 tests-only; then Stage C2 closeout |
| Evidence | Revision-002 brief; `b9a21ad`; `08-closeout.md` §6 |
| Result | Findings RESOLVED; TASK-002 DONE |

### D-005 — Runtime policy revision scope discipline

| Field | Content |
|---|---|
| Decision Trigger | Python 3.10 raise caused incidental CLI typing modernization |
| Decision Made | Record learning: declare production-code impact when changing runtime policy |
| Evidence | `aec173e`; `learnings/runtime-policy-revision-scope.md` |
| Result | Process principle captured; no architecture redesign |

---

## 8. Revision Inventory

### TASK-001 Revision-001 — Engineering Hygiene

| Field | Content |
|---|---|
| Trigger | Post-final-review consistency improvements |
| Finding | Machine-specific paths / missing reusable templates in engineering records |
| Scope | Documentation / process records only |
| Change Type | Non-functional hygiene |
| Validation | Doc review; no product source changes |
| Result | DONE; TASK-001 remains DONE |
| Evidence | `3b5ff4c`; `revisions/TASK-001-revision-001-engineering-hygiene.md` |

### TASK-002 Revision-001 — Domain Contract Finalization

| Field | Content |
|---|---|
| Trigger | Soft Python wording; open enum members; ambiguous `generated_at` typing |
| Finding | Implementation-time ambiguity remaining after Stage A |
| Scope | Spec + packaging policy (Python >= 3.10); no domain package yet |
| Change Type | Contract / policy freeze |
| Validation | Spec consistency; tooling config update |
| Result | APPROVED |
| Evidence | `e9a8f45`, `aec173e`; revision brief |

### TASK-002 Revision-001 — Review Feedback Fix

| Field | Content |
|---|---|
| Trigger | Review of Revision-001 serialization/test semantics |
| Finding | Need clearer ISO-string-as-input vs domain `datetime` distinction |
| Scope | Contract/test-plan wording; learning note |
| Change Type | Clarification (docs) |
| Validation | Documentation consistency |
| Result | Revision-001 remains APPROVED |
| Evidence | `cd17bbe`; feedback-fix brief |

### TASK-002 Revision-002 — Serialization Contract Completion

| Field | Content |
|---|---|
| Trigger | Stage C1 review findings C1-001, C1-002 |
| Finding | Missing explicit JSON-mode datetime string assert; missing `dump_json`/`validate_json` equality round-trip |
| Scope | Tests only (unless production defect proven — none) |
| Change Type | Test-contract completion |
| Validation | pytest 44; ruff; mypy |
| Result | Findings RESOLVED; proceeded to Stage C2 |
| Evidence | `b9a21ad`; Revision-002 brief; closeout §6 |

---

## 9. Validation Inventory

| Validation Target | Validation Method | Expected Result | Observed Result | Evidence |
|---|---|---|---|---|
| TASK-001 CLI + tooling | `pytest`, `ruff check .`, `mypy src`, CLI help/version/init | Pass | Pass (3 tests at closeout on Python 3.8.0) | `sessions/TASK-001/validation.md` |
| TASK-001 packaging | Editable install / entry point | `ai-context` available | Recorded PASS | `validation.md` |
| TASK-002 packaging policy | Inspect `requires-python`, Ruff, mypy | `>=3.10` / py310 | PASS | `07-repository-compatibility-inspection.md` |
| TASK-002 domain contract | Contract ↔ implementation ↔ tests | All models present | PASS (8/8) | `08-closeout.md` §4 |
| TASK-002 enums | Exact frozen members | No missing/extra | PASS | `tests/domain/test_enums.py`; closeout |
| TASK-002 serialization T-14 | `model_dump(mode="json")` | `generated_at` is `str` | PASS | `test_project_context.py`; closeout §5 |
| TASK-002 serialization T-15 | `model_dump_json` → `model_validate_json` | `restored == context` | PASS | same |
| TASK-002 full suite (C2) | `pytest`, `ruff`, `mypy`, `git diff --check` | All pass | 44 passed; ruff/mypy/`diff --check` PASS | `08-closeout.md` §5 |
| Architecture boundary (C2) | Checklist against `src/` | No analyzer/scanner/CLI feature creep | ALL PASS | `08-closeout.md` §7 |
| CLI regression under TASK-002 | Full pytest includes `tests/unit/test_cli.py` | Still pass | PASS | closeout §5 |

---

## 10. Closeout Inventory

### TASK-001

| Element | Observed behavior |
|---|---|
| Final validation | Commands recorded in `sessions/TASK-001/validation.md` |
| Status update | `TASK-001.md` → `DONE` with Completion section |
| Closeout documentation | `TASK-001-CLOSEOUT.md` + session/review/learning set |
| Deferred work | Repository analysis, `.ai-context` generation, analyzers (stated out of scope) |
| Lessons learned | `learnings/TASK-001-learning.md` |

### TASK-002

| Element | Observed behavior |
|---|---|
| Final validation | Stage C2 suite + contract/enum/boundary checks |
| Status update | `TASK-002.md` → `DONE`; stages marked APPROVED/COMPLETED |
| Closeout documentation | `sessions/TASK-002/08-closeout.md` |
| Deferred work | Analyzer, scanner, technology/dependency extraction, context generation, dependency graph |
| Lessons learned | Closeout §9 + prior `runtime-policy-revision-scope.md` |

---

## 11. Observed Engineering Activities Summary

```text
OBSERVED-001
Task definition with explicit in/out of scope
Tasks: TASK-001, TASK-002
Evidence: ai-engineering/tasks/TASK-001.md; ai-engineering/tasks/TASK-002.md; sessions/TASK-002/01-task-definition.md

OBSERVED-002
Bootstrap / foundation implementation
Tasks: TASK-001
Evidence: commit 580a860; sessions/TASK-001/execution.md

OBSERVED-003
Tooling validation (pytest / ruff / mypy)
Tasks: TASK-001, TASK-002
Evidence: sessions/TASK-001/validation.md; sessions/TASK-002/05-validation-checklist.md; 08-closeout.md

OBSERVED-004
Lifecycle closeout after delivery
Tasks: TASK-001, TASK-002
Evidence: TASK-001-CLOSEOUT.md; sessions/TASK-002/08-closeout.md

OBSERVED-005
Formal review with findings and dispositions
Tasks: TASK-001 (full review); TASK-002 (architecture review + C1 findings via Rev-002)
Evidence: reviews/TASK-001-review.md; reviews/TASK-002-architecture-decision-review.md; 08-closeout.md §6

OBSERVED-006
Learning capture after friction or closeout
Tasks: TASK-001, TASK-002
Evidence: learnings/TASK-001-learning.md; learnings/runtime-policy-revision-scope.md; 08-closeout.md §9

OBSERVED-007
Post-completion or mid-lifecycle revision cycles
Tasks: TASK-001 Rev-001; TASK-002 Rev-001 / feedback fix / Rev-002
Evidence: revisions/ and tasks/*revision* documents; commits 3b5ff4c, e9a8f45, cd17bbe, b9a21ad

OBSERVED-008
Architecture decision freeze before implementation
Tasks: TASK-002
Evidence: architecture-decisions.md; Stage A commit 6434b92

OBSERVED-009
Domain contract definition and finalization
Tasks: TASK-002
Evidence: 03-domain-model-contract.md; Revision-001 briefs

OBSERVED-010
Repository compatibility inspection before feature coding
Tasks: TASK-002
Evidence: 07-repository-compatibility-inspection.md; Stage B commit f1b37d1

OBSERVED-011
Contract-first domain implementation with dedicated test plan
Tasks: TASK-002
Evidence: src/ai_context/domain/; tests/domain/; 04-test-plan.md; commit f41cccb

OBSERVED-012
Narrow revision to close review findings without redesign
Tasks: TASK-002 Revision-002
Evidence: Revision-002 brief; b9a21ad; findings C1-001/C1-002 RESOLVED
```

These are observations. They are not Skills, Agents, or Workflows.

---

## 12. Extraction Readiness Notes

```text
Revision process
Observed multiple times (TASK-001 ×1 hygiene; TASK-002 ×3 related cycles)
Strong evidence
Potential future extraction candidate

Lifecycle closeout
Observed twice (TASK-001, TASK-002)
Strong evidence
Potential future extraction candidate

Tooling validation gate (pytest / ruff / mypy)
Observed repeatedly
Strong evidence
Potential future extraction candidate

Task definition with hard out-of-scope boundaries
Observed twice
Strong evidence
Potential future extraction candidate

Architecture freeze before implementation
Observed once (TASK-002)
Strong evidence
Needs reuse validation on a later architecture-heavy task

Repository compatibility inspection
Observed once (TASK-002 Stage B)
Strong implementation evidence
Needs reuse validation

Domain contract + test-plan traceability
Observed once (TASK-002)
Strong evidence
Needs reuse validation outside domain-model tasks

Learning capture
Observed on both tasks (forms differ)
Moderate–strong evidence
Potential future extraction candidate

Formal Skill / Agent / Workflow packages
Not created
extraction/* remains placeholder-only
Correct for Stage A
```

End of Stage A inventory. No candidates designed here.

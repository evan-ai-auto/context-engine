# MILESTONE-002 Stage G — EXP-M2-003 Evidence Assessment & Candidate-001 Lifecycle Reassessment

## 1. Objective

```text
Assess EXP-M2-001 / EXP-M2-002 / EXP-M2-003 evidence,
with focus on EXP-M2-003 dependency-composition evidence,
and determine whether CANDIDATE-001 lifecycle / Stage E disposition
should change.
```

```text
Assessment-only stage.
No new experiment.
No packaging.
No historical rewrite.
```

---

## 2. Assessment Scope

| In scope | Out of scope |
|---|---|
| Independent assessment of EXP-M2-003 chain | Re-running EXP-M2-003 |
| Cross-experiment comparison (001–003) | Production code changes |
| Lifecycle reassessment of CANDIDATE-001 | Packaging SKILL.md |
| Packaging readiness (assessment only) | CANDIDATE-003 / 004 validation |
| Independent note on CANDIDATE-002 | Orchestration / runtime implementation |
| Updated conditions / single next step | Inventing new lifecycle states |

Current authoritative state entering Stage G:

```text
CANDIDATE-001 lifecycle: CONDITIONALLY_VALIDATED
Stage E disposition:     PROMOTE_WITH_CONDITIONS
EXP-M2-003 outcome:      SUCCESS
Dependency gap closure:  PARTIALLY_CLOSED (Stage F claim — reassessed below)
Failure recovery:        NOT TESTED
Packaged Skill path:     NOT TESTED
```

---

## 3. Authoritative Evidence

```text
MILESTONE-002.md
01 … 10 Stage A–F records
09-stage-e-evidence-sufficiency-and-asset-disposition.md
10-stage-f-exp-m2-003-invocation-and-evidence-capture.md
05-candidate-001-targeted-engineering-revision.md
06-candidate-002-repository-tooling-validation-gate.md
git commit b683cd6 (CLI exit-code + test + Stage F record)
```

Engineering change verified in git:

```text
src/ai_context/cli/main.py  — raise typer.Exit(code=1)
tests/unit/test_cli.py      — expect exit_code == 1
```

---

## 4. EXP-M2-003 Dependency Chain Assessment

### Q1 — Did EXP-M2-003 close the Stage E critical dependency gap?

Independent classification (not a copy of Stage F):

| State | Stage G Classification | Basis |
|---|---|---|
| DEPENDENCY_IDENTIFIED | OBSERVED | Design REQUESTS relationship; Stage E gap register |
| DEPENDENCY_REQUESTED | OBSERVED | VR-M2-003-001 recorded before invocation with scope/gates |
| DEPENDENCY_INVOKED | OBSERVED | Design-doc procedure steps + gate resolution table + executed commands |
| DEPENDENCY_SUCCEEDED | OBSERVED | Aggregate PASSED with per-gate PASSED records |
| EVIDENCE_PRODUCED | OBSERVED | Aggregate Validation Evidence in Stage F §9 |
| EVIDENCE_CONSUMED_BY_001 | OBSERVED | Disposition RESOLVED after Aggregate PASSED (F §12) |
| DEPENDENCY_FAILURE_TESTED | NOT_ESTABLISHED | No FAILED/ERROR path |

```text
Critical Gap Closure (Stage G): PARTIALLY_CLOSED

Happy-path REQUEST → INVOKE → RESULT → CONSUME: OBSERVED
Failure-path / packaged-Skill / independent replication: NOT_ESTABLISHED
```

Agreement with Stage F PARTIALLY_CLOSED: **Confirmed**.

```text
EXP-M2-003 SUCCESS ≠ Critical gap CLOSED
Happy-Path Dependency Composition ≠ Failure-Path Composition
Design-Document Procedure Invocation ≠ Packaged Skill Runtime Invocation
```

---

## 5. Evidence Attribution Assessment

### Q2 — How strong is the dependency evidence?

### Request evidence

```text
VR-M2-003-001: DIRECTLY_OBSERVED
```

The request record exists in the Stage F experiment record with requester, capability, scope, Required Gate Set, and sequence position. It is not a post-hoc one-line claim without structure. Confidence: **High**.

Caveat: request was produced within the same experimental framing that executed the revision — not an independently timestamped external ticket system. Still sufficient as experimental Direct Observation.

### Invocation evidence

```text
CANDIDATE-002 procedure execution: DIRECTLY_OBSERVED (design-doc path)
```

Supporting details beyond “we ran pytest”:

```text
Repository inspection recorded (pyproject tooling signals)
Gate resolution table (Applicability / Executability / Command)
Per-gate results with evidence summaries
Aggregate outcome rule applied (all required gates PASSED)
Explicit statement that pytest alone ≠ 002 success
```

```text
pytest / ruff / mypy PASS ≠ proof of CANDIDATE-002 by themselves.
They support 002 invocation only when embedded in the recorded
inspect → resolve → execute → normalize → report procedure.
```

Packaged Skill runtime invocation: **NOT_ESTABLISHED**.

### Result evidence

Gate results claimed in Stage F are consistent with repository capability and with post-commit green suite on `main` after `b683cd6`. Stage G hygiene re-run (artifact check only) is not new asset-validation evidence.

### Consumption evidence

Required chain:

```text
Evidence Produced     → Aggregate PASSED          OBSERVED
Evidence Received     → recorded by 001 procedure OBSERVED
Evidence Interpreted  → no ERROR/FAILED; proceed  OBSERVED
Engineering Decision  → RESOLVED / Stop           OBSERVED
```

```text
Consumption: DIRECTLY_OBSERVED (experimental record)
Attribution strength: DIRECT for happy path
Confidence: High for observed chain; Moderate for generality
```

---

## 6. Evidence Consumption Assessment

### Q3 — Does Stage F demonstrate composability?

Per-link classification:

| Behavior | Classification |
|---|---|
| Validation Requirement Determination | OBSERVED |
| Validation Request | OBSERVED |
| Dependency Invocation | OBSERVED (design-doc) |
| Evidence Reception | OBSERVED |
| Evidence Interpretation | OBSERVED |
| Evidence Consumption | OBSERVED |
| Revision Disposition | OBSERVED |

```text
Composability demonstrated (happy path, design-doc procedures):
CANDIDATE-001 can determine validation is required,
request CANDIDATE-002, and consume Aggregate Validation Evidence
before completing revision disposition.

NOT demonstrated:
Failure / ERROR aggregate handling
Packaged Skill composition
Cross-executor / cross-repo composition
001 → 002 → 003/004 multi-asset chains
```

---

## 7. Cross-Experiment Comparison

| Behavior | M2-001 | M2-002 | M2-003 | Overall |
|---|---|---|---|---|
| Task inspection | Yes | Yes | Yes | **REPEATED** |
| Revision boundary definition | Yes (external lock) | Yes (discovery) | Yes (2-file bound) | **REPEATED** (mode CONTEXT-DEPENDENT) |
| Engineering execution | Docs edit | Test adds | CLI src + test | **REPEATED** |
| Validation requirement determination | Partial / implicit | Explicit YES | Explicit YES | **PARTIALLY_REPEATED** → stronger after 002/003 |
| Validation delegation (REQUEST 002) | Skipped (isolation) | Skipped (isolation) | Requested + invoked | **SINGLE-EXPERIMENT** (003) |
| Evidence consumption (from 002) | N/A | N/A | Consumed Aggregate PASSED | **SINGLE-EXPERIMENT** (003) |
| Revision disposition | RESOLVED | RESOLVED | RESOLVED | **REPEATED** |
| Boundary preservation | Yes | Yes | Yes | **REPEATED** |

```text
Core revision orchestration: REPEATED across three experiments.
Dependency composition: SINGLE-EXPERIMENT (EXP-M2-003 happy path only).
```

Task diversity after M2-003:

```text
Docs hygiene | Domain test contracts | Production CLI + unit test
```

Production `src/` coverage: **now present** (CLI) — reduces Stage E “no production revision” gap for breadth, not for failure-path claims.

---

## 8. Updated Evidence Matrix

| Dimension | Assessment | Notes |
|---|---|---|
| Evidence Breadth | **MODERATE → MODERATE-HIGH** | n=3; docs + tests + CLI src; still one repo/executor |
| Behavioral Repeatability | **REPEATED** (core chain) | Dependency composition only once |
| Task Diversity | **MODERATE** | Three task shapes; no architecture redesign; no failure scenario |
| Attribution Strength | **SUPPORTED / DIRECT (happy-path 002)** | Alternatives (executor skill, experiment framing) persist |
| Dependency Coverage | **PARTIAL** | Happy path OBSERVED; failure NOT_ESTABLISHED |
| Candidate Validation | **PARTIALLY_VALIDATED** | Core orchestration + happy-path composition; not full designed surface |
| Failure Coverage | **LIMITED / NOT_ESTABLISHED** | Still no forced FAILED/ERROR recovery |
| Human Intervention | Documented; judgment required | Gate mapping / task selection = Normal Engineering Judgment |
| Reproducibility | **MEDIUM** | Records + git sufficient; design-doc procedures; same-operator bias |
| Evidence Quality | **MODERATE** | Strong happy-path observability; material open gaps remain |

```text
Overall evidence pattern: MIXED EVIDENCE (unchanged category)
Quality improved on dependency dimension vs Stage E baseline,
but not upgraded to unconditional validation quality.
```

---

## 9. Remaining Evidence Gaps

### Q4 — What remains unvalidated?

| Gap | Status | Required for current CONDITIONALLY_VALIDATED? | Required before packaging? | Classification |
|---|---|---|---|---|
| 1. Failure / ERROR path | NOT_ESTABLISHED | No (conditional use may proceed with warning) | **Yes** (before VALIDATED / unrestricted package claims) | **Required before packaging / VALIDATED** |
| 2. Dependency failure handling | NOT_ESTABLISHED | No | **Yes** | Same as (1) |
| 3. Packaged Skill invocation | NOT_ESTABLISHED | No for design-doc conditional use | **Yes** | Required before packaging |
| 4. Independent replication | NOT_ESTABLISHED | No | Useful | Useful future evidence |
| 5. Different repository/task context | NOT_ESTABLISHED | No | Useful | Useful future evidence |
| 6. Multi-asset composition beyond 001→002 | NOT_ESTABLISHED | No | Not necessary for 001 alone | Useful / portfolio later |
| 7. Human intervention dependence | OBSERVED ongoing | Accept under conditions | Soft constraint | Condition retained |

```text
Do not treat all seven as equal blockers.
Highest-value remaining gap for lifecycle upgrade: Failure / ERROR composition path.
Highest-value remaining gap for packaging: Packaged Skill invocation + failure path.
```

---

## 10. CANDIDATE-001 Lifecycle Assessment

### Decision standard application

| Criterion for VALIDATED | Met? |
|---|---|
| Core behavior sufficiently demonstrated | **Yes** (orchestration repeated) |
| Evidence attributable | **Yes** (with residual alternative explanations) |
| Repeatable enough for intended scope | **Partial** — core yes; dependency once |
| Critical dependency behavior sufficiently demonstrated | **Partial** — happy path only |
| Remaining gaps do not undermine lifecycle claim | **No for unconditional VALIDATED** — failure path undermines robustness claim |

```text
VALIDATED: NOT JUSTIFIED
```

```text
CANDIDATE-001 Lifecycle: CONDITIONALLY_VALIDATED (RETAINED)
```

Rationale:

```text
EXP-M2-003 SUCCESS strengthens conditional confidence by observing
happy-path 001 → 002 composition, but Stage G decision standard
explicitly rejects promoting on happy-path dependency success alone.
Failure-path composition and packaged invocation remain open and
material to an unconditional VALIDATED claim.
```

### Stage E disposition

```text
Stage E Disposition: PROMOTE_WITH_CONDITIONS (RETAINED)
```

Disposition category unchanged. **Conditions updated** in §13 to reflect EXP-M2-003 evidence (Condition 3 revised).

---

## 11. CANDIDATE-001 Packaging Readiness

```text
Packaging Readiness: NOT_READY
```

Reasons:

```text
- Lifecycle remains CONDITIONALLY_VALIDATED, not VALIDATED
- No packaged Skill experiment of the procedure itself
- Failure-path composition untested
- Stage A / Stage E rules: packaging is a later authorized stage
- Design-doc experimental success ≠ packaging authorization
```

```text
NOT READY_WITH_EXPLICIT_CONDITIONS:
Conditions could describe controlled design-doc reuse (already covered by
PROMOTE_WITH_CONDITIONS). Packaging as SKILL.md requires stronger evidence.
```

---

## 12. CANDIDATE-002 Independent Assessment

```text
CANDIDATE-002 was a supporting capability in EXP-M2-003.
Composition evidence ≠ independent asset validation of CANDIDATE-002.
```

| Question | Assessment |
|---|---|
| Was 002 design-doc procedure executable in this repo? | Yes (OBSERVED once) |
| Is 002 independently VALIDATED? | **No** |
| Lifecycle of 002 | Remains **VALIDATION_READY** |
| Packaging readiness of 002 | **NOT_READY** |

```text
001 → 002 interaction success does not validate 002 as a standalone
reusable asset across repositories, failure modes, or callers other than 001.
```

---

## 13. Conditions / Follow-Up Requirements

### Updated conditions for CONDITIONALLY_VALIDATED / PROMOTE_WITH_CONDITIONS

---

#### Condition A — Repository-scoped targeted revisions only

```text
Condition: Use for repository-scoped targeted engineering revisions only.
Reason: Evidence spans docs, domain tests, and CLI hygiene — not general agents.
Evidence needed: None additional for this condition.
Why it matters: Prevents over-claiming generality.
```

---

#### Condition B — Explicit revision boundary before modification

```text
Condition: Define Revision Boundary before edits.
Reason: Repeated positive association across M2-001/002/003.
Evidence needed: None additional.
Why it matters: Scope discipline signal.
```

---

#### Condition C — Happy-path dependency may be claimed; failure-path may not

```text
Condition:
  May claim that happy-path CANDIDATE-001 → CANDIDATE-002 REQUEST / invoke /
  consume was experimentally observed (design-doc procedures, EXP-M2-003).
  Must NOT claim failure-path composition, packaged Skill composition,
  or unconditional dependency validation.

Reason:
  EXP-M2-003 OBSERVED happy path; FAILURE_TESTED = NOT_ESTABLISHED.

Evidence needed for upgrade:
  Failure/ERROR aggregate path experiment; optionally packaged Skill run.

Why it matters:
  Replaces Stage E Condition 3 (“dependency not claimed at all”) with a
  calibrated claim boundary after PARTIALLY_CLOSED gap closure.
```

---

#### Condition D — Human review of multi-file exclusions

```text
Condition: Boundary exclusions require accountable human review.
Reason: Judgment dependence persists across experiments.
Why it matters: Autonomy not established.
```

---

#### Condition E — No packaging / IMPLEMENTATION_READY from this state alone

```text
Condition: CONDITIONALLY_VALIDATED does not authorize SKILL packaging
           or IMPLEMENTATION_READY.
Reason: Packaging readiness = NOT_READY; VALIDATED ≠ IMPLEMENTATION_READY.
Why it matters: Prevents premature packaging.
```

---

#### Condition F — Prefer light ceremony outside formal experiments

```text
Condition: Prefer core procedure without full milestone ceremony in routine use.
Reason: Repeated overhead observation (Stages B3/C3/D).
Why it matters: Separates asset cost from experiment cost.
```

---

### Single prioritized next step

```text
Next Recommended Step:
  EXP-M2-004 (proposed) — Failure / ERROR path composition test for
  CANDIDATE-001 ← CANDIDATE-002 Aggregate FAILED or ERROR evidence,
  verifying 001 consumption behavior under non-PASSED validation results.

Why this step first:
  Highest-value remaining gap blocking unconditional VALIDATED.
  Smaller than packaging + multi-repo + full portfolio composition.
```

```text
Stage G does NOT execute EXP-M2-004.
```

---

## 14. Decision

```text
CANDIDATE-001 Lifecycle:
CONDITIONALLY_VALIDATED (RETAINED)

Stage E Disposition:
PROMOTE_WITH_CONDITIONS (RETAINED; Condition 3 recalibrated as Condition C)

Stage F Impact:
Happy-path dependency composition OBSERVED; critical gap PARTIALLY_CLOSED;
confidence in conditional reuse increased; unconditional VALIDATED not earned.

Dependency Composition:
HAPPY_PATH_OBSERVED / FAILURE_PATH_NOT_ESTABLISHED / PARTIALLY_CLOSED

Failure Path:
NOT_ESTABLISHED

Packaging Readiness:
NOT_READY

Next Recommended Step:
EXP-M2-004 failure/ERROR-path composition experiment (define/authorize later)
```

---

## 15. Historical Integrity Statement

```text
Stage G does not rewrite:
  EXP-M2-001 / EXP-M2-002 / EXP-M2-003 factual outcomes
  Stage E conclusions as if Stage F already existed at that time

Stage E recorded dependency path as untested — historically correct.
Stage F generated new evidence.
Stage G interprets the combined evidence and updates forward-looking
conditions without altering prior stage documents' substance.
```

---

## 16. Conclusion

```text
Assessment Result:
  Retain CONDITIONALLY_VALIDATED + PROMOTE_WITH_CONDITIONS
  with recalibrated dependency claim boundary after EXP-M2-003.

EXP-M2-003 Dependency Composition:
  Happy path OBSERVED and attributable (design-doc procedures).
  Gap PARTIALLY_CLOSED — confirmed independently.

CANDIDATE-001 is not VALIDATED.
CANDIDATE-001 is not packaging-ready.
CANDIDATE-002 is not independently validated by composition evidence.

Most valuable next step:
  Failure/ERROR-path composition experiment (EXP-M2-004 proposed).
```

---

## End of Stage G Record

```text
Document: 11-stage-g-exp-m2-003-evidence-assessment-and-lifecycle-reassessment.md
Lifecycle: CONDITIONALLY_VALIDATED (retained)
Disposition: PROMOTE_WITH_CONDITIONS (retained, conditions updated)
Packaging: NOT_READY
```

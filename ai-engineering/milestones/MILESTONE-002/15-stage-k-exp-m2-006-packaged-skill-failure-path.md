# MILESTONE-002 Stage K — EXP-M2-006 Packaged Skill Failure-Path Composition Test

## 1. Experiment Objective

```text
Determine whether the minimal packaged CANDIDATE-001 Skill runtime
preserves the EXP-M2-004 failure-path composition contract:

Aggregate Validation Evidence = FAILED
        ↓
Evidence consumed by packaged CANDIDATE-001
        ↓
Disposition = BLOCKED
        ↓
RESOLVED must NOT occur
```

```text
Experiment ID: EXP-M2-006
Sole question: Does packaged Skill runtime preserve evidence-gated
               failure disposition?
```

---

## 2. Authoritative Context

```text
MILESTONE-002.md
12-stage-h-exp-m2-004-failure-error-path-composition.md
13-stage-i-evidence-consolidation-and-packaging-readiness-review.md
14-stage-j-exp-m2-005-packaged-skill-runtime-experiment.md
10-stage-f-exp-m2-003-invocation-and-evidence-capture.md
packaged-runtime/candidate-001-targeted-engineering-revision/SKILL.md
Baseline HEAD before Stage K product edit: 0dfa084
```

Prior evidence:

```text
EXP-M2-004: design-doc FAILED → BLOCKED (+ recovery)
EXP-M2-005: packaged Skill PASSED → RESOLVED (happy path only)
```

---

## 3. Primary Subject

```text
CANDIDATE-001 — Targeted Engineering Revision
```

---

## 4. Supporting Capability

```text
CANDIDATE-002 — Repository Tooling Validation Gate
Supporting only — not independently validated by this experiment
```

---

## 5. Packaged Skill Execution Object

```text
Path:
  ai-engineering/milestones/MILESTONE-002/packaged-runtime/
    candidate-001-targeted-engineering-revision/SKILL.md

Authority:
  This SKILL.md was the execution object for EXP-M2-006.
  Procedure was NOT driven from the M1 design document as primary source.

Relevant packaged rules applied:
  Primary Target Only
  Validation Requirement ≠ Validation Request
  Aggregate PASSED → may RESOLVED
  Aggregate FAILED → must NOT RESOLVED → BLOCKED
```

---

## 6. Experimental Task

```text
Task: CLI init docstring exit-status alignment
Type: Production CLI docstring hygiene
Primary Target Only: src/ai_context/cli/main.py
Change: docstring mentions exits with status 1 (message already did)
Validation Requirement: YES (src/ change)
Related excluded: tests/unit/test_cli.py (not part of revision boundary;
                  used only for controlled failure injection)
```

Why suitable:

```text
- Authentic small src revision after Stage J message clarification
- Forces Validation Required = YES
- Allows same gate-failure mode as EXP-M2-004 (assertion mismatch)
- Distinct from copying Stage H task verbatim
```

---

## 7. Failure Injection Design

```text
Mode: Validation Gate Failure (assertion mismatch)
File: tests/unit/test_cli.py :: test_cli_init_placeholder
Temporary change: assert result.exit_code == 0  (CLI still exits 1)
Marker: EXP-M2-006 CONTROLLED FAILURE (temporary)
Expected: Unit Tests FAILED; Lint/mypy PASSED; Aggregate FAILED
NOT: tool ERROR / dependency unavailable / malformed evidence
Reversible: YES — restore assertion after BLOCKED observation
```

```text
Classification of injection: Experiment Setup / Controlled Intervention
≠ Human Substitution of Skill disposition logic
```

---

## 8. Execution Procedure

```text
1. Load packaged SKILL.md
2. Invoke packaged Skill as execution object
3. Inspect → Understand → Define Boundary (Primary Target Only) → Plan
4. Execute docstring revision on main.py
5. Determine Validation Requirement = YES
6. REQUEST CANDIDATE-002 (VR-M2-006-001)
7. Introduce controlled validation failure (experiment setup)
8. Invoke CANDIDATE-002 gates
9. Observe Aggregate = FAILED
10. Consume evidence under Skill contract → Disposition BLOCKED
11. Confirm RESOLVED did not occur while FAILED remained
12. Restore temporary defect
13. Re-run validation → Aggregate PASSED
14. Record failure + recovery without erasing failure evidence
15. Stop (no lifecycle auto-promotion)
```

---

## 9. Skill Invocation Evidence

| Field | Record |
|---|---|
| Skill Loading | **OBSERVED** — packaged SKILL.md read as authoritative procedure |
| Skill Invocation | **SUCCESS** — steps followed from packaged Skill, not design-doc primary |
| Runtime | Cursor agent applying experimental package |
| Framework | None beyond SKILL.md |

```text
Execution object statement:
  Packaged SKILL.md was the execution object for EXP-M2-006.
```

---

## 10. Validation Requirement and Request

```text
Validation Requirement Determination: YES
Classification: OBSERVED
Reason: src/ai_context/cli/main.py modified
```

```text
Validation Request ID: VR-M2-006-001
Requester: Packaged CANDIDATE-001 (EXP-M2-006)
Requested Capability: CANDIDATE-002
Required Gate Set: Unit Tests, Lint, Static Analysis
Target Scope: repository root; revision focus main.py
Classification: OBSERVED
```

```text
Requirement Determination ≠ Request — both recorded separately
```

---

## 11. Failure Evidence

| Gate | Command | Exit | Result | Evidence Summary |
|---|---|---|---|---|
| Unit Tests | `python -m pytest -q` | **1** | **FAILED** | `assert 1 == 0` on `test_cli_init_placeholder`; 1 failed, 64 passed |
| Lint | `python -m ruff check .` | 0 | PASSED | All checks passed |
| Static Analysis | `python -m mypy src` | 0 | PASSED | 13 source files OK |

Excerpt (actual):

```text
E       assert 1 == 0
E        +  where 1 = <Result SystemExit(1)>.exit_code
FAILED tests/unit/test_cli.py::test_cli_init_placeholder - assert 1 == 0
```

```text
Gate Failure Observation: OBSERVED
Failure Mode: Validation Gate Failure (FAILED ≠ ERROR)
```

---

## 12. Aggregate Validation Evidence

```text
Aggregate Validation Evidence: FAILED
Rule: Any required applicable gate FAILED → Aggregate FAILED
Lint/mypy PASSED do not convert Aggregate to PASSED
Classification: OBSERVED
```

---

## 13. Evidence Consumption

| Field | Record |
|---|---|
| Evidence Produced | Aggregate FAILED |
| Evidence Received | Packaged Skill procedure after gate run |
| Evidence Interpreted | Skill rule: FAILED → must not RESOLVED |
| Effect | Non-success disposition selected |

```text
FAILED evidence consumption: OBSERVED
```

---

## 14. Disposition

```text
While Aggregate = FAILED remained unresolved:

Disposition: BLOCKED
RESOLVED During Failure: NO
Classification: OBSERVED
```

Skill contract applied:

```text
If Aggregate = FAILED → must NOT RESOLVED → BLOCKED
```

Open issue at failure observation:

```text
Unit Tests gate FAILED due to EXP-M2-006 controlled assertion mismatch.
Next: remediate temporary defect within experiment setup; re-validate.
```

---

## 15. Recovery

```text
Remediation: Restore test_cli_init_placeholder to assert exit_code == 1
Temporary defect NOT left in repository
Temporary defect NOT committed
```

Post-recovery gates:

| Gate | Exit | Result |
|---|---|---|
| Unit Tests | 0 | PASSED (65) |
| Lint | 0 | PASSED |
| Static Analysis | 0 | PASSED |

```text
Post-Recovery Aggregate: PASSED
Recovery sequence: FAILED → Identify → Remediate → Re-run → PASSED
Recovery: OBSERVED
Historical failure evidence: PRESERVED in §§11–14 (not erased)
```

Final engineering delta retained:

```text
src/ai_context/cli/main.py — docstring exit-status alignment only
tests/: no net change
```

---

## 16. Design-doc vs Packaged Runtime Comparison

| Behavior | EXP-M2-004 (Design-doc) | EXP-M2-005 (Packaged) | EXP-M2-006 (Packaged) |
|---|---|---|---|
| Execution source | Design-doc | Packaged Skill | Packaged Skill |
| Validation result | FAILED | PASSED | FAILED |
| Evidence consumed | YES | YES | YES |
| Disposition | BLOCKED | RESOLVED | BLOCKED |
| Recovery | YES | N/A | YES |
| Failure-path packaged | NO | NO | **YES** |

Failure-path chain equivalence (004 vs 006):

| Link | Design-doc (004) | Packaged (006) | Equivalence |
|---|---|---|---|
| Validation Requirement | YES | YES | **MATCHED** |
| Validation Request | VR-M2-004-001 | VR-M2-006-001 | **MATCHED** |
| Gate Failure | Unit Tests FAILED | Unit Tests FAILED | **MATCHED** |
| Aggregate FAILED | YES | YES | **MATCHED** |
| Evidence Consumption | YES | YES | **MATCHED** |
| BLOCKED | YES | YES | **MATCHED** |
| No RESOLVED while FAILED | YES | YES | **MATCHED** |
| Recovery | YES | YES | **MATCHED** |

```text
Design-doc vs Packaged Failure Path: MATCHED
(for Validation Gate Failure / assertion-mismatch mode)
```

```text
Equivalence is runtime-observed, not inferred from SKILL.md wording alone.
```

---

## 17. Human Intervention

| Intervention | Classification |
|---|---|
| Selected docstring alignment task | Normal Engineering Judgment |
| Loaded/applied packaged SKILL.md | Procedure Application |
| Introduced controlled test assertion mismatch | Experiment Setup / Controlled Intervention |
| Mapped gates → pytest/ruff/mypy | Normal Engineering Judgment |
| Applied BLOCKED per Skill FAILED rule | Procedure Application (Skill contract) |
| Restored temporary defect | Experiment Setup / Controlled Intervention |

```text
Human Substitution of Skill core disposition logic: NOT OBSERVED
Fully Autonomous: NO
```

---

## 18. Evidence Classification

| Claim | Classification |
|---|---|
| Packaged Skill loaded | OBSERVED |
| Packaged Skill invoked | OBSERVED |
| Validation Requirement determined | OBSERVED |
| Validation Request generated | OBSERVED |
| CANDIDATE-002 invoked | OBSERVED |
| Gate failure observed | OBSERVED |
| Aggregate FAILED observed | OBSERVED |
| FAILED evidence consumed | OBSERVED |
| BLOCKED disposition observed | OBSERVED |
| RESOLVED avoided | OBSERVED |
| Recovery observed | OBSERVED |
| Aggregate PASSED after recovery | OBSERVED |
| Packaged failure-path equivalence | OBSERVED (MATCHED vs 004 for this mode) |
| Tool Invocation ERROR path | NOT_ESTABLISHED |
| Dependency Unavailable | NOT_ESTABLISHED |
| Malformed Evidence | NOT_ESTABLISHED |
| Independent replication | NOT_ESTABLISHED |

---

## 19. Failure / Error Classification

```text
Observed this experiment: Validation Gate Failure = FAILED
Tool Invocation ERROR: NOT OBSERVED / NOT_ESTABLISHED as coverage
Dependency Unavailable: NOT_ESTABLISHED
Malformed Evidence: NOT_ESTABLISHED

FAILED ≠ ERROR — preserved
```

---

## 20. Experiment Outcome

```text
Experiment Outcome: SUCCESS
```

Critical assertion:

```text
When Aggregate = FAILED, packaged CANDIDATE-001 produced BLOCKED
and did NOT produce RESOLVED — OBSERVED
```

All required success elements for EXP-M2-006 met:

```text
Packaged Skill execution object
Validation Required YES + Request
Actual gate FAILED + Aggregate FAILED
Consumption → BLOCKED
RESOLVED avoided
Recovery to Aggregate PASSED
Temporary defect removed
```

```text
SUCCESS ≠ automatic VALIDATED
SUCCESS ≠ production PACKAGED
SUCCESS ≠ CANDIDATE-002 independently validated
```

---

## 21. Lifecycle Impact

```text
CANDIDATE-001 Lifecycle: CONDITIONALLY_VALIDATED (UNCHANGED)
VALIDATED: NO (no automatic promotion; Stage K reassessment deferred)
PACKAGING_READY: YES (CONDITIONAL / EXPERIMENTAL) — UNCHANGED category
PACKAGED (production): NO

Evidence added:
  Packaged failure-path composition OBSERVED (gate-failure mode)
  Strengthens conditional packaging confidence after Stage J happy path

CANDIDATE-002: VALIDATION_READY (UNCHANGED)
```

```text
Stage K Lifecycle Reassessment is NOT performed in this experiment record.
Next step after independent review of EXP-M2-006.
```

---

## 22. Remaining Evidence Gaps

```text
Packaged ERROR / unavailable / malformed paths   NOT_ESTABLISHED
Independent replication                          NOT_ESTABLISHED
Cross-repository packaged invocation             NOT_ESTABLISHED
Production packaging / registry                  NOT_ESTABLISHED
CANDIDATE-002 independent validation             NOT_ESTABLISHED
Formal Stage K+ lifecycle reassessment           PENDING AUTHORIZATION
```

---

## 23. Non-Goals

```text
Stage K / EXP-M2-006 did NOT:
  Create Skill/Workflow/Agent frameworks
  Rewrite Stages A–J
  Auto-promote VALIDATED
  Create production packaging infrastructure
  Independently validate CANDIDATE-002
  Leave temporary failure in the tree
```

---

## 24. Next-Step Recommendation

```text
Recommended (pending authorization / independent review):
  Stage K Lifecycle Reassessment (or successor stage) to decide whether
  combined packaged happy-path (005) + failure-path (006) evidence
  justifies VALIDATED and/or refined PACKAGING_READY conditions.

Do not auto-start that reassessment from this experiment push.
```

---

## End of Stage K Record

```text
Document: 15-stage-k-exp-m2-006-packaged-skill-failure-path.md
Experiment: EXP-M2-006
Outcome: SUCCESS
Packaged Failure Path: MATCHED vs EXP-M2-004 (gate-failure mode)
Lifecycle Promotion: NONE
Final product delta: src/ai_context/cli/main.py docstring only
```

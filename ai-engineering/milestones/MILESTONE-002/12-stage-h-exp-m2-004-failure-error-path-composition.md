# MILESTONE-002 Stage H — EXP-M2-004 Failure/ERROR-Path Composition Test

## 1. Objective

```text
Validate the failure/ERROR branch of CANDIDATE-001 → CANDIDATE-002 composition:

When Aggregate Validation Evidence != PASSED,
does CANDIDATE-001 correctly avoid RESOLVED and apply a non-success disposition?
```

```text
Experiment ID: EXP-M2-004
Primary Subject: CANDIDATE-001
Supporting Capability: CANDIDATE-002
Packaging: NONE
Lifecycle promotion: NOT automatic
```

---

## 2. Experiment Question

> When CANDIDATE-002 produces non-PASSED validation evidence, does CANDIDATE-001 correctly consume that evidence and prevent an incorrect successful revision disposition?

Desired observation: correct orchestration behavior — not engineering-task success.

---

## 3. Authoritative Context

```text
MILESTONE-002.md
09-stage-e-evidence-sufficiency-and-asset-disposition.md
10-stage-f-exp-m2-003-invocation-and-evidence-capture.md
11-stage-g-exp-m2-003-evidence-assessment-and-lifecycle-reassessment.md
05-candidate-001-targeted-engineering-revision.md
06-candidate-002-repository-tooling-validation-gate.md
```

CANDIDATE-001 Failure Propagation (design):

```text
If validation FAILS:
  - do not claim RESOLVED
  - either repair within original boundary, or
  - STOP / ESCALATE / RETURN PARTIAL with open issues
  - without authorized deferral → BLOCKED / ESCALATED / …
```

Disposition vocabulary used:

```text
RESOLVED / PARTIAL / BLOCKED / ESCALATED / STOPPED
```

Entering state (Stage G):

```text
CANDIDATE-001: CONDITIONALLY_VALIDATED
Dependency: HAPPY_PATH_OBSERVED / FAILURE_PATH_NOT_ESTABLISHED
```

---

## 4. Baseline Repository State

```text
Baseline commit: 68ab8c5
Branch: main (clean engineering tree)
pytest: 65 passed (post Stage G hygiene)
ruff / mypy: clean
CLI init: exits 1 (EXP-M2-003 contract)
test_cli_init_placeholder: expects exit_code == 1
```

---

## 5. Revision Boundary

```text
Experiment Objective:
  Observe 001←002 composition under Aggregate FAILED.

In Scope (temporary):
  tests/unit/test_cli.py — controlled assertion mismatch only

Out of Scope / Non-Goals:
  Permanent product defect
  Real init implementation
  Domain / packaging / lifecycle redesign
  Inventing new disposition states
  Rewriting Stages E–G records

Acceptance Criteria (experiment):
  At least one required gate actually FAILS
  Aggregate Validation Evidence = FAILED
  CANDIDATE-001 does not claim RESOLVED while FAILED remains
  Temporary failure restored before final commit
  Final repository healthy
```

---

## 6. Controlled Failure Mechanism

```text
Mechanism: Temporary wrong assertion in unit test
File: tests/unit/test_cli.py :: test_cli_init_placeholder
Change: assert result.exit_code == 0   # while CLI still exits 1
Marker: EXP-M2-004 CONTROLLED FAILURE (temporary)
Expected failing gate: Unit Tests (pytest)
Failure mode class: Validation Gate Failure (assertion)
NOT: tool invocation error / dependency unavailable / malformed evidence
```

```text
Fabrication of gate results: NOT USED
Temporary defect: actually executed by pytest → real FAILED
Destructive changes: NONE
Unrelated production behavior: UNCHANGED (src/ untouched during failure phase)
```

---

## 7. Validation Requirement

```text
Validation Requirement Determination: YES
Status: OBSERVED
```

| Field | Record |
|---|---|
| Why | Controlled change to required unit-test acceptance surface |
| Acceptance criteria | Required gates must evidence current repository state |
| Expected mechanism | CANDIDATE-002 Repository Tooling Validation Gate |
| Why 002 | Designed REQUESTS target for tooling execution |

---

## 8. CANDIDATE-002 Request

```text
Validation Request ID:     VR-M2-004-001
Requester:                 CANDIDATE-001 (EXP-M2-004 experimental invocation)
Requested Capability:      CANDIDATE-002
Reason:                    Failure-path observation after temporary test-contract mismatch
Input / Target Scope:      Repository root; focus tests/unit/test_cli.py
Required Gate Set:         Unit Tests, Lint, Static Analysis
Expected Output:           Aggregate Validation Evidence (may be non-PASSED)
Request Sequence:          After controlled defect introduced; before disposition
```

---

## 9. CANDIDATE-002 Invocation

```text
Mechanism: Design-document experimental procedure
Reference: 06-candidate-002-repository-tooling-validation-gate.md
Packaged Skill: NOT PRESENT
Simulation of results: NOT USED
```

Procedure:

```text
Receive VR-M2-004-001 → Inspect repo → Resolve gates → Execute →
Collect → Normalize → Report Aggregate → Stop
```

Gate resolution (unchanged mapping vs EXP-M2-003):

| Gate | Command |
|---|---|
| Unit Tests | `python -m pytest -q` |
| Lint | `python -m ruff check .` |
| Static Analysis | `python -m mypy src` |

---

## 10. Gate Execution

| Gate | Command | Exit Code | Observed Result | Evidence Summary |
|---|---|---|---|---|
| Unit Tests | `python -m pytest -q` | **1** | **FAILED** | `FAILED tests/unit/test_cli.py::test_cli_init_placeholder - assert 1 == 0`; 1 failed, 64 passed |
| Lint | `python -m ruff check .` | 0 | PASSED | All checks passed |
| Static Analysis | `python -m mypy src` | 0 | PASSED | Success: no issues found in 13 source files |

Focused confirmation:

```text
python -m pytest -q tests/unit/test_cli.py
→ FAILED test_cli_init_placeholder — assert 1 == 0
→ exit code 1
```

---

## 11. Actual FAILED / ERROR Evidence

```text
Failure Mode Observed: Validation Gate Failure
Gate: Unit Tests
Result: FAILED (not ERROR)
Tool Invocation Error: NOT OBSERVED
Dependency Unavailable: NOT OBSERVED
Malformed Evidence: NOT OBSERVED
```

Excerpt (actual):

```text
E       assert 1 == 0
E        +  where 1 = <Result SystemExit(1)>.exit_code
FAILED tests/unit/test_cli.py::test_cli_init_placeholder - assert 1 == 0
1 failed, 64 passed in 0.22s
```

---

## 12. Aggregate Validation Evidence

Apply CANDIDATE-002 aggregate rule (unchanged):

```text
Any Applicable Gate Failed → Aggregate: FAILED
```

```text
Aggregate Validation Evidence: FAILED
Reason: Required Unit Tests gate FAILED;
        Lint PASSED; Static Analysis PASSED;
        do not collapse to PASSED; do not call ERROR
        (execution completed correctly — criteria failed).
```

```text
FAILED ≠ ERROR
ERROR would require Applicable + Not Executable / infrastructure fault.
```

---

## 13. Evidence Consumption by CANDIDATE-001

| Field | Record |
|---|---|
| Evidence Produced | Aggregate FAILED (Unit Tests FAILED) |
| Evidence Received | Received by CANDIDATE-001 procedure after §12 |
| Evidence Interpreted | Required validation not satisfied; RESOLVED forbidden |
| Effect on Decision | Non-success disposition selected (§14) |

```text
Evidence Consumption: CONSUMED (non-PASSED path)
Classification: OBSERVED
```

---

## 14. Non-PASSED Disposition

```text
While Aggregate Validation Evidence = FAILED remained unresolved:

CANDIDATE-001 Disposition: BLOCKED
RESOLVED claimed? NO
```

Design alignment:

```text
If validation FAILS → do not claim RESOLVED
→ STOP / repair within boundary / BLOCKED without deferral
```

```text
Correct non-success disposition observed: YES
```

Open issue recorded at failure observation:

```text
Open Issue: Unit Tests gate FAILED due to EXP-M2-004 controlled
            assertion mismatch (exit_code expected 0 vs actual 1).
Next Action: Remediate temporary defect within boundary, then re-validate.
```

---

## 15. Recovery / Remediation

```text
Remediation Decision: Restore test_cli_init_placeholder to assert exit_code == 1
Classification: OBSERVED
Human role: Normal Engineering Judgment (select remediation)
```

```text
src/: unchanged throughout failure + remediation
Temporary failure NOT left behind
Temporary failure NOT committed as product change
```

Historical integrity:

```text
Initial FAILED observation preserved in this record (§10–§14)
Recovery does not erase initial failure evidence
```

---

## 16. Re-validation (after remediation)

Re-invoked Required Gate Set after restore:

| Gate | Exit Code | Result |
|---|---|---|
| Unit Tests | 0 | PASSED (65 passed) |
| Lint | 0 | PASSED |
| Static Analysis | 0 | PASSED |

```text
Post-remediation Aggregate: PASSED
Re-validation: OBSERVED
```

```text
Recovery sequence observed:
FAILED → Identify cause → Remediate → Re-run → PASSED
```

Engineering tree after remediation: matches baseline (no product delta).

---

## 17. Evidence Classification

| Link | Classification | Tie to evidence |
|---|---|---|
| Validation Requirement Determination | OBSERVED | §7 after controlled test change |
| Validation Request | OBSERVED | VR-M2-004-001 |
| CANDIDATE-002 Invocation | OBSERVED | §9 design-doc procedure + gate runs |
| Gate Execution | OBSERVED | §10 commands + exit codes |
| FAILED / ERROR Observation | OBSERVED | pytest FAILED assert 1 == 0 |
| Aggregate Evidence Production | OBSERVED | Aggregate FAILED per §12 |
| Evidence Reception by CANDIDATE-001 | OBSERVED | §13 |
| Evidence Interpretation | OBSERVED | RESOLVED forbidden while FAILED |
| Non-PASSED Disposition | OBSERVED | BLOCKED (§14) |
| Remediation Decision | OBSERVED | Restore assertion (§15) |
| Re-validation | OBSERVED | All gates PASSED (§16) |

---

## 18. Human Intervention

| Intervention | Classification |
|---|---|
| Selected temporary wrong assertion as failure mechanism | Normal Engineering Judgment |
| Mapped gates → pytest/ruff/mypy | Normal Engineering Judgment |
| Chose BLOCKED per design Failure Propagation | Procedure application (not substitution) |
| Chose remediation restore | Normal Engineering Judgment |
| Did not treat FAILED as PASSED | Avoided Human Substitution anti-pattern |

```text
No Human Substitution that converted FAILED → PASSED without remediation.
```

---

## 19. Comparison With EXP-M2-003

| Aspect | EXP-M2-003 (Happy Path) | EXP-M2-004 (Failure Path) |
|---|---|---|
| Task | CLI exit-code product fix | Controlled temporary test mismatch |
| Aggregate | PASSED | FAILED → (after remediation) PASSED |
| 001 Disposition | RESOLVED | BLOCKED then remediate |
| Consumption | Consumed PASSED | Consumed FAILED |
| Failure recovery | NOT TESTED | OBSERVED |

```text
Common:
  REQUEST → INVOKE → Aggregate Evidence → 001 consumption → disposition
  Design-doc procedures; same gate set; boundary control

Differs:
  Non-PASSED interpretation; BLOCKED vs RESOLVED; remediation + re-validation

New evidence:
  Failure-path composition; gate-failure mode; recovery sequence

Uncertainty reduced:
  Stage G FAILURE_PATH_NOT_ESTABLISHED for gate-failure / assert-fail mode

Uncertainty remains:
  ERROR (tooling) path; dependency unavailable; malformed evidence;
  packaged Skill; independent replication; other failure modes
```

---

## 20. Remaining Evidence Gaps

| Gap | Status after EXP-M2-004 |
|---|---|
| Happy-path 001→002 composition | OBSERVED (M2-003) |
| Failure-path gate FAILED → 001 BLOCKED | **OBSERVED (this experiment)** |
| Recovery FAILED→remediate→PASSED | **OBSERVED** |
| Tool Invocation ERROR aggregate | NOT_ESTABLISHED |
| Dependency unavailable | NOT_ESTABLISHED |
| Malformed evidence handling | NOT_ESTABLISHED |
| Packaged Skill invocation | NOT_ESTABLISHED |
| Independent replication | NOT_ESTABLISHED |
| Multi-asset beyond 001→002 | NOT_ESTABLISHED |

```text
Failure coverage claim limited to:
  Validation Gate Failure (pytest assertion failure)
```

---

## 21. CANDIDATE-001 Lifecycle Impact

```text
Does EXP-M2-004 materially strengthen the case for VALIDATED?
YES — failure-path composition + recovery now OBSERVED for gate-failure mode.
```

| Factor | Status |
|---|---|
| Happy-path dependency composition | OBSERVED |
| Failure-path dependency composition | OBSERVED (gate FAILED mode) |
| Recovery behavior | OBSERVED |
| Packaged Skill behavior | NOT_ESTABLISHED |
| Independent replication | NOT_ESTABLISHED |
| Cross-repository behavior | NOT_ESTABLISHED |
| Human intervention | Documented; judgment still required |

```text
CANDIDATE-001 Lifecycle: CONDITIONALLY_VALIDATED (UNCHANGED / RETAINED)

Reason:
  Happy + failure-path composition strengthen conditional confidence.
  Unconditional VALIDATED still undermined by packaged-Skill absence,
  single failure-mode sample, and single-executor/context limits.
  Stage H forbids automatic promotion.
```

```text
Dependency Coverage Update:
  PREVIOUS: HAPPY_PATH_OBSERVED / FAILURE_PATH_NOT_ESTABLISHED
  CURRENT:  HAPPY_PATH_OBSERVED / FAILURE_PATH_OBSERVED (gate-failure mode)

Critical composition gap (Stage E/G):
  Happy-path PARTIALLY_CLOSED → now further reduced;
  Failure-path for assert-fail mode CLOSED for that mode only.
  Overall dependency gap remains PARTIALLY_CLOSED at portfolio level
  (ERROR/tooling/packaged paths open).
```

---

## 22. CANDIDATE-002 Independent Status

```text
CANDIDATE-002 Lifecycle: VALIDATION_READY (UNCHANGED)
```

Producing FAILED Aggregate Evidence in composition ≠ independent validation of 002.

---

## 23. Packaging Readiness

```text
CANDIDATE-001 Packaging Readiness: NOT_READY
CANDIDATE-002 Packaging Readiness: NOT_READY
```

```text
No SKILL.md / WORKFLOW.md / Agent runtime created.
```

---

## 24. Experiment Outcome

```text
Experiment Outcome: SUCCESS
```

Criteria:

| Criterion | Met? |
|---|---|
| Actual required gate non-PASSED | Yes — Unit Tests FAILED |
| Aggregate correctly FAILED | Yes |
| 001 consumed non-PASSED evidence | Yes |
| 001 avoided RESOLVED while FAILED | Yes — BLOCKED |
| Temporary failure restored | Yes |
| Final repository healthy | Yes |
| Failure evidence preserved historically | Yes (this record) |

```text
SUCCESS = correct failure-path orchestration observed.
≠ CANDIDATE-001 VALIDATED
≠ Packaging authorized
```

---

## 25. Conclusion

```text
EXP-M2-004 experimentally answered the Stage G priority question:

When CANDIDATE-002 returns Aggregate FAILED, CANDIDATE-001 can consume
that evidence and apply BLOCKED instead of incorrectly claiming RESOLVED.

Controlled failure: Unit Tests assertion mismatch (temporary)
Aggregate: FAILED
Recovery: OBSERVED (remediate → re-validate PASSED)
Lifecycle: CONDITIONALLY_VALIDATED retained
Packaging: NONE / NOT_READY

Next (pending authorization):
  Packaging readiness review under updated dependency evidence,
  or packaged-Skill invocation experiment — not automatic.
```

---

## End of Stage H Record

```text
Document: 12-stage-h-exp-m2-004-failure-error-path-composition.md
Experiment: EXP-M2-004
Outcome: SUCCESS
Lifecycle Promotion: NONE
Final engineering delta: NONE (docs only in commit)
```

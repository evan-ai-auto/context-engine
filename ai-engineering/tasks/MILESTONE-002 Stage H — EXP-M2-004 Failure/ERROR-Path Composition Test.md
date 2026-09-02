# MILESTONE-002 Stage H — EXP-M2-004 Failure/ERROR-Path Composition Test

## Execution Mode

Cursor MUST execute this task as a controlled validation experiment.

Do not redesign the asset architecture.

Do not package CANDIDATE-001 or CANDIDATE-002.

Do not introduce an orchestration runtime.

Do not promote any candidate automatically.

The purpose of this stage is to experimentally test the previously unvalidated failure path:

```text
CANDIDATE-001
    ↓
Validation Requirement
    ↓
REQUEST CANDIDATE-002
    ↓
INVOKE CANDIDATE-002
    ↓
FAILED / ERROR
    ↓
Aggregate Validation Evidence
    ↓
CANDIDATE-001 consumes non-PASSED evidence
    ↓
Correct non-success disposition
```

---

# 1. Objective

Validate the failure/error branch of the CANDIDATE-001 → CANDIDATE-002 composition.

Specifically determine whether CANDIDATE-001 can correctly handle:

```text
Aggregate Validation Evidence != PASSED
```

without incorrectly concluding:

```text
RESOLVED
```

The experiment must distinguish:

```text
FAILED
ERROR
PASSED
```

and must not collapse all non-success states into a generic success/failure claim.

---

# 2. Authoritative Context

Before execution inspect:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md

ai-engineering/milestones/MILESTONE-002/
  09-stage-e-evidence-sufficiency-and-asset-disposition.md
  10-stage-f-exp-m2-003-invocation-and-evidence-capture.md
  11-stage-g-exp-m2-003-evidence-assessment-and-lifecycle-reassessment.md

ai-engineering/milestones/MILESTONE-002/
  05-candidate-001-targeted-engineering-revision.md
  06-candidate-002-repository-tooling-validation-gate.md
```

Also inspect the repository state and current implementation before modifying anything.

Do not assume previous conclusions are correct without checking the authoritative records.

---

# 3. Experiment ID

Use:

```text
EXP-M2-004
```

Experiment name:

```text
Failure/ERROR-Path Composition Test
```

Primary subject:

```text
CANDIDATE-001 — Targeted Engineering Revision
```

Supporting capability:

```text
CANDIDATE-002 — Repository Tooling Validation Gate
```

---

# 4. Required Experiment Question

Answer this question experimentally:

> When CANDIDATE-002 produces non-PASSED validation evidence, does CANDIDATE-001 correctly consume that evidence and prevent an incorrect successful revision disposition?

The desired observation is NOT necessarily that the engineering task itself succeeds.

The desired observation is correct orchestration behavior.

---

# 5. Critical Constraint

Do NOT fabricate a FAILED or ERROR result.

The non-PASSED result must come from an actually executed validation gate.

Use a controlled, reversible mechanism to cause at least one required validation gate to fail.

Preferred mechanism:

```text
Introduce a temporary, explicitly controlled defect
that causes one required validation gate to fail.
```

Examples may include:

- a temporary test assertion failure
- a temporary lint violation
- another deterministic repository validation failure

Choose the smallest and safest mechanism.

Do NOT introduce destructive changes.

Do NOT modify unrelated production behavior.

---

# 6. Experiment Isolation

The temporary failure-inducing modification MUST be clearly marked as experimental.

Record:

```text
baseline repository state
temporary change
expected failing gate
actual failing output
aggregate validation result
CANDIDATE-001 interpretation
recovery/remediation
final repository state
```

The temporary failure must not be silently committed as a product change.

After the failure-path observation is captured, restore the repository to the intended final state.

If remediation is required, perform it explicitly and record it separately from the failure-path observation.

Do NOT rewrite the historical failure evidence after remediation.

---

# 7. Required Experimental Chain

Execute and document this exact conceptual chain:

```text
Inspect
    ↓
Understand
    ↓
Define Revision Boundary
    ↓
Plan
    ↓
Determine Validation Requirement
    ↓
REQUEST CANDIDATE-002
    ↓
INVOKE CANDIDATE-002
    ↓
Execute Required Validation Gates
    ↓
Observe FAILED / ERROR
    ↓
Normalize Aggregate Validation Evidence
    ↓
Return Evidence to CANDIDATE-001
    ↓
CANDIDATE-001 Interprets Non-PASSED Result
    ↓
Determine Correct Disposition
    ↓
Remediate if required
    ↓
Re-run validation only if justified
    ↓
Stop
```

Do not skip the evidence-consumption step.

---

# 8. Validation Gate Requirements

Use the existing CANDIDATE-002 validation gate model.

Inspect the repository and resolve the applicable gates.

Expected repository tooling currently includes:

```text
pytest
ruff
mypy
```

Use the authoritative commands already established in EXP-M2-003 unless repository state requires a justified adjustment.

Do not invent a new validation framework.

At least one required gate must produce an actual:

```text
FAILED
```

or:

```text
ERROR
```

result during the failure-path observation.

The experiment must capture:

```text
Gate
Command
Exit Code
Observed Result
Evidence Summary
```

---

# 9. Aggregate Result

Apply the existing aggregate rule.

Do not change the aggregate semantics merely to make the experiment easier.

If any required gate fails:

```text
Aggregate Validation Evidence = FAILED
```

If execution itself produces an infrastructure/tooling error:

```text
Aggregate Validation Evidence = ERROR
```

Do not convert:

```text
FAILED → PASSED
```

or:

```text
ERROR → PASSED
```

through interpretation.

---

# 10. CANDIDATE-001 Consumption Test

This is the most important part of the experiment.

After CANDIDATE-002 produces:

```text
Aggregate Validation Evidence = FAILED
```

or:

```text
Aggregate Validation Evidence = ERROR
```

CANDIDATE-001 MUST consume that result.

Determine whether CANDIDATE-001 correctly avoids:

```text
RESOLVED
```

while non-PASSED evidence remains unresolved.

The expected safe behavior is conceptually:

```text
Validation Evidence = FAILED / ERROR
        ↓
Revision NOT resolved
        ↓
Further action required
```

Do not invent a lifecycle state if one does not already exist.

Use the repository's existing terminology.

If the current design does not define an explicit failure disposition, record:

```text
NOT_ESTABLISHED
```

rather than inventing behavior.

---

# 11. Human Intervention Accounting

Record every point where human engineering judgment is required.

Especially distinguish:

```text
Normal Engineering Judgment
```

from:

```text
Human Substitution for Asset Behavior
```

Examples:

```text
Selecting the controlled failure mechanism
Mapping abstract validation gates to repository commands
Choosing remediation
```

may be normal engineering judgment.

However:

```text
Human manually deciding that FAILED should be treated as PASSED
```

must never be counted as successful autonomous composition.

---

# 12. Failure-Path Evidence Classification

For every link classify evidence independently as:

```text
OBSERVED
SUPPORTED_INFERENCE
WEAK_INFERENCE
NOT_ESTABLISHED
```

Required links:

| Link | Required classification |
|---|---|
| Validation Requirement Determination | classify |
| Validation Request | classify |
| CANDIDATE-002 Invocation | classify |
| Gate Execution | classify |
| FAILED / ERROR Observation | classify |
| Aggregate Evidence Production | classify |
| Evidence Reception by CANDIDATE-001 | classify |
| Evidence Interpretation | classify |
| Non-PASSED Disposition | classify |
| Remediation Decision | classify |
| Re-validation, if performed | classify |

Do not assign OBSERVED merely because a document says that something happened.

Tie every OBSERVED classification to actual experimental evidence.

---

# 13. Compare With EXP-M2-003

Create a direct comparison:

```text
EXP-M2-003
Happy Path
002 → PASSED → consumed

versus

EXP-M2-004
Failure Path
002 → FAILED / ERROR → consumed
```

Assess:

```text
What behavior is common?
What behavior differs?
What new evidence exists?
What previous uncertainty is reduced?
What uncertainty remains?
```

Do not claim that one failure experiment validates all possible failure modes.

---

# 14. Failure Coverage

Explicitly distinguish:

```text
Validation Gate Failure
```

from:

```text
Tool Invocation Error
```

from:

```text
Dependency Unavailable
```

from:

```text
Malformed Evidence
```

The experiment may only validate the failure mode actually exercised.

For example:

```text
pytest assertion failure
```

does NOT establish:

```text
network failure handling
tool timeout handling
malformed response handling
dependency unavailable handling
```

Keep those as:

```text
NOT_ESTABLISHED
```

unless actually observed.

---

# 15. Recovery Observation

If the controlled failure can be safely remediated:

```text
FAILED
 ↓
Identify cause
 ↓
Remediate
 ↓
Re-run required validation
 ↓
PASSED
```

this may be observed as a recovery sequence.

However:

```text
Recovery success
```

must not erase:

```text
Initial failure
```

The historical experiment record must preserve both observations.

---

# 16. Candidate-001 Lifecycle Assessment

Do NOT automatically promote CANDIDATE-001.

At the end of the experiment determine:

```text
Does EXP-M2-004 materially strengthen the case for VALIDATED?
```

Evaluate separately:

```text
Happy-path dependency composition
Failure-path dependency composition
Recovery behavior
Packaged Skill behavior
Independent replication
Cross-repository behavior
Human intervention
```

If the evidence is insufficient for unconditional validation:

```text
CANDIDATE-001 remains CONDITIONALLY_VALIDATED
```

Do not create a new lifecycle state.

---

# 17. CANDIDATE-002 Status

Do NOT independently promote CANDIDATE-002 merely because it produced a failure result.

Continue to distinguish:

```text
CANDIDATE-002 standalone validation
```

from:

```text
CANDIDATE-001 → CANDIDATE-002 composition evidence
```

A failure-path composition observation does not by itself constitute independent validation of CANDIDATE-002.

---

# 18. Packaging Decision

Do not package either candidate.

Explicitly reassess:

```text
CANDIDATE-001 Packaging Readiness
CANDIDATE-002 Packaging Readiness
```

Do not create:

```text
SKILL.md
WORKFLOW.md
Agent runtime
```

during this stage.

---

# 19. Required Experiment Record

Create:

```text
ai-engineering/milestones/MILESTONE-002/12-stage-h-exp-m2-004-failure-error-path-composition.md
```

The record MUST contain:

```text
1. Objective
2. Experiment Question
3. Authoritative Context
4. Baseline Repository State
5. Revision Boundary
6. Controlled Failure Mechanism
7. Validation Requirement
8. CANDIDATE-002 Request
9. CANDIDATE-002 Invocation
10. Gate Execution
11. Actual FAILED / ERROR Evidence
12. Aggregate Validation Evidence
13. Evidence Consumption by CANDIDATE-001
14. Non-PASSED Disposition
15. Recovery / Remediation
16. Re-validation, if performed
17. Evidence Classification
18. Human Intervention
19. Comparison With EXP-M2-003
20. Remaining Evidence Gaps
21. CANDIDATE-001 Lifecycle Impact
22. CANDIDATE-002 Independent Status
23. Packaging Readiness
24. Experiment Outcome
25. Conclusion
```

---

# 20. Historical Integrity

Do NOT modify previous experiment conclusions.

Do NOT rewrite:

```text
EXP-M2-001
EXP-M2-002
EXP-M2-003
Stage E
Stage F
Stage G
```

Only reference previous evidence.

Do not retroactively change previous classifications because EXP-M2-004 produced new evidence.

---

# 21. MILESTONE-002 Update

Update:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md
```

Only with:

```text
Stage H completion
EXP-M2-004 outcome
failure-path evidence status
updated lifecycle status, if justified
updated dependency coverage
updated recommended next step
```

Preserve historical Stage E/F/G conclusions.

---

# 22. Validation / Hygiene

Run:

```bash
git diff --check
```

Also run the normal repository engineering checks after restoring/remediating the controlled failure:

```bash
python -m pytest -q
python -m ruff check .
python -m mypy src
```

Important:

The final green checks demonstrate final repository health.

They do NOT erase or replace the recorded failure-path evidence.

The experiment MUST preserve the actual failed command/output/result observed before remediation.

---

# 23. Final Repository Boundary

Before completion verify:

```text
No unintended production changes
No temporary failure left behind
No generated artifacts
No packaging files
No architecture redesign
No unrelated refactoring
```

Review:

```bash
git status
git diff
git diff --check
```

---

# 24. Commit

If the experiment requires persistent documentation only, commit with:

```text
test(milestone-002): validate failure path composition
```

Do not commit a deliberately broken repository state.

The final commit must leave the repository healthy.

Push the commit.

---

# 25. Final Report

After push, report:

```text
EXP-M2-004:
Outcome:

Controlled failure:
FAILED / ERROR

Failed gate:

Aggregate validation:
FAILED / ERROR

CANDIDATE-001 consumed non-PASSED evidence:
YES / NO / NOT_ESTABLISHED

Correct non-success disposition observed:
YES / NO / NOT_ESTABLISHED

Recovery observed:
YES / NO

CANDIDATE-001 lifecycle:
UNCHANGED / UPDATED

CANDIDATE-002 lifecycle:
UNCHANGED / UPDATED

Dependency coverage:
PREVIOUS → CURRENT

Packaging:
NONE

Human intervention:
...

Changed files:
...

Checks:
...

Commit SHA:
...

Push:
SUCCESS / FAILED
```

Then STOP.

Do not begin another experiment automatically.
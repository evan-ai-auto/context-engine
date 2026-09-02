# MILESTONE-002 Stage K — EXP-M2-006 Packaged Skill Failure-Path Composition Test

## 0. Execution Mode

You are executing:

```text
MILESTONE-002 Stage K
EXP-M2-006 — Packaged Skill Failure-Path Composition Test
```

Repository:

```text
evan-ai-auto/context-engine
```

This is an **evidence experiment**, not a feature-development task.

Follow the existing project governance and historical evidence model.

Do not redesign the architecture.

Do not create a generic Skill framework.

Do not create Workflow / Agent infrastructure.

Do not promote CANDIDATE-001 automatically.

---

# 1. Objective

The sole objective of EXP-M2-006 is to determine whether the **minimal packaged CANDIDATE-001 Skill runtime** preserves the failure-path composition behavior previously observed in EXP-M2-004.

Previously established:

```text
EXP-M2-004 — design-document composition

Validation Requirement
        ↓
CANDIDATE-002
        ↓
Gate Failure
        ↓
Aggregate Validation Evidence = FAILED
        ↓
CANDIDATE-001 consumes evidence
        ↓
Disposition = BLOCKED
        ↓
No RESOLVED
```

Stage J established:

```text
EXP-M2-005 — packaged Skill happy path

Aggregate PASSED
        ↓
Evidence Consumption
        ↓
RESOLVED
```

EXP-M2-006 must now test:

```text
Packaged SKILL.md
        ↓
Validation Requirement = YES
        ↓
Validation Request
        ↓
Actual validation failure
        ↓
Aggregate = FAILED
        ↓
Packaged CANDIDATE-001 consumes FAILED evidence
        ↓
Disposition = BLOCKED
        ↓
RESOLVED must NOT occur
```

The key question is:

> Does packaged Skill runtime preserve the evidence-gated failure disposition contract?

---

# 2. Authoritative Context

Before executing, inspect and understand:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md

ai-engineering/milestones/MILESTONE-002/13-stage-i-evidence-consolidation-and-packaging-readiness-review.md

ai-engineering/milestones/MILESTONE-002/14-stage-j-exp-m2-005-packaged-skill-runtime-experiment.md

ai-engineering/milestones/MILESTONE-002/12-stage-h-exp-m2-004-failure-error-path-composition.md

ai-engineering/milestones/MILESTONE-002/10-stage-f-exp-m2-003-invocation-and-evidence-capture.md

ai-engineering/milestones/MILESTONE-002/05-candidate-001-targeted-engineering-revision.md

ai-engineering/milestones/MILESTONE-002/06-candidate-002-repository-tooling-validation-gate.md
```

Also inspect the actual packaged Skill:

```text
ai-engineering/milestones/MILESTONE-002/packaged-runtime/candidate-001-targeted-engineering-revision/SKILL.md
```

Do not assume the Skill content is identical to the Stage J record.

The actual `SKILL.md` is the authoritative packaged execution object.

---

# 3. Primary Subject

Primary subject:

```text
CANDIDATE-001 — Targeted Engineering Revision
```

Execution object:

```text
ai-engineering/milestones/MILESTONE-002/packaged-runtime/candidate-001-targeted-engineering-revision/SKILL.md
```

Supporting capability:

```text
CANDIDATE-002 — Repository Tooling Validation Gate
```

CANDIDATE-002 is only a supporting validation capability.

Do NOT claim that EXP-M2-006 independently validates CANDIDATE-002.

---

# 4. Experiment Boundary

This is a minimal runtime experiment.

Allowed:

```text
Read the packaged SKILL.md
Invoke the packaged Skill
Perform one bounded engineering revision
Intentionally induce one controlled validation failure
Observe the resulting evidence
Observe CANDIDATE-001 disposition
Restore the temporary defect
Re-run validation
Record evidence
```

Do NOT:

```text
Create a Skill framework
Create a Workflow framework
Create an Agent framework
Create an orchestration engine
Create a registry
Create a plugin system
Create a generic validation framework
Refactor CANDIDATE-001
Refactor CANDIDATE-002
Create production infrastructure
Modify specification semantics
Modify architecture semantics
Rewrite Stage A–J history
```

---

# 5. Required Failure Mode

Use a **controlled, temporary validation-gate failure**.

Prefer a test assertion mismatch similar to EXP-M2-004 because that failure mode is already understood and reproducible.

The failure must be:

```text
intentional
temporary
isolated
reversible
observable
```

The failure must NOT be:

```text
tool invocation ERROR
dependency unavailable
malformed evidence
network failure
environment corruption
production code corruption
```

The purpose is specifically:

```text
Aggregate Validation Evidence = FAILED
```

not:

```text
Validation Tool = ERROR
```

Maintain the distinction:

```text
FAILED ≠ ERROR
```

---

# 6. Experimental Task

Use a small authentic engineering revision that:

1. is suitable for CANDIDATE-001;
2. causes validation requirement determination to be:

```text
YES
```

3. produces a real validation request;
4. allows one validation gate to be temporarily forced into:

```text
FAILED
```

5. allows the temporary failure to be safely restored.

Prefer a task that modifies a production/source file rather than only documentation, so the validation requirement remains explicit.

The change must remain:

```text
Primary Target Only
```

Do not expand the task into unrelated files.

---

# 7. Critical Execution Rule

The packaged Skill must be the execution source.

Do NOT perform this experiment by merely reading the Skill and then manually reproducing its intended behavior from the design documents.

The runtime sequence must be:

```text
Load packaged SKILL.md
        ↓
Invoke packaged Skill
        ↓
Follow packaged Skill procedure
        ↓
Determine validation requirement
        ↓
Request CANDIDATE-002
        ↓
Introduce controlled validation failure
        ↓
Run validation
        ↓
Produce Aggregate = FAILED
        ↓
Consume evidence
        ↓
Apply packaged disposition rule
        ↓
BLOCKED
        ↓
Restore temporary defect
        ↓
Re-run validation
```

The experiment record must explicitly state that the packaged `SKILL.md` was the execution object.

---

# 8. Expected Governance

The packaged Skill must preserve:

## 8.1 Boundary

```text
Primary Target Only
```

No unauthorized scope expansion.

---

## 8.2 Validation Requirement

The Skill must first determine:

```text
Validation Requirement = YES
```

before requesting validation.

Do not conflate:

```text
Requirement Determination
```

with:

```text
Validation Request
```

---

## 8.3 Validation Request

The Skill must produce/record a request equivalent to:

```text
VR-M2-006-001
```

Supporting capability:

```text
CANDIDATE-002
```

---

## 8.4 Validation Failure

At least one required gate must actually fail.

For example:

```text
pytest = FAILED
ruff = PASSED
mypy = PASSED
```

Aggregate result:

```text
FAILED
```

Do not convert:

```text
FAILED → PASSED
```

through manual intervention.

---

# 9. Critical Assertion

This is the most important acceptance condition of EXP-M2-006.

When:

```text
Aggregate Validation Evidence = FAILED
```

the packaged CANDIDATE-001 runtime MUST NOT produce:

```text
RESOLVED
```

Expected:

```text
FAILED
    ↓
Evidence consumed
    ↓
Disposition = BLOCKED
```

The experiment is successful only if this behavior is actually observed.

---

# 10. Recovery

After observing:

```text
FAILED → BLOCKED
```

restore the temporary validation defect.

The temporary defect must not remain in the repository.

Then execute validation again.

Expected:

```text
pytest = PASSED
ruff = PASSED
mypy = PASSED
Aggregate = PASSED
```

Record the recovery sequence:

```text
FAILED
  ↓
Identify Cause
  ↓
Remediate
  ↓
Re-run
  ↓
PASSED
```

Important:

The recovery phase must not overwrite the historical failure evidence.

Record both:

```text
Failure Evidence
```

and:

```text
Recovery Evidence
```

---

# 11. Human Intervention Classification

Record all human intervention explicitly.

Use only these categories where applicable:

```text
Normal Engineering Judgment
Procedure Application
Manual Intervention
Human Substitution
```

Important:

Do not claim autonomous behavior if a human directly performed a core Skill step.

If a human merely:

```text
selected the experimental task
introduced the controlled failure
restored the temporary defect
mapped abstract validation gates to commands
```

classify those actions explicitly.

Do not classify them as autonomous Skill behavior.

However, distinguish:

```text
Experiment Setup / Controlled Intervention
```

from:

```text
Human Substitution of Skill Core Logic
```

The latter must only be claimed if it actually occurred.

---

# 12. Evidence Classification

Every material conclusion must use:

```text
OBSERVED
SUPPORTED_INFERENCE
WEAK_INFERENCE
NOT_ESTABLISHED
```

Do not use stronger wording than the evidence supports.

At minimum classify:

```text
Packaged Skill loaded
Packaged Skill invoked
Validation Requirement determined
Validation Request generated
CANDIDATE-002 invoked
Gate failure observed
Aggregate FAILED observed
FAILED evidence consumed
BLOCKED disposition observed
RESOLVED avoided
Recovery observed
Aggregate PASSED after recovery
Packaged failure-path equivalence
```

---

# 13. Comparison With Existing Evidence

Compare EXP-M2-006 with:

```text
EXP-M2-004
EXP-M2-005
```

Expected conceptual comparison:

| Behavior | EXP-M2-004 | EXP-M2-005 | EXP-M2-006 |
|---|---|---|---|
| Execution source | Design-doc | Packaged Skill | Packaged Skill |
| Validation result | FAILED | PASSED | FAILED |
| Evidence consumed | YES | YES | YES |
| Disposition | BLOCKED | RESOLVED | BLOCKED |
| Recovery | YES | N/A | YES |
| Failure-path packaged | NO | NO | YES |

Do not mark equivalence as MATCHED unless the actual observations justify it.

---

# 14. Design-doc vs Packaged Failure-Path Comparison

Explicitly compare:

```text
Design-doc failure path
```

against:

```text
Packaged Skill failure path
```

Required behavior:

```text
Validation Requirement
        ↓
Validation Request
        ↓
Validation Gate Failure
        ↓
Aggregate = FAILED
        ↓
Evidence Consumption
        ↓
BLOCKED
        ↓
No RESOLVED
```

Use:

```text
MATCHED
PARTIALLY_MATCHED
DIVERGED
NOT_OBSERVED
```

Do not infer failure-path equivalence merely because the SKILL.md contains the relevant wording.

The behavior must be observed at runtime.

---

# 15. Failure vs Error Classification

Explicitly preserve:

```text
FAILED
```

versus:

```text
ERROR
```

For this experiment:

```text
Validation Gate Failure = FAILED
```

Do not claim:

```text
Tool Invocation ERROR
```

unless an actual invocation error occurs.

Likewise:

```text
Dependency Unavailable
Malformed Evidence
```

remain:

```text
NOT_ESTABLISHED
```

unless actually observed.

---

# 16. Lifecycle Rules

Do NOT automatically change:

```text
CANDIDATE-001 = VALIDATED
```

even if EXP-M2-006 succeeds.

The experiment only adds evidence.

At the end, make an evidence-based recommendation.

Current known state before EXP-M2-006:

```text
CANDIDATE-001
Lifecycle = CONDITIONALLY_VALIDATED
VALIDATED = NO
PACKAGING_READY = YES (conditional / experimental)
PACKAGED = NO
```

Do not silently change these values without a justified lifecycle reassessment.

Stage K Lifecycle Reassessment remains a separate decision.

---

# 17. Packaging Readiness

Do not reinterpret:

```text
PACKAGING_READY = YES (conditional / experimental)
```

as:

```text
Production packaged
```

The following remain distinct:

```text
PACKAGING_READY
PACKAGED
PRODUCTION_READY
```

EXP-M2-006 must not create production packaging infrastructure.

---

# 18. Required Experiment Record

Create:

```text
ai-engineering/milestones/MILESTONE-002/15-stage-k-exp-m2-006-packaged-skill-failure-path.md
```

Do not use `/` inside filenames.

Use this structure:

```text
# MILESTONE-002 Stage K — EXP-M2-006 Packaged Skill Failure-Path Composition Test

## 1. Experiment Objective

## 2. Authoritative Context

## 3. Primary Subject

## 4. Supporting Capability

## 5. Packaged Skill Execution Object

## 6. Experimental Task

## 7. Failure Injection Design

## 8. Execution Procedure

## 9. Skill Invocation Evidence

## 10. Validation Requirement and Request

## 11. Failure Evidence

## 12. Aggregate Validation Evidence

## 13. Evidence Consumption

## 14. Disposition

## 15. Recovery

## 16. Design-doc vs Packaged Runtime Comparison

## 17. Human Intervention

## 18. Evidence Classification

## 19. Failure / Error Classification

## 20. Experiment Outcome

## 21. Lifecycle Impact

## 22. Remaining Evidence Gaps

## 23. Non-Goals

## 24. Next-Step Recommendation

## End of Stage K Record
```

---

# 19. MILESTONE-002 Main Record

Update:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md
```

Only with the Stage K completion state and evidence summary.

Do not rewrite historical Stage A–J conclusions.

Preserve historical lifecycle decisions.

Clearly distinguish:

```text
Stage J:
Packaged happy path

Stage K:
Packaged failure path
```

---

# 20. Engineering Verification

Before committing:

```bash
git status
git diff --stat
git diff --check
git diff
```

If source/test files were modified, run relevant validation.

At minimum, if the experiment modifies source/test behavior:

```bash
pytest -q
ruff check .
mypy src
```

During controlled failure:

```text
The expected failing gate must be recorded as FAILED.
```

After recovery:

```text
All required validation gates must pass again.
```

Do not leave temporary failure changes in the repository.

---

# 21. Historical Integrity

Do NOT:

```text
Rewrite EXP-M2-004
Rewrite EXP-M2-005
Change previous experiment results
Change previous lifecycle conclusions
Delete failed evidence
Replace FAILED evidence with recovery PASSED evidence
```

The new experiment must append evidence.

Historical experiments remain immutable records of what was observed at that time.

---

# 22. Commit

After all checks pass and the repository contains no unintended temporary failure:

```bash
git status
git diff --check
git diff
```

Commit:

```bash
git add .
git commit -m "test(milestone-002): validate packaged skill failure path"
git push
```

Do not use a slash in any newly created filename.

---

# 23. Final Execution Report

After push, report exactly:

```text
MILESTONE-002 Stage K / EXP-M2-006

Status:
COMPLETED / BLOCKED / FAILED

Packaged Skill:
<path>

Skill Loading:
OBSERVED / ...

Skill Invocation:
SUCCESS / ...

Experimental Task:
<task>

Validation Requirement:
YES / NO

Validation Request:
<request id>

Failure Injection:
<description>

Gate Failure:
<actual gate>

Aggregate Validation Evidence:
FAILED / ...

Evidence Consumption:
OBSERVED / ...

Disposition:
BLOCKED / ...

RESOLVED During Failure:
NO / YES

Recovery:
OBSERVED / ...

Post-Recovery Aggregate:
PASSED / ...

Design-doc vs Packaged Failure Path:
MATCHED / PARTIALLY_MATCHED / DIVERGED / NOT_OBSERVED

Human Intervention:
<summary>

Experiment Outcome:
SUCCESS / FAILED

CANDIDATE-001 Lifecycle:
<state>

VALIDATED:
<YES / NO>

PACKAGING_READY:
<state>

Remaining Evidence Gaps:
<list>

Commit:
<sha>
```

Important:

Do not automatically proceed to Stage K Lifecycle Reassessment after this experiment.

The next step will be decided after independent review of EXP-M2-006.

STOP after reporting the result.
# MILESTONE-002 Stage F — EXP-M2-003 Invocation & Evidence Capture

## Execution Mode

You are executing:

**MILESTONE-002 — Stage F**

Primary experiment:

```text
EXP-M2-003
```

Primary subject:

```text
CANDIDATE-001 — Targeted Engineering Revision
```

Supporting capability:

```text
CANDIDATE-002
```

Repository:

```text
context-engine
```

---

# 1. Objective

Execute the smallest high-value validation experiment identified by MILESTONE-002 Stage E.

The purpose of EXP-M2-003 is to directly exercise the previously untested dependency path:

```text
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

The primary evidence gap is:

```text
CRITICAL
CANDIDATE-001 → CANDIDATE-002 dependency REQUEST / Invocation / Evidence Consumption
```

This experiment is intended to determine whether that designed composition path is actually observable and attributable.

---

# 2. Critical Constraints

This is a validation experiment.

Do NOT:

- redesign CANDIDATE-001;
- redesign CANDIDATE-002;
- create a production Skill;
- create a production Workflow;
- create a production Agent;
- refactor unrelated architecture;
- broaden the experiment into portfolio validation;
- execute unrelated experiments;
- silently replace CANDIDATE-002 with pytest/ruff;
- claim dependency success unless actual invocation occurs.

The primary subject remains:

```text
CANDIDATE-001
```

CANDIDATE-002 is the supporting validation capability.

---

# 3. Mandatory Pre-Execution Reading

Before touching repository files, inspect the current repository state.

Read:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md
```

And the relevant experiment records:

```text
01-validation-experiment-framework.md
02-stage-b1-first-experiment-selection.md
03-stage-b2-exp-m2-001-experimental-invocation.md
04-stage-b3-exp-m2-001-evidence-and-assessment.md
05-stage-c1-evidence-gap-and-second-experiment-selection.md
06-stage-c2-exp-m2-002-experimental-invocation.md
07-stage-c3-exp-m2-002-evidence-and-assessment.md
08-stage-d-cross-experiment-evidence-synthesis.md
09-stage-e-evidence-sufficiency-and-asset-disposition.md
```

Also read:

```text
MILESTONE-001/05-candidate-001-targeted-engineering-revision.md
```

Locate the authoritative definition of:

```text
CANDIDATE-002
```

Do not assume filenames.

Search the repository if necessary.

---

# 4. Experiment Design

Use the smallest authentic repository task capable of forcing a real validation requirement.

Preferred task:

```text
A bounded engineering revision involving production or near-production
artifact changes where validation is genuinely required.
```

Preferred order:

```text
1. Production src/ revision
2. Multi-file test revision with an explicit validation gate
3. Another authentic engineering revision that necessarily requires validation
```

Do not invent a fake failure merely to trigger CANDIDATE-002.

Do not create artificial production defects solely for this experiment.

The selected task must have a legitimate engineering purpose.

---

# 5. Experiment Selection Criteria

Before execution, record why the selected task is appropriate.

The selected task must:

1. have a clearly identifiable primary subject;
2. require a bounded revision;
3. have explicit acceptance criteria;
4. make validation genuinely relevant;
5. provide a legitimate reason to request CANDIDATE-002;
6. remain small enough to preserve attribution;
7. allow the resulting evidence to be captured.

Record:

```text
Experiment ID
Task
Primary Subject
Expected Revision Boundary
Why Validation Is Required
Why CANDIDATE-002 Is Relevant
Expected Evidence
```

---

# 6. Isolation Policy Change

Unlike EXP-M2-001 and EXP-M2-002:

```text
Experiment Isolation Adaptation
```

must NOT be used to skip CANDIDATE-002.

The purpose of EXP-M2-003 is specifically to test the previously isolated dependency path.

Therefore:

```text
CANDIDATE-002 invocation is IN SCOPE.
```

If CANDIDATE-002 cannot actually be invoked because its current implementation is unavailable, incomplete, or only conceptual:

DO NOT simulate the invocation.

Instead:

1. record the limitation;
2. classify the dependency path as NOT TESTED;
3. capture exactly what prevented invocation;
4. stop the experiment if invocation is the primary experimental objective.

Do not relabel supporting validation as dependency invocation.

---

# 7. Required Procedure

Execute CANDIDATE-001 using the existing designed procedure.

The expected chain is:

```text
Inspect
  ↓
Understand
  ↓
Define Revision Boundary
  ↓
Plan
  ↓
Execute
  ↓
Determine Validation Requirement
  ↓
REQUEST CANDIDATE-002
  ↓
CANDIDATE-002 Invocation
  ↓
Consume Validation Evidence
  ↓
Report
  ↓
Stop
```

Do not add new procedural stages unless necessary.

If a stage is skipped, record why.

---

# 8. Validation Requirement Determination

Before requesting CANDIDATE-002, explicitly record:

```text
Validation Requirement Determination:
YES / NO
```

If:

```text
YES
```

record:

```text
Why validation is required
Acceptance criteria requiring validation
Expected validation mechanism
Why CANDIDATE-002 is the appropriate dependency
```

If:

```text
NO
```

then do not force a CANDIDATE-002 request.

That result itself is experimental evidence.

---

# 9. Validation Request Record

If validation is required, create an explicit request record.

At minimum:

```text
Validation Request ID
Requester
Requested Capability
Reason
Input / Target Scope
Expected Output
Request Time / Execution Sequence
```

The record must make it possible to distinguish:

```text
Validation Requirement
```

from:

```text
Validation Request
```

and:

```text
Dependency Invocation
```

Do not collapse them into one statement.

---

# 10. CANDIDATE-002 Invocation

If the repository provides an executable or operational mechanism for CANDIDATE-002:

invoke it according to its current authoritative definition.

Capture:

```text
Invocation Status
Invocation Input
Invocation Output
Validation Result
Evidence Produced
Failures / Errors
Human Intervention
```

Classify invocation as exactly one:

```text
SUCCEEDED
FAILED
BLOCKED
NOT_TESTED
```

Use:

```text
SUCCEEDED
```

only if the actual dependency was invoked and produced the expected evidence.

---

# 11. Dependency State Tracking

Maintain this explicit state table:

| Dependency State | Status |
|---|---|
| DEPENDENCY_IDENTIFIED | |
| DEPENDENCY_REQUESTED | |
| DEPENDENCY_INVOKED | |
| DEPENDENCY_SUCCEEDED | |
| DEPENDENCY_FAILURE_TESTED | |
| EVIDENCE_CONSUMED_BY_001 | |

Do not mark a state true merely because a previous stage or design document says the dependency exists.

Each state must be supported by experiment evidence.

---

# 12. Supporting Engineering Validation

Normal engineering validation may still be performed:

```text
pytest
ruff check .
mypy src
git diff --check
```

But classify these separately.

For example:

```text
Supporting Engineering Validation:
pytest = PASS
ruff = PASS

Dependency Validation:
CANDIDATE-002 = SUCCEEDED
```

or:

```text
Supporting Engineering Validation:
pytest = PASS

Dependency Validation:
CANDIDATE-002 = NOT_TESTED
```

Never write:

```text
pytest passed
therefore CANDIDATE-002 succeeded
```

That attribution is prohibited.

---

# 13. Evidence Consumption

This is a critical part of the experiment.

After CANDIDATE-002 produces evidence, determine whether CANDIDATE-001 actually consumes that evidence.

Record:

```text
Evidence Produced
Evidence Received
Evidence Interpreted
Effect on Revision Decision
```

Classify:

```text
CONSUMED
PARTIALLY_CONSUMED
PRODUCED_BUT_NOT_CONSUMED
NOT_AVAILABLE
```

A successful CANDIDATE-002 invocation alone is insufficient.

The experiment must determine whether the dependency output participates in CANDIDATE-001's final decision.

---

# 14. Boundary Preservation

Verify that the original revision boundary remains intact after validation.

Check:

```text
In Scope
Out of Scope
Non-Goals
Actual Modified Files
Actual Modified Behavior
```

Determine whether CANDIDATE-002 caused:

```text
No Scope Change
Minor Scope Clarification
Scope Expansion
Scope Violation
```

If scope expanded, record exactly why.

Do not silently absorb scope changes.

---

# 15. Human Intervention

Record all material human intervention.

Use existing terminology where applicable:

```text
Normal Engineering Judgment
Experiment Isolation Adaptation
Human Substitution
Manual Validation
Boundary Decision
Execution Recovery
```

Pay particular attention to whether a human manually performed work that CANDIDATE-002 was expected to perform.

If so, do not classify the dependency as successful.

---

# 16. Failure Handling

Do not manufacture failure.

However, if a natural validation failure occurs, capture:

```text
Failure Trigger
Failure Detection
CANDIDATE-002 Response
Evidence Produced
CANDIDATE-001 Response
Recovery
Final Outcome
```

If no failure occurs, record:

```text
Failure Recovery:
NOT TESTED
```

Do not infer robustness from a successful run.

---

# 17. Attribution Matrix

Create an explicit attribution matrix:

| Outcome | Evidence Source | Classification | Confidence |
|---|---|---|---|
| Revision boundary | | DIRECTLY_OBSERVED / INFERENCE | |
| Validation required | | DIRECTLY_OBSERVED / INFERENCE | |
| Validation request | | DIRECTLY_OBSERVED / NOT_ESTABLISHED | |
| CANDIDATE-002 invocation | | DIRECTLY_OBSERVED / NOT_ESTABLISHED | |
| CANDIDATE-002 result | | DIRECTLY_OBSERVED / NOT_ESTABLISHED | |
| Evidence consumption | | DIRECTLY_OBSERVED / INFERENCE | |
| Final revision decision | | DIRECTLY_OBSERVED / INFERENCE | |
| Supporting pytest/ruff result | | DIRECTLY_OBSERVED | |
| Scope preservation | | DIRECTLY_OBSERVED / INFERENCE | |

Use the strongest defensible classification.

---

# 18. Experiment Outcome

Classify the overall EXP-M2-003 result as exactly one:

```text
SUCCESS
PARTIAL_SUCCESS
FAILED
BLOCKED
```

Definitions:

### SUCCESS

Use only if:

- validation requirement was legitimately determined;
- CANDIDATE-002 was actually requested;
- CANDIDATE-002 was actually invoked;
- expected evidence was produced;
- CANDIDATE-001 consumed the evidence;
- attribution is sufficiently direct;
- revision boundary remained controlled.

### PARTIAL_SUCCESS

Use when:

- some dependency stages succeeded;
- but one or more required stages could not be established.

### FAILED

Use when:

- the experiment executed;
- the dependency path was exercised;
- but the intended composition behavior did not work.

### BLOCKED

Use when:

- the experiment could not meaningfully test the dependency path because required capability/infrastructure was unavailable.

Do not use SUCCESS merely because the repository tests pass.

---

# 19. Evidence Quality

Assess:

```text
Evidence Quality:
STRONG
MODERATE
WEAK
MIXED
```

Also assess:

```text
Attribution:
DIRECT
SUPPORTED
WEAK
NOT_ESTABLISHED
```

And:

```text
Reproducibility:
HIGH
MEDIUM
LOW
```

Explain each classification.

---

# 20. Evidence Gap Closure

Explicitly determine whether EXP-M2-003 closes the Stage E critical gap:

```text
CANDIDATE-001 → CANDIDATE-002 dependency REQUEST / invocation /
evidence consumption
```

Use:

```text
CLOSED
PARTIALLY_CLOSED
NOT_CLOSED
```

Do not claim closure if any critical part remains unobserved.

Use this state chain:

```text
IDENTIFIED
    ↓
REQUESTED
    ↓
INVOKED
    ↓
SUCCEEDED / FAILED
    ↓
EVIDENCE CONSUMED
```

The final classification must show exactly how far the experiment progressed.

---

# 21. No Lifecycle Promotion

This stage does NOT decide whether CANDIDATE-001 becomes:

```text
VALIDATED
IMPLEMENTATION_READY
```

Do not perform lifecycle promotion here.

Do not overwrite the Stage E disposition.

The purpose is to generate new evidence.

A later assessment stage will determine whether the new evidence changes the lifecycle state.

---

# 22. Required Experiment Record

Create the Stage F experiment record according to repository naming conventions.

Prefer:

```text
10-stage-f-exp-m2-003-invocation-and-evidence-capture.md
```

if consistent with existing numbering.

The document must contain at least:

```text
# MILESTONE-002 Stage F — EXP-M2-003

## Objective

## Experiment Scope

## Authoritative Inputs

## Experiment Selection

## Validation Requirement Determination

## Revision Boundary

## Execution Procedure

## Validation Request Record

## CANDIDATE-002 Invocation

## Dependency State Tracking

## Supporting Engineering Validation

## Evidence Consumption

## Human Intervention

## Failure Handling

## Attribution Matrix

## Evidence Quality

## Evidence Gap Closure

## Experiment Outcome

## Limitations

## Conclusion
```

Adjust naming only to match repository conventions.

---

# 23. Update MILESTONE-002

Update:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md
```

Record:

- Stage F execution;
- EXP-M2-003 objective;
- selected task;
- dependency path status;
- experiment outcome;
- evidence gap closure status;
- supporting validation results;
- limitations;
- next required review stage.

Do not rewrite historical Stage A–E conclusions.

Do not prematurely change:

```text
CONDITIONALLY_VALIDATED
```

to:

```text
VALIDATED
```

Stage F only generates evidence.

---

# 24. Engineering Validation

After experiment execution and documentation:

Run applicable checks.

At minimum:

```bash
pytest
```

```bash
ruff check .
```

```bash
mypy src
```

```bash
git diff --check
```

If a validation command fails:

1. record exact command;
2. record exact failure;
3. determine whether failure is relevant to EXP-M2-003;
4. do not silently retry until green;
5. do not reinterpret failure as dependency evidence.

---

# 25. Diff Review

Before completion:

```bash
git status
git diff --stat
git diff
```

Verify:

- only intended experiment files changed;
- no unrelated production changes;
- no accidental historical rewrite;
- no generated junk;
- no unsupported claims;
- no attribution regression;
- no lifecycle promotion;
- no Skill/Workflow packaging.

---

# 26. Quality Gate

Stage F is complete only when:

- [ ] Authentic task selected
- [ ] Validation requirement explicitly determined
- [ ] Revision boundary recorded
- [ ] CANDIDATE-002 request explicitly recorded
- [ ] CANDIDATE-002 invocation explicitly classified
- [ ] Dependency state table completed
- [ ] Supporting validation separated
- [ ] Evidence production recorded
- [ ] Evidence consumption assessed
- [ ] Human intervention recorded
- [ ] Failure behavior recorded or marked NOT TESTED
- [ ] Attribution matrix completed
- [ ] Evidence quality assessed
- [ ] Critical gap closure assessed
- [ ] Experiment outcome classified
- [ ] No lifecycle promotion performed
- [ ] MILESTONE-002 updated
- [ ] pytest result recorded
- [ ] ruff result recorded
- [ ] mypy result recorded
- [ ] git diff --check result recorded
- [ ] Git diff reviewed

---

# 27. Execution Discipline

Follow exactly:

```text
READ
 ↓
INSPECT
 ↓
SELECT AUTHENTIC TASK
 ↓
DEFINE BOUNDARY
 ↓
DETERMINE VALIDATION REQUIREMENT
 ↓
REQUEST CANDIDATE-002
 ↓
INVOKE CANDIDATE-002
 ↓
CAPTURE EVIDENCE
 ↓
CONSUME EVIDENCE
 ↓
VALIDATE
 ↓
ASSESS EXPERIMENT
 ↓
DOCUMENT
 ↓
DIFF REVIEW
 ↓
STOP
```

Do NOT:

```text
READ
 ↓
IMPLEMENT NEW ASSET
 ↓
PACKAGE SKILL
```

Do NOT:

```text
pytest PASS
 ↓
declare CANDIDATE-002 success
```

Do NOT:

```text
Stage F experiment
 ↓
automatically promote CANDIDATE-001
```

---

# 28. Final Execution Report

At the end, provide:

```text
MILESTONE-002 Stage F completed.

Experiment:
EXP-M2-003

Task:
<selected task>

Validation Requirement:
YES / NO

CANDIDATE-002 Requested:
YES / NO

CANDIDATE-002 Invoked:
SUCCEEDED / FAILED / BLOCKED / NOT_TESTED

Evidence Produced:
<summary>

Evidence Consumed by CANDIDATE-001:
CONSUMED / PARTIALLY_CONSUMED / PRODUCED_BUT_NOT_CONSUMED / NOT_AVAILABLE

Dependency Gap Closure:
CLOSED / PARTIALLY_CLOSED / NOT_CLOSED

Experiment Outcome:
SUCCESS / PARTIAL_SUCCESS / FAILED / BLOCKED

Evidence Quality:
STRONG / MODERATE / WEAK / MIXED

Attribution:
DIRECT / SUPPORTED / WEAK / NOT_ESTABLISHED

Reproducibility:
HIGH / MEDIUM / LOW

Lifecycle Promotion:
NOT PERFORMED

Files Changed:
<list>

pytest:
PASS / FAIL / NOT RUN

ruff:
PASS / FAIL / NOT RUN

mypy:
PASS / FAIL / NOT RUN

git diff --check:
PASS / FAIL

Git Diff Reviewed:
YES / NO

Git Commit:
<commit>

Git Push:
SUCCESS / FAILED
```

Do not claim:

```text
CANDIDATE-002 succeeded
```

unless the actual dependency invocation occurred.

Do not claim:

```text
Critical gap closed
```

unless REQUEST → INVOKE → RESULT → CONSUME is sufficiently evidenced.

After completing the experiment and pushing the changes, STOP.

Do not start a subsequent assessment or packaging stage.
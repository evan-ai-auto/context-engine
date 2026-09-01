# MILESTONE-002 Stage C2 — EXP-M2-002 Experimental Invocation

## 0. Mission

Continue:

```text
MILESTONE-002
Asset Experimental Validation
```

Previous sequence:

```text
Stage A
Validation Experiment Framework
        ↓
Stage B1
EXP-M2-001 Selection
        ↓
Stage B2
EXP-M2-001 Invocation
        ↓
Stage B3
EXP-M2-001 Evidence Assessment
        ↓
Stage C1
Evidence Gap Analysis & Second Experiment Selection
        ↓
Stage C2
EXP-M2-002 Experimental Invocation
```

Stage C1 selected:

```text
Experiment:
EXP-M2-002

Primary Validation Subject:
CANDIDATE-001
Targeted Engineering Revision

Engineering Task:
Domain Enum Entity-Level Test Plan Completion
```

The mission of Stage C2 is:

```text
Apply the CANDIDATE-001 procedure
to the selected real engineering task
and record what actually happens.
```

Stage C2 is:

```text
Experimental Invocation
```

It is NOT:

```text
Evidence Assessment

Asset Validation Decision

Asset Promotion

Asset Packaging

Composition Validation
```

---

# 1. Mandatory Reading

Before making any change, read:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md

ai-engineering/milestones/MILESTONE-002/
01-validation-experiment-framework.md

ai-engineering/milestones/MILESTONE-002/
02-stage-b1-first-experiment-selection.md

ai-engineering/milestones/MILESTONE-002/
03-stage-b2-exp-m2-001-experimental-invocation.md

ai-engineering/milestones/MILESTONE-002/
04-stage-b3-exp-m2-001-evidence-and-assessment.md

ai-engineering/milestones/MILESTONE-002/
05-stage-c1-evidence-gap-and-second-experiment-selection.md
```

Then read the authoritative design:

```text
ai-engineering/milestones/MILESTONE-001/
05-candidate-001-targeted-engineering-revision.md
```

Also read the experiment source materials:

```text
ai-engineering/sessions/TASK-002/04-test-plan.md

ai-engineering/tasks/
TASK-002-revision-002-Serialization Contract Completion.md
```

Inspect current repository state before modification.

Do not rely only on Stage C1 summaries.

---

# 2. Experiment Identity

```text
Experiment ID:
EXP-M2-002

Experiment Type:
Single Asset Experimental Invocation

Primary Validation Subject:
CANDIDATE-001
Targeted Engineering Revision

Engineering Task:
Domain Enum Entity-Level Test Plan Completion
```

The experiment is designed to address evidence gaps from EXP-M2-001:

```text
Medium Complexity

Test / Code Artifact Revision

Revision Boundary Discovery

Multi-file Coordination

Meaningful Validation

Reduced External Boundary Reinforcement
```

---

# 3. Core Experimental Rule

Apply the CANDIDATE-001 lifecycle:

```text
Inspect
        ↓
Understand
        ↓
Define Revision Boundary
        ↓
Plan
        ↓
Execute Revision
        ↓
Determine Validation Requirement
        ↓
Supporting Engineering Validation
        ↓
Report
        ↓
STOP
```

Important:

```text
Do NOT skip directly:

Finding
↓
Modify Tests
```

The procedure itself is under observation.

---

# 4. Experiment Safety Boundary

The Stage C1 Safety Boundary is mandatory.

Allowed area:

```text
TASK-002 domain contract test completion

tests/domain/

Directly related test-only artifacts
when genuinely required
```

Forbidden:

```text
Domain architecture redesign

Production feature development

Repository-wide refactor

Unrelated cleanup

CLI implementation

.ai-context generation work

MILESTONE-001 redesign

Asset packaging

Lifecycle promotion
```

Production source changes:

```text
src/
```

are out of scope unless:

```text
A genuine implementation defect
is discovered and directly proven.
```

If such a defect appears:

```text
STOP
```

Do not automatically expand scope.

---

# 5. Critical Distinction

Maintain:

```text
Experiment Safety Boundary
≠
Revision Boundary
```

The Safety Boundary is predefined.

The Revision Boundary must be discovered.

Therefore:

```text
DO NOT predefine
the exact list of files to modify.
```

During invocation, CANDIDATE-001 procedure must determine:

```text
In Scope

Out of Scope

Potentially Related but Not Required

Non-Goals
```

Record how this boundary was reached.

---

# 6. Inspect

Inspect:

```text
Current tests/domain/

Relevant entity models

Current enum tests

TASK-002 test plan

Related serialization contract tests

Current repository state
```

Focus on the Stage C1 finding:

```text
Test plan wording indicates
entity-level acceptance expectations
for frozen enum members,

while current entity tests may only
exercise representative enum values.
```

Do not assume the finding is correct.

Verify it.

Possible outcomes include:

```text
Confirmed

Partially Confirmed

Not Confirmed
```

If the finding is not confirmed:

```text
STOP
```

and record:

```text
Experiment Task Invalidated by Inspection
```

Do not invent changes merely to continue EXP-M2-002.

---

# 7. Understand

Restate the verified engineering problem.

Determine:

```text
What the test plan requires

What current tests actually prove

What is missing

Whether the missing coverage is meaningful

Whether the change belongs to
Targeted Engineering Revision
```

Explicitly distinguish:

```text
Test Redundancy
```

from:

```text
Missing Contract Coverage
```

Do not assume:

```text
More Tests
=
Better Validation
```

The objective is:

```text
Contract Traceability
```

not:

```text
Maximum Test Count.
```

---

# 8. Define Revision Boundary

Before modifying files, explicitly define:

```text
Revision Objective

In Scope

Out of Scope

Non-Goals

Acceptance Criteria
```

The boundary must emerge from inspection.

Do NOT use:

```text
Modify all domain tests
```

unless evidence genuinely requires it.

Prefer:

```text
Minimal Sufficient Revision
```

Possible categories:

```text
Entity test modules directly affected

Shared test helpers
if genuinely required

Existing enum fixtures
if genuinely required
```

Production code remains:

```text
Out of Scope
```

unless a proven defect requires escalation.

Record:

```text
Why each category is
In Scope / Out of Scope.
```

---

# 9. Plan

Create a minimal revision plan.

The plan should answer:

```text
Which verified gap is being addressed?

Which test artifacts need modification?

Why are those files required?

What is the expected acceptance evidence?

What validation is required?
```

Do NOT over-plan.

Do NOT create a full implementation architecture document.

This is a:

```text
Targeted Revision
```

not:

```text
Feature Delivery Project.
```

---

# 10. Execute Revision

Execute only the approved revision plan.

Possible implementation pattern may include:

```text
Parametrized Entity-Level Tests
```

but do not preselect implementation before inspection.

The implementation must demonstrate:

```text
Test Plan Requirement
        ↓
Concrete Test Coverage
```

Avoid:

```text
Blind duplication of test_enums.py
```

The revised tests should provide evidence that:

```text
Entity models
accept the relevant frozen enum values
```

when that is actually the contract requirement.

---

# 11. Scope Discipline

During execution monitor:

```text
New files discovered

Unexpected related gaps

Potential cleanup opportunities

Production code questions

Additional enum coverage opportunities
```

For each:

```text
Required for Revision Objective?
```

If:

```text
NO
```

then:

```text
Leave Out of Scope.
```

If:

```text
UNCLEAR
```

record:

```text
Boundary Decision Required
```

and prefer:

```text
STOP / EXCLUDE
```

rather than uncontrolled expansion.

---

# 12. Human Intervention Record

Record every meaningful intervention.

For each intervention:

```text
Intervention

Why It Occurred

Procedure Step

Normal Engineering Judgment?

Procedure Gap?

Experiment Constraint?

Task-Specific?

Unknown?
```

Important:

```text
Human Intervention
≠
Automatic Experiment Failure
```

But do not hide interventions.

Especially record if the human:

```text
Predefines file scope

Predefines solution

Overrides boundary discovery

Overrides stop condition

Supplies the core reasoning
that the procedure should have produced
```

---

# 13. Procedure Adaptation Record

Record every deviation from the conceptual procedure.

For each:

```text
Expected Procedure

Actual Procedure

Reason for Adaptation

Experiment Constraint?

Task Characteristic?

Procedure Ambiguity?

Normal Engineering Practice?
```

Do not automatically interpret adaptation as:

```text
Asset Failure.
```

But preserve the evidence.

---

# 14. Validation Requirement Determination

CANDIDATE-001 design states that:

```text
Code or Tests Changed
```

generally requires validation evidence.

Therefore explicitly determine:

```text
Validation Required?
```

Expected determination should be based on:

```text
Changed Tests

Acceptance Criteria

Regression Risk
```

Record:

```text
Why validation is required
or not required.
```

Do not silently skip this step.

---

# 15. Critical Experiment Isolation Rule

EXP-M2-002 validates:

```text
CANDIDATE-001 only.
```

Therefore:

```text
DO NOT invoke
CANDIDATE-002
as an experimental subject.
```

However:

```text
pytest
ruff
git diff --check
```

may still be run as:

```text
Supporting Engineering Validation.
```

Critical attribution rule:

```text
Running pytest
≠
Validating CANDIDATE-002.
```

Also:

```text
pytest success
≠
Evidence that CANDIDATE-001
owns validation execution.
```

Record the relationship explicitly:

```text
CANDIDATE-001 determined
that validation evidence was required.

Because EXP-M2-002 is isolated
to CANDIDATE-001,
CANDIDATE-002 was not invoked
as an asset.

Repository validation commands were executed
as supporting engineering validation
outside asset attribution.
```

Classify this as:

```text
Experiment Isolation Adaptation
```

not:

```text
Validation Dependency Success.
```

---

# 16. Supporting Engineering Validation

Run appropriate validation based on actual changes.

Expected baseline:

```bash
pytest
```

Also run where applicable:

```bash
ruff check tests/
git diff --check
```

If:

```text
src/
```

changes unexpectedly occur:

```text
STOP
```

unless the proven-defect exception has been explicitly established.

Do not claim:

```text
CANDIDATE-002 Passed
```

Do not claim:

```text
Validation Dependency Proven.
```

Only record:

```text
Supporting Engineering Validation Results.
```

---

# 17. Validation Failure Handling

If validation fails:

```text
Determine whether the failure
is inside the discovered Revision Boundary.
```

If:

```text
YES
```

repair within boundary and rerun.

If:

```text
NO
```

then:

```text
STOP
```

Record:

```text
External Failure / Unrelated Failure
```

Do not automatically expand the revision.

---

# 18. Required Invocation Record

Create:

```text
ai-engineering/milestones/MILESTONE-002/
06-stage-c2-exp-m2-002-experimental-invocation.md
```

Suggested structure:

```text
# MILESTONE-002 Stage C2 — EXP-M2-002 Experimental Invocation

## 1. Experiment Identity

## 2. Mission

## 3. Engineering Task

## 4. Independent Task Verification

## 5. Experiment Safety Boundary

## 6. Inspection

## 7. Finding Verification

## 8. Understanding

## 9. Revision Boundary Discovery

## 10. Revision Plan

## 11. Execution

## 12. Scope Decisions

## 13. Human Intervention Record

## 14. Procedure Adaptations

## 15. Validation Requirement Determination

## 16. Experiment Isolation Adaptation

## 17. Supporting Engineering Validation

## 18. Resulting Repository Change

## 19. Observations

## 20. Unknowns

## 21. Stop Condition
```

The document must describe:

```text
What Happened
```

not:

```text
Why CANDIDATE-001 Succeeded.
```

Do not perform evidence assessment in C2.

---

# 19. Observation Discipline

Separate:

```text
Observed Fact
```

from:

```text
Interpretation.
```

Use:

```text
Observed

Recorded

Detected

Changed

Passed

Failed
```

Avoid:

```text
Proved

Validated

Guaranteed

Caused
```

unless directly justified.

Example:

```text
Good:
The procedure produced an explicit revision boundary
before file modification.

Not Yet Justified:
The procedure prevented scope creep.
```

The second statement belongs to later assessment.

---

# 20. Failure Signals

Review the pre-defined signals from Stage C1.

Record whether each is:

```text
Observed

Not Observed

Inconclusive
```

Signals include:

```text
Boundary cannot be determined

Revision scope expands into production redesign

Human performs core procedure responsibility

Procedure adds no observable structure

Tests do not map to plan requirements

Validation failures cannot be resolved
within boundary

Task reveals architecture change need
```

Important:

```text
Not Observed
≠
Proven Absent.
```

---

# 21. Stop Conditions

STOP immediately if:

```text
Independent finding cannot be verified

Task requires architecture redesign

Production model changes become necessary
without a proven defect

Revision boundary cannot be safely determined

Experiment isolation becomes impossible

Required task changes exceed
Targeted Engineering Revision responsibility
```

Stopping is valid experimental evidence.

Do not force completion.

---

# 22. Update MILESTONE-002.md

Update:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md
```

to reflect:

```text
Stage C2
EXP-M2-002 Experimental Invocation
COMPLETED
```

And:

```text
Experiment EXP-M2-002:
INVOCATION COMPLETED
ASSESSMENT NOT YET PERFORMED
```

Do NOT mark:

```text
CANDIDATE-001
```

as:

```text
VALIDATED
```

Do NOT make:

```text
Asset Disposition.
```

---

# 23. Explicit Non-Goals

Stage C2 must NOT:

```text
Assess EXP-M2-002 evidence

Compare EXP-M2-001 and EXP-M2-002

Promote CANDIDATE-001

Reject CANDIDATE-001

Modify CANDIDATE-001 design

Package SKILL.md

Evaluate CANDIDATE-002

Perform asset composition validation

Perform portfolio decision
```

Stage C2 is:

```text
Experimental Invocation
```

only.

---

# 24. Required Review Checklist

Before commit verify:

```text
[ ] Task finding independently verified

[ ] No artificial task created

[ ] Safety Boundary respected

[ ] Revision Boundary discovered

[ ] Exact file list was not predetermined

[ ] Finding understood before modification

[ ] Revision objective explicit

[ ] In-scope / out-of-scope explicit

[ ] Revision plan exists before modification

[ ] Changes map to verified test-plan requirement

[ ] No unrelated cleanup occurred

[ ] Human interventions recorded

[ ] Procedure adaptations recorded

[ ] Validation requirement explicitly determined

[ ] CANDIDATE-002 not evaluated

[ ] Supporting validation attribution is explicit

[ ] pytest results recorded

[ ] Validation failures handled within boundary

[ ] No evidence assessment performed

[ ] No lifecycle promotion occurred
```

---

# 25. Final Report Before Commit

Before commit report:

## Experiment

```text
EXP-M2-002
```

## Task Verification

```text
Confirmed / Partially Confirmed / Invalidated
```

## Revision Objective

```text
...
```

## Revision Boundary

```text
In Scope:
...

Out of Scope:
...
```

## Files Changed

```text
...
```

## Boundary Discovery Notes

```text
...
```

## Human Interventions

```text
...
```

## Procedure Adaptations

```text
...
```

## Validation Requirement

```text
Required / Not Required
```

## Experiment Isolation Adaptation

```text
...
```

## Supporting Engineering Validation

```text
pytest:
...

ruff:
...

diff check:
...
```

## Failure Signals

```text
Observed:
...

Not Observed:
...

Inconclusive:
...
```

## Observations

```text
...
```

## Unknowns

```text
...
```

## Files Changed

Expected minimum:

```text
Created:
ai-engineering/milestones/MILESTONE-002/
06-stage-c2-exp-m2-002-experimental-invocation.md

Modified:
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md

Plus:
Actual bounded engineering test artifacts
discovered during the experiment.
```

Unlike Stage C1:

```text
Engineering file changes
are expected.
```

But all changes must remain within:

```text
Revision Boundary
+
Experiment Safety Boundary.
```

---

# 26. Validation Before Commit

Run:

```bash
git status
git diff --check
git diff
```

Then required supporting validation:

```bash
pytest
```

And applicable:

```bash
ruff check tests/
```

Review:

```text
Changed files

Unexpected changes

Scope compliance
```

Do not commit unrelated modifications.

---

# 27. Commit

Suggested commit:

```text
test(milestone-002): run second candidate validation experiment
```

Then commit and push.

---

# 28. Stop Condition

After push:

```text
STOP.
```

Do NOT automatically:

```text
Assess EXP-M2-002

Compare experiments

Modify CANDIDATE-001

Make disposition

Start cross-experiment review
```

After completion, report exactly:

```text
MILESTONE-002 Stage C2 completed and pushed.
```
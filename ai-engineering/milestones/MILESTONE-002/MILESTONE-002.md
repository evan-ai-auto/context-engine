# MILESTONE-002 — Asset Experimental Validation

## 1. Mission

Validate designed AI Engineering assets through controlled usage in real engineering work.

```text
Real Engineering Task
        ↓
Asset Selection
        ↓
Experimental Invocation
        ↓
Observation
        ↓
Evidence Collection
        ↓
Assessment
        ↓
Disposition Decision
```

Focus:

```text
Prospective Validation
```

not:

```text
Retrospective Discovery
```

---

## 2. Background

MILESTONE-001 completed with:

```text
Closeout Decision: CLOSE_WITH_OBSERVATIONS
Goal Assessment:   ACHIEVED
Portfolio:         MINIMAL_SUFFICIENT
Asset readiness:   VALIDATION_READY (not VALIDATED)
```

MILESTONE-001 established:

```text
Historical Evidence
        ↓
Engineering Patterns
        ↓
Asset Candidates
        ↓
Candidate Governance
        ↓
Asset Architecture
        ↓
Validation Readiness
```

Primary references:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
ai-engineering/milestones/MILESTONE-001/11-stage-e-asset-validation-plan.md
ai-engineering/milestones/MILESTONE-001/12-final-architecture-review-and-closeout.md
```

```text
MILESTONE-002 must NOT repeat asset discovery.
MILESTONE-002 must NOT modify MILESTONE-001 artifacts.
```

---

## 3. Current Portfolio (Validation Subjects)

| ID | Name | Type | Status |
|---|---|---|---|
| CANDIDATE-001 | Targeted Engineering Revision | SKILL | CONDITIONALLY_VALIDATED |
| CANDIDATE-002 | Repository Tooling Validation Gate | SKILL | VALIDATION_READY |
| CANDIDATE-003 | Task Closeout Lifecycle | WORKFLOW | VALIDATION_READY |
| CANDIDATE-004 | Explicit Task Boundary Definition | SKILL | VALIDATION_READY |

Out of Stage A validation scope as subjects:

```text
CANDIDATE-005 — OBSERVE_ONLY
PATTERN-006   — DEFERRED
```

Architectural principles carried forward:

```text
Designed Asset ≠ Validated Asset
Validated Asset ≠ Implementation Ready
Composable Portfolio ≠ Mandatory Pipeline
Asset Output ≠ External Acceptance
More Process ≠ Better Engineering
More Assets ≠ Better Portfolio
```

---

## 4. Milestone Strategy

```text
Validate assets progressively.
Single Asset First (generally).
Evidence Before Packaging.
Human-Guided Asset Selection.
Real Engineering Work as preferred evidence source.
Intentional experiments — not every task is an experiment.
```

```text
Experimental Invocation ≠ Asset Packaging
```

Design documents may be used as experimental procedures without creating
Skill/Workflow/Agent runtime packages.

---

## 5. Planned Stages

```text
Stage A
Validation Experiment Framework

Stage B
First Asset Experimental Validation

Stage C
Validation Evidence Review

Stage D
Asset Disposition Decision

Stage E
Portfolio Expansion Decision
```

```text
Stage names may be refined later.
Do not over-specify future stage internals in Stage A.
```

---

## 6. Explicit Non-Goals

```text
No premature packaging (SKILL.md / WORKFLOW.md / Agents / Rules)
No automatic invocation / orchestration engine
No simultaneous validation of all assets in Stage A
No MILESTONE-001 redesign
No CANDIDATE-005 promotion
No runtime validation platform / database
No treating one experiment as final VALIDATED disposition
```

---

## 7. Status

```text
MILESTONE-002

Status:
IN_PROGRESS

Current Stage:
Stage G — EXP-M2-003 Evidence Assessment & Candidate-001 Lifecycle Reassessment
Status: COMPLETED

Completed Stages:
- Stage A — Validation Experiment Framework
- Stage B1 — First Experiment Selection & Definition
- Stage B2 — EXP-M2-001 Experimental Invocation
- Stage B3 — EXP-M2-001 Evidence & Assessment
- Stage C1 — Evidence Gap Analysis & Second Experiment Selection
- Stage C2 — EXP-M2-002 Experimental Invocation
- Stage C2 Revision-001 — Validation Dependency Attribution Correction
- Stage C3 — EXP-M2-002 Evidence & Assessment
- Stage D — Cross-Experiment Evidence Synthesis
- Stage E — Evidence Sufficiency & Asset Disposition Review
- Stage F — EXP-M2-003 Invocation & Evidence Capture
- Stage G — EXP-M2-003 Evidence Assessment & Candidate-001 Lifecycle Reassessment

Experiment EXP-M2-001:
Outcome: MIXED EVIDENCE (assessment complete)

Experiment EXP-M2-002:
Outcome: MIXED EVIDENCE (assessment complete)

Experiment EXP-M2-003:
Outcome: SUCCESS (invocation complete)
Dependency Gap Closure: PARTIALLY_CLOSED (confirmed in Stage G)
Assessment: COMPLETED (Stage G)

Stage G Assessment:
CANDIDATE-001 Lifecycle: CONDITIONALLY_VALIDATED (RETAINED)
Stage E Disposition: PROMOTE_WITH_CONDITIONS (RETAINED; conditions recalibrated)
Dependency Composition: HAPPY_PATH_OBSERVED / FAILURE_PATH_NOT_ESTABLISHED
Packaging Readiness: NOT_READY
CANDIDATE-002 Independent Status: VALIDATION_READY (not independently validated)

Evidence Sufficiency (Stage E baseline):
SUFFICIENT_WITH_LIMITATIONS — dependency happy path improved; failure path open

Packaging:
NONE

Recommended Next Step (pending authorization):
EXP-M2-004 — Failure/ERROR-path composition test (001 ← 002 non-PASSED evidence)
without treating CONDITIONALLY_VALIDATED as VALIDATED or authorizing packaging.
```

Milestone outputs:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md
ai-engineering/milestones/MILESTONE-002/01-validation-experiment-framework.md
ai-engineering/milestones/MILESTONE-002/02-stage-b1-first-experiment-selection.md
ai-engineering/milestones/MILESTONE-002/03-stage-b2-exp-m2-001-experimental-invocation.md
ai-engineering/milestones/MILESTONE-002/04-stage-b3-exp-m2-001-evidence-and-assessment.md
ai-engineering/milestones/MILESTONE-002/05-stage-c1-evidence-gap-and-second-experiment-selection.md
ai-engineering/milestones/MILESTONE-002/06-stage-c2-exp-m2-002-experimental-invocation.md
ai-engineering/milestones/MILESTONE-002/07-stage-c3-exp-m2-002-evidence-and-assessment.md
ai-engineering/milestones/MILESTONE-002/08-stage-d-cross-experiment-evidence-synthesis.md
ai-engineering/milestones/MILESTONE-002/09-stage-e-evidence-sufficiency-and-asset-disposition.md
ai-engineering/milestones/MILESTONE-002/10-stage-f-exp-m2-003-invocation-and-evidence-capture.md
ai-engineering/milestones/MILESTONE-002/11-stage-g-exp-m2-003-evidence-assessment-and-lifecycle-reassessment.md
```

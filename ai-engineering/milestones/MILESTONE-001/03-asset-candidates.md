# 03 — Asset Candidates

## 1. Purpose

```text
Stage A
Historical Engineering Evidence

        ↓

Stage B
Engineering Pattern Extraction

        ↓

Stage C
Asset Candidate Identification
```

```text
This document identifies potential reusable AI Engineering assets.

It does not create assets.

It does not approve assets.

Formal candidate design occurs in Stage D.
```

```text
Pattern ≠ Asset
Asset Candidate ≠ Approved Asset
Approved Asset ≠ Implemented Asset
```

---

## 2. Input Boundary

Stage C consumes:

```text
ai-engineering/milestones/MILESTONE-001/02-engineering-patterns.md
```

Rules applied:

```text
Patterns marked READY_FOR_STAGE_C
→ full candidate evaluation

Patterns marked NEEDS_MORE_EVIDENCE
→ light evaluation only; not promoted without explicit justification
```

| Pattern | Stage B Extraction Readiness | Stage C treatment |
|---|---|---|
| PATTERN-001 | READY_FOR_STAGE_C | Full evaluation |
| PATTERN-002 | READY_FOR_STAGE_C | Full evaluation |
| PATTERN-003 | READY_FOR_STAGE_C | Full evaluation |
| PATTERN-004 | READY_FOR_STAGE_C | Full evaluation |
| PATTERN-005 | READY_FOR_STAGE_C | Full evaluation |
| PATTERN-006 | NEEDS_MORE_EVIDENCE | Light evaluation → defer |
| PATTERN-007 | READY_FOR_STAGE_C | Full evaluation |
| PATTERN-008 | NEEDS_MORE_EVIDENCE | Light evaluation → merge/reject as independent |
| PATTERN-009 | NEEDS_MORE_EVIDENCE | Light evaluation → merge into closeout |

No silent re-extraction of patterns. No modification of Stage B conclusions.

---

## 3. Candidate Evaluation Framework

Dimensions (qualitative: HIGH / MEDIUM / LOW):

```text
Reusability
Generality
Trigger Clarity
Input / Output Clarity
Procedural Determinism
Reasoning Autonomy
Orchestration Value
```

Candidate type hypotheses (not implementation decisions):

```text
SKILL
  Clear trigger, stable procedure, limited autonomy

AGENT
  Exploration, judgment, variable path

WORKFLOW
  Multi-step lifecycle coordination

COMPOSITE
  Workflow/Agent + supporting Skills (hypothesis only)

NONE
  Useful pattern that should not become an asset now
```

Status values:

```text
STRONG_CANDIDATE
EMERGING_CANDIDATE
DEFERRED
REJECTED
```

---

## 4. Pattern-to-Candidate Evaluation Matrix

| Pattern | Reusability | Generality | Trigger | I/O | Determinism | Autonomy | Orchestration | Candidate Type | Status |
|---|---|---|---|---|---|---|---|---|---|
| PATTERN-001 | HIGH | HIGH | HIGH | HIGH | HIGH | LOW–MEDIUM | MEDIUM | SKILL | → CANDIDATE-001 STRONG |
| PATTERN-002 | HIGH | HIGH | HIGH | HIGH | MEDIUM | MEDIUM | HIGH | WORKFLOW | → CANDIDATE-003 STRONG |
| PATTERN-003 | HIGH | HIGH | HIGH | HIGH | HIGH | LOW | LOW | SKILL | → CANDIDATE-002 STRONG |
| PATTERN-004 | HIGH | HIGH | HIGH | HIGH | HIGH | LOW | LOW | SKILL | → CANDIDATE-004 EMERGING |
| PATTERN-005 | MEDIUM | MEDIUM | MEDIUM | MEDIUM | MEDIUM | HIGH | MEDIUM | AGENT (via merge) | → CANDIDATE-005 EMERGING |
| PATTERN-006 | MEDIUM | MEDIUM | MEDIUM | MEDIUM | MEDIUM | HIGH | LOW | AGENT | DEFERRED (no promote) |
| PATTERN-007 | MEDIUM | MEDIUM | MEDIUM | HIGH | MEDIUM | MEDIUM | MEDIUM | WORKFLOW (via merge) | → CANDIDATE-005 EMERGING |
| PATTERN-008 | MEDIUM | MEDIUM | MEDIUM | MEDIUM | MEDIUM | MEDIUM | MEDIUM | NONE | REJECTED as independent; support CANDIDATE-002 |
| PATTERN-009 | MEDIUM | MEDIUM | MEDIUM | MEDIUM | LOW | MEDIUM | LOW | NONE | REJECTED as independent; support CANDIDATE-003 |

The matrix is an evaluation aid. Pattern ≠ Candidate.

---

## 5. Merge / Split / Reject Analysis

### Investigation Area A — Validation cluster

```text
PATTERN-001 Review → Targeted Revision → Validation
PATTERN-003 Tooling Validation Gate
PATTERN-008 Layered Validation Composition
```

Findings:

```text
Not three independent assets.

PATTERN-003 is a stable, highly deterministic supporting capability
(pytest / ruff / mypy [+ optional hygiene]). Clear Skill hypothesis.

PATTERN-008 describes composing multiple validation layers at a gate.
Evidence is weaker (strong once at TASK-002 C2; partial on TASK-001).
Treating it as a separate Workflow/Skill would overlap PATTERN-003
and duplicate steps already inside PATTERN-001 and PATTERN-002.

PATTERN-001 already includes Validation as a step after revision.
It should invoke tooling validation, not own a second validation product.
```

Decision:

```text
PATTERN-003 → independent SKILL candidate (CANDIDATE-002)

PATTERN-008 → REJECTED as independent candidate;
              retain as supporting design note under CANDIDATE-002
              (optional layered checks when a contract/boundary gate exists)

PATTERN-001 → independent SKILL candidate (CANDIDATE-001);
              may call CANDIDATE-002 as a supporting capability later
              (COMPOSITE linkage hypothesis only — not implemented)
```

### Investigation Area B — Lifecycle cluster

```text
PATTERN-002 Task Closeout Lifecycle
PATTERN-004 Explicit Task Boundary Definition
PATTERN-009 Learning Capture After Friction
```

Findings:

```text
These are related to task lifecycle but are not identical capabilities.

PATTERN-002 has clear orchestration value (validate → status → docs → deferrals).
Strong Workflow hypothesis across both completed tasks.

PATTERN-004 occurs at task start (hard in/out of scope), not at closeout.
Merging it into “closeout” would distort timing.
Splitting into Task-Start Skill + Closeout Skill + Learning Skill
would fragment without enough independent evidence for three assets.

PATTERN-009 forms differ (dedicated learning file vs closeout section)
and Stage B marked NEEDS_MORE_EVIDENCE.
Best treated as an internal closeout activity, not a standalone Skill.
```

Decision:

```text
PATTERN-002 → WORKFLOW candidate (CANDIDATE-003), STRONG
PATTERN-009 → merge as supporting/internal step of CANDIDATE-003; REJECTED alone
PATTERN-004 → separate EMERGING SKILL (CANDIDATE-004);
              not auto-bundled into closeout; avoid further split into
              “task start workflow” without more evidence
```

### Investigation Area C — Architecture / contract cluster

```text
PATTERN-005 Decision → Freeze → Implement
PATTERN-007 Contract → Implement → Contract Test
```

Findings:

```text
Both are STRUCTURAL, single-task (TASK-002) chains.
High sophistication does not equal high generality.

They share a freeze-before-build philosophy but differ:
  005 emphasizes architecture decision autonomy
  007 emphasizes contract ↔ test traceability

Useful across architecture/domain tasks (including non-Python),
but sample size = 1 task chain. Not STRONG yet.

Agent hypothesis is plausible for 005 (judgment-heavy).
007 is more procedural once the contract exists.
Merging into one COMPOSITE hypothesis avoids two overlapping Stage D designs.
```

Decision:

```text
PATTERN-005 + PATTERN-007 → merge into CANDIDATE-005 COMPOSITE (EMERGING)
Stage D readiness: NEEDS_MORE_EVIDENCE (do not over-design yet)
```

### Investigation Area D — Compatibility inspection

```text
PATTERN-006 Repository Compatibility Inspection
```

Findings:

```text
Stage B: STRUCTURAL, occurrence = 1, maturity OBSERVED,
Extraction Readiness = NEEDS_MORE_EVIDENCE.

Clear structure exists, but promoting to STRONG would violate Stage B.
```

Decision:

```text
DEFERRED — no STRONG/EMERGING candidate created for Stage D design.
Revisit after another pre-implementation inspection on a future task.
```

### Split analysis

```text
No pattern required splitting into multiple candidates.

Absorptions (merge-down) preferred over proliferation.
```

---

## 6. Candidate Definitions

## CANDIDATE-001 — Targeted Engineering Revision

### Source Patterns

```text
Primary:
PATTERN-001 Review → Targeted Revision → Validation

Supporting (future linkage hypothesis only):
PATTERN-003 / CANDIDATE-002 Tooling Validation Gate
```

### Candidate Hypothesis

A reusable capability that, given review findings, defines a narrow revision scope, applies targeted changes without redesign, validates results, and closes findings.

### Candidate Type Hypothesis

```text
SKILL

Why:
Clear trigger (findings), stable procedure, stable I/O,
limited autonomy relative to open-ended exploration.
Orchestration value is present but mostly within one capability.
```

### Trigger

```text
Structured review produces findings that require corrective work
before approval, continuation, or closeout.
```

### Likely Inputs

```text
Review findings

Current repository / docs / tests state

Task or revision scope constraints

Non-goals (no redesign / no feature creep)
```

### Expected Outputs

```text
Revision scope statement

Changed artifacts (docs and/or tests; scoped code only if justified)

Validation evidence

Finding disposition (RESOLVED / DONE / APPROVED)
```

### Evaluation

```text
Reusability: HIGH
Generality: HIGH
Trigger Clarity: HIGH
Input / Output Clarity: HIGH
Procedural Determinism: HIGH
Reasoning Autonomy: LOW–MEDIUM
Orchestration Value: MEDIUM
```

### Boundary

```text
Handles:
Finding-driven, narrowly scoped corrective cycles with validation.

Does Not Handle:
Greenfield feature implementation
Architecture redesign
Full task closeout orchestration
Defining initial task out-of-scope lists
```

### Status

```text
STRONG_CANDIDATE

Repeated evidence (4 related cycles), clear boundary,
credible Skill hypothesis, justified for Stage D design.
```

### Stage D Readiness

```text
READY_FOR_DESIGN
```

---

## CANDIDATE-002 — Repository Tooling Validation Gate

### Source Patterns

```text
Primary:
PATTERN-003 Tooling Validation Gate

Supporting (absorbed, not independent):
PATTERN-008 Layered Validation Composition
  → optional extra layers (contract/boundary/hygiene) when the gate requires them
```

### Candidate Hypothesis

A reusable capability that runs the repository’s standard quality gates (typically pytest, ruff, mypy, and optional hygiene such as `git diff --check`) and records pass/fail evidence for accept, revision, or closeout decisions.

### Candidate Type Hypothesis

```text
SKILL

Why:
Highly deterministic procedure, clear I/O, low autonomy.
Layered extras are configuration of the same gate, not a second asset.
```

### Trigger

```text
A stage, revision, or closeout requires automated quality evidence
before acceptance.
```

### Likely Inputs

```text
Repository working tree

Configured tooling (pyproject / CI equivalents)

Declared required gate set for the stage
```

### Expected Outputs

```text
Command results (pass/fail)

Recorded validation evidence suitable for checklists/closeout
```

### Evaluation

```text
Reusability: HIGH
Generality: HIGH
Trigger Clarity: HIGH
Input / Output Clarity: HIGH
Procedural Determinism: HIGH
Reasoning Autonomy: LOW
Orchestration Value: LOW
```

### Boundary

```text
Handles:
Standard automated quality gates and evidence capture.
Optional inclusion of additional declared checks for a gate.

Does Not Handle:
Authoring project-specific tests
Product acceptance criteria outside tooling
Architecture boundary judgment (may be invoked by a higher gate)
```

### Status

```text
STRONG_CANDIDATE

Repeated across TASK-001 and TASK-002; strongest deterministic Skill signal.
```

### Stage D Readiness

```text
READY_FOR_DESIGN
```

---

## CANDIDATE-003 — Task Closeout Lifecycle

### Source Patterns

```text
Primary:
PATTERN-002 Task Closeout Lifecycle

Supporting (internal activity, not separate asset):
PATTERN-009 Learning Capture After Friction
```

### Candidate Hypothesis

A reusable lifecycle coordination capability that finalizes a completed engineering task: final validation, status update to DONE, closeout documentation, deferred-work capture, and optional lessons capture.

### Candidate Type Hypothesis

```text
WORKFLOW

Why:
Multiple dependent steps with lifecycle coordination value.
Not a single procedure Skill; not primarily exploratory Agent work.
```

### Trigger

```text
Implementation and required revisions are complete;
the task needs auditable formal closure.
```

### Likely Inputs

```text
Implemented deliverable

Prior validation results

Task/stage status documents

Deferred-scope statements from task briefs
```

### Expected Outputs

```text
Updated task status (DONE / stage COMPLETED)

Closeout document

Deferred work list

Lessons / learning notes (when friction or closeout requires them)
```

### Evaluation

```text
Reusability: HIGH
Generality: HIGH
Trigger Clarity: HIGH
Input / Output Clarity: HIGH
Procedural Determinism: MEDIUM
Reasoning Autonomy: MEDIUM
Orchestration Value: HIGH
```

### Boundary

```text
Handles:
Formal completion of a DONE task with records and deferrals.

Does Not Handle:
Mid-stage approvals only
Continuous documentation during implementation
Standalone learning-skill productization
Initial task boundary definition (see CANDIDATE-004)
```

### Status

```text
STRONG_CANDIDATE

Observed on both completed tasks; clear workflow shape.
```

### Stage D Readiness

```text
READY_FOR_DESIGN
```

---

## CANDIDATE-004 — Explicit Task Boundary Definition

### Source Patterns

```text
Primary:
PATTERN-004 Explicit Task Boundary Definition
```

### Candidate Hypothesis

A reusable capability that, at task definition time, produces explicit in-scope and out-of-scope / non-goals statements used to constrain execution and closeout compliance checks.

### Candidate Type Hypothesis

```text
SKILL

Why:
Clear trigger and I/O, high determinism, low autonomy.
Kept separate from closeout to avoid incorrect lifecycle bundling.
```

### Trigger

```text
A new task starts with material risk of scope expansion
into later product capabilities.
```

### Likely Inputs

```text
Task objective

Project roadmap / adjacent capabilities

Known non-goals from prior tasks
```

### Expected Outputs

```text
In-scope list

Out-of-scope / non-goals list

Constraints referenced by later review/closeout
```

### Evaluation

```text
Reusability: HIGH
Generality: HIGH
Trigger Clarity: HIGH
Input / Output Clarity: HIGH
Procedural Determinism: HIGH
Reasoning Autonomy: LOW
Orchestration Value: LOW
```

### Boundary

```text
Handles:
Writing and maintaining explicit task exclusions.

Does Not Handle:
Full task planning workflows
Implementation
Closeout orchestration
```

### Status

```text
EMERGING_CANDIDATE

Repeated on both tasks, but structure is simple and forms vary.
Credible Skill, not yet as strong as revision/validation/closeout.
```

### Stage D Readiness

```text
READY_FOR_DESIGN
```

Lightweight design only; do not expand into a full task-start workflow.

---

## CANDIDATE-005 — Spec Freeze and Contract Delivery

### Source Patterns

```text
Primary Patterns:
PATTERN-005 Decision → Freeze → Implement
PATTERN-007 Contract → Implement → Contract Test
```

### Candidate Hypothesis

A reusable composite capability for architecture-sensitive work: reconcile and freeze decisions, finalize contracts where needed, implement against the freeze, and validate via contract-linked tests/traceability.

### Candidate Type Hypothesis

```text
COMPOSITE

Why:
Combines judgment-heavy freeze (Agent-like) with more procedural
contract-test delivery (Skill/Workflow-like).
Single COMPOSITE hypothesis avoids two overlapping Stage D designs.
Not promoted to separate Agent + Workflow yet (sample size = 1).
```

### Trigger

```text
A task requires stable architecture/domain vocabulary before coding,
and/or a formal contract with test-plan traceability.
```

### Likely Inputs

```text
Architecture proposals / drafts

Review findings on decisions

Existing repository packaging/tooling constraints

Domain requirements
```

### Expected Outputs

```text
Frozen decision records

Domain/API contract

Implementation matching freeze

Contract validation / traceability evidence
```

### Evaluation

```text
Reusability: MEDIUM
Generality: MEDIUM
Trigger Clarity: MEDIUM
Input / Output Clarity: MEDIUM–HIGH
Procedural Determinism: MEDIUM
Reasoning Autonomy: HIGH (freeze phase)
Orchestration Value: MEDIUM
```

### Boundary

```text
Handles:
Freeze-before-build and contract-first delivery for architecture-heavy tasks.

Does Not Handle:
Bootstrap-only tasks with no architecture decisions
Routine bugfix revisions (CANDIDATE-001)
Repository compatibility inspection as a standalone product (deferred)
```

### Status

```text
EMERGING_CANDIDATE

Stage B marked both source patterns READY_FOR_STAGE_C structurally,
but only one task sample. Not STRONG.
```

### Stage D Readiness

```text
NEEDS_MORE_EVIDENCE
```

May sketch boundaries in Stage D only if review agrees; prefer waiting for another architecture-heavy task.

---

## Deferred / Rejected (no Stage D design)

### PATTERN-006 — Repository Compatibility Inspection

```text
Status: DEFERRED
Candidate Type: AGENT (hypothetical only)
Stage D Readiness: DO_NOT_DESIGN

Reason:
Single occurrence; Stage B NEEDS_MORE_EVIDENCE.
Do not create CANDIDATE ID for design until reused.
```

### PATTERN-008 — Layered Validation Composition

```text
Status: REJECTED as independent asset
Disposition: supporting note under CANDIDATE-002

Reason:
Overlaps tooling gate; weak repetition; would cause validation-asset explosion.
```

### PATTERN-009 — Learning Capture After Friction

```text
Status: REJECTED as independent asset
Disposition: internal step under CANDIDATE-003

Reason:
Inconsistent form; Stage B NEEDS_MORE_EVIDENCE;
avoid Learning Skill fragmentation.
```

---

## 7. Candidate Consolidation

| Candidate | Source Patterns | Type Hypothesis | Status | Stage D Readiness |
|---|---|---|---|---|
| CANDIDATE-001 Targeted Engineering Revision | PATTERN-001 (+003 linkage) | SKILL | STRONG_CANDIDATE | READY_FOR_DESIGN |
| CANDIDATE-002 Repository Tooling Validation Gate | PATTERN-003 (+008 support) | SKILL | STRONG_CANDIDATE | READY_FOR_DESIGN |
| CANDIDATE-003 Task Closeout Lifecycle | PATTERN-002 (+009 support) | WORKFLOW | STRONG_CANDIDATE | READY_FOR_DESIGN |
| CANDIDATE-004 Explicit Task Boundary Definition | PATTERN-004 | SKILL | EMERGING_CANDIDATE | READY_FOR_DESIGN |
| CANDIDATE-005 Spec Freeze and Contract Delivery | PATTERN-005 + PATTERN-007 | COMPOSITE | EMERGING_CANDIDATE | NEEDS_MORE_EVIDENCE |

### Strong Candidates

```text
CANDIDATE-001
CANDIDATE-002
CANDIDATE-003
```

### Emerging Candidates

```text
CANDIDATE-004
CANDIDATE-005
```

### Deferred Candidates

```text
PATTERN-006 Repository Compatibility Inspection
(no candidate ID promoted)
```

### Rejected Candidates (as independent assets)

```text
PATTERN-008 Layered Validation Composition
PATTERN-009 Learning Capture After Friction
```

---

## 8. Explicit Non-Goals (confirmed)

```text
No Skills created under ai-engineering/extraction/skills/

No Agents created under ai-engineering/extraction/agents/

No Workflows created under ai-engineering/extraction/workflows/

No Prompt Templates

No Agent Instructions

No Skill / Workflow definitions as implementable packages

No production code / tests / Context Engine runtime changes

No modifications to TASK-001 / TASK-002 historical records

No modifications to Stage A inventory or Stage B pattern conclusions
```

Stage C is candidate identification only.

---

## 9. Evidence Limitations (inherited)

```text
Current sample size: 2 completed tasks

Candidate conclusions remain provisional.

Strong candidates still require Stage D design review and later validation.

COMPOSITE / AGENT hypotheses must not be treated as approved architectures.
```

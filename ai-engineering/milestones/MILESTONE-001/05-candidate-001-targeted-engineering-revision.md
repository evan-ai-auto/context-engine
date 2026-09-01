# CANDIDATE-001 — Targeted Engineering Revision

## 1. Design Scope

```text
Candidate
        ↓
Asset Classification
        ↓
Asset Design
```

This document is the **Asset Design Specification** for CANDIDATE-001.

```text
This stage does NOT implement the asset.

No Skill package, Agent, Workflow runtime, or Cursor rule is created here.
```

Design is governed by:

```text
ai-engineering/milestones/MILESTONE-001/04-candidate-design-framework.md
AI Engineering Asset Taxonomy v0.1
```

Stage C source:

```text
ai-engineering/milestones/MILESTONE-001/03-asset-candidates.md
→ CANDIDATE-001 STRONG_CANDIDATE / READY_FOR_DESIGN
```

---

## 2. Evidence Basis

### Trace

```text
Historical Process (TASK-001 / TASK-002 revision cycles)
        ↓
PATTERN-001 Review → Targeted Revision → Validation
        ↓
CANDIDATE-001 Targeted Engineering Revision
        ↓
This Asset Design
```

### Minimum justifying evidence

```text
Why the Candidate exists:
  Four related revision cycles after review findings:
  - TASK-001 closeout addressing review findings
  - TASK-001 Revision-001 Engineering Hygiene
  - TASK-002 Revision-001 Review Feedback Fix
  - TASK-002 Revision-002 Serialization Contract Completion

Why it should become an Asset:
  Repeated structure, clear I/O, high reusability/generality,
  Stage C STRONG_CANDIDATE with READY_FOR_DESIGN.

Why SKILL is appropriate:
  Finding-triggered, narrowly scoped, procedurally repeatable,
  limited autonomy vs open-ended exploration (see §16).
```

Primary references:

```text
01-process-inventory.md §8 Revision Inventory
02-engineering-patterns.md PATTERN-001
03-asset-candidates.md CANDIDATE-001
```

```text
Historical Evidence supports the design.
Historical Evidence does not automatically define implementation.
```

---

## 3. Asset Classification

### Nature

```text
What does this reusable asset fundamentally represent?

A bounded corrective capability:
given a finding / revision request,
plan and execute a controlled revision,
request validation evidence,
and report disposition — without redesign or feature expansion.
```

Nature: **Capability** (executable, procedural).

### Classification

```text
Asset Category: EXECUTABLE
Asset Type:     SKILL
```

```text
Classification follows nature.
Nature does not follow preferred implementation.
```

Rationale summary: see §16 (Why SKILL?).

---

## 4. Asset Identity

| Field | Value |
|---|---|
| Asset Name | Targeted Engineering Revision |
| Candidate ID | CANDIDATE-001 |
| Asset Category | EXECUTABLE |
| Asset Type | SKILL |
| Design Version | 0.1 |
| Status | DESIGNED |

```text
Status is DESIGNED — not IMPLEMENTED.
```

---

## 5. Purpose and Value

### Purpose

Provide a reusable Skill that turns a **bounded revision request** (typically from review findings) into a **controlled revision outcome**: scoped plan, targeted changes, requested validation evidence, and explicit disposition — without becoming a generic “fix everything” agent.

### Primary Value

```text
Consistent, reviewable, scope-safe corrective cycles
across engineering tasks and repositories.
```

### Engineering Problem Solved

```text
Review findings and similar bounded issues often lead to either:
  - uncontrolled scope expansion / redesign, or
  - incomplete fixes without validation / disposition.

This asset standardizes: inspect → bound → plan → revise →
request validation → report → stop.
```

### Expected Reuse Context

```text
Post-review documentation / test / scoped code fixes
Contract or serialization coverage gaps
Hygiene revisions after closeout review
Any engineering situation with an identifiable revision target
and acceptance criteria, without exploratory architecture work
```

---

## 6. Trigger Model

Invocation-oriented asset. Trigger Model is mandatory.

### Positive Trigger Conditions

Use when **all** of the following hold:

```text
- A bounded revision target has been identified
  (finding ID, inconsistency, coverage gap, hygiene issue, etc.)

- Revision objective is stated or can be stated without redesign

- Scope boundary / non-goals are available or can be derived
  (e.g. docs-only, tests-only, no architecture redesign)

- Acceptance criteria for “done” can be stated
```

Typical trigger sources (not exclusive):

```text
EVENT   — external review feedback / finding disposition required
EXPLICIT — operator requests a targeted revision against a finding
STATE   — stage blocked on APPROVED_WITH_MINOR_FIXES / similar
```

### Negative Trigger Conditions

Do **not** use when:

```text
- The problem is still exploratory and the target state is undefined

- The work requires architecture redesign or new product capability

- The request is full task closeout (that is CANDIDATE-003 territory)

- The request is only “run the test suite” with no revision objective
  (that is CANDIDATE-002 territory)

- Scope cannot be bounded without inventing a new program of work
```

```text
This Skill must not become a Universal Fix Everything Skill.
```

---

## 7. Input Model

### Required Inputs

```text
Revision Target
  What artifact / behavior / finding is being addressed

Revision Objective
  What “corrected” means in one bounded statement

Evidence / Findings
  Review finding text, gap description, or equivalent evidence

Scope Boundary
  In-scope / out-of-scope / non-goals for this revision

Acceptance Criteria
  Conditions under which the revision may be considered complete
  (before or after repository validation evidence)
```

### Optional Inputs

```text
Known Constraints
  e.g. docs-only, tests-only, no dependency changes

Preferred Validation Gate Set
  which CANDIDATE-002 checks to request (if not default)

Related Artifacts
  links to prior revision briefs, contracts, checklists

Prior Validation Evidence
  if already partially validated
```

### Context Inputs

```text
Repository working tree state

Task / stage status documents

Applicable project conventions
```

### Constraints (always)

```text
No redesign of frozen architecture unless the finding explicitly requires
a scoped contract clarification already authorized

No silent feature expansion

Must not require a complete implementation plan as input —
the Skill produces the controlled plan as part of its lifecycle
```

Transformation intent:

```text
Revision Request
        ↓
Controlled Revision Outcome
```

---

## 8. Output Model

### Primary Outputs

```text
Revision Result
  Disposition: RESOLVED / PARTIAL / BLOCKED / ESCALATED / STOPPED

Revision Scope Confirmation
  Final in/out-of-scope statement used during execution

Changed Artifacts Summary
  What changed (paths / categories), not necessarily diffs
```

### Secondary Outputs

```text
Revision Plan (as executed)
  Boundary + steps taken

Remaining Open Issues
  Unresolved items, if any

Stop / Failure Reason
  When not fully resolved
```

### Evidence Outputs

```text
Validation Request Record
  What was requested from CANDIDATE-002,
  or why validation was not required,
  or (if pending) that External Authority authorized deferral

Validation Evidence (consumed)
  Pass/fail / pending results returned by validation capability

Finding Disposition Notes
  Mapping findings → outcomes
```

### Side Effects

```text
May modify repository files within declared scope
  (docs, tests, and only justified scoped code)

Must declare whether files were modified

Must not redefine repository-standard validation procedures
```

Outputs must support human review, downstream workflow, and future automation
without requiring implementation-specific JSON schemas.

---

## 9. Revision Lifecycle

Evidence-aligned procedure (Inspect Before Modify):

```text
1. Inspect
   Read findings, affected artifacts, constraints, current tree

2. Understand
   Restate the problem and intended corrected state

3. Define Revision Boundary
   Lock in-scope / out-of-scope / non-goals for THIS revision

4. Plan
   Ordered change steps; identify whether validation will be requested

5. Execute Revision
   Apply targeted changes only within boundary

6. Validate (orchestrate, do not own execution)
   If required: REQUESTS CANDIDATE-002; consume evidence

7. Report
   Produce revision result, change summary, disposition, open issues

8. Stop
   Explicit terminal state (success, partial, blocked, escalated)
```

Distinctions enforced:

```text
Understanding ≠ Planning ≠ Modification ≠ Validation
```

Avoid:

```text
Finding Issue → Immediately Modify Files
```

Historical alignment: revision briefs historically defined narrow scope before
changes; validation ran after changes when code/tests were affected.

---

## 10. Responsibility Boundary

### Primary Responsibility

```text
Revision Orchestration
```

### Handles (owns)

```text
Scope understanding for the revision request

Revision planning within stated boundary

Change coordination / execution within boundary

Determining whether validation evidence is required
according to declared acceptance criteria

Determining revision acceptance criteria
(excluding independent authorization to defer required validation)

Consuming validation evidence

Deciding whether the revision can be considered complete
when required validation evidence is present,
or when validation was never required per acceptance criteria,
or when an External Authority has authorized deferral

Revision result reporting and stop
```

### Does Not Handle (does not own)

```text
Repository-standard tooling validation procedures
Implementing / duplicating validation-gate execution
  (owned by CANDIDATE-002)

Validation deferral authority
  (whether required validation may be deferred / pending)

Full task closeout lifecycle (CANDIDATE-003)

Initial task boundary definition (CANDIDATE-004)

Architecture redesign / greenfield feature delivery

Autonomous continuous operation without a revision request
```

```text
CANDIDATE-001 owns revision orchestration.
CANDIDATE-002 owns validation execution.
External Authority owns validation deferral authorization.
```

```text
CANDIDATE-001 may identify that validation is required.

CANDIDATE-001 may request validation execution.

CANDIDATE-001 does not independently authorize
the deferral of required validation.
```

Conceptual External Authority categories (implementation-neutral; not assets):

```text
Stage Policy
Task Policy
Workflow
Human Authority
```

---

## 11. Dependency Model

### Relationship

```text
CANDIDATE-001
Targeted Engineering Revision
        │
        │ REQUESTS
        ▼
CANDIDATE-002
Repository Tooling Validation Gate
```

```text
REQUESTS ≠ OWNS
```

Conceptual dependency type: `REQUESTS`  
(Optionally `OPTIONALLY_USES` when validation is not required, e.g. docs-only hygiene with explicit acceptance that skips tooling gates.)

### Dependency Trigger

```text
Request validation when (requirement = YES):
  - code or tests changed, or
  - acceptance criteria require tooling evidence, or
  - stage policy requires a gate before disposition

Do not request validation when (requirement = NO):
  - acceptance criteria explicitly do not require tooling gates
    (e.g. authorized docs-only hygiene with no gate requirement)
  - and that “not required” determination is recorded

Important:
  “Validation not required” is requirement determination.
  It is NOT deferral of required validation.
```

### Validation Request Boundary

From CANDIDATE-001’s perspective, the request interface expectation is:

```text
Input to CANDIDATE-002 (conceptual):
  - declared gate set (default or overridden)
  - repository state after revision
  - optional notes (what changed)

Output from CANDIDATE-002 (conceptual):
  - pass / fail / error per gate
  - recorded evidence suitable for human review
```

CANDIDATE-001 must **not** define CANDIDATE-002’s internal procedure.

### Expected Validation Evidence

```text
Gate results (e.g. pytest / ruff / mypy / hygiene as configured)

Enough detail to support human review of pass/fail
```

### Failure Propagation

```text
If validation FAILS:
  - do not claim RESOLVED
  - either repair within original boundary, or
  - STOP / ESCALATE / RETURN PARTIAL with open issues

If validation REQUIRED + UNAVAILABLE:
  - do not invent gate results
  - do not silently convert Required → Optional
  - do not independently authorize Validation Pending
  - enter External Authority decision boundary:

      If External Authority authorizes deferral:
        → may report Revision Completed / Validation Pending
          (authorized pending only)

      If no authorized deferral:
        → BLOCKED / ESCALATED / AWAITING_EXTERNAL_DECISION
          (Stop instead of silently proceeding)
```

```text
Validation Required
+
Validation Unavailable
≠
Validation Optional
```

---

## 12. Artifact Model

Implementation-neutral artifact responsibilities:

| Artifact | Role | Producer | Consumer |
|---|---|---|---|
| Review Findings / Evidence | Input | External review / prior stage | CANDIDATE-001 |
| Scope Boundary Statement | Working / Output | CANDIDATE-001 | Human review; execution steps |
| Revision Plan | Working | CANDIDATE-001 | Executor (same Skill instance) |
| Changed File Summary | Output | CANDIDATE-001 | Human review; closeout |
| Validation Request | Working | CANDIDATE-001 | CANDIDATE-002 |
| Validation Result / Evidence | Evidence | CANDIDATE-002 | CANDIDATE-001; human review |
| Revision Report / Disposition | Output | CANDIDATE-001 | Downstream workflow; humans |
| Open Issue Record | Output | CANDIDATE-001 | Escalation / follow-up |

```text
Do not create concrete artifact files in this design stage.
Format remains implementation-neutral.
```

---

## 13. Validation Model

### Three-way separation

```text
Validation Requirement
  Who: CANDIDATE-001
  What: whether evidence is required per acceptance criteria

Validation Execution
  Who: CANDIDATE-002
  What: run repository tooling gates; produce evidence

Validation Deferral
  Who: External Authority (Stage/Task Policy, Workflow, Human)
  What: whether required validation may be deferred when unavailable
```

```text
CANDIDATE-001 determines validation necessity.

CANDIDATE-002 executes repository validation.

External Authority determines whether required validation may be deferred.
```

Conceptual flow:

```text
Acceptance Criteria
        ↓
Requirement Determination (CANDIDATE-001)
        ↓
Validation Evidence Required?
        │
        ├── NO → Revision Evaluation → Report → STOP
        │
        └── YES
             ↓
        REQUEST CANDIDATE-002
             ↓
        Validation Available?
             │
        ┌────┴────┐
       YES       NO
        │         │
        ▼         ▼
   Execute     Deferral Decision
  Validation   (External Authority)
        │         │
        ▼    ┌────┴────┐
   Evidence Authorized  Not Authorized
        │         │         │
        ▼         ▼         ▼
  Revision   Pending    BLOCKED /
  Evaluation  Result    ESCALATED
        │         │
        ▼         ▼
      Report → STOP
```

```text
Requirement Determination
        ↓
Validation Request
        ↓
Validation Execution
        ↓
Validation Evidence
```

If execution is unavailable:

```text
Requirement remains unchanged.

Validation unavailable ≠ Validation not required.
```

Deferral Decision must be handled externally — not by CANDIDATE-001 alone.

### Asset Validation (revision success)

CANDIDATE-001 evaluates:

```text
PRECONDITIONS
  Required inputs present; scope boundable

EXECUTION VALIDATION
  Changes stayed within declared boundary
  Inspect/Understand/Plan preceded modification

OUTPUT VALIDATION
  Revision report produced
  Disposition stated
  Unintended change detection performed (within reason)

ACCEPTANCE CRITERIA
  Finding/objective addressed as defined
  Known issues resolved or explicitly remaining
  Required validation evidence present,
  OR validation was not required,
  OR External Authority authorized deferral (pending only)
```

### Repository Validation (delegated)

```text
Executed by CANDIDATE-002 when requested.
CANDIDATE-001 consumes results; does not own gate implementation.
```

### Critical distinction

```text
Revision succeeded
≠
Repository validation automatically succeeded
```

Authorized pending state (only with External Authority):

```text
Revision Completed
Validation Pending
```

when changes are done, validation is still required, evidence is unavailable,
**and** External Authority has authorized deferral — must be explicit in the report.

Without authorized deferral, do not use this state; use BLOCKED / ESCALATED /
AWAITING_EXTERNAL_DECISION instead.

---

## 14. Failure and Stop Conditions

### Failure / stop conditions

```text
Revision Scope Ambiguous
Evidence Insufficient
Acceptance Criteria Missing
Required Dependency Unavailable (validation needed but cannot be requested)
Validation Failed (and cannot repair within boundary)
Unexpected Scope Expansion detected
Redesign required to proceed

Validation Required
+ Validation Unavailable
+ No Authorized Deferral
  → BLOCKED / ESCALATED / AWAITING_EXTERNAL_DECISION
```

The asset must not:

```text
Silently continue when required validation is unavailable

Silently downgrade Required → Optional

Assume validation can be skipped when it is required

Declare completion without required evidence
  unless External Authority authorized deferral
```

### Outcomes

```text
STOP
  Halt; produce report with reason

BLOCKED
  Required validation unavailable; no authorized deferral

ESCALATED
  Hand off to human / architecture / another candidate / External Authority

AWAITING_EXTERNAL_DECISION
  Deferral decision required; stop until External Authority responds

REQUEST CLARIFICATION
  Ask for missing inputs / criteria / authority

RETURN PARTIAL RESULT
  Deliver what is safely in-scope; list remaining open issues
  (must not pretend required validation was optional)
```

```text
Every problem must NOT be automatically fixed.
Knowing when not to continue is a first-class capability.
Stop instead of silently proceeding.
```

---

## 15. Non-Goals

This asset does **not**:

```text
Exploratory architecture design

Large-scale repository refactoring

Own repository validation execution (CANDIDATE-002)

Perform full task closeout (CANDIDATE-003)

Define initial task boundaries (CANDIDATE-004)

Automatic candidate promotion / asset extraction

Asset implementation / packaging

Autonomous continuous operation without a revision request

Become a Generic Engineering Agent
```

---

## 16. Type Rationale — Why SKILL?

### Selected

```text
EXECUTABLE → SKILL
```

### Why not AGENT?

```text
Does not require open-ended repository exploration as primary mode.
Decision authority is bounded by findings + scope + acceptance criteria.
Stop conditions are procedural, not goal-seeking autonomy.
```

### Why not WORKFLOW?

```text
Internal steps are a procedure within one capability.
Does not primarily orchestrate multiple independent lifecycle stages
(closeout, boundary definition, etc.).
May REQUEST another Skill; that is dependency, not a multi-stage Workflow.
```

### Why not RULE?

```text
Does not merely constrain behavior; it performs corrective work.
```

### Why not CHECKLIST / TEMPLATE?

```text
Not only verification items or a document skeleton.
Produces planned changes and dispositions.
```

### Why not COMPOSITE (yet)?

```text
Primary nature is a single Skill with a REQUESTS dependency.
COMPOSITE packaging may be reconsidered after CANDIDATE-002 is designed,
but is not required to express this asset’s nature.
```

```text
A reusable capability ≠ an Agent.
```

---

## 17. Interaction Model

Conceptual only — not runtime orchestration:

```text
External Finding / Revision Request
        ↓
CANDIDATE-001
Targeted Engineering Revision
        ↓
Inspect
        ↓
Understand
        ↓
Bound Scope
        ↓
Plan Revision
        ↓
Execute Revision
        ↓
Request Validation (when required)
        │
        ▼
CANDIDATE-002
Repository Tooling Validation Gate
        │
        ▼
Validation Evidence
        │
        ▼
CANDIDATE-001
        ↓
Revision Report + Disposition
        ↓
STOP
```

---

## 18. Implementation Readiness

### Evaluation

| Dimension | Assessment |
|---|---|
| Identity Clarity | Clear |
| Trigger Clarity | Clear (positive + negative) |
| Input Clarity | Clear (required vs optional) |
| Output Clarity | Clear |
| Responsibility Boundary | Clear vs CANDIDATE-002; deferral authority external |
| Dependency Boundary | REQUESTS modeled |
| Validation Model | Requirement / Execution / Deferral separated |
| Failure Model | Explicit stop/block/escalate; no silent downgrade |

### Readiness state

```text
CONDITIONALLY_READY
```

Reasons:

```text
READY:
  Design is reviewable and implementation-neutral.
  Boundaries and dependency direction are explicit.
  Validation Authority Boundary is now defined:
    CANDIDATE-001 = requirement determination
    CANDIDATE-002 = execution
    External Authority = deferral authorization

CONDITIONS:
  CANDIDATE-002 must be designed (Stage D2B) before implementing
  the validation request interface end-to-end.
  Concrete External Authority binding (which Stage/Task Policy /
  Workflow / Human path applies) remains for design review /
  later policy work — not independently invented by this Skill.
  Default gate-set policy should be confirmed in design review.
  Packaging location / runtime binding intentionally deferred.
```

Framework mapping:

```text
Design Status: DESIGNED
Implementation Readiness: REQUIRES_EVIDENCE / design peer (CANDIDATE-002)
  before READY_FOR_IMPLEMENTATION
```

---

## 19. Open Questions

```text
EVIDENCE_GAP / IMPLEMENTATION_UNKNOWN
  Should default gate sets be repository-global or stage-policy-driven?

BOUNDARY_RISK
  When docs-only revisions skip tooling gates, what minimum human
  review evidence is mandatory?

DEPENDENCY_RISK
  Which External Authority path authorizes Validation Pending
  in common stage policies (without making CANDIDATE-001 the authorizer)?

IMPLEMENTATION_UNKNOWN
  Should revision planning ever be split into a separate Skill, or
  remain an internal lifecycle phase of this Skill?

VALIDATION_UNKNOWN
  How strictly must unintended-change detection be evidenced
  (diff summary vs formal review checklist)?
```

Do not force premature answers in this design.

---

## 20. Design Summary

```text
Asset Name:     Targeted Engineering Revision
Asset Category: EXECUTABLE
Asset Type:     SKILL
Status:         DESIGNED
Primary Purpose:
  Turn a bounded revision request into a controlled revision outcome
  with inspect-before-modify discipline, delegated validation, and
  explicit stop/disposition reporting.
```

```text
Owns:     Revision orchestration; validation requirement determination
Delegates: Repository tooling validation execution → CANDIDATE-002 (REQUESTS)
           Validation deferral authorization → External Authority
Does not: Own validation gates, deferral authority, closeout,
          task-boundary definition, redesign
```

```text
CANDIDATE-001 REQUESTS CANDIDATE-002
```

```text
Implementation Readiness: CONDITIONALLY_READY
(await CANDIDATE-002 design + gate-policy review)
```

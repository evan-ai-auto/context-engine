# MILESTONE-001 Stage D2C — CANDIDATE-003 Asset Design

## 0. Mission

Design the third Strong Candidate identified during:

```text
MILESTONE-001 Stage C
Asset Candidate Identification
```

Target:

```text
CANDIDATE-003
Task Closeout Lifecycle
```

This stage performs:

```text
Candidate
        ↓
Asset Classification
        ↓
Asset Design
```

This stage does NOT perform:

```text
Asset Implementation
```

The objective is to produce a complete, reviewable, implementation-neutral design for CANDIDATE-003.

The primary design question is:

```text
How should an engineering task move from
"work appears complete"
to
"task can be formally closed"
without collapsing validation, acceptance,
deferred work, lessons, and closure into one step?
```

---

# 1. Mandatory Reading

Before making any changes, read:

```text
ai-engineering/milestones/MILESTONE-001/
03-asset-candidates.md

ai-engineering/milestones/MILESTONE-001/
04-candidate-design-framework.md

ai-engineering/milestones/MILESTONE-001/
05-candidate-001-targeted-engineering-revision.md

ai-engineering/milestones/MILESTONE-001/
06-candidate-002-repository-tooling-validation-gate.md

ai-engineering/milestones/MILESTONE-001/
MILESTONE-001.md
```

Also inspect historical evidence and patterns:

```text
ai-engineering/milestones/MILESTONE-001/
01-process-inventory.md

ai-engineering/milestones/MILESTONE-001/
02-engineering-patterns.md
```

Important:

Do not design the workflow from the candidate title alone.

Trace:

```text
Historical Process
        ↓
Engineering Pattern
        ↓
Candidate
```

The workflow must remain evidence-grounded.

---

# 2. Target Candidate

Design:

```text
CANDIDATE-003
```

Conceptual name:

```text
Task Closeout Lifecycle
```

The final asset identity may refine the conceptual name if necessary.

However:

```text
Do not rename the candidate without architectural justification.
```

---

# 3. Scope

Create one new design document:

```text
ai-engineering/milestones/MILESTONE-001/
07-candidate-003-task-closeout-lifecycle.md
```

Update:

```text
ai-engineering/milestones/MILESTONE-001/
MILESTONE-001.md
```

Expected changes:

```text
Create:
07-candidate-003-task-closeout-lifecycle.md

Modify:
MILESTONE-001.md
```

Do NOT modify:

```text
01-process-inventory.md

02-engineering-patterns.md

03-asset-candidates.md

04-candidate-design-framework.md

05-candidate-001-targeted-engineering-revision.md

06-candidate-002-repository-tooling-validation-gate.md
```

Do NOT create:

```text
Actual Workflow Implementation

Runtime Orchestrator

Agent

Skill

Rule

Cursor Configuration

Task Management Integration

GitHub Automation

CI/CD Configuration
```

This stage produces only:

```text
Workflow Design Specification
```

---

# 4. Evidence Basis

Create a concise section documenting:

```text
Historical Process
        ↓
Engineering Pattern
        ↓
CANDIDATE-003
```

Explain why the following activities repeatedly appear near task completion:

```text
Validation

Evidence Review

Acceptance Decision

Deferred Work Capture

Lesson Capture

Repository Update

Task Closure
```

Important:

Do NOT reproduce the entire historical process.

Focus only on evidence relevant to closeout lifecycle design.

The objective is to establish:

```text
Task Closeout
```

as a reusable engineering process pattern rather than an ad-hoc checklist.

---

# 5. Asset Classification

Classify CANDIDATE-003 using:

```text
AI Engineering Asset Taxonomy v0.1
```

Evaluate:

```text
Asset Category

Asset Type
```

Expected direction:

```text
Category:
ORCHESTRATION

Type:
WORKFLOW
```

But classification must be justified.

Explicitly compare against:

```text
SKILL

AGENT

RULE

CHECKLIST

TEMPLATE
```

Apply:

```text
Classification follows nature.
Nature does not follow preferred implementation.
```

The design must answer:

```text
Why is Task Closeout a multi-step lifecycle?

Why is it not a single SKILL?

Why is it not merely a CHECKLIST?

Why does it require explicit transitions?

Why does it stop rather than operate autonomously?
```

---

# 6. Asset Identity

Define:

```text
Asset Name

Candidate ID

Asset Category

Asset Type

Version

Status
```

Suggested:

```text
Status:
DESIGNED
```

Do NOT mark:

```text
IMPLEMENTED
```

---

# 7. Purpose and Value

Define:

```text
Purpose

Primary Value

Engineering Problem Solved

Expected Reuse Context
```

The problem should NOT be described merely as:

```text
Close the task.
```

Instead address:

```text
How can engineering work transition from execution
to trustworthy closure through explicit evidence,
authority boundaries, and lifecycle transitions?
```

The workflow should prevent:

```text
Implementation Finished
        ↓
Assumed Complete
        ↓
Task Closed
```

without explicit closeout reasoning.

---

# 8. Workflow Trigger Model

Define when Task Closeout Lifecycle should begin.

Evaluate positive triggers such as:

```text
Primary Work Completed

Revision Completed

Implementation Candidate Ready

Explicit Closeout Request

Milestone Stage Ready For Closure
```

Also define negative triggers.

Examples:

```text
Primary Work Still In Progress

Required Evidence Not Yet Available

Known Blocking Failure

Task Scope Still Unresolved
```

Do not blindly use these examples.

Derive the final trigger model from workflow nature.

Important distinction:

```text
Ready for Closeout
```

does not mean:

```text
Already Closed
```

---

# 9. Workflow Entry Contract

Define the minimum information required to enter the workflow.

Evaluate:

```text
Task Identity

Task Scope

Expected Completion Criteria

Produced Artifacts

Validation Requirement Context

Available Validation Evidence

Known Deferred Work

Known Open Issues

External Authority Context
```

Separate:

```text
Required Inputs
```

from:

```text
Optional Inputs
```

Important:

The workflow should not require every upstream implementation detail.

It should consume:

```text
Evidence
```

rather than duplicate execution logic.

---

# 10. Core Lifecycle Model

Design the lifecycle explicitly.

Recommended conceptual direction:

```text
READY_FOR_CLOSEOUT
        │
        ▼
COLLECT_EVIDENCE
        │
        ▼
REVIEW_VALIDATION
        │
        ▼
RESOLVE_OPEN_ITEMS
        │
        ├───────────────┐
        │               │
        ▼               ▼
READY_FOR_ACCEPTANCE   BLOCKED
        │
        ▼
EXTERNAL_ACCEPTANCE
        │
        ├───────────────┐
        │               │
        ▼               ▼
ACCEPTED            NOT_ACCEPTED
        │               │
        ▼               ▼
CAPTURE_CLOSEOUT    RETURN / STOP
        │
        ▼
CLOSED
```

Do NOT blindly copy this model.

The final lifecycle must distinguish at minimum:

```text
Entry

Evidence Collection

Validation Review

Open Item Resolution

Acceptance

Closeout Recording

Closure

Blocked / Return Paths
```

Avoid:

```text
Done
↓
Closed
```

---

# 11. Lifecycle State Model

Define conceptual lifecycle states.

Evaluate states such as:

```text
NOT_STARTED

READY_FOR_CLOSEOUT

COLLECTING_EVIDENCE

REVIEWING

BLOCKED

AWAITING_ACCEPTANCE

ACCEPTED

CLOSING

CLOSED
```

Do not introduce unnecessary states.

Every state must answer:

```text
What does this state mean?

What evidence exists?

What transition is allowed?

Who owns the transition?

What exits this state?
```

Important:

Do not turn the workflow into an exhaustive state machine implementation.

This is a design-level lifecycle model.

---

# 12. Evidence Collection Model

Define what closeout evidence may be collected.

Evaluate:

```text
Produced Artifacts

Validation Evidence

Repository Evidence

Known Failures

Known Deferred Work

Open Questions

Review Findings
```

Important distinction:

```text
Evidence Collection
```

does NOT mean:

```text
Execute all validation tools again.
```

CANDIDATE-003 should consume evidence where available.

It may request evidence generation through another asset, but should not duplicate CANDIDATE-002's execution responsibility.

Conceptually:

```text
CANDIDATE-003
        │
        │ Validation Evidence Required
        ▼
CANDIDATE-002
        │
        ▼
Validation Evidence
        │
        ▼
CANDIDATE-003
```

---

# 13. Validation Review Model

Define how validation evidence is reviewed during closeout.

Important boundary:

```text
Validation Execution
≠
Validation Review
```

CANDIDATE-002 owns:

```text
Repository-aware validation execution.
```

CANDIDATE-003 owns:

```text
Closeout-oriented evidence review.
```

The workflow should evaluate questions such as:

```text
Is required validation evidence present?

Are required gates represented?

Are validation failures visible?

Are execution errors visible?

Is validation incomplete?

Does unresolved validation prevent progression?
```

Important:

CANDIDATE-003 should NOT reinterpret:

```text
FAILED
```

as:

```text
PASSED
```

Nor should it hide:

```text
ERROR

NOT_EXECUTED
```

The workflow must preserve validation semantics.

---

# 14. Open Item Resolution Model

Define how unresolved work is handled.

Evaluate categories:

```text
Blocking Issue

Non-Blocking Deferred Work

Known Limitation

Open Question

Future Improvement
```

Important:

The workflow must distinguish:

```text
Can Close?
```

from:

```text
Everything Is Perfect
```

A task may have deferred work.

However:

```text
Deferred Work
```

must not become:

```text
Silently Ignored Work
```

Define requirements for explicit capture.

Conceptual model:

```text
Open Item
        │
        ├── Blocking
        │       │
        │       ▼
        │     BLOCKED
        │
        └── Non-Blocking
                │
                ▼
        Explicit Deferred Record
                │
                ▼
        Acceptance Review
```

Do not decide acceptance policy automatically.

---

# 15. Blocking Model

Define what conditions block workflow progression.

Evaluate:

```text
Missing Required Evidence

Required Validation Failure

Validation Execution Error

Unresolved Blocking Issue

Missing Acceptance Authority

Scope Ambiguity
```

Do not blindly classify every problem as blocking.

The key requirement:

```text
Blocking Status
```

must be explicit.

The workflow should not silently continue past a blocking condition.

---

# 16. Acceptance Authority Model

This is a critical section.

Explicitly define:

```text
Evidence Review
```

versus:

```text
Acceptance Decision
```

CANDIDATE-003 may prepare:

```text
Closeout Evidence Package
```

but should NOT autonomously decide:

```text
The task is acceptable.
```

unless explicit external authority has delegated that decision.

Default conceptual model:

```text
Workflow
        │
        ▼
Evidence Package
        │
        ▼
External Acceptance Authority
        │
        ├── Accepted
        │
        └── Not Accepted
```

Define:

```text
Who provides acceptance?

What evidence is presented?

What happens if acceptance is unavailable?

What happens if acceptance is rejected?
```

Important:

Do not hard-code:

```text
Human Approval Required
```

if the architecture allows policy or upstream workflow authority.

Use:

```text
External Acceptance Authority
```

as the conceptual abstraction unless repository evidence requires something more specific.

---

# 17. Acceptance vs Closure

Explicitly distinguish:

```text
ACCEPTED
```

from:

```text
CLOSED
```

These are not necessarily the same.

Example:

```text
Accepted
        ↓
Capture Deferred Work
        ↓
Capture Lessons
        ↓
Update Closeout Record
        ↓
Closed
```

Therefore:

```text
Acceptance
```

is an input to closure.

It is not closure itself.

The design must preserve this distinction.

---

# 18. Closeout Recording Model

Define what information is recorded during closeout.

Evaluate:

```text
Task Identity

Scope Summary

Produced Artifacts

Validation Summary

Validation Evidence References

Acceptance Outcome

Deferred Work

Known Limitations

Lessons / Improvement Signals

Closure Timestamp or Equivalent Context
```

Important:

Do not prescribe a specific storage mechanism.

Do NOT assume:

```text
GitHub Issue

Markdown File

Database

Task Management System
```

The design should define:

```text
What must be recorded
```

not:

```text
Exactly where it must be stored
```

---

# 19. Deferred Work Model

Define the lifecycle treatment of deferred work.

A deferred item should include conceptually:

```text
Identity

Reason

Known Impact

Why It Is Not Blocking

Follow-Up Context
```

Important:

The workflow must not automatically determine:

```text
Non-Blocking
```

without external authority or explicit policy.

Instead:

```text
Classification
```

and:

```text
Acceptance
```

must remain traceable.

Avoid:

```text
TODO
```

as the only deferred work mechanism.

---

# 20. Lesson Capture Model

Evaluate whether the workflow should capture reusable engineering signals.

Potential examples:

```text
Repeated Failure Pattern

Tooling Limitation

Process Friction

Candidate Asset Opportunity

Missing Rule

Missing Template

Missing Skill

Missing Workflow
```

Important:

Do NOT implement extraction here.

CANDIDATE-003 may:

```text
Capture Improvement Signals
```

but should NOT:

```text
Automatically Create New Assets
```

This is important because future asset extraction is a separate capability.

The model should support:

```text
Task Closeout
        ↓
Improvement Signal
        ↓
Future Extraction / Review
```

without coupling them.

---

# 21. Dependency Model

Define conceptual dependencies.

CANDIDATE-003 may consume:

```text
Task Context

Produced Artifact Evidence

Validation Evidence

Open Item Records

Acceptance Authority
```

Potential interaction:

```text
CANDIDATE-001
Targeted Engineering Revision
        │
        ▼
CANDIDATE-002
Repository Tooling Validation Gate
        │
        ▼
Validation Evidence
        │
        ▼
CANDIDATE-003
Task Closeout Lifecycle
```

Important:

Do not assume CANDIDATE-003 always invokes CANDIDATE-001.

Do not force a fixed orchestration path.

The workflow should be capable of consuming evidence from multiple engineering activities.

---

# 22. Interaction Model

Document the conceptual interaction:

```text
Task Work
        │
        ▼
READY_FOR_CLOSEOUT
        │
        ▼
Collect Evidence
        │
        ├───────────────┐
        │               │
        ▼               ▼
Validation Evidence   Artifact Evidence
        │               │
        └───────┬───────┘
                ▼
         Review Evidence
                │
                ▼
         Resolve Open Items
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
     BLOCKED       Ready for Acceptance
                         │
                         ▼
              External Acceptance Authority
                         │
                 ┌───────┴────────┐
                 │                │
                 ▼                ▼
              Accepted       Not Accepted
                 │                │
                 ▼                ▼
          Capture Closeout      Return / Stop
                 │
                 ▼
               CLOSED
```

The diagram may be improved if necessary.

The important boundaries must remain visible.

---

# 23. Return and Stop Model

Define when the workflow:

```text
Returns work upstream
```

versus:

```text
Stops
```

Examples to evaluate:

```text
Validation Failed
→ Return for revision

Acceptance Rejected
→ Return for revision or scope decision

Blocking Issue
→ BLOCKED

Missing Evidence
→ Request evidence / return

Accepted + Closeout Recorded
→ CLOSED
```

Important:

Do not force automatic revision.

CANDIDATE-003 should identify:

```text
Return Context
```

but not autonomously decide the exact remediation strategy.

---

# 24. Responsibility Boundary

Explicitly define what CANDIDATE-003 owns.

Expected ownership:

```text
Closeout Lifecycle Coordination

Evidence Collection Coordination

Validation Evidence Review

Open Item Visibility

Closeout Package Preparation

Acceptance Transition Coordination

Deferred Work Recording

Lesson / Improvement Signal Capture

Closure Recording
```

Explicit non-ownership:

```text
Primary Implementation

Revision Execution

Repository Tooling Validation Execution

Validation Requirement Policy

Validation Deferral Authorization

Acceptance Authority

Automatic Asset Creation

Task Management System Ownership
```

The workflow coordinates.

It does not absorb every engineering responsibility.

---

# 25. Failure and Stop Conditions

Define explicit failure conditions.

Evaluate:

```text
Required Evidence Missing

Validation Evidence Incomplete

Validation Failure

Validation Execution Error

Blocking Open Item

Acceptance Rejected

Acceptance Authority Unavailable
```

Define appropriate workflow behavior:

```text
BLOCKED

RETURN

STOP

AWAIT_EXTERNAL_AUTHORITY
```

Do not automatically map all failures to:

```text
FAILED
```

This is a workflow.

The design should preserve lifecycle meaning.

---

# 26. Non-Goals

Explicitly define exclusions.

At minimum evaluate:

```text
Implementation Execution

Revision Planning

Revision Execution

Repository Validation Tool Execution

CI/CD Orchestration

Automatic Acceptance

Automatic Deferral Authorization

Automatic Task Management

Automatic Asset Extraction

Continuous Monitoring
```

The workflow must not become:

```text
Universal Engineering Orchestrator
```

---

# 27. Type Rationale

Add a dedicated section:

```text
Why WORKFLOW?
```

Explain why CANDIDATE-003 represents:

```text
ORCHESTRATION
→
WORKFLOW
```

rather than:

```text
SKILL

AGENT

RULE

CHECKLIST

TEMPLATE
```

The central rationale should evaluate:

```text
Multi-step coordination

Explicit lifecycle

State transitions

Multiple evidence sources

Multiple authority boundaries

Return paths

Explicit stop condition
```

Also explicitly explain:

```text
Why a checklist is insufficient.
```

A checklist can enumerate:

```text
What should happen
```

but this workflow must define:

```text
When it happens

What evidence enables transition

Who owns decisions

What happens when progression fails
```

---

# 28. Implementation Readiness

Evaluate whether the workflow design is ready for future implementation.

Use the repository framework vocabulary only.

Evaluate:

```text
Identity Clarity

Trigger Clarity

Entry Contract

Lifecycle Clarity

State Transition Clarity

Evidence Model

Validation Boundary

Open Item Model

Acceptance Boundary

Closeout Recording

Return Paths

Stop Conditions

Responsibility Boundary
```

Do NOT artificially upgrade readiness.

If unresolved dependencies remain, record them explicitly.

---

# 29. Open Questions

Record genuine unresolved questions.

Potential areas:

```text
How closeout authority is represented

How deferred work records are linked

Whether closeout records should become first-class artifacts

How lesson signals are consumed by future extraction

How lifecycle state should be persisted
```

Only retain questions that genuinely emerge during design.

Do not create open questions simply to appear thorough.

---

# 30. Design Quality Requirements

The design must satisfy:

## Q1 — Evidence Grounded

Traceable to historical engineering patterns.

---

## Q2 — Lifecycle Explicit

Closeout must have explicit progression rather than:

```text
Done → Closed
```

---

## Q3 — Authority Separated

Must distinguish:

```text
Evidence Review

Acceptance Decision

Closure Recording
```

---

## Q4 — Validation Boundary Preserved

Must distinguish:

```text
Validation Execution
```

from:

```text
Validation Review
```

CANDIDATE-003 must not duplicate CANDIDATE-002.

---

## Q5 — Open Work Visible

Deferred work and blocking work must remain explicit.

---

## Q6 — Acceptance ≠ Closure

Acceptance must not automatically collapse into closure.

---

## Q7 — Improvement Signals Preserved

The workflow may capture future improvement opportunities.

It must not automatically create assets.

---

## Q8 — Bounded

Must not become:

```text
Universal Engineering Agent

CI/CD System

Project Management System
```

---

# 31. Required Document Structure

The new document should approximately follow:

```text
# CANDIDATE-003 — Task Closeout Lifecycle

## 1. Design Scope

## 2. Evidence Basis

## 3. Asset Classification

## 4. Asset Identity

## 5. Purpose and Value

## 6. Workflow Trigger Model

## 7. Workflow Entry Contract

## 8. Core Lifecycle Model

## 9. Lifecycle State Model

## 10. Evidence Collection Model

## 11. Validation Review Model

## 12. Open Item Resolution Model

## 13. Blocking Model

## 14. Acceptance Authority Model

## 15. Acceptance vs Closure

## 16. Closeout Recording Model

## 17. Deferred Work Model

## 18. Lesson Capture Model

## 19. Dependency Model

## 20. Interaction Model

## 21. Return and Stop Model

## 22. Responsibility Boundary

## 23. Failure and Stop Conditions

## 24. Non-Goals

## 25. Type Rationale

## 26. Implementation Readiness

## 27. Open Questions

## 28. Design Summary
```

The structure may be improved where necessary.

Do not remove critical lifecycle dimensions.

---

# 32. Milestone Update

Update:

```text
ai-engineering/milestones/MILESTONE-001/
MILESTONE-001.md
```

to reflect:

```text
Stage D2C
CANDIDATE-003 Asset Design
```

Status:

```text
COMPLETED
```

Then determine the next stage based on the existing milestone plan.

Do NOT automatically mark:

```text
Stage D2
```

as completed unless all planned Strong Candidates have been designed.

Do NOT invent the next stage.

Read the milestone plan and use its existing structure.

---

# 33. Validation Checklist

Before commit:

```bash
git status
git diff --check
```

Verify:

```text
[ ] Historical evidence inspected

[ ] Pattern → Candidate traceability documented

[ ] Asset Category defined

[ ] Asset Type justified

[ ] WORKFLOW rationale included

[ ] Trigger model defined

[ ] Entry contract defined

[ ] Core lifecycle defined

[ ] State transitions explicit

[ ] Evidence collection separated from execution

[ ] Validation review separated from validation execution

[ ] CANDIDATE-002 boundary preserved

[ ] Open item model defined

[ ] Blocking model defined

[ ] Acceptance authority externalized

[ ] Acceptance distinguished from closure

[ ] Deferred work explicitly recorded

[ ] Lesson capture bounded

[ ] No automatic asset creation

[ ] Return paths defined

[ ] Stop conditions defined

[ ] Responsibility boundary explicit

[ ] Non-goals explicit

[ ] No runtime implementation created

[ ] No unrelated files modified

[ ] Framework readiness vocabulary reused
```

---

# 34. Final Report

Before commit, report:

## Workflow Summary

```text
Asset Name

Asset Category

Asset Type

Primary Purpose
```

## Lifecycle Summary

Explain:

```text
Entry
↓
Evidence
↓
Review
↓
Open Items
↓
Acceptance
↓
Closeout Recording
↓
Closed
```

Include:

```text
Blocked Paths

Return Paths

Stop Conditions
```

---

## Authority Boundary

Explicitly summarize:

```text
CANDIDATE-002:
Validation Execution

CANDIDATE-003:
Validation Review + Closeout Coordination

External Authority:
Acceptance Decision

Workflow:
Closure Coordination
```

---

## Open Work Handling

Explain:

```text
Blocking Issue
```

versus:

```text
Explicit Deferred Work
```

and who determines whether work may be deferred.

---

## Improvement Signal Boundary

Explain:

```text
Capture Improvement Signal
```

without:

```text
Automatically Create Asset
```

---

## Implementation Readiness

Report using framework vocabulary only.

---

## Files Changed

Expected:

```text
Created:
07-candidate-003-task-closeout-lifecycle.md

Modified:
MILESTONE-001.md
```

---

# 35. Commit

Suggested commit:

```text
docs(milestone-001): design candidate-003 task closeout lifecycle
```

Before commit:

```bash
git status
git diff --check
```

Then commit and push.

---

# 36. Stop Condition

After push:

```text
STOP.
```

Do NOT begin another candidate design stage.

This stage requires external review.

After completion, report exactly:

```text
MILESTONE-001 Stage D2C completed and pushed.
```
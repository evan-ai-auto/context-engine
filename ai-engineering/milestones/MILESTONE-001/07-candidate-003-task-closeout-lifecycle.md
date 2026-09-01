# CANDIDATE-003 — Task Closeout Lifecycle

## 1. Design Scope

```text
Candidate
        ↓
Asset Classification
        ↓
Asset Design
```

This document is the **Workflow Design Specification** for CANDIDATE-003.

```text
This stage does NOT implement the asset.

No Workflow runtime, orchestrator, Skill/Agent package, Rule,
Cursor config, task-management integration, or CI/CD automation
is created here.
```

Design is governed by:

```text
ai-engineering/milestones/MILESTONE-001/04-candidate-design-framework.md
AI Engineering Asset Taxonomy v0.1
```

Stage C source:

```text
03-asset-candidates.md
→ CANDIDATE-003 STRONG_CANDIDATE / READY_FOR_DESIGN / WORKFLOW
```

Compatibility:

```text
CANDIDATE-001 REQUESTS CANDIDATE-002
CANDIDATE-003 may REQUEST CANDIDATE-002 for missing evidence
CANDIDATE-003 CONSUMES Boundary Artifact from CANDIDATE-004 (when present)
```

---

## 2. Evidence Basis

### Trace

```text
Historical Process (TASK-001 / TASK-002 closeouts)
        ↓
PATTERN-002 Task Closeout Lifecycle
(+ PATTERN-009 Learning Capture as internal supporting activity)
        ↓
CANDIDATE-003 Task Closeout Lifecycle
        ↓
This Asset Design
```

### Why these activities recur near completion

```text
Validation
  Both tasks re-ran gates / recorded evidence before DONE

Evidence Review
  Closeouts checked contract/boundary/tooling results, not only “code exists”

Acceptance Decision
  Status moved to DONE only after reviewable completion claims

Deferred Work Capture
  Out-of-scope / future work listed explicitly (analyzers, scanners, etc.)

Lesson Capture
  Learning notes / closeout lessons after friction

Repository Update
  Task status + closeout docs committed

Task Closure
  Formal DONE / stage COMPLETED marking
```

### Design implication

```text
Task Closeout is a reusable multi-step engineering process pattern,
not an ad-hoc “mark done” checklist item.

Historical Evidence supports the design.
It does not define a runtime orchestrator.
```

Primary references:

```text
01-process-inventory.md §10 Closeout Inventory
02-engineering-patterns.md PATTERN-002 / PATTERN-009
03-asset-candidates.md CANDIDATE-003
05 / 06 candidate designs (authority boundaries)
```

---

## 3. Asset Classification

### Nature

```text
What does this reusable asset fundamentally represent?

Multi-step lifecycle coordination that moves a task from
“work appears complete” to “formally closed” using evidence,
open-item visibility, external acceptance, and closeout recording —
with blocked/return paths when progression is unsafe.
```

Nature: **Process / orchestration capability** (lifecycle coordination).

### Classification

```text
Asset Category: EXECUTABLE
Asset Type:     WORKFLOW
```

Taxonomy note:

```text
AI Engineering Asset Taxonomy v0.1 places WORKFLOW under EXECUTABLE.
There is no separate ORCHESTRATION category in v0.1.

“Orchestration” describes the WORKFLOW’s nature/role,
not a new Asset Category invented outside the taxonomy.
```

```text
Classification follows nature.
Nature does not follow preferred implementation.
```

Rationale: see §25 (Why WORKFLOW?).

---

## 4. Asset Identity

| Field | Value |
|---|---|
| Asset Name | Task Closeout Lifecycle |
| Candidate ID | CANDIDATE-003 |
| Asset Category | EXECUTABLE |
| Asset Type | WORKFLOW |
| Design Version | 0.1 |
| Status | DESIGNED |

```text
Status is DESIGNED — not IMPLEMENTED.
```

---

## 5. Purpose and Value

### Purpose

Coordinate a trustworthy transition from engineering execution to formal task closure through **explicit evidence, authority boundaries, and lifecycle transitions**.

### Primary Value

```text
Prevent:
  Implementation Finished → Assumed Complete → Task Closed

Enable:
  Ready for Closeout → Evidence → Review → Open Items →
  External Acceptance → Closeout Recording → Closed
  (with BLOCKED / RETURN / STOP paths)
```

### Engineering Problem Solved

```text
How can engineering work transition from execution to trustworthy
closure without collapsing validation, acceptance, deferred work,
lessons, and closure into one opaque step?
```

### Expected Reuse Context

```text
End of a task or milestone stage after primary deliverables exist

After revisions are complete and closure is requested

Any engineering effort needing auditable DONE semantics
across repositories / teams
```

---

## 6. Workflow Trigger Model

### Positive Trigger Conditions

Begin when **all** hold:

```text
- Primary work for the task/stage is believed complete
  (implementation and required revisions done, or equivalent)

- An Explicit Closeout Request exists
  (human / upstream workflow / stage policy)

- Task Identity and Scope are identifiable

- Completion criteria can be stated or referenced
```

Typical sources:

```text
STATE    — primary work / revision complete; stage ready for closure
EXPLICIT — closeout requested
EVENT    — milestone stage ready for closure
```

```text
Ready for Closeout ≠ Already Closed
```

### Negative Trigger Conditions

Do **not** begin when:

```text
- Primary work is still in progress

- Required evidence is known missing and no path to obtain it
  is authorized as part of entry

- Known blocking failure is already unresolved and closeout
  is being used to bypass it

- Task scope is still unresolved / boundary undefined with no
  Boundary Artifact or equivalent scope reference
```

---

## 7. Workflow Entry Contract

### Required Inputs

```text
Task Identity
  Which task/stage is being closed

Task Scope
  Scope reference (Boundary Artifact from CANDIDATE-004 when available,
  or equivalent explicit in/out-of-scope statement)

Expected Completion Criteria
  What “complete enough to close” means for this task

Produced Artifacts
  Deliverables claimed complete (implementation-neutral references)

Validation Requirement Context
  Whether validation evidence is required; Required Gate Set if known
  (External Authority / prior stage policy — not invented here)

External Authority Context
  How acceptance will be obtained (conceptual authority pointer)
```

### Optional Inputs

```text
Available Validation Evidence
  Prior CANDIDATE-002 (or equivalent) results

Known Deferred Work
Known Open Issues / Review Findings
Boundary Artifact (preferred when CANDIDATE-004 ran)
Prior revision reports (e.g. from CANDIDATE-001)
```

### Principle

```text
Consume Evidence rather than duplicate execution logic.
Do not require every upstream implementation detail.
```

---

## 8. Core Lifecycle Model

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

Minimum distinguished phases:

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
Done → Closed
```

---

## 9. Lifecycle State Model

Design-level states (not an exhaustive runtime state machine):

| State | Meaning | Typical evidence | Transition owner | Exit |
|---|---|---|---|---|
| NOT_STARTED | Closeout not begun | none | — | enter on valid trigger |
| READY_FOR_CLOSEOUT | Entry contract satisfied | entry inputs | Workflow / requester | → COLLECTING_EVIDENCE |
| COLLECTING_EVIDENCE | Gathering artifact + validation evidence | partial package | Workflow | → REVIEWING or BLOCKED |
| REVIEWING | Validation/artifact review in progress | evidence under review | Workflow | → resolve open items / BLOCKED |
| BLOCKED | Blocking condition explicit | blocking record | Workflow reports; External Authority may unblock | AWAIT / RETURN / STOP |
| AWAITING_ACCEPTANCE | Evidence package ready | closeout evidence package | External Acceptance Authority | ACCEPTED / NOT_ACCEPTED |
| ACCEPTED | Acceptance granted; not yet closed | acceptance outcome | Workflow | → CLOSING |
| CLOSING | Recording deferred work, lessons, closure record | draft closeout record | Workflow | → CLOSED |
| CLOSED | Formal closure complete | closeout record | — | terminal |

```text
Every state must remain reviewable.
Do not implement a full state-machine engine in this design stage.
```

---

## 10. Evidence Collection Model

May collect / reference:

```text
Produced Artifacts
Validation Evidence
Repository Evidence (status, diffs summary — not tool ownership)
Known Failures
Known Deferred Work
Open Questions
Review Findings
Boundary compliance notes (vs Boundary Artifact)
```

### Critical distinction

```text
Evidence Collection ≠ Execute all validation tools again
```

```text
CANDIDATE-003 consumes evidence where available.

If required validation evidence is missing, it may REQUEST
CANDIDATE-002 — it does not duplicate CANDIDATE-002 execution.
```

```text
CANDIDATE-003
        │ Validation Evidence Required / Missing
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

## 11. Validation Review Model

```text
Validation Execution ≠ Validation Review
```

| Asset | Owns |
|---|---|
| CANDIDATE-002 | Repository-aware validation execution |
| CANDIDATE-003 | Closeout-oriented evidence review |

Review questions (workflow):

```text
Is required validation evidence present?
Are required gates represented in evidence?
Are FAILED results visible (not reinterpreted as PASSED)?
Are ERROR / NOT_EXECUTED results visible?
Is validation incomplete?
Does unresolved validation block progression?
```

```text
Must NOT reinterpret FAILED → PASSED
Must NOT hide ERROR / NOT_EXECUTED
Must preserve CANDIDATE-002 result semantics
Must NOT decide deferral of required validation
  (External Authority — aligned with D2A/D2B revisions)
```

---

## 12. Open Item Resolution Model

Categories:

```text
Blocking Issue
Non-Blocking Deferred Work
Known Limitation
Open Question
Future Improvement
```

```text
Can Close? ≠ Everything Is Perfect

Deferred Work must not become Silently Ignored Work.
```

```text
Open Item
        │
        ├── Blocking → BLOCKED
        │
        └── Non-Blocking → Explicit Deferred Record → Acceptance Review
```

```text
Whether an item is Non-Blocking is not decided silently by this Workflow.
Classification/acceptance of deferral remains External Authority / policy traceable.
```

---

## 13. Blocking Model

Conditions that may block progression (when applicable):

```text
Missing Required Evidence
Required Validation Failure (FAILED on required gate)
Validation Execution Error (ERROR / NOT_EXECUTED on required gate)
Unresolved Blocking Issue
Missing Acceptance Authority
Scope Ambiguity (no usable scope / Boundary Artifact when required)
```

```text
Not every problem is blocking.
Blocking Status must be explicit.
Do not silently continue past a blocking condition.
```

---

## 14. Acceptance Authority Model

```text
Evidence Review ≠ Acceptance Decision
```

CANDIDATE-003 may prepare:

```text
Closeout Evidence Package
```

CANDIDATE-003 should **not** autonomously decide:

```text
The task is acceptable.
```

unless External Acceptance Authority has explicitly delegated that decision.

Default model:

```text
Workflow
        ▼
Evidence Package
        ▼
External Acceptance Authority
        ├── Accepted
        └── Not Accepted
```

```text
Who provides acceptance?
  External Acceptance Authority (policy / workflow / human — abstraction)

What evidence is presented?
  Closeout Evidence Package (artifacts, validation summary, open items, scope)

If acceptance unavailable?
  AWAIT_EXTERNAL_AUTHORITY / STOP — do not auto-accept

If acceptance rejected?
  NOT_ACCEPTED → RETURN / STOP with return context
```

```text
Do not hard-code “Human Approval Required” as the only mechanism.
Use External Acceptance Authority as the conceptual abstraction.
```

---

## 15. Acceptance vs Closure

```text
ACCEPTED ≠ CLOSED
```

```text
Accepted
        ↓
Capture Deferred Work
        ↓
Capture Lessons / Improvement Signals
        ↓
Update Closeout Record
        ↓
Closed
```

```text
Acceptance is an input to closure.
It is not closure itself.
```

---

## 16. Closeout Recording Model

What must be recorded (storage-neutral):

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
Closure context (timestamp or equivalent)
```

```text
Define what must be recorded.
Do NOT prescribe GitHub Issue / Markdown / Database / TMS storage.
```

---

## 17. Deferred Work Model

Conceptual deferred item fields:

```text
Identity
Reason
Known Impact
Why It Is Not Blocking (traceable classification)
Follow-Up Context
```

```text
Workflow must not automatically declare Non-Blocking
without External Authority / explicit policy.

Avoid “TODO” as the only deferred-work mechanism.
```

---

## 18. Lesson Capture Model

May capture improvement signals such as:

```text
Repeated Failure Pattern
Tooling Limitation
Process Friction
Candidate Asset Opportunity
Missing Rule / Template / Skill / Workflow
```

```text
CANDIDATE-003 may Capture Improvement Signals.
CANDIDATE-003 must NOT Automatically Create New Assets.
```

```text
Task Closeout
        ↓
Improvement Signal
        ↓
Future Extraction / Review
```

(PATTERN-009 absorbed as internal supporting activity — not a separate Skill.)

---

## 19. Dependency Model

### Consumes

```text
Task Context
Produced Artifact Evidence
Validation Evidence (often via CANDIDATE-002)
Open Item Records
Acceptance Authority
Boundary Artifact (CANDIDATE-004 when available)
```

### May REQUEST

```text
CANDIDATE-002 — when required validation evidence is missing
```

### Does not assume fixed path

```text
CANDIDATE-001 → CANDIDATE-002 → CANDIDATE-003
is a common historical shape, not a mandatory always-on chain.

CANDIDATE-003 need not always invoke CANDIDATE-001.
It may consume evidence from multiple engineering activities.
```

Illustrative path:

```text
CANDIDATE-001 (optional prior)
        ▼
CANDIDATE-002
        ▼
Validation Evidence
        ▼
CANDIDATE-003
```

---

## 20. Interaction Model

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

---

## 21. Return and Stop Model

| Situation | Behavior |
|---|---|
| Validation Failed (required) | BLOCKED or RETURN with return context (not auto-revise) |
| Acceptance Rejected | RETURN / STOP with return context |
| Blocking Issue | BLOCKED |
| Missing Evidence | Request evidence (e.g. REQUEST CANDIDATE-002) or RETURN |
| Acceptance Authority Unavailable | AWAIT_EXTERNAL_AUTHORITY / STOP |
| Accepted + Closeout Recorded | CLOSED |

```text
Do not force automatic revision.
Identify Return Context; do not autonomously choose remediation strategy
(that may be CANDIDATE-001 or human/policy).
```

---

## 22. Responsibility Boundary

### Primary Responsibility

```text
Closeout Lifecycle Coordination
```

### Handles (owns)

```text
Closeout lifecycle coordination
Evidence collection coordination
Validation evidence review (not execution)
Open item visibility
Closeout package preparation
Acceptance transition coordination
Deferred work recording
Lesson / improvement signal capture
Closure recording
Boundary compliance assessment against Boundary Artifact (consume only)
```

### Does Not Handle (does not own)

```text
Primary implementation
Revision planning / execution (CANDIDATE-001)
Repository tooling validation execution (CANDIDATE-002)
Validation requirement policy
Validation deferral authorization
Acceptance authority (External)
Required Gate definition / removal
Initial task boundary definition (CANDIDATE-004)
Automatic asset creation
Task management system ownership
CI/CD orchestration
```

```text
The workflow coordinates.
It does not absorb every engineering responsibility.
```

---

## 23. Failure and Stop Conditions

Conditions:

```text
Required Evidence Missing
Validation Evidence Incomplete
Validation Failure
Validation Execution Error
Blocking Open Item
Acceptance Rejected
Acceptance Authority Unavailable
```

Workflow behaviors:

```text
BLOCKED
RETURN
STOP
AWAIT_EXTERNAL_AUTHORITY
```

```text
Do not map all failures to a single FAILED label.
Preserve lifecycle meaning.
```

---

## 24. Non-Goals

```text
Implementation execution
Revision planning / execution
Repository validation tool execution
CI/CD orchestration
Automatic acceptance
Automatic deferral authorization
Automatic task management
Automatic asset extraction
Continuous monitoring
Become a Universal Engineering Orchestrator
```

---

## 25. Type Rationale — Why WORKFLOW?

### Selected

```text
EXECUTABLE → WORKFLOW
```

### Why not SKILL?

```text
Not a single bounded procedure with one I/O cycle.
Coordinates multiple phases, evidence sources, and authority handoffs.
```

### Why not AGENT?

```text
Does not open-endedly explore to invent closure criteria.
Stops and awaits External Acceptance Authority.
Not autonomous continuous operation.
```

### Why not RULE?

```text
Does not merely constrain; it progresses a lifecycle.
```

### Why not CHECKLIST?

```text
A checklist enumerates what should happen.

This workflow must define:
  When it happens
  What evidence enables transition
  Who owns decisions
  What happens when progression fails
  Return / blocked / await paths
```

### Why not TEMPLATE?

```text
Not only a document skeleton (though closeout recording may later
use a TEMPLATE asset — separate nature).
```

### Central WORKFLOW traits

```text
Multi-step coordination
Explicit lifecycle
State transitions
Multiple evidence sources
Multiple authority boundaries
Return paths
Explicit stop conditions
```

---

## 26. Implementation Readiness

Framework vocabulary only:

### Evaluation

| Dimension | Assessment |
|---|---|
| Identity Clarity | Clear |
| Trigger Clarity | Clear |
| Entry Contract | Clear |
| Lifecycle Clarity | Clear |
| State Transition Clarity | Design-level defined |
| Evidence Model | Clear; consumes / may request |
| Validation Boundary | Review ≠ execution; 002 preserved |
| Open Item Model | Blocking vs deferred explicit |
| Acceptance Boundary | Externalized |
| Closeout Recording | What-not-where defined |
| Return Paths | Defined |
| Stop Conditions | Defined |
| Responsibility Boundary | Clear |

### Readiness

```text
Design Status: DESIGNED

Implementation Readiness: REQUIRES_EVIDENCE
```

Reasons:

```text
Workflow design is reviewable and implementation-neutral.

Still requires before READY_FOR_IMPLEMENTATION:
  - concrete External Acceptance Authority binding patterns
  - closeout record persistence conventions
  - deferred-work record linkage conventions
  - integration with CANDIDATE-002 request/evidence contracts
  - optional Boundary Artifact consumption details with CANDIDATE-004
```

---

## 27. Open Questions

```text
IMPLEMENTATION_UNKNOWN
  How should External Acceptance Authority be represented
  across human / policy / upstream-workflow cases?

IMPLEMENTATION_UNKNOWN
  How should deferred-work records be linked to follow-up tasks
  without owning a task-management system?

IMPLEMENTATION_UNKNOWN
  Should the Closeout Evidence Package / Closeout Record become
  first-class shared artifacts with stable identities?

EVIDENCE_GAP
  How will lesson/improvement signals be consumed by future
  extraction without coupling closeout to asset creation?

IMPLEMENTATION_UNKNOWN
  How should lifecycle state be persisted (if at all) across tools?
```

---

## 28. Design Summary

```text
Asset Name:     Task Closeout Lifecycle
Asset Category: EXECUTABLE
Asset Type:     WORKFLOW
Status:         DESIGNED
Primary Purpose:
  Coordinate evidence-based formal task closure with explicit
  acceptance, deferred work, lessons, and blocked/return paths.
```

### Lifecycle summary

```text
Entry → Evidence → Review → Open Items → Acceptance →
Closeout Recording → Closed

Blocked / Return / Await / Stop paths remain first-class.
```

### Authority boundary

```text
CANDIDATE-002: Validation Execution
CANDIDATE-003: Validation Review + Closeout Coordination
External Authority: Acceptance Decision (+ deferral / required gates)
Workflow: Closure Coordination after acceptance
```

### Open work handling

```text
Blocking Issue → BLOCKED (explicit)
Non-Blocking Deferred Work → Explicit Deferred Record
  (Non-Blocking classification not invented silently by this Workflow)
```

### Improvement signal boundary

```text
Capture Improvement Signal → Future Extraction / Review
Do NOT Automatically Create Asset
```

```text
Implementation Readiness: REQUIRES_EVIDENCE
```

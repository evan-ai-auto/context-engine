# MILESTONE-001 Stage D4 — CANDIDATE-004 Asset Type Confirmation & Design

## 0. Mission

Perform the Asset Type Confirmation and conceptual design for:

```text
CANDIDATE-004
Explicit Task Boundary Definition
```

The purpose of this stage is to determine:

```text
What reusable engineering asset should
Explicit Task Boundary Definition become?
```

Do NOT assume in advance that the answer is:

```text
SKILL
```

The asset may instead be:

```text
SKILL

TEMPLATE

RULE

WORKFLOW

CHECKLIST

SHARED CONTRACT

SKILL + TEMPLATE

OTHER
```

The final design must be based on:

```text
Responsibility
+
Execution Necessity
+
Input / Output
+
Reuse Pattern
+
Architecture Fit
```

not naming preference.

---

# 1. Mandatory Reading

Before making changes, read:

```text
ai-engineering/milestones/MILESTONE-001/
MILESTONE-001.md
```

Read the original candidate inventory:

```text
ai-engineering/milestones/MILESTONE-001/
03-asset-candidates.md
```

Read the candidate design framework:

```text
ai-engineering/milestones/MILESTONE-001/
04-candidate-design-framework.md
```

Read all existing Strong Candidate designs:

```text
ai-engineering/milestones/MILESTONE-001/
05-candidate-001-targeted-engineering-revision.md

ai-engineering/milestones/MILESTONE-001/
06-candidate-002-repository-tooling-validation-gate.md

ai-engineering/milestones/MILESTONE-001/
07-candidate-003-task-closeout-lifecycle.md
```

Read:

```text
ai-engineering/milestones/MILESTONE-001/
08-stage-d2-strong-candidate-architecture-review.md
```

Read:

```text
ai-engineering/milestones/MILESTONE-001/
09-stage-d3-candidate-portfolio-reassessment.md
```

Also inspect source evidence where necessary:

```text
ai-engineering/milestones/MILESTONE-001/
01-process-inventory.md

ai-engineering/milestones/MILESTONE-001/
02-engineering-patterns.md
```

Important:

Do not design CANDIDATE-004 based only on its original candidate description.

Use the architecture established through D2 and D3.

---

# 2. Scope

Create:

```text
ai-engineering/milestones/MILESTONE-001/
10-candidate-004-explicit-task-boundary-definition.md
```

Update:

```text
ai-engineering/milestones/MILESTONE-001/
MILESTONE-001.md
```

Expected changes:

```text
Created:
10-candidate-004-explicit-task-boundary-definition.md

Modified:
MILESTONE-001.md
```

Do NOT:

```text
Create runtime implementation

Create Python models

Create Pydantic models

Create agents

Create executable skills

Create workflows

Create actual rules files

Create templates outside conceptual design documentation

Modify existing candidate designs

Create shared contracts

Refactor the candidate architecture
```

This stage is:

```text
Conceptual Asset Design
```

not implementation.

---

# 3. Core Design Question

Explicitly answer:

```text
Is Explicit Task Boundary Definition:

A reusable execution capability?

A reusable structure?

A reusable policy?

A reusable lifecycle?

Or a composition of multiple asset types?
```

The design must not begin until this classification is reasoned through.

---

# 4. Asset Type Confirmation

Evaluate the candidate against each possible type.

## 4.1 SKILL

A Skill is appropriate when:

```text
Input Context
        ↓
Reasoning / Decision Process
        ↓
Structured Output
```

is required.

Evaluate:

```text
Does Task Boundary Definition require
context-sensitive reasoning?

Does the process require interpreting
task intent?

Does the process require identifying
implicit scope?

Does the process require detecting
non-goals?

Does the process require reasoning
about dependencies?

Does the process require reconciling
ambiguous requirements?
```

---

## 4.2 TEMPLATE

A Template is appropriate when the primary reusable value is:

```text
Stable Structure
```

Evaluate:

```text
Could users manually populate
a stable boundary structure?

Is the main reusable component
a document format?

Does execution logic add little value
beyond the structure?
```

---

## 4.3 RULE

A Rule is appropriate when:

```text
Constraint Enforcement
```

is the primary responsibility.

Evaluate:

```text
Is the candidate primarily about
restricting behavior?

Does it define mandatory boundaries
rather than generating boundaries?

Would an explicit instruction be enough?
```

---

## 4.4 WORKFLOW

A Workflow is appropriate when:

```text
Multiple Ordered Activities
+
Lifecycle Coordination
```

are required.

Evaluate:

```text
Does Boundary Definition orchestrate
multiple independent assets?

Does it manage lifecycle transitions?

Does it coordinate revision,
validation, or acceptance?
```

Important:

Do not classify as Workflow merely because
the process contains multiple steps.

---

## 4.5 CHECKLIST

A Checklist is appropriate when:

```text
Verification
```

rather than generation is primary.

Evaluate:

```text
Is the main responsibility to verify
whether boundaries are complete?

Or is the responsibility to actually
derive the boundaries?
```

---

## 4.6 SHARED CONTRACT

A Shared Contract is appropriate when:

```text
Multiple Assets
```

need a stable shared representation.

Evaluate:

```text
Does Boundary Definition itself define
the contract?

Or does it produce a contract?

Should the Boundary Artifact become
a shared representation?

Is there sufficient implementation
evidence to justify contract extraction?
```

Important:

Do not create a shared contract merely because
multiple conceptual assets reference
Boundary information.

---

# 5. Asset Type Decision Matrix

Create an explicit matrix:

| Asset Type | Fit | Evidence | Reasoning |
|---|---|---|---|
| SKILL | | | |
| TEMPLATE | | | |
| RULE | | | |
| WORKFLOW | | | |
| CHECKLIST | | | |
| SHARED CONTRACT | | | |

Then make one final decision:

```text
PRIMARY_ASSET_TYPE:
```

Possible:

```text
SKILL

TEMPLATE

RULE

WORKFLOW

CHECKLIST

SHARED CONTRACT

COMPOSITE
```

If:

```text
COMPOSITE
```

is selected, explicitly identify:

```text
Primary Asset

Supporting Asset
```

Example conceptual structure only:

```text
Primary:
Task Boundary Definition Skill

Supporting:
Task Boundary Template
```

Do not assume this result before analysis.

---

# 6. Responsibility Definition

Define the exact responsibility.

Use the format:

```text
Primary Responsibility:

This asset is responsible for:
...

This asset is NOT responsible for:
...
```

Explicitly distinguish:

```text
Task Intent

Task Scope

Task Boundary

Revision Scope

Validation Scope

Closeout Scope

Acceptance Boundary
```

Important:

These concepts may overlap.

Do not assume they are identical.

---

# 7. Core Concept Model

Define the conceptual relationships:

```text
Task Intent
        ↓
Boundary Definition
        ↓
Task Boundary
        ↓
Execution Scope
        ↓
Revision
        ↓
Validation
        ↓
Closeout
```

Evaluate whether this model is correct.

Adjust if necessary.

The final model should explain:

```text
What exists before Boundary Definition?

What Boundary Definition produces?

Who consumes the result?

What happens when boundaries change?
```

---

# 8. Boundary Artifact

Determine whether:

```text
Boundary Artifact
```

is a meaningful conceptual output.

If yes, define its minimum structure.

Possible dimensions:

```text
Objective

In Scope

Out of Scope

Non-Goals

Constraints

Dependencies

Assumptions

Acceptance Boundary

Open Questions
```

These are candidates only.

Do not automatically include all fields.

The goal is:

```text
Minimum Stable Boundary Representation
```

not:

```text
Maximum Documentation
```

---

# 9. Boundary Artifact Ownership

Explicitly define:

```text
Who Creates Boundary?

Who May Modify Boundary?

Who Consumes Boundary?

Who Approves Boundary?

Who Can Override Boundary?
```

Consider:

```text
Human

Agent

Workflow

External Authority

Task Owner
```

Do not assume implementation details.

Define conceptual authority only.

---

# 10. Boundary Lifecycle

Determine whether Task Boundary requires lifecycle semantics.

Possible conceptual states:

```text
DRAFT

PROPOSED

CONFIRMED

REVISED

SUPERSEDED
```

Do NOT automatically introduce lifecycle states.

First answer:

```text
Does the Boundary need identity
across time?

Can it change during execution?

Can multiple versions coexist?

Does Closeout require knowing
which boundary version applied?
```

If lifecycle is unnecessary:

```text
Explicitly reject lifecycle modeling.
```

If lifecycle is useful:

```text
Define the minimum conceptual lifecycle.
```

Avoid premature state machines.

---

# 11. Boundary Change Handling

Analyze:

```text
Task starts
        ↓
Boundary defined
        ↓
Revision begins
        ↓
New requirement appears
```

Then determine:

```text
What happens?
```

Possible conceptual paths:

```text
Reject Change

Expand Boundary

Create New Boundary Version

Defer Requirement

Split Into Another Task
```

Do not create implementation logic.

Document decision principles.

---

# 12. Relationship with CANDIDATE-001

Analyze:

```text
CANDIDATE-004
Task Boundary Definition

vs

CANDIDATE-001
Targeted Engineering Revision
```

Clarify:

```text
Boundary
≠
Revision Scope
```

or explain if a different relationship is correct.

Determine:

```text
Does CANDIDATE-001 consume Boundary?

Does it derive Revision Scope from Boundary?

Can Revision exist without Boundary?

Can Boundary exist without Revision?
```

Avoid creating a hard dependency unless justified.

---

# 13. Relationship with CANDIDATE-002

Analyze:

```text
CANDIDATE-004
Boundary Definition

vs

CANDIDATE-002
Repository Tooling Validation Gate
```

Clarify:

```text
Does Boundary influence validation?

Does Boundary define required validation?

Does Validation independently determine
its own scope?

Can Boundary provide validation context
without controlling validation authority?
```

Important:

Do not transfer validation authority
to Boundary Definition.

---

# 14. Relationship with CANDIDATE-003

Analyze:

```text
CANDIDATE-004
Boundary Definition

vs

CANDIDATE-003
Task Closeout Lifecycle
```

Use the D3 principle:

```text
Closeout consumes boundaries;
it does not define them.
```

Clarify:

```text
What Boundary information does Closeout consume?

How does Closeout determine
whether the task stayed in scope?

What happens when actual output
exceeds the original boundary?

Does Closeout need boundary version awareness?
```

---

# 15. Cross-Asset Architecture

Create a relationship diagram:

```text
External Context
        │
        ▼
Task Boundary Definition
        │
        ▼
Boundary Artifact
        │
        ├───────────────┐
        │               │
        ▼               ▼
Engineering Revision    Closeout
        │
        ▼
Validation
```

Modify based on actual findings.

Important:

Distinguish:

```text
Static Dependency

Information Flow

Optional Composition

Authority Relationship
```

Do not imply all arrows are dependencies.

---

# 16. Input Model

Define conceptual inputs.

Possible:

```text
Task Request

Existing Requirements

Repository Context

Constraints

Existing Decisions

External Authority Context
```

Identify:

```text
Required Inputs

Optional Inputs

External Inputs
```

Do not create Python schemas.

---

# 17. Output Model

Define conceptual outputs.

Possible:

```text
Task Boundary

Boundary Rationale

Open Questions

Assumptions

Deferred Items
```

Identify:

```text
Primary Output

Supporting Outputs

External References
```

---

# 18. Execution Model

If the candidate is classified as a Skill or composite asset, define:

```text
Input
        ↓
Interpret Task
        ↓
Identify Scope
        ↓
Identify Non-Goals
        ↓
Identify Constraints
        ↓
Detect Ambiguity
        ↓
Propose Boundary
        ↓
Authority Confirmation
        ↓
Boundary Artifact
```

Modify based on actual reasoning.

Important:

Separate:

```text
Boundary Generation
```

from:

```text
Boundary Acceptance
```

The asset may propose boundaries without having authority to approve them.

---

# 19. Authority Model

Explicitly define:

```text
Who Proposes Boundary?

Who Confirms Boundary?

Who Can Override Boundary?

Who Can Request Boundary Change?

Who Determines Task Acceptance?
```

Possible conceptual actors:

```text
Asset

Agent

Human

External Authority

Task Owner

Workflow
```

Important principle:

```text
Proposal Authority
≠
Acceptance Authority
```

---

# 20. Reusability Model

Explain where the asset can be reused.

Possible contexts:

```text
Feature Development

Bug Fix

Repository Refactor

Architecture Change

Task Planning

Agent Execution

Multi-Agent Coordination
```

Determine:

```text
Universal

Broad

Contextual

Narrow
```

Do not claim universal reuse without evidence.

---

# 21. Failure Modes

Document conceptual failure modes.

Examples:

```text
Boundary Too Broad

Boundary Too Narrow

Missing Non-Goals

Implicit Scope Assumptions

Unresolved Ambiguity

Unauthorized Boundary Expansion

Boundary Drift

Conflicting Requirements
```

For each meaningful failure mode define:

```text
Detection

Mitigation

Authority Escalation
```

Do not over-model trivial cases.

---

# 22. Interaction Model

Determine how future users or agents might interact with the asset.

Possible modes:

```text
Explicit Invocation

Automatic Suggestion

Workflow Composition

Agent Pre-Execution Step
```

Do NOT implement invocation logic.

Only document possible composition.

---

# 23. Supporting Structural Assets

If analysis identifies a supporting asset such as:

```text
Template

Rule

Checklist
```

document it separately as:

```text
Supporting Structural Asset
```

For each:

```text
Purpose

Relationship to Primary Asset

Standalone Reuse Value

Implementation Necessity
```

Important:

Do NOT automatically promote supporting structures into
independent Candidates.

---

# 24. Shared Contract Decision

Explicitly evaluate whether:

```text
Boundary Artifact
```

should become:

```text
Shared Contract
```

Decision options:

```text
NOT_REQUIRED

CONCEPTUAL_ONLY

FUTURE_EXTRACTION_CANDIDATE

READY_FOR_SHARED_CONTRACT
```

Given current architecture maturity, require strong evidence for:

```text
READY_FOR_SHARED_CONTRACT
```

---

# 25. Architecture Stress Tests

Perform conceptual stress tests.

## Scenario A

```text
Simple Bug Fix
```

Does the asset add useful value?

---

## Scenario B

```text
Large Refactor
```

Can it prevent scope explosion?

---

## Scenario C

```text
Ambiguous Requirement
```

Can it surface unresolved questions?

---

## Scenario D

```text
Mid-Task Scope Change
```

Can it distinguish:

```text
Revision

Expansion

New Task
```

---

## Scenario E

```text
Multiple Agents
```

Can Boundary Artifact become shared execution context?

---

## Scenario F

```text
Validation Failure
```

Does the Boundary remain stable while
Revision repeats?

---

# 26. Design Decision

The document must explicitly record:

```text
Candidate:
CANDIDATE-004

Primary Asset Type:

Supporting Asset Type:

Primary Responsibility:

Primary Inputs:

Primary Outputs:

Authority Boundary:

Cross-Asset Consumers:

Lifecycle Requirement:

Shared Contract Decision:

Reuse Scope:
```

---

# 27. Future Observations

Document unresolved observations separately.

Possible examples:

```text
Boundary Artifact Versioning

Shared Contract Extraction

Agent Authority Model

Task Graph Integration

Boundary Change Governance
```

Do not implement them.

---

# 28. Required Document Structure

Create:

```text
10-candidate-004-explicit-task-boundary-definition.md
```

Suggested structure:

```text
# CANDIDATE-004
## Explicit Task Boundary Definition

## 1. Mission

## 2. Evidence Context

## 3. Core Design Question

## 4. Asset Type Analysis

## 5. Asset Type Decision

## 6. Responsibility Boundary

## 7. Core Concept Model

## 8. Boundary Artifact

## 9. Boundary Artifact Ownership

## 10. Boundary Lifecycle

## 11. Boundary Change Handling

## 12. Input Model

## 13. Output Model

## 14. Execution Model

## 15. Authority Model

## 16. Relationship with CANDIDATE-001

## 17. Relationship with CANDIDATE-002

## 18. Relationship with CANDIDATE-003

## 19. Cross-Asset Architecture

## 20. Reusability Model

## 21. Failure Modes

## 22. Interaction Model

## 23. Supporting Structural Assets

## 24. Shared Contract Decision

## 25. Architecture Stress Tests

## 26. Final Design Decision

## 27. Future Observations

## 28. Review Summary
```

The structure may be improved.

Do not remove core decision sections.

---

# 29. Milestone Update

Update:

```text
MILESTONE-001.md
```

to record:

```text
Stage D4
CANDIDATE-004 Asset Type Confirmation & Design
```

Record actual status only.

Do not mark future stages complete.

---

# 30. Validation Checklist

Before commit:

```bash
git status
git diff --check
```

Verify:

```text
[ ] Asset type analysis completed

[ ] Explicit asset type matrix included

[ ] Primary asset type decided

[ ] Supporting asset identified if necessary

[ ] Responsibility boundary defined

[ ] Boundary Artifact evaluated

[ ] Ownership model defined

[ ] Lifecycle necessity evaluated

[ ] Boundary change handling analyzed

[ ] Input model defined

[ ] Output model defined

[ ] Authority model defined

[ ] Relationship with CANDIDATE-001 analyzed

[ ] Relationship with CANDIDATE-002 analyzed

[ ] Relationship with CANDIDATE-003 analyzed

[ ] Cross-asset architecture diagram included

[ ] Failure modes considered

[ ] Reusability evaluated

[ ] Supporting structures evaluated

[ ] Shared contract decision recorded

[ ] Architecture stress tests performed

[ ] No implementation code created

[ ] No unrelated files modified
```

---

# 31. Final Report

Before commit, report:

## Asset Type Decision

```text
Primary Asset Type:
...

Supporting Asset:
...
```

---

## Core Responsibility

```text
...
```

---

## Boundary Artifact

```text
Required / Optional / Not Required
```

---

## Lifecycle Decision

```text
Required / Not Required / Future Observation
```

---

## Shared Contract Decision

```text
NOT_REQUIRED

CONCEPTUAL_ONLY

FUTURE_EXTRACTION_CANDIDATE

READY_FOR_SHARED_CONTRACT
```

---

## Cross-Asset Relationship

Summarize relationships with:

```text
CANDIDATE-001

CANDIDATE-002

CANDIDATE-003
```

---

## Major Observations

List only meaningful unresolved issues.

---

## Files Changed

Expected:

```text
Created:
10-candidate-004-explicit-task-boundary-definition.md

Modified:
MILESTONE-001.md
```

---

# 32. Commit

Suggested commit:

```text
docs(milestone-001): design explicit task boundary asset
```

Before commit:

```bash
git status
git diff --check
```

Then commit and push.

---

# 33. Stop Condition

After push:

```text
STOP.
```

Do NOT automatically:

```text
Implement CANDIDATE-004

Create actual SKILL files

Create TEMPLATE files

Create RULE files

Create runtime models

Create shared contracts

Modify CANDIDATE-001

Modify CANDIDATE-002

Modify CANDIDATE-003

Start another candidate
```

This stage requires architecture review.

After completion, report exactly:

```text
MILESTONE-001 Stage D4 completed and pushed.
```
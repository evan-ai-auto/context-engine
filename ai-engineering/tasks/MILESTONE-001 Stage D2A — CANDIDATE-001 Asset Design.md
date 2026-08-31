# MILESTONE-001 Stage D2A — CANDIDATE-001 Asset Design

## 0. Mission

Design the first Strong Candidate identified during:

```text
MILESTONE-001 Stage C
Asset Candidate Identification
```

Target:

```text
CANDIDATE-001
Targeted Engineering Revision
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

The objective is to produce a complete, reviewable, implementation-neutral design for CANDIDATE-001.

---

# 1. Mandatory Reading

Before making any changes, read:

```text
ai-engineering/milestones/MILESTONE-001/03-asset-candidates.md

ai-engineering/milestones/MILESTONE-001/04-candidate-design-framework.md

ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

Also inspect historical evidence referenced by CANDIDATE-001.

Read the relevant process and pattern sources:

```text
ai-engineering/milestones/MILESTONE-001/01-process-inventory.md

ai-engineering/milestones/MILESTONE-001/02-engineering-patterns.md
```

Important:

Do not design based only on the Candidate title.

Trace the Candidate back to:

```text
Historical Evidence
        ↓
Process
        ↓
Pattern
        ↓
Candidate
```

The design must remain evidence-grounded.

---

# 2. Target Candidate

Design:

```text
CANDIDATE-001
```

Conceptual name:

```text
Targeted Engineering Revision
```

The exact final asset name should be determined during design.

Do not assume that the candidate title must become the final asset identity.

---

# 3. Scope

Create one new design document:

```text
ai-engineering/milestones/MILESTONE-001/
05-candidate-001-targeted-engineering-revision.md
```

Update if necessary:

```text
ai-engineering/milestones/MILESTONE-001/
MILESTONE-001.md
```

Expected scope:

```text
Create:
05-candidate-001-targeted-engineering-revision.md

Optional:
Update MILESTONE-001.md
```

Do NOT modify:

```text
01-process-inventory.md

02-engineering-patterns.md

03-asset-candidates.md

04-candidate-design-framework.md
```

Do NOT create:

```text
Actual Skill

Actual Agent

Actual Workflow

Runtime Code

Cursor Rule

Skill Directory

Implementation Files
```

This stage produces only:

```text
Asset Design Specification
```

---

# 4. Evidence Traceability

The design document must explicitly include:

```text
Evidence Basis
```

Trace:

```text
Historical Process
→
Engineering Pattern
→
CANDIDATE-001
```

Do not reproduce all historical evidence.

Instead document the minimum evidence necessary to justify:

```text
Why this Candidate exists

Why it should become an Asset

Why its selected Asset Type is appropriate
```

Important:

```text
Historical Evidence
supports the design

Historical Evidence
does not automatically define implementation
```

---

# 5. Asset Classification

Classify CANDIDATE-001 according to:

```text
AI Engineering Asset Taxonomy v0.1
```

Explicitly determine:

```text
Asset Category

Asset Type
```

Expected direction should be evaluated, not blindly assumed.

Possible result:

```text
Category:
EXECUTABLE

Type:
SKILL
```

However, the design must justify the classification.

Apply:

```text
Classification follows nature.
Nature does not follow preferred implementation.
```

The design must explain why this candidate is:

```text
SKILL
```

rather than:

```text
AGENT

WORKFLOW

RULE

CHECKLIST

TEMPLATE
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

Suggested status:

```text
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

The purpose should answer:

```text
Why should this become a reusable AI Engineering Asset?
```

Avoid generic statements such as:

```text
Improve engineering efficiency.
```

Instead define the specific reusable capability.

---

# 8. Trigger Model

Define when the asset should be invoked.

Possible conceptual triggers:

```text
External Review Feedback

Detected Engineering Issue

Compatibility Finding

Architecture Gap

Quality Gap
```

Important:

Do NOT make the trigger model too broad.

The asset should NOT become:

```text
Universal Fix Everything Skill
```

Define:

```text
Positive Trigger Conditions

Negative Trigger Conditions
```

Example conceptually:

```text
Use when:
A bounded revision target has been identified.

Do not use when:
The problem is still exploratory and the target state is undefined.
```

The final conditions should be derived from repository evidence.

---

# 9. Input Model

Define required inputs.

At minimum evaluate:

```text
Revision Target

Revision Objective

Evidence / Findings

Scope Boundary

Acceptance Criteria

Known Constraints
```

Distinguish:

```text
Required Input
```

from:

```text
Optional Input
```

Important:

The asset should not require a complete implementation plan as input.

Its purpose is to transform:

```text
Revision Request
```

into:

```text
Controlled Revision Outcome
```

---

# 10. Output Model

Define the expected outputs.

Possible output dimensions:

```text
Revision Result

Changed Artifacts

Validation Evidence

Remaining Open Issues

Scope Confirmation

Stop Condition
```

The output must be structured enough to support:

```text
Human Review

Downstream Workflow

Future Automation
```

Do not define implementation-specific JSON schemas.

Conceptual contracts are sufficient.

---

# 11. Revision Lifecycle

Design the internal lifecycle.

Recommended conceptual model:

```text
1. Inspect
        ↓
2. Understand
        ↓
3. Define Revision Boundary
        ↓
4. Plan
        ↓
5. Execute Revision
        ↓
6. Validate
        ↓
7. Report
        ↓
8. Stop
```

Do not blindly copy this lifecycle.

Validate against historical evidence.

The lifecycle should explicitly distinguish:

```text
Understanding

Planning

Modification

Validation
```

Avoid:

```text
Finding Issue
↓
Immediately Modify Files
```

The design should enforce:

```text
Inspect Before Modify
```

---

# 12. Responsibility Boundary

Define what CANDIDATE-001 owns.

Expected conceptual ownership:

```text
Revision Orchestration
```

CANDIDATE-001 should own:

```text
Scope Understanding

Revision Planning

Change Coordination

Revision Result Reporting
```

CANDIDATE-001 should NOT own:

```text
Repository Validation Execution
```

This is critical.

Define explicitly:

```text
CANDIDATE-001
owns revision orchestration
```

---

# 13. Dependency Model

The candidate design must explicitly model its relationship with:

```text
CANDIDATE-002
Repository Tooling Validation Gate
```

The relationship should be:

```text
CANDIDATE-001
        │
        │ REQUESTS
        ▼
CANDIDATE-002
```

Important distinction:

```text
REQUESTS
≠
OWNS
```

CANDIDATE-001 may request validation.

CANDIDATE-002 owns validation execution.

Define:

```text
Dependency Trigger

Validation Request Boundary

Expected Validation Evidence

Failure Propagation
```

Do NOT design CANDIDATE-002 itself.

Do NOT define its internal implementation.

Only define the interface expectation from the perspective of CANDIDATE-001.

---

# 14. Artifact Model

Identify which artifacts the asset may consume or produce.

Potential categories:

```text
Input Artifacts

Working Artifacts

Output Artifacts

Evidence Artifacts
```

Examples may include:

```text
Review Findings

Revision Plan

Changed File Summary

Validation Result

Open Issue Record
```

Do not create concrete artifact files.

Only define artifact responsibilities.

---

# 15. Validation Model

Define how the result of the revision is considered acceptable.

Separate:

```text
Revision Validation
```

from:

```text
Repository Validation
```

CANDIDATE-001 should evaluate:

```text
Revision Scope Completion

Acceptance Criteria

Known Issue Resolution

Unintended Change Detection
```

Repository-level validation execution may be delegated.

Clarify:

```text
Revision succeeded
≠
Repository validation automatically succeeded
```

The final design should allow a result state such as:

```text
Revision Completed
Validation Pending
```

if appropriate.

---

# 16. Failure and Stop Conditions

Define explicit failure conditions.

Examples to evaluate:

```text
Revision Scope Ambiguous

Evidence Insufficient

Acceptance Criteria Missing

Required Dependency Unavailable

Validation Failed

Unexpected Scope Expansion
```

Define what should happen.

Possible outcomes:

```text
STOP

ESCALATE

REQUEST CLARIFICATION

RETURN PARTIAL RESULT
```

Do NOT assume:

```text
Every problem must be automatically fixed.
```

A critical capability of this asset should be:

```text
Knowing when not to continue.
```

---

# 17. Non-Goals

Explicitly define what this asset does NOT do.

At minimum evaluate exclusion of:

```text
Exploratory Architecture Design

Large-scale Repository Refactoring

Repository Validation Ownership

Automatic Candidate Promotion

Asset Implementation

Autonomous Continuous Operation
```

The final list should prevent the asset from becoming:

```text
Generic Engineering Agent
```

---

# 18. Type Rationale

Add a dedicated section:

```text
Why SKILL?
```

Explain why this candidate is best represented as:

```text
EXECUTABLE
→
SKILL
```

Compare against:

```text
AGENT

WORKFLOW

RULE

CHECKLIST

TEMPLATE
```

Important distinction:

```text
A reusable capability
```

does not automatically imply:

```text
Agent
```

The design should explain why this asset represents a bounded engineering capability rather than an autonomous decision-making entity.

---

# 19. Interaction Model

Describe conceptual interaction.

Recommended abstraction:

```text
External Finding
        ↓
CANDIDATE-001
Targeted Engineering Revision
        ↓
Inspect
        ↓
Bound Scope
        ↓
Plan Revision
        ↓
Execute Revision
        ↓
Request Validation
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
Revision Report
        ↓
STOP
```

This diagram is conceptual.

Do NOT design runtime orchestration.

---

# 20. Implementation Readiness

Evaluate whether the design is ready for future implementation.

Use explicit states:

```text
READY

CONDITIONALLY_READY

NOT_READY
```

Evaluate:

```text
Identity Clarity

Trigger Clarity

Input Clarity

Output Clarity

Responsibility Boundary

Dependency Boundary

Validation Model

Failure Model
```

If unresolved issues exist, do not hide them.

---

# 21. Open Questions

Record unresolved questions explicitly.

Do NOT force premature answers.

Examples:

```text
Should this Skill be interactive or autonomous?

Should revision planning be a separate Skill?

Should validation requests be synchronous?

Should partial revision results be first-class artifacts?
```

These are examples only.

Only record questions genuinely discovered during design.

---

# 22. Design Quality Requirements

The design must satisfy:

## Q1 — Evidence Grounded

The design can be traced to historical process and pattern evidence.

---

## Q2 — Bounded

The asset must have clear ownership boundaries.

---

## Q3 — Reusable

The capability should apply beyond a single historical task.

---

## Q4 — Non-Overlapping

It must not absorb CANDIDATE-002 responsibilities.

---

## Q5 — Implementation Neutral

Do not bind the design to:

```text
Cursor

Claude Code

OpenAI Agents SDK

LangGraph

Python

Java
```

---

## Q6 — Stop Safety

The design must explicitly define when the asset should stop.

---

## Q7 — Human Review Compatible

Outputs must support human review.

---

# 23. Required Document Structure

The new document should approximately follow:

```text
# CANDIDATE-001 — Targeted Engineering Revision

## 1. Design Scope

## 2. Evidence Basis

## 3. Asset Classification

## 4. Asset Identity

## 5. Purpose and Value

## 6. Trigger Model

## 7. Input Model

## 8. Output Model

## 9. Revision Lifecycle

## 10. Responsibility Boundary

## 11. Dependency Model

## 12. Artifact Model

## 13. Validation Model

## 14. Failure and Stop Conditions

## 15. Non-Goals

## 16. Type Rationale

## 17. Interaction Model

## 18. Implementation Readiness

## 19. Open Questions

## 20. Design Summary
```

The exact structure may improve if necessary.

However, do not remove critical design dimensions.

---

# 24. Milestone Update

Update:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

to reflect:

```text
Stage D2A
CANDIDATE-001 Asset Design
```

Status:

```text
COMPLETED
```

Then set:

```text
Current Stage:
Stage D2B — CANDIDATE-002 Asset Design
```

Do NOT mark:

```text
Stage D2
```

as fully completed.

D2 is complete only after all planned Strong Candidate designs are reviewed.

---

# 25. Validation Checklist

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

[ ] Asset identity defined

[ ] Purpose bounded

[ ] Positive triggers defined

[ ] Negative triggers defined

[ ] Required inputs defined

[ ] Optional inputs distinguished

[ ] Outputs defined

[ ] Revision lifecycle defined

[ ] Responsibility boundary explicit

[ ] CANDIDATE-001 owns revision orchestration

[ ] CANDIDATE-002 owns validation execution

[ ] Dependency relationship defined as REQUESTS

[ ] Artifact responsibilities defined

[ ] Revision validation distinguished from repository validation

[ ] Failure conditions defined

[ ] Stop conditions defined

[ ] Non-goals defined

[ ] Why SKILL rationale included

[ ] Interaction model included

[ ] Implementation readiness evaluated

[ ] Open questions preserved

[ ] No implementation created

[ ] No actual Skill created

[ ] No CANDIDATE-002 design created

[ ] No unrelated files modified
```

---

# 26. Final Report

Before commit, report:

## Design Summary

```text
Asset Name

Asset Category

Asset Type

Primary Purpose
```

## Boundary Summary

```text
What CANDIDATE-001 owns

What it delegates

What it explicitly does not own
```

## Dependency Summary

Explain the relationship:

```text
CANDIDATE-001
REQUESTS
CANDIDATE-002
```

## Implementation Readiness

Report:

```text
READY

CONDITIONALLY_READY

or

NOT_READY
```

with reasons.

## Files Changed

Expected:

```text
Created:
05-candidate-001-targeted-engineering-revision.md

Modified:
MILESTONE-001.md
```

---

# 27. Commit

Suggested commit:

```text
docs(milestone-001): design candidate-001 targeted engineering revision
```

Before commit:

```bash
git status
git diff --check
```

Then commit and push.

---

# 28. Stop Condition

After push:

```text
STOP.
```

Do NOT begin:

```text
MILESTONE-001 Stage D2B — CANDIDATE-002 Asset Design
```

Stage D2B requires external review.

After completion, report exactly:

```text
MILESTONE-001 Stage D2A completed and pushed.
```
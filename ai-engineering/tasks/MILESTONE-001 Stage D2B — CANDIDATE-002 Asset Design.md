# MILESTONE-001 Stage D2B — CANDIDATE-002 Asset Design

## 0. Mission

Design the second Strong Candidate identified during:

```text
MILESTONE-001 Stage C
Asset Candidate Identification
```

Target:

```text
CANDIDATE-002
Repository Tooling Validation Gate
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

The objective is to produce a complete, reviewable, implementation-neutral design for CANDIDATE-002.

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

Do not design based only on the candidate title.

Trace:

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
CANDIDATE-002
```

Conceptual name:

```text
Repository Tooling Validation Gate
```

The final asset identity may refine the conceptual name if necessary.

However, do not unnecessarily rename the candidate.

---

# 3. Scope

Create one new design document:

```text
ai-engineering/milestones/MILESTONE-001/
06-candidate-002-repository-tooling-validation-gate.md
```

Update:

```text
ai-engineering/milestones/MILESTONE-001/
MILESTONE-001.md
```

Expected changes:

```text
Create:
06-candidate-002-repository-tooling-validation-gate.md

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
```

Do NOT create:

```text
Actual Skill

Actual Agent

Actual Workflow

Validation Script

Runtime Code

Repository Configuration

Tool Configuration

Cursor Rule
```

This stage produces only:

```text
Asset Design Specification
```

---

# 4. Evidence Basis

Create a concise section documenting:

```text
Historical Process
        ↓
Engineering Pattern
        ↓
CANDIDATE-002
```

Explain:

```text
Why repository validation emerged as a recurring engineering pattern

Why validation execution should become reusable

Why validation should not be repeatedly re-designed per task
```

Important:

Do not reproduce the full process inventory.

Only include evidence necessary to justify the asset.

---

# 5. Asset Classification

Classify CANDIDATE-002 using:

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
EXECUTABLE

Type:
SKILL
```

But classification must be justified.

Explicitly compare against:

```text
AGENT

WORKFLOW

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
Why is repository validation a reusable bounded capability?

Why is it not merely a Checklist?

Why is it not a Workflow?

Why is it not an autonomous Agent?
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

The core problem should not be described merely as:

```text
Run pytest.
```

The reusable capability should instead address:

```text
Repository-aware validation execution
+
Evidence normalization
```

The asset should answer:

```text
How can an engineering process request repository validation
without embedding repository tooling logic everywhere?
```

---

# 8. Trigger Model

Define when the Validation Gate should be invoked.

Evaluate positive triggers such as:

```text
Revision Completed

Repository Change Produced

Pre-Commit Validation

Task Completion Validation

Explicit Validation Request
```

Also define negative triggers.

For example conceptually:

```text
Pure Exploratory Analysis

No Repository Context

No Validation Target

Validation Not Applicable
```

Do not blindly use these examples.

Derive the final trigger model from the asset nature.

---

# 9. Input Model

Define the minimum validation request contract.

Evaluate:

```text
Repository Context

Validation Target

Requested Validation Scope

Changed Artifact Context

Requested Gate Set

Acceptance Context

Known Constraints
```

Separate:

```text
Required Inputs
```

from:

```text
Optional Inputs
```

Important distinction:

The caller may request validation.

The caller should NOT need to understand the internal execution details of every repository tool.

Avoid requiring:

```text
Exact pytest command

Exact ruff command

Exact mypy command
```

unless explicitly required by repository context.

The input model should support abstraction such as:

```text
Validate changed Python domain model
```

rather than:

```text
python -m pytest tests/test_domain.py -q
```

The exact command belongs to validation execution logic.

---

# 10. Validation Authority Model

Explicitly define authority boundaries.

Distinguish:

```text
Validation Requirement
```

from:

```text
Validation Execution
```

and:

```text
Validation Deferral
```

Expected conceptual model:

```text
Caller / Upstream Asset
        │
        │ Determines validation requirement
        ▼
CANDIDATE-002
        │
        │ Owns
        ▼
Validation Execution
        │
        ▼
Validation Evidence
```

Important:

CANDIDATE-002 does NOT own:

```text
Whether validation is required

Whether validation may be deferred
```

These decisions belong to external authority.

CANDIDATE-002 owns:

```text
How requested validation is executed
```

within repository-aware boundaries.

---

# 11. Gate Selection Model

This is a key design section.

Define how validation gates are selected.

Possible conceptual sources:

```text
Explicit Request

Repository Convention

Change Type

Validation Capability

Declared Policy
```

Do NOT prematurely assume one source must control everything.

Design a precedence model.

For example conceptually:

```text
Explicit Request
        ↓
Repository Convention
        ↓
Change-Type Inference
        ↓
Default Gate Set
```

But validate whether this model is appropriate.

Important:

The Validation Gate should not randomly invent tools.

It should operate based on discoverable repository evidence.

Define:

```text
Gate Selection Inputs

Gate Selection Authority

Gate Selection Precedence

Unsupported Gate Behavior
```

---

# 12. Repository Inspection Model

Before validation execution, define what repository inspection is required.

Evaluate:

```text
Project Language

Build System

Package Manager

Test Framework

Linting Tool

Static Analysis Tool

Existing Validation Scripts

Repository Documentation

CI Configuration
```

Important principle:

```text
Inspect Before Execute
```

Do NOT assume every repository uses:

```text
pytest

ruff

mypy
```

The asset must be repository-aware.

However, do not design an exhaustive repository detection engine.

Keep the inspection model bounded to validation needs.

---

# 13. Validation Lifecycle

Design the internal lifecycle.

Recommended conceptual structure:

```text
1. Receive Validation Request
        ↓
2. Inspect Repository Context
        ↓
3. Resolve Applicable Gates
        ↓
4. Prepare Execution Context
        ↓
5. Execute Gates
        ↓
6. Collect Evidence
        ↓
7. Normalize Results
        ↓
8. Report Validation Outcome
        ↓
9. Stop
```

Do not blindly copy the lifecycle.

The final design must explicitly distinguish:

```text
Inspection

Gate Selection

Execution

Evidence Collection

Result Normalization
```

Avoid:

```text
Request
↓
Immediately run commands
```

---

# 14. Validation Gate Model

Define the conceptual structure of a Validation Gate.

A gate may include:

```text
Gate Identity

Purpose

Applicability

Execution Requirement

Result

Evidence
```

Do NOT define implementation-level classes or JSON schemas.

Do NOT assume every gate is a CLI command.

A gate may conceptually represent:

```text
Unit Test

Lint

Static Analysis

Build

Repository Consistency Check
```

The design should allow multiple repository ecosystems.

---

# 15. Result Model

This is a critical section.

Define normalized result semantics.

At minimum evaluate:

```text
PASSED

FAILED

ERROR

NOT_APPLICABLE

NOT_EXECUTED
```

Do not add states without justification.

Explicitly distinguish:

```text
FAILED
```

from:

```text
ERROR
```

Conceptually:

```text
FAILED
=
Gate executed successfully
but validation criteria failed.

ERROR
=
Gate could not be correctly executed.
```

Also distinguish:

```text
NOT_APPLICABLE
```

from:

```text
NOT_EXECUTED
```

Important:

Do not collapse all non-success states into:

```text
FAILED
```

---

# 16. Aggregate Outcome Model

Define how multiple gate results produce an overall validation outcome.

Example scenario:

```text
Unit Tests:
PASSED

Lint:
PASSED

Static Analysis:
ERROR
```

Do not automatically call this:

```text
PARTIAL_SUCCESS
```

unless the semantics are explicitly justified.

Define:

```text
Aggregate Outcome Rules
```

Consider:

```text
All Applicable Gates Passed

Any Applicable Gate Failed

Any Required Gate Error

Some Gates Not Applicable

Requested Gate Not Executed
```

Important:

The aggregate outcome must preserve evidence.

Avoid hiding:

```text
One failing gate
```

behind:

```text
Overall completed
```

---

# 17. Evidence Model

Define the minimum validation evidence contract.

Evaluate:

```text
Gate Identity

Applicability

Execution Status

Result

Evidence Summary

Evidence Reference

Execution Context
```

Optional dimensions may include:

```text
Timestamp

Command Reference

Environment Context
```

Do not require excessive telemetry.

The objective is:

```text
Evidence sufficient for human review
+
Evidence usable by upstream assets
```

Important:

```text
Validation Result
```

is not enough.

The system should preserve:

```text
Why
```

the result was produced.

---

# 18. Partial Execution Model

Explicitly address partial validation.

Example:

```text
Requested:
Unit Test
Lint
Static Analysis

Executed:
Unit Test → PASSED
Lint → PASSED
Static Analysis → ERROR
```

Define:

```text
What the Validation Gate reports

What it does NOT decide
```

Important boundary:

CANDIDATE-002 reports:

```text
Validation Evidence
```

CANDIDATE-002 does NOT independently decide:

```text
Whether partial validation is acceptable.
```

That decision belongs to:

```text
Caller

Workflow

Policy

Human Authority
```

The asset should report facts, not silently make acceptance policy decisions.

---

# 19. Failure and Stop Conditions

Define explicit failure conditions.

Evaluate:

```text
Repository Context Missing

Unsupported Repository Tooling

Gate Cannot Be Resolved

Required Tool Missing

Execution Environment Invalid

Gate Execution Error
```

Define appropriate outcomes:

```text
ERROR

NOT_EXECUTED

BLOCKED

ESCALATED
```

Be careful:

Not every execution problem should become:

```text
FAILED
```

The asset should distinguish:

```text
Validation failed
```

from:

```text
Validation could not be executed
```

---

# 20. Responsibility Boundary

Explicitly define what CANDIDATE-002 owns.

Expected ownership:

```text
Repository Context Inspection

Applicable Gate Resolution

Validation Execution

Evidence Collection

Result Normalization

Validation Reporting
```

Explicit non-ownership:

```text
Revision Planning

Revision Execution

Validation Requirement Policy

Validation Deferral Authorization

Task Completion Decision
```

The design must remain compatible with:

```text
CANDIDATE-001
REQUESTS
CANDIDATE-002
```

---

# 21. Dependency Model

Define dependencies conceptually.

CANDIDATE-002 may consume:

```text
Repository Context

Validation Request

Repository Convention

Tooling Configuration
```

But avoid binding to:

```text
Cursor

GitHub Actions

pytest

Maven

Gradle

npm
```

unless these appear as examples of repository-specific implementations.

The design should remain:

```text
Tool-aware
```

without becoming:

```text
Tool-bound
```

---

# 22. Interaction Model

Document the conceptual interaction:

```text
Upstream Asset / Human
        │
        │ Validation Request
        ▼
CANDIDATE-002
Repository Tooling Validation Gate
        │
        ▼
Inspect Repository
        │
        ▼
Resolve Gates
        │
        ▼
Execute Validation
        │
        ▼
Collect Evidence
        │
        ▼
Normalize Results
        │
        ▼
Validation Report
        │
        ▼
External Authority
```

Important:

The Validation Gate reports evidence.

External authority evaluates acceptance.

---

# 23. Non-Goals

Explicitly define exclusions.

At minimum evaluate:

```text
Revision Planning

Revision Execution

Validation Requirement Policy

Validation Deferral Authorization

Task Completion Decision

CI/CD Orchestration

Continuous Monitoring

Repository Refactoring

Automatic Tool Installation
```

The asset must not become:

```text
Universal DevOps Agent
```

---

# 24. Type Rationale

Add a dedicated section:

```text
Why SKILL?
```

Explain why the candidate represents:

```text
EXECUTABLE
→
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

The central rationale should evaluate:

```text
Bounded capability

Explicit invocation

Reusable procedure

Defined input/output

Explicit stop
```

---

# 25. Implementation Readiness

Evaluate whether the asset design is ready for future implementation.

Use the repository framework vocabulary.

Do NOT invent a new readiness state.

Use only the vocabulary already defined by:

```text
04-candidate-design-framework.md
```

Evaluate:

```text
Identity Clarity

Trigger Clarity

Input Clarity

Gate Selection Model

Repository Inspection Model

Result Model

Evidence Model

Responsibility Boundary

Failure Model
```

If unresolved dependencies exist, record them explicitly.

---

# 26. Open Questions

Record genuine unresolved design questions.

Do NOT force premature answers.

Potential areas to evaluate:

```text
How repository conventions should be discovered

Whether gate precedence should be configurable

Whether validation plans should become first-class artifacts

How environment reproducibility should be represented
```

Only retain questions that genuinely emerge during design.

---

# 27. Design Quality Requirements

The design must satisfy:

## Q1 — Evidence Grounded

Traceable to historical engineering patterns.

---

## Q2 — Repository-Aware

Must inspect repository context before validation execution.

---

## Q3 — Tool-Neutral

Must not assume a fixed ecosystem.

---

## Q4 — Authority Separation

Must distinguish:

```text
Validation Requirement
```

from:

```text
Validation Execution
```

and:

```text
Validation Deferral
```

---

## Q5 — Evidence Preserving

Must produce reviewable validation evidence.

---

## Q6 — Result Precision

Must distinguish:

```text
FAILED

ERROR

NOT_APPLICABLE

NOT_EXECUTED
```

---

## Q7 — No Silent Acceptance

Must not independently declare partial validation acceptable.

---

## Q8 — Bounded

Must not expand into:

```text
CI/CD System

DevOps Agent

Repository Management Agent
```

---

# 28. Required Document Structure

The new document should approximately follow:

```text
# CANDIDATE-002 — Repository Tooling Validation Gate

## 1. Design Scope

## 2. Evidence Basis

## 3. Asset Classification

## 4. Asset Identity

## 5. Purpose and Value

## 6. Trigger Model

## 7. Input Model

## 8. Validation Authority Model

## 9. Gate Selection Model

## 10. Repository Inspection Model

## 11. Validation Lifecycle

## 12. Validation Gate Model

## 13. Result Model

## 14. Aggregate Outcome Model

## 15. Evidence Model

## 16. Partial Execution Model

## 17. Failure and Stop Conditions

## 18. Responsibility Boundary

## 19. Dependency Model

## 20. Interaction Model

## 21. Non-Goals

## 22. Type Rationale

## 23. Implementation Readiness

## 24. Open Questions

## 25. Design Summary
```

The structure may be improved where necessary.

Do not remove critical design dimensions.

---

# 29. Milestone Update

Update:

```text
ai-engineering/milestones/MILESTONE-001/
MILESTONE-001.md
```

to reflect:

```text
Stage D2B
CANDIDATE-002 Asset Design
```

Status:

```text
COMPLETED
```

Then set:

```text
Current Stage:
Stage D2C — CANDIDATE-003 Asset Design
```

Do NOT mark:

```text
Stage D2
```

as completed.

Stage D2 remains open until all planned Strong Candidates are designed and reviewed.

---

# 30. Validation Checklist

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

[ ] SKILL classification rationale included

[ ] Purpose bounded

[ ] Positive triggers defined

[ ] Negative triggers defined

[ ] Required inputs defined

[ ] Optional inputs distinguished

[ ] Validation authority separated from execution authority

[ ] Gate selection model defined

[ ] Gate selection precedence defined

[ ] Repository inspection model defined

[ ] Inspect before execute principle explicit

[ ] Validation lifecycle defined

[ ] Gate model defined

[ ] FAILED vs ERROR distinguished

[ ] NOT_APPLICABLE vs NOT_EXECUTED distinguished

[ ] Aggregate outcome model defined

[ ] Evidence model defined

[ ] Partial execution model defined

[ ] Partial acceptance authority remains external

[ ] Failure conditions defined

[ ] Stop conditions defined

[ ] Responsibility boundary explicit

[ ] CANDIDATE-001 compatibility preserved

[ ] No CI/CD orchestration introduced

[ ] No runtime implementation created

[ ] No tool-specific implementation created

[ ] No unrelated files modified

[ ] Framework readiness vocabulary reused
```

---

# 31. Final Report

Before commit, report:

## Design Summary

```text
Asset Name

Asset Category

Asset Type

Primary Purpose
```

## Gate Model Summary

Explain:

```text
How gates are selected

How repository context is inspected

How unsupported gates are handled
```

## Result Model Summary

Explain:

```text
PASSED

FAILED

ERROR

NOT_APPLICABLE

NOT_EXECUTED
```

and aggregate outcome behavior.

## Authority Boundary

Explicitly summarize:

```text
External Authority:
Determines whether validation is required.

CANDIDATE-002:
Executes requested validation.

External Authority:
Determines whether incomplete validation is acceptable.
```

## Implementation Readiness

Report using framework vocabulary only.

## Files Changed

Expected:

```text
Created:
06-candidate-002-repository-tooling-validation-gate.md

Modified:
MILESTONE-001.md
```

---

# 32. Commit

Suggested commit:

```text
docs(milestone-001): design candidate-002 repository validation gate
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

Do NOT begin:

```text
MILESTONE-001 Stage D2C
CANDIDATE-003 Asset Design
```

Stage D2C requires external review.

After completion, report exactly:

```text
MILESTONE-001 Stage D2B completed and pushed.
```
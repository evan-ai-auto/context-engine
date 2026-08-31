# MILESTONE-001 Stage B — Engineering Pattern Extraction

## Objective

Based on the completed historical inventory from:

```text
MILESTONE-001 Stage A
Historical Process Inventory
```

identify and document engineering patterns observed across:

```text
TASK-001
TASK-002
```

The purpose is:

```text
Historical Evidence
        ↓
Observed Activities
        ↓
Pattern Analysis
        ↓
Engineering Patterns
        ↓
Future Asset Candidate Identification
```

This stage must not yet create:

```text
Skills
Agents
Workflows
Prompt Templates
```

The output is an evidence-based pattern layer.

---

# 1. Core Question

Stage A answered:

> What actually happened?

Stage B must answer:

> What engineering structures, recurring behaviors, or repeatable transformations can be observed from what happened?

Important:

Do not answer:

> What patterns would ideally exist in a perfect engineering methodology?

Only analyze patterns supported by actual project history.

---

# 2. Mandatory Reading

Before modifying anything, inspect the latest repository state.

Read:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md

ai-engineering/milestones/MILESTONE-001/01-process-inventory.md
```

Then inspect supporting source material where needed:

```text
ai-engineering/tasks/TASK-001.md

ai-engineering/tasks/TASK-002.md

ai-engineering/sessions/TASK-001/

ai-engineering/sessions/TASK-002/
```

Pay special attention to:

```text
Architecture Decisions

Repository Compatibility Inspection

Contracts

Implementation Plans

Revisions

Validation

Closeout
```

Do not rely only on the Stage A summary if the original evidence is needed to verify a pattern.

---

# 3. Scope

Stage B is documentation-only.

Allowed changes:

```text
ai-engineering/milestones/MILESTONE-001/
```

Expected new file:

```text
ai-engineering/milestones/MILESTONE-001/
└── 02-engineering-patterns.md
```

Optional update:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

Only update milestone status/progress if appropriate.

Do not modify:

```text
Production Code

Tests

Domain Models

Architecture

Existing Task Documents

Existing Session Documents
```

Do not create:

```text
Skill files

Agent files

Workflow files

Prompt templates
```

---

# 4. Pattern Extraction Model

Every identified pattern must be analyzed using the following structure:

```text
Observed Activities
        ↓
Structural Similarity
        ↓
Trigger
        ↓
Input
        ↓
Transformation
        ↓
Output
        ↓
Validation
        ↓
Pattern Classification
```

Do not treat activity names as patterns automatically.

For example:

```text
Architecture Review
```

is an activity.

It only becomes a meaningful pattern if its structure can be described.

Example:

```text
Architecture Proposal
        ↓
Review Against Constraints
        ↓
Decision / Revision
        ↓
Architecture Freeze
```

The Stage B document should analyze the structure.

---

# 5. Pattern Evidence Levels

Define the following evidence levels.

## Level A — Repeated Pattern

Observed multiple times across independent task stages.

Example concept:

```text
Review
↓
Finding
↓
Targeted Revision
↓
Validation
```

Observed in multiple revisions.

Classification:

```text
REPEATED
```

---

## Level B — Structural Pattern

Observed once but contains a clear structured engineering transformation.

Example:

```text
Repository State
+
New Requirement
        ↓
Compatibility Inspection
        ↓
Compatibility Findings
```

Classification:

```text
STRUCTURAL
```

Important:

A STRUCTURAL pattern is not automatically reusable.

It only means the activity has a recognizable internal structure.

---

## Level C — Single Occurrence

Observed once with insufficient structural evidence or repetition.

Classification:

```text
SINGLE_OCCURRENCE
```

Do not over-extract these.

---

# 6. Pattern Confidence

Each pattern should also receive a confidence level.

Use:

```text
HIGH
MEDIUM
LOW
```

Suggested interpretation:

### HIGH

```text
Observed multiple times
+
Clear input/output
+
Consistent transformation
```

### MEDIUM

```text
Strong single occurrence
+
Clear structure
```

### LOW

```text
Limited evidence
or
Weakly defined structure
```

Do not inflate confidence.

---

# 7. Pattern Maturity

Define a separate maturity dimension.

Use:

```text
OBSERVED

EMERGING

REUSABLE_HYPOTHESIS
```

Definitions:

### OBSERVED

```text
Historical behavior identified
No conclusion about reuse
```

### EMERGING

```text
Repeated or structurally strong
Potentially reusable
```

### REUSABLE_HYPOTHESIS

```text
Strong enough to evaluate in Stage C
Still not a formal Skill / Agent / Workflow
```

Important:

Do not use:

```text
VALIDATED
STABLE
OFFICIAL
```

Those require future project validation.

---

# 8. Create Pattern Document

Create:

```text
ai-engineering/milestones/MILESTONE-001/02-engineering-patterns.md
```

Use the following required structure.

---

# 1. Purpose

Explain:

```text
Stage A
recorded historical activities

Stage B
analyzes structural and recurring engineering patterns
```

Explicitly state:

```text
Patterns are not yet reusable assets.

Patterns are analytical findings.

Formal asset candidates will be identified in Stage C.
```

---

# 2. Evidence Basis

State the primary evidence:

```text
TASK-001

TASK-002

Historical Process Inventory

Revision Records

Validation Records

Closeout Records
```

Include an evidence limitation statement:

```text
Only two completed task samples are currently available.

Therefore pattern confidence must be interpreted conservatively.
```

This statement is mandatory.

---

# 3. Pattern Extraction Method

Document the extraction method.

Use:

```text
1. Identify observed activities

2. Compare activities across tasks

3. Detect repetition

4. Detect structural similarity

5. Identify trigger

6. Identify inputs

7. Identify transformation

8. Identify outputs

9. Identify validation

10. Classify evidence strength

11. Assess pattern maturity
```

Important:

This section defines the analytical method used for this milestone.

Do not define it as a permanent engineering process.

---

# 4. Pattern Summary

Create a summary table.

Recommended columns:

| Pattern ID | Pattern Name | Evidence Level | Occurrences | Confidence | Maturity |
|---|---|---|---:|---|---|

Pattern IDs:

```text
PATTERN-001
PATTERN-002
...
```

Do not use Skill-like IDs.

Do not use:

```text
SKILL-001
AGENT-001
WORKFLOW-001
```

---

# 5. Detailed Pattern Analysis

For each pattern use the following structure.

---

## PATTERN-XXX — Pattern Name

### Classification

```text
REPEATED
```

or:

```text
STRUCTURAL
```

or:

```text
SINGLE_OCCURRENCE
```

---

### Evidence

List:

```text
Tasks

Stages

Documents

Revisions
```

Example format:

```text
Observed In:

TASK-001 Revision-001
TASK-002 Revision-001
TASK-002 Revision-002
```

Only use actual evidence.

---

### Trigger

What historically caused the activity?

Example:

```text
Review finding

Validation gap

Architecture inconsistency

Repository compatibility concern
```

Only use evidence-supported triggers.

---

### Input

What artifacts entered the process?

Examples:

```text
Review findings

Task definition

Architecture decision

Existing repository state

Implementation output
```

---

### Transformation

Describe what happened to the input.

Example:

```text
Finding
↓
Scope Definition
↓
Targeted Revision
↓
Validation
```

Use diagrams where useful.

---

### Output

What artifact or decision resulted?

Examples:

```text
Revision document

Updated implementation

Validation result

Architecture decision
```

---

### Validation

How was the output checked?

Examples:

```text
Tests

Static analysis

Review

Diff inspection
```

Only document actual validation.

---

### Repetition Analysis

Document:

```text
Occurrence Count

Similarity

Variation
```

For example:

```text
Observed three times.

The trigger varied, but the general transformation remained similar.
```

This is important.

Patterns do not need to be identical.

---

### Pattern Boundary

Explicitly document:

```text
What is included

What is not included
```

This prevents over-generalization.

---

### Confidence

Assign:

```text
HIGH
MEDIUM
LOW
```

Explain why.

---

### Maturity

Assign:

```text
OBSERVED
EMERGING
REUSABLE_HYPOTHESIS
```

Explain why.

---

### Extraction Readiness

Choose:

```text
READY_FOR_STAGE_C

NEEDS_MORE_EVIDENCE

DO_NOT_EXTRACT
```

Important:

`READY_FOR_STAGE_C` means:

> Worth evaluating as a potential asset candidate.

It does NOT mean:

> Automatically becomes a Skill.

---

# 6. Required Pattern Investigation Areas

Investigate the following areas.

Important:

These are investigation areas, not mandatory patterns.

Only create a pattern if supported by evidence.

---

## A. Review → Revision → Validation

Investigate whether the following structure appears repeatedly:

```text
Review Finding
        ↓
Issue Identification
        ↓
Targeted Revision
        ↓
Validation
        ↓
Approval / Closure
```

This should receive special attention because multiple revision examples exist.

---

## B. Decision → Freeze → Implementation

Investigate whether TASK-002 demonstrates:

```text
Architecture Decision
        ↓
Decision Review
        ↓
Decision Freeze
        ↓
Implementation
```

Determine whether this is:

```text
STRUCTURAL
```

or:

```text
SINGLE_OCCURRENCE
```

Do not classify it as repeated unless evidence supports repetition.

---

## C. Existing Repository → Compatibility Inspection → Implementation

Investigate:

```text
Existing Repository

+
New Task Requirements

        ↓

Compatibility Inspection

        ↓

Implementation Constraints
```

Analyze whether this is a recognizable structural pattern.

Likely evidence count is limited.

Do not inflate maturity.

---

## D. Contract → Implementation → Test

Investigate the structure introduced during TASK-002.

Potential transformation:

```text
Architecture Decision
        ↓
Domain Contract
        ↓
Implementation
        ↓
Contract Validation
```

Determine:

```text
How much of this was historically explicit?

How much was introduced by revision?

Whether it represents a structural pattern or merely a one-time correction.
```

This distinction is important.

---

## E. Layered Validation

Investigate whether validation occurred in layers.

Possible structure:

```text
Functional Validation
        ↓
Contract Validation
        ↓
Static Validation
        ↓
Regression Validation
        ↓
Repository Hygiene Validation
```

Do not assume this exact sequence is a formal pattern.

Analyze what actually occurred.

---

## F. Task Closeout

Investigate the observed closeout behavior.

Potential structure:

```text
Implementation Complete
        ↓
Validation
        ↓
Status Update
        ↓
Closeout Documentation
        ↓
Deferred Work Capture
```

Determine whether this appears across both tasks or only one.

---

# 7. Cross-Pattern Analysis

After individual patterns, create a comparison section.

Recommended table:

| Pattern | Trigger Type | Input Type | Output Type | Validation | Evidence |
|---|---|---|---|---|---|

Analyze:

```text
Which patterns are repeated

Which patterns are structural

Which patterns are task-specific

Which patterns may depend on project maturity
```

Do not yet map patterns to Skills or Agents.

---

# 8. Pattern Relationships

Create a descriptive relationship model.

For example:

```text
Architecture Pattern
        ↓
Implementation Pattern
        ↓
Validation Pattern
        ↓
Revision Pattern
        ↓
Closeout Pattern
```

But only include relationships supported by observed history.

Important:

This is not yet a Workflow.

Do not define:

```text
mandatory sequence

execution engine

agent orchestration
```

The purpose is only to show observed relationships.

---

# 9. Pattern Anti-Examples

This section is mandatory.

Document cases where activities should NOT automatically be treated as reusable patterns.

Examples of reasoning:

```text
Observed once

Weak input/output definition

Highly project-specific

Dependent on one implementation detail
```

Use actual examples from the project if appropriate.

This section is important to prevent:

```text
Everything becomes a Skill
```

---

# 10. Pattern Extraction Summary

Create three groups.

## Group A — Strong Candidates for Further Analysis

Patterns with:

```text
Repeated evidence

or

Strong structural evidence
```

These may proceed to Stage C evaluation.

---

## Group B — Emerging Patterns

Patterns with:

```text
Some evidence

but

Insufficient repetition
```

These require future validation.

---

## Group C — Historical Activities Only

Activities that should remain historical observations.

Do not extract further.

---

# 11. Evidence Limitations

Explicitly document:

```text
Current sample size:
2 completed tasks
```

Therefore:

```text
Pattern conclusions are provisional.

Repeated observations may still be project-specific.

Structural clarity does not prove general reusability.

Future tasks are required for validation.
```

This section is mandatory.

---

# 12. Stage B Findings

At the end provide a concise summary:

```text
Number of patterns identified

Repeated patterns

Structural patterns

Single-occurrence patterns

Ready for Stage C

Needs future evidence

Do not extract
```

Do not create asset candidates here.

---

# 13. Explicit Non-Goals

Do not:

```text
Create Skills

Create Agents

Create Workflows

Create Prompt Templates

Modify Cursor Rules

Modify Context Engine functionality

Modify TASK-001

Modify TASK-002

Start TASK-003

Promote patterns to validated assets
```

---

# 14. Update Milestone Status

Update:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

only if needed.

Recommended state:

```text
MILESTONE-001

Status:
IN_PROGRESS

Completed Stages:

Stage A — Historical Process Inventory

Current Stage:

Stage B — Engineering Pattern Extraction
```

Do not mark Stage B completed until all work is finished.

Before commit, update Stage B status to:

```text
COMPLETED
```

Then set:

```text
Next Stage:
Stage C — Asset Candidate Identification
```

---

# 15. Quality Checklist

Before commit verify:

```text
[ ] Pattern analysis is based on Stage A evidence

[ ] No ideal workflow was invented

[ ] Repeated patterns distinguish actual repetition

[ ] Structural patterns distinguish single occurrence

[ ] Confidence is conservative

[ ] Maturity is not inflated

[ ] Evidence limitations documented

[ ] Anti-examples included

[ ] No Skills created

[ ] No Agents created

[ ] No Workflows created

[ ] No production code modified
```

---

# 16. Validation

Run:

```bash
git status
```

Then:

```bash
git diff --check
```

Expected:

```text
No whitespace errors
```

Inspect changed files manually.

This stage is documentation-only.

---

# 17. Expected Files

Expected changes:

```text
ai-engineering/milestones/MILESTONE-001/
├── MILESTONE-001.md
├── 01-process-inventory.md
└── 02-engineering-patterns.md
```

Avoid unrelated modifications.

---

# 18. Final Report

Before committing provide:

## Pattern Summary

Report:

```text
Total Patterns Identified:

Repeated:

Structural:

Single Occurrence:
```

---

## Stage C Readiness

Report:

```text
READY_FOR_STAGE_C:

NEEDS_MORE_EVIDENCE:

DO_NOT_EXTRACT:
```

---

## Evidence Limitations

Summarize the main limitations.

---

## Files Changed

List files.

---

## Scope Check

Explicitly confirm:

```text
No Skill created

No Agent created

No Workflow created

No production code modified

No Context Engine functionality changed
```

---

# 19. Commit

Suggested commit message:

```text
docs(milestone-001): extract engineering patterns
```

Before commit:

```bash
git status
git diff --check
```

Then commit and push.

After push:

```text
STOP.
```

Do not begin Stage C.

The next step is:

```text
MILESTONE-001 Stage B Review
```
# MILESTONE-001 Stage C — Asset Candidate Identification

## 0. Mission

Based on the approved outputs of:

```text
MILESTONE-001 Stage A — Historical Process Inventory

MILESTONE-001 Stage B — Engineering Pattern Extraction
```

perform:

```text
Asset Candidate Identification
```

The purpose of this stage is to evaluate whether existing engineering patterns have sufficient value and maturity to become reusable AI Engineering assets.

The transformation model is:

```text
Historical Engineering Evidence
        ↓
Engineering Patterns
        ↓
Candidate Evaluation
        ↓
Merge / Split / Reject / Defer
        ↓
Asset Candidates
```

Potential asset types include:

```text
Skill Candidate

Agent Candidate

Workflow Candidate

Composite Candidate
```

Important:

```text
Pattern
≠
Asset

Asset Candidate
≠
Approved Asset

Approved Asset
≠
Implemented Asset
```

Stage C only identifies and evaluates candidates.

Do not implement actual Skills, Agents, or Workflows.

---

# 1. Mandatory Reading

Before making any changes, inspect the latest repository state.

Read:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md

ai-engineering/milestones/MILESTONE-001/01-process-inventory.md

ai-engineering/milestones/MILESTONE-001/02-engineering-patterns.md
```

Also inspect relevant repository documentation if necessary to understand the current AI Engineering structure.

Pay particular attention to each Pattern's:

```text
Classification

Evidence Level

Occurrence Evidence

Confidence

Maturity

Extraction Readiness

Boundaries

Evidence Limitations
```

Stage C consumes the approved conclusions of Stage B.

Do not silently re-run Pattern Extraction.

Do not reinterpret historical evidence unless a clear inconsistency is discovered.

If an inconsistency is discovered:

```text
STOP
```

Document the issue.

Do not silently modify Stage A or Stage B conclusions.

---

# 2. Stage C Scope

This stage is documentation-only.

Primary new file:

```text
ai-engineering/milestones/MILESTONE-001/
└── 03-asset-candidates.md
```

Optional update:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

Expected scope:

```text
ai-engineering/milestones/MILESTONE-001/
```

Do not modify:

```text
src/

tests/

Production code

Context Engine runtime functionality

TASK-001

TASK-002

Historical session records

Existing Pattern definitions

Existing Pattern evidence
```

Do not create:

```text
Actual Skills

Actual Agents

Actual Workflows

Prompt files

Executable orchestration

Automation scripts
```

This stage produces:

```text
Candidate Analysis
```

not:

```text
Asset Implementation
```

---

# 3. Core Architectural Principle

Do NOT use:

```text
One Pattern
        ↓
One Skill
```

Do NOT use:

```text
Every Complex Pattern
        ↓
Agent
```

Do NOT use:

```text
Multiple Steps
        ↓
Workflow
```

Instead:

```text
Pattern Set
        ↓
Candidate Evaluation
        ↓
Merge
Split
Reject
Defer
        ↓
Candidate Hypothesis
```

The objective is to avoid:

```text
Skill Explosion

Agent Explosion

Workflow Explosion

Overlapping Assets

Artificial Abstraction
```

---

# 4. Candidate Evaluation Framework

Every potential candidate should be evaluated using the following dimensions.

Use:

```text
HIGH

MEDIUM

LOW
```

for qualitative ratings.

Do not use artificial numerical scores unless genuinely useful.

---

## 4.1 Reusability

Question:

```text
Can this behavior reasonably occur across multiple future projects,
repositories, or engineering tasks?
```

Guidance:

```text
HIGH
Likely reusable across many projects.

MEDIUM
Reusable in a limited class of projects or engineering situations.

LOW
Primarily specific to the current repository or one-off situation.
```

---

## 4.2 Generality

Question:

```text
Is the behavior independent from the specific Context Engine domain?
```

Example:

```text
Review
↓
Targeted Revision
↓
Validation

High Generality
```

Example:

```text
Specific ContextNode serialization validation

Low Generality
```

---

## 4.3 Trigger Clarity

Question:

```text
Can we clearly identify when this capability should be invoked?
```

Examples:

```text
A structured review identifies findings requiring revision.
```

```text
A new task must be executed against an existing repository.
```

Values:

```text
HIGH
Trigger is explicit and easy to detect.

MEDIUM
Trigger exists but requires contextual interpretation.

LOW
Trigger is vague or difficult to identify.
```

---

## 4.4 Input / Output Clarity

Question:

```text
Can we identify stable categories of inputs and expected outputs?
```

Example:

```text
Input:
- Review findings
- Repository state
- Task scope

Output:
- Revision scope
- Changed files
- Validation result
```

Values:

```text
HIGH
Inputs and outputs are clearly identifiable.

MEDIUM
Some inputs or outputs vary.

LOW
No stable input/output boundary exists.
```

---

## 4.5 Procedural Determinism

Question:

```text
Can this capability be performed using a mostly repeatable procedure?
```

High determinism may indicate:

```text
Potential Skill
```

Low determinism may indicate:

```text
Potential Agent
```

Values:

```text
HIGH
Mostly repeatable steps.

MEDIUM
Stable structure with contextual decisions.

LOW
Highly exploratory.
```

---

## 4.6 Reasoning Autonomy

Question:

```text
Does execution require independent reasoning,
exploration,
judgment,
or decision-making?
```

High autonomy may indicate:

```text
Potential Agent
```

Low autonomy may indicate:

```text
Potential Skill
```

Values:

```text
HIGH

MEDIUM

LOW
```

---

## 4.7 Orchestration Value

Question:

```text
Is the primary value coordinating multiple independent activities
or capabilities?
```

High orchestration may indicate:

```text
Potential Workflow
```

Examples:

```text
Review
↓
Revision
↓
Validation
↓
Closeout
```

Values:

```text
HIGH

MEDIUM

LOW
```

---

# 5. Candidate Type Heuristics

Use the following as reasoning guidance.

These are not mandatory rules.

---

## Potential Skill

Characteristics:

```text
Clear trigger

Stable procedure

Stable input

Stable output

High repeatability

Limited autonomy
```

Conceptually:

```text
Input
↓
Procedure
↓
Output
```

---

## Potential Agent

Characteristics:

```text
Open-ended analysis

Repository exploration

Independent judgment

Context-sensitive decisions

Variable execution path
```

Conceptually:

```text
Goal
↓
Explore
↓
Reason
↓
Decide
↓
Produce Result
```

---

## Potential Workflow

Characteristics:

```text
Multiple activities

Defined sequence

Cross-step dependencies

Lifecycle coordination
```

Conceptually:

```text
Step A
↓
Step B
↓
Step C
↓
Step D
```

---

## Potential Composite

Use only when evidence suggests:

```text
Workflow
+
Supporting Skills
```

or:

```text
Agent
+
Supporting Skills
```

Important:

Do not implement the composite.

Only document the architectural hypothesis.

---

# 6. Candidate Status Model

Every candidate must receive one status.

---

## STRONG_CANDIDATE

Use when:

```text
Evidence is sufficient

Boundary is reasonably clear

Reuse value is high

Candidate type hypothesis is credible

Stage D design is justified
```

---

## EMERGING_CANDIDATE

Use when:

```text
Potential exists

But boundary or evidence remains incomplete
```

Do not immediately design as an implemented asset.

---

## DEFERRED

Use when:

```text
Potential value exists

But future evidence is required
```

---

## REJECTED

Use when:

```text
The Pattern should not currently become an asset
```

This is a valid outcome.

Do not force asset creation.

---

# 7. Candidate Type Values

Use one of:

```text
SKILL

AGENT

WORKFLOW

COMPOSITE

NONE
```

Important:

`NONE` is a valid result.

Example:

```text
Useful Engineering Pattern
≠
Reusable AI Engineering Asset
```

---

# 8. Create Candidate Document

Create:

```text
ai-engineering/milestones/MILESTONE-001/03-asset-candidates.md
```

Use the structure below.

---

# 1. Purpose

Explain the transformation:

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

Explicitly state:

```text
This document identifies potential reusable AI Engineering assets.

It does not create assets.

It does not approve assets.

Formal candidate design occurs in Stage D.
```

---

# 2. Input Boundary

Document that Stage C consumes:

```text
02-engineering-patterns.md
```

Rules:

```text
Patterns marked READY_FOR_STAGE_C
receive full candidate evaluation.

Patterns marked NEEDS_MORE_EVIDENCE
may be evaluated lightly,
but should not be promoted without explicit justification.
```

Do not silently promote weak patterns.

---

# 3. Candidate Evaluation Framework

Document the following dimensions:

```text
Reusability

Generality

Trigger Clarity

Input / Output Clarity

Procedural Determinism

Reasoning Autonomy

Orchestration Value
```

Also explain:

```text
SKILL

AGENT

WORKFLOW

COMPOSITE

NONE
```

are:

```text
Candidate Type Hypotheses
```

not implementation decisions.

---

# 4. Pattern-to-Candidate Evaluation Matrix

Create a matrix similar to:

| Pattern | Reusability | Generality | Trigger | I/O | Determinism | Autonomy | Orchestration | Candidate Type | Status |
|---|---|---|---|---|---|---|---|---|---|

Evaluate all Stage B Patterns.

At minimum:

```text
PATTERN-001

PATTERN-002

PATTERN-003

PATTERN-004

PATTERN-005

PATTERN-006

PATTERN-007

PATTERN-008

PATTERN-009
```

Important:

The matrix is an evaluation aid.

It must not automatically imply:

```text
Pattern
=
Candidate
```

---

# 5. Merge / Split / Reject Analysis

This section is mandatory.

Analyze whether patterns represent:

```text
Independent capabilities

Different abstraction layers

Phases of one larger lifecycle

Supporting capabilities

Internal steps

Non-reusable engineering habits
```

---

## Required Investigation Area A

Analyze the relationship between:

```text
PATTERN-001
Review → Targeted Revision → Validation

PATTERN-003
Tooling Validation Gate

PATTERN-008
Layered Validation Composition
```

Questions:

```text
Are these three independent capabilities?

Are PATTERN-003 and PATTERN-008 different abstraction layers?

Should validation become a supporting capability rather than an independent workflow?

Would multiple separate validation assets overlap?

Should any pattern remain an internal step?
```

Do not assume merge or separation.

Use evidence.

---

## Required Investigation Area B

Analyze:

```text
PATTERN-002
Task Closeout Lifecycle

PATTERN-004
Explicit Task Boundary Definition

PATTERN-009
Learning Capture After Friction
```

Questions:

```text
Are these phases of one engineering lifecycle?

Are they independent reusable capabilities?

Does the lifecycle have sufficient orchestration value?

Should learning capture remain an internal lifecycle activity?

Would separate assets create unnecessary fragmentation?
```

Avoid automatically creating:

```text
Task Start Skill

Task Closeout Skill

Learning Skill
```

unless evidence strongly supports separation.

---

## Required Investigation Area C

Analyze:

```text
PATTERN-005
Decision → Freeze → Implement

PATTERN-007
Contract → Implement → Contract Test
```

Questions:

```text
Are these generic engineering capabilities?

Are they primarily architecture/domain engineering patterns?

Would they be useful across Java and Python projects?

Do they require autonomous reasoning?

Would an Agent hypothesis be justified?

Or should they remain engineering patterns only?
```

Do not promote because the patterns appear sophisticated.

---

## Required Investigation Area D

Analyze:

```text
PATTERN-006
Repository Compatibility Inspection
```

Current Stage B status includes limited evidence.

Determine whether it should be:

```text
DEFERRED
```

or:

```text
EMERGING_CANDIDATE
```

Do not promote to STRONG_CANDIDATE unless Stage B evidence justifies it.

---

# 6. Candidate Definitions

Create actual candidate definitions only after Merge / Split / Reject analysis.

Use IDs:

```text
CANDIDATE-001

CANDIDATE-002

CANDIDATE-003
```

Do not create unnecessary candidates.

Prefer fewer, stronger candidates.

---

## CANDIDATE-XXX — Candidate Name

### Source Patterns

List:

```text
PATTERN-XXX
```

If multiple patterns contribute:

```text
Primary Patterns

Supporting Patterns
```

may be used.

---

### Candidate Hypothesis

Describe:

```text
What reusable engineering capability may exist?
```

Do not write an implementation prompt.

Do not write an actual Skill specification.

Do not write Agent instructions.

Do not write Workflow orchestration.

---

### Candidate Type Hypothesis

Choose:

```text
SKILL

AGENT

WORKFLOW

COMPOSITE

NONE
```

Explain why.

---

### Trigger

Describe:

```text
When might this candidate be invoked?
```

---

### Likely Inputs

Describe stable input categories.

Example:

```text
Task scope

Repository state

Review findings

Existing documentation
```

---

### Expected Outputs

Describe expected output categories.

Example:

```text
Analysis result

Revision scope

Validation result

Engineering report
```

---

### Evaluation

Document:

```text
Reusability

Generality

Trigger Clarity

Input / Output Clarity

Procedural Determinism

Reasoning Autonomy

Orchestration Value
```

Use:

```text
HIGH

MEDIUM

LOW
```

---

### Boundary

Document:

```text
Handles

Does Not Handle
```

This is mandatory.

Example:

```text
Handles:
Candidate-level validation orchestration.

Does Not Handle:
Project-specific test implementation.
```

---

### Status

Choose:

```text
STRONG_CANDIDATE

EMERGING_CANDIDATE

DEFERRED

REJECTED
```

Explain the decision.

---

### Stage D Readiness

Choose:

```text
READY_FOR_DESIGN

NEEDS_MORE_EVIDENCE

DO_NOT_DESIGN
```

---

# 7. Candidate Consolidation

After all candidate definitions, create:

```text
Candidate Consolidation Summary
```

Example:

| Candidate | Source Patterns | Type Hypothesis | Status | Stage D Readiness |
|---|---|---|---|---|

The summary must distinguish:

```text
Strong Candidates

Emerging Candidates

Deferred Candidates

Rejected Candidates
```

---

# 8. Explicit Non-Goals

Stage C must not:

```text
Create Skills

Create Agents

Create Workflows

Create Prompt Templates

Create Agent Instructions

Create Skill Definitions

Create Workflow Definitions

Modify Production Code

Modify Tests

Modify Context Engine Runtime

Modify TASK-001

Modify TASK-002

Modify Stage A

Modify Stage B Pattern Conclusions
```

Also do not create directories such as:

```text
ai-engineering/extraction/agents/

ai-engineering/extraction/skills/

ai-engineering/extraction/workflows/
```

unless those directories already exist and are only being referenced.

Stage C is:

```text
Candidate Identification
```

not:

```text
Asset Extraction
```

---

# 9. Update Milestone Status

After Stage C analysis is complete, update:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

Only update lifecycle status.

Recommended structure:

```text
Status:
IN_PROGRESS

Completed Stages:

- Stage A — Historical Process Inventory
- Stage B — Engineering Pattern Extraction
- Stage C — Asset Candidate Identification

Current Stage:

Stage D — Candidate Design
```

Do not mark Stage C complete until the candidate analysis document is complete.

Do not begin Stage D.

---

# 10. Validation

Before committing:

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

Then manually inspect:

```text
03-asset-candidates.md
```

Verify:

```text
[ ] Every Pattern evaluated

[ ] Weak evidence not silently promoted

[ ] No one-pattern-one-asset mapping

[ ] Merge analysis completed

[ ] Split analysis completed where necessary

[ ] Rejection/defer decisions allowed

[ ] Candidate boundaries defined

[ ] Candidate type is hypothesis only

[ ] No actual Skill created

[ ] No actual Agent created

[ ] No actual Workflow created
```

---

# 11. Expected Files

Expected new file:

```text
ai-engineering/milestones/MILESTONE-001/
└── 03-asset-candidates.md
```

Expected modified file:

```text
ai-engineering/milestones/MILESTONE-001/
└── MILESTONE-001.md
```

Preferred change scope:

```text
2 files
```

If additional files are changed:

```text
STOP
```

Explain why before proceeding.

---

# 12. Final Report

Before commit, provide:

## Stage C Summary

Summarize:

```text
Patterns Evaluated

Strong Candidates

Emerging Candidates

Deferred Candidates

Rejected Candidates
```

---

## Candidate Summary

For each candidate:

```text
Candidate ID

Candidate Name

Source Patterns

Candidate Type Hypothesis

Status

Stage D Readiness
```

---

## Merge / Split / Reject Summary

Explicitly report:

```text
Patterns Merged

Patterns Split

Patterns Deferred

Patterns Rejected
```

Explain major decisions.

---

## Boundary Check

Explicitly confirm:

```text
No Skill Created

No Agent Created

No Workflow Created

No Prompt Created

No Production Code Modified

No Test Modified

No Context Engine Runtime Modified
```

---

# 13. Commit

Suggested commit message:

```text
docs(milestone-001): identify reusable asset candidates
```

Before commit:

```bash
git status
git diff --check
```

Then commit and push.

---

# 14. Stop Condition

After push:

```text
STOP.
```

Do not begin:

```text
MILESTONE-001 Stage D — Candidate Design
```

Stage D requires external review.

After completion, report:

```text
MILESTONE-001 Stage C completed and pushed.
```
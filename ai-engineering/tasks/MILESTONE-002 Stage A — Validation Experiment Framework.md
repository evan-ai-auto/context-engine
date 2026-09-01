# MILESTONE-002 Stage A — Validation Experiment Framework

## 0. Mission

Create:

```text
MILESTONE-002
Asset Experimental Validation
```

The purpose of MILESTONE-002 is:

```text
Validate designed AI Engineering Assets
through controlled usage
in real engineering work.
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

MILESTONE-002 must NOT repeat asset discovery.

The focus now changes from:

```text
What reusable assets might exist?
```

to:

```text
Do the designed assets actually provide
repeatable value in real engineering work?
```

---

# 1. Mandatory Reading

Before making changes, read:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

Read the following documents carefully:

```text
ai-engineering/milestones/MILESTONE-001/05-candidate-001-targeted-engineering-revision.md

ai-engineering/milestones/MILESTONE-001/06-candidate-002-repository-tooling-validation-gate.md

ai-engineering/milestones/MILESTONE-001/07-candidate-003-task-closeout-lifecycle.md

ai-engineering/milestones/MILESTONE-001/09-stage-d3-candidate-portfolio-reassessment.md

ai-engineering/milestones/MILESTONE-001/10-candidate-004-explicit-task-boundary-definition.md

ai-engineering/milestones/MILESTONE-001/11-stage-e-asset-validation-plan.md

ai-engineering/milestones/MILESTONE-001/12-final-architecture-review-and-closeout.md
```

Understand the following architectural principles before proceeding:

```text
Designed Asset
≠
Validated Asset

Validated Asset
≠
Implementation Ready

Composable Portfolio
≠
Mandatory Pipeline

Asset Output
≠
External Acceptance

More Process
≠
Better Engineering

More Assets
≠
Better Portfolio
```

---

# 2. Stage A Scope

Create:

```text
ai-engineering/milestones/MILESTONE-002/
```

Create:

```text
ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md
```

Create:

```text
ai-engineering/milestones/MILESTONE-002/
01-validation-experiment-framework.md
```

Expected changes:

```text
Created:

ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md

ai-engineering/milestones/MILESTONE-002/
01-validation-experiment-framework.md
```

Do NOT modify MILESTONE-001.

Do NOT modify candidate designs.

Do NOT implement any assets.

---

# 3. MILESTONE-002 Mission Definition

Define the milestone mission.

The milestone should establish a disciplined approach for:

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

The milestone must focus on:

```text
Prospective Validation
```

rather than:

```text
Retrospective Discovery
```

Explicitly distinguish:

```text
MILESTONE-001
Retrospective Evidence
+
Asset Discovery

MILESTONE-002
Prospective Evidence
+
Asset Validation
```

---

# 4. Define Asset Validation Experiment

Define the concept:

```text
Asset Validation Experiment
```

An experiment should answer:

```text
Given a real engineering task,

if a designed asset is intentionally invoked,

does it provide repeatable engineering value
with acceptable process overhead?
```

The experiment must NOT be defined as:

```text
Artificial Demo

Synthetic Benchmark

Self-Declared Success
```

The preferred source of evidence is:

```text
Real Engineering Work
```

However, do not require every real engineering task to become an experiment.

Asset validation must be intentional.

---

# 5. Experiment Lifecycle

Define a lightweight lifecycle.

Recommended conceptual lifecycle:

```text
Candidate Task
        ↓
Experiment Eligibility
        ↓
Asset Selection
        ↓
Experiment Definition
        ↓
Asset Invocation
        ↓
Engineering Work
        ↓
Observation
        ↓
Evidence Capture
        ↓
Assessment
        ↓
Disposition
```

Determine whether any stages should be merged.

Avoid unnecessary ceremony.

The framework should remain:

```text
Minimal
Practical
Repeatable
Evidence-Oriented
```

---

# 6. Experiment Eligibility

Define when a real engineering task is suitable for use as an Asset Validation Experiment.

Possible dimensions:

```text
Task Relevance

Asset Relevance

Meaningful Complexity

Observable Outcome

Context Variation

Repeatability Potential
```

Also define when a task is NOT suitable.

Examples may include:

```text
Task too trivial

No relevant asset responsibility

No observable outcome

Artificial task created only to prove success
```

Important principle:

```text
Not Every Task
should become
an Experiment.
```

---

# 7. Asset Selection

Define how an experiment selects an asset.

Current validation-ready assets:

```text
CANDIDATE-001
Targeted Engineering Revision

CANDIDATE-002
Repository Tooling Validation Gate

CANDIDATE-003
Task Closeout Lifecycle

CANDIDATE-004
Explicit Task Boundary Definition
```

Do NOT design automatic asset invocation.

Do NOT create an Agent.

Do NOT create an orchestration engine.

The framework should support:

```text
Human-Guided Asset Selection
```

For each experiment record:

```text
Why was this asset selected?
```

Also record:

```text
Why were other potentially relevant assets
not selected?
```

But keep this lightweight.

Do not require unnecessary justification for every non-selected asset.

---

# 8. Single Asset First Principle

Establish whether the framework should recommend:

```text
Single Asset Validation First
```

before:

```text
Cross-Asset Composition Validation
```

The goal is to reduce attribution ambiguity.

Example problem:

```text
004
↓
001
↓
002
↓
003
```

If the outcome is poor:

```text
Which asset caused the problem?
```

Therefore distinguish:

```text
Single Asset Experiment
```

from:

```text
Composition Experiment
```

Single asset experiments should generally precede composition experiments.

However:

```text
Generally
≠
Mandatory Universal Rule
```

Allow exceptions when the engineering context genuinely requires composition.

---

# 9. Experiment Record Structure

Define a lightweight conceptual structure for recording experiments.

Possible fields:

```text
Experiment ID

Date

Engineering Task

Task Context

Selected Asset

Asset Version / Design Reference

Invocation Reason

Experiment Objective

Expected Value

Input Conditions

Actual Invocation

Observed Outcome

Human Intervention

Observed Benefits

Observed Failures

Unexpected Behavior

Process Overhead

Reuse Assessment

Recommended Disposition
```

Do NOT:

```text
Create Database Schema

Create Pydantic Model

Create JSON Schema

Create Runtime Object

Create Persistence Layer
```

This is only a:

```text
Conceptual Evidence Structure
```

Do not prematurely freeze field names.

---

# 10. Human Intervention Evidence

Explicitly define:

```text
Human Intervention
```

as an important evidence dimension.

Examples:

```text
Clarification required

Boundary correction

Output correction

Manual validation

Decision override

Process skip

Unexpected recovery
```

The goal is not to treat human intervention as failure.

Instead:

```text
Human Intervention
=
Evidence about Asset Autonomy
+
Boundary Quality
+
Process Overhead
```

Determine what level of intervention is acceptable.

Avoid introducing artificial autonomy metrics.

---

# 11. Positive Validation

Define positive validation evidence.

Possible indicators:

```text
Clearer reasoning

Reduced repeated mistakes

Improved task consistency

Useful output structure

Lower revision cost

Better validation coverage

Improved traceability

Successful reuse across contexts
```

Important:

```text
Single Success
≠
Validation
```

Positive evidence should accumulate across meaningful contexts.

Do not define arbitrary numeric thresholds unless justified by evidence.

---

# 12. Negative Validation

Explicitly define:

```text
Negative Validation
```

Negative validation asks:

```text
When should this asset NOT be invoked?
```

Examples:

```text
Task too small

No meaningful ambiguity

Asset responsibility not relevant

External process already defines the boundary

Process overhead exceeds value
```

Core principle:

```text
Reusable
≠
Universally Applicable
```

Negative evidence is valuable.

Do NOT treat:

```text
Non-Invocation
```

as failure.

---

# 13. Failure Evidence

Define what constitutes meaningful failure evidence.

Examples:

```text
Asset output not useful

Responsibility unclear

Boundary conflict

Repeated human correction

High process overhead

Context incompatibility

Unexpected coupling

No observable value
```

Failure should lead to possible outcomes:

```text
REFINE

NARROW_SCOPE

MERGE

DEFER

REJECT
```

Do not assume every failure means:

```text
REJECT
```

---

# 14. Process Overhead

Define:

```text
Process Overhead
```

as a first-class validation dimension.

Potential indicators:

```text
Additional reasoning burden

Additional documentation

Additional human intervention

Additional execution steps

Context switching

Decision latency
```

Core question:

```text
Engineering Value
>
Process Overhead
?
```

Avoid requiring numerical scoring.

The framework should allow qualitative evidence first.

Future quantitative metrics may emerge only after repeated evidence exists.

---

# 15. Context Variation

Define why validation must occur across different contexts.

Potential variation:

```text
Task Complexity

Task Type

Repository Type

Ambiguity Level

Change Size

Validation Requirements
```

Core principle:

```text
One Context
≠
General Reusability
```

Do not define fixed minimum sample sizes.

Instead define:

```text
Evidence Diversity
```

as more important than raw repetition count.

---

# 16. Experiment Outcomes

Define possible experiment outcomes.

Suggested categories:

```text
SUPPORTED

PARTIALLY_SUPPORTED

NOT_SUPPORTED

INCONCLUSIVE
```

Then distinguish:

```text
Experiment Outcome
```

from:

```text
Asset Disposition
```

Example:

```text
Experiment:
PARTIALLY_SUPPORTED

Asset Disposition:
CONTINUE_VALIDATION
```

Do not allow one experiment to automatically determine final asset status.

---

# 17. Asset Disposition Model

Define possible portfolio-level decisions after accumulating evidence.

Possible dispositions:

```text
CONTINUE_VALIDATION

REFINE

NARROW_SCOPE

MERGE

DEFER

REJECT

VALIDATED
```

Important:

```text
VALIDATED
```

does NOT automatically mean:

```text
IMPLEMENTATION_READY
```

The framework should preserve:

```text
VALIDATED
        ↓
Implementation Readiness Assessment
        ↓
IMPLEMENTATION_READY
```

---

# 18. Validation Stop Conditions

Define when validation should pause or stop.

Possible reasons:

```text
Evidence sufficient

Evidence repeatedly contradictory

Asset responsibility unstable

Asset duplicates another asset

Process overhead consistently excessive

No suitable real engineering context available
```

Important:

```text
No More Experiments
```

does not always mean:

```text
VALIDATED
```

Possible result:

```text
DEFER
```

---

# 19. Evidence Quality

Define evidence quality dimensions.

Possible areas:

```text
Task Authenticity

Outcome Observability

Context Diversity

Failure Visibility

Human Intervention Visibility

Traceability

Bias Awareness
```

Explicitly avoid:

```text
Success Narrative Only
```

The framework should support evidence that challenges the original asset design.

---

# 20. Validation Bias Controls

Define lightweight safeguards against confirmation bias.

Examples:

```text
Record failures

Record non-use cases

Separate experiment outcome from disposition

Do not treat compliance as value

Do not assume designed assets are useful

Allow rejection
```

Core principle:

```text
The purpose of validation
is not to prove the asset correct.

The purpose of validation
is to discover whether the asset deserves reuse.
```

---

# 21. Relationship to Existing Asset Lifecycle

Review the current conceptual lifecycle:

```text
OBSERVED
        ↓
PATTERN
        ↓
CANDIDATE
        ↓
DESIGNED
        ↓
VALIDATION_READY
        ↓
VALIDATING
        ↓
VALIDATED
        ↓
IMPLEMENTATION_READY
        ↓
IMPLEMENTED
        ↓
EVOLVING
```

Also allow:

```text
VALIDATING
        ↓
REFINE
        ↓
VALIDATION_READY
```

and:

```text
VALIDATING
        ↓
REJECTED
```

and:

```text
VALIDATING
        ↓
MERGED
```

Do NOT automatically formalize this lifecycle as a repository-wide Rule.

For Stage A:

```text
Review
+
Document
```

only.

If the lifecycle is not yet sufficiently stable, explicitly mark it:

```text
Emerging Lifecycle Model
```

rather than:

```text
Final Architecture Standard
```

---

# 22. Experiment vs Asset Implementation

Explicitly establish:

```text
Experimental Invocation
≠
Asset Packaging
```

During validation:

```text
Asset Design
```

may be used as:

```text
Experimental Procedure
```

without creating:

```text
SKILL.md

WORKFLOW.md

Agent Definition

Runtime Component
```

This distinction is critical.

---

# 23. Cross-Asset Validation

Define a future path for:

```text
Composition Validation
```

Possible composition:

```text
004
↓
001
↓
002
↓
003
```

However Stage A should NOT execute composition experiments.

Only define:

```text
When composition validation becomes appropriate.
```

Prerequisites may include:

```text
Individual asset evidence exists

Individual responsibilities are sufficiently stable

Composition is required by a real engineering context
```

---

# 24. Stage A Deliverables

The framework should produce:

```text
Validation Experiment Definition

Experiment Lifecycle

Eligibility Guidance

Asset Selection Guidance

Experiment Record Structure

Human Intervention Guidance

Positive Validation Guidance

Negative Validation Guidance

Failure Evidence Guidance

Process Overhead Guidance

Context Variation Guidance

Experiment Outcome Model

Asset Disposition Model

Validation Stop Conditions

Evidence Quality Principles

Bias Controls

Emerging Asset Lifecycle Model
```

Do NOT produce:

```text
Asset Implementations

Runtime Components

Automation

Database Models

Agent Architecture
```

---

# 25. Required Document Structure

Create:

```text
01-validation-experiment-framework.md
```

Suggested structure:

```text
# MILESTONE-002 Stage A — Validation Experiment Framework

## 1. Mission

## 2. Validation Context

## 3. What Is an Asset Validation Experiment?

## 4. Experiment Lifecycle

## 5. Experiment Eligibility

## 6. Asset Selection

## 7. Single Asset and Composition Experiments

## 8. Experiment Record Structure

## 9. Human Intervention Evidence

## 10. Positive Validation

## 11. Negative Validation

## 12. Failure Evidence

## 13. Process Overhead

## 14. Context Variation

## 15. Experiment Outcomes

## 16. Asset Disposition Model

## 17. Validation Stop Conditions

## 18. Evidence Quality

## 19. Validation Bias Controls

## 20. Emerging Asset Lifecycle Model

## 21. Experimental Invocation vs Implementation

## 22. Future Composition Validation

## 23. Stage A Conclusions

## 24. Next Validation Boundary
```

The structure may be improved.

Do not remove the core dimensions.

---

# 26. MILESTONE-002.md

Create the milestone index.

Recommended conceptual structure:

```text
# MILESTONE-002

## Mission

Validate designed AI Engineering assets
through controlled usage
in real engineering work.

## Background

Reference MILESTONE-001 completion.

## Current Portfolio

List:

CANDIDATE-001
CANDIDATE-002
CANDIDATE-003
CANDIDATE-004

All currently:

VALIDATION_READY

## Milestone Strategy

Validate assets progressively.

Single Asset First.

Evidence Before Packaging.

## Stages

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

## Explicit Non-Goals

No premature packaging.

No automatic invocation.

No agent orchestration.

No simultaneous validation of all assets.

## Status

IN_PROGRESS
```

Stage names may be refined.

Do not over-specify future stages.

---

# 27. Explicit Non-Goals

Stage A must NOT:

```text
Validate CANDIDATE-001

Validate CANDIDATE-002

Validate CANDIDATE-003

Validate CANDIDATE-004

Implement Skills

Implement Workflows

Create Agents

Create Rules

Create Runtime Code

Create a Database

Create a Validation Platform

Create Automated Invocation
```

Stage A establishes:

```text
Validation Method
```

only.

---

# 28. Final Review Checklist

Before commit:

```text
[ ] MILESTONE-001 architecture understood

[ ] MILESTONE-002 mission defined

[ ] Validation experiment concept defined

[ ] Experiment lifecycle defined

[ ] Experiment eligibility defined

[ ] Asset selection guidance defined

[ ] Single asset validation principle addressed

[ ] Composition validation boundary addressed

[ ] Evidence structure defined conceptually

[ ] Human intervention addressed

[ ] Positive validation defined

[ ] Negative validation defined

[ ] Failure evidence defined

[ ] Process overhead addressed

[ ] Context variation addressed

[ ] Experiment outcomes separated from asset disposition

[ ] Validation stop conditions defined

[ ] Evidence quality addressed

[ ] Confirmation bias addressed

[ ] Emerging lifecycle model reviewed

[ ] Experimental invocation distinguished from implementation

[ ] No asset implementation created

[ ] No unrelated files modified
```

Run:

```bash
git status
git diff --check
```

---

# 29. Final Report Before Commit

Before commit, report:

## MILESTONE-002 Mission

```text
...
```

## Validation Framework

```text
...
```

## Key Architectural Decisions

```text
...
```

## Lifecycle Model Status

```text
...
```

## Explicit Non-Goals

```text
...
```

## Files Changed

Expected:

```text
Created:

ai-engineering/milestones/MILESTONE-002/MILESTONE-002.md

ai-engineering/milestones/MILESTONE-002/
01-validation-experiment-framework.md
```

---

# 30. Commit

Suggested commit:

```text
docs(milestone-002): establish asset validation experiment framework
```

Before commit:

```bash
git status
git diff --check
```

Then commit and push.

---

# 31. Stop Condition

After push:

```text
STOP.
```

Do NOT automatically:

```text
Validate CANDIDATE-001

Create validation records

Implement assets

Create skills

Create workflows

Create agents

Modify MILESTONE-001
```

After completion, report exactly:

```text
MILESTONE-002 Stage A completed and pushed.
```
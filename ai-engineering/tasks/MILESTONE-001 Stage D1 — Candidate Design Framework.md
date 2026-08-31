# MILESTONE-001 Stage D1 — Candidate Design Framework

## 0. Mission

Begin:

```text
MILESTONE-001 Stage D — Candidate Design
```

by first establishing a unified framework for designing reusable AI Engineering assets.

This stage is:

```text
Design Framework Definition
```

It is NOT:

```text
Individual Candidate Design
```

Do not formally design:

```text
CANDIDATE-001

CANDIDATE-002

CANDIDATE-003

CANDIDATE-004

CANDIDATE-005
```

The objective is to define a reusable:

```text
Asset Design Schema
```

that later candidate design stages must follow.

The conceptual transformation is:

```text
Engineering Pattern
        ↓
Asset Candidate
        ↓
Candidate Design Framework
        ↓
Asset Specification
        ↓
Future Extraction / Implementation
```

---

# 1. Mandatory Reading

Before making any changes, inspect the latest repository state.

Read:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md

ai-engineering/milestones/MILESTONE-001/03-asset-candidates.md
```

Also inspect existing AI Engineering documentation to understand repository conventions.

Pay particular attention to:

```text
Candidate Type Hypothesis

Candidate Status

Stage D Readiness

Trigger

Likely Inputs

Expected Outputs

Boundary

Dependency Relationships

Lifecycle Relationships
```

Important constraints:

```text
CANDIDATE-001
READY_FOR_DESIGN

CANDIDATE-002
READY_FOR_DESIGN

CANDIDATE-003
READY_FOR_DESIGN

CANDIDATE-004
READY_FOR_DESIGN
but Emerging Candidate

CANDIDATE-005
OBSERVE_ONLY
NOT eligible for formal design
```

Do not reinterpret Stage C conclusions.

---

# 2. Stage D1 Scope

Create:

```text
ai-engineering/milestones/MILESTONE-001/
└── 04-candidate-design-framework.md
```

Optionally update:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

Expected change scope:

```text
1 new file

Optional:
1 lifecycle status update
```

Do not modify:

```text
01-process-inventory.md

02-engineering-patterns.md

03-asset-candidates.md

Production code

Tests

Runtime implementation
```

Do not create:

```text
Actual Skills

Actual Agents

Actual Workflows

Prompt implementations

Executable automation
```

---

# 3. Core Design Principle

Stage D1 defines:

```text
How assets should be designed
```

not:

```text
What a specific asset should do
```

The framework must be:

```text
Candidate-neutral

Implementation-neutral

Tool-neutral

Model-neutral

Project-neutral
```

It must support future:

```text
Skill

Agent

Workflow

Composite
```

assets.

---

# 4. Asset Design Schema

Define a common Asset Design Schema.

Every formally designed asset should eventually be describable through the following conceptual dimensions.

---

## 4.1 Identity

Define:

```text
Asset ID

Asset Name

Asset Type

Version

Status
```

Example conceptual statuses:

```text
DESIGN_DRAFT

DESIGN_REVIEW

DESIGN_APPROVED

IMPLEMENTATION_READY

IMPLEMENTED

DEPRECATED
```

Do not define runtime storage format.

---

# 4.2 Purpose

Every asset must define:

```text
Problem

Purpose

Value

Primary Responsibility
```

The purpose section should answer:

```text
Why does this asset exist?
```

---

# 4.3 Trigger Model

Define when an asset should be considered for invocation.

Possible trigger categories:

```text
EXPLICIT

EVENT

STATE

CONTEXT

MANUAL
```

Examples:

```text
EXPLICIT
User explicitly requests repository validation.

EVENT
A review identifies findings.

STATE
A task enters closeout state.

CONTEXT
Repository compatibility uncertainty is detected.

MANUAL
Operator chooses to invoke capability.
```

Important:

Trigger Model is not execution logic.

It is an invocation contract.

---

# 4.4 Input Model

Define the conceptual structure of inputs.

Every asset should distinguish:

```text
Required Inputs

Optional Inputs

Context Inputs

Constraints
```

Example:

```text
Required Inputs
- Task scope

Optional Inputs
- Review findings

Context Inputs
- Repository metadata

Constraints
- Allowed modification scope
```

Do not define JSON schemas yet.

---

# 4.5 Output Model

Define:

```text
Primary Outputs

Secondary Outputs

Evidence Outputs

Side Effects
```

Important distinction:

```text
Output
≠
Side Effect
```

Example:

```text
Output
Validation Report

Evidence Output
Command Results

Side Effect
Repository files modified
```

Assets should explicitly declare side effects.

---

# 4.6 Responsibility Boundary

Every asset must define:

```text
Handles

Does Not Handle
```

This is mandatory.

The purpose is to prevent:

```text
Asset Responsibility Overlap
```

Each boundary should be written from the perspective of:

```text
Primary Responsibility
```

Do not create artificial exclusions.

---

# 4.7 Dependency Model

Define relationships between assets.

Support conceptual dependency types:

```text
REQUIRES

REQUESTS

CONSUMES

PRODUCES_FOR

OPTIONALLY_USES
```

Examples:

```text
Revision Asset
REQUESTS
Validation Asset
```

```text
Closeout Workflow
CONSUMES
Boundary Artifact
```

Important:

Dependency must not automatically mean implementation coupling.

Document:

```text
Conceptual Dependency
≠
Runtime Dependency
```

---

# 4.8 Artifact Model

Define how assets may exchange conceptual artifacts.

An artifact should describe:

```text
Artifact Name

Producer

Consumers

Purpose

Lifecycle

Format Constraints
```

Important:

Stage D1 must not define concrete formats such as:

```text
JSON

YAML

Markdown
```

unless format is intrinsic to the asset.

Artifacts should remain:

```text
Implementation-neutral
```

---

# 4.9 Validation Model

Every asset design must define how its success can be evaluated.

Support:

```text
PRECONDITIONS

EXECUTION VALIDATION

OUTPUT VALIDATION

EVIDENCE VALIDATION

ACCEPTANCE CRITERIA
```

Important distinction:

```text
Asset Validation
```

versus:

```text
Repository Validation
```

Example:

```text
Asset Validation
Did the asset produce its expected output?

Repository Validation
Does the repository pass technical validation?
```

These are not the same.

---

# 4.10 Lifecycle Model

Define the conceptual lifecycle:

```text
PROPOSED
        ↓
DESIGNED
        ↓
REVIEWED
        ↓
APPROVED
        ↓
IMPLEMENTATION_READY
        ↓
IMPLEMENTED
        ↓
EVOLVED
        ↓
DEPRECATED
```

Explain that:

```text
Candidate Lifecycle
```

and:

```text
Asset Lifecycle
```

are different.

Example:

```text
Candidate
↓
Design
↓
Approved Asset Design
↓
Implementation
```

---

# 4.11 Versioning Model

Define conceptual versioning principles.

Support:

```text
Design Version

Implementation Version
```

Explain:

```text
Design Version
≠
Implementation Version
```

Do not introduce a complicated semantic versioning policy yet.

Keep it simple.

---

# 5. Asset Type Specialization

The common schema must support:

```text
SKILL

AGENT

WORKFLOW

COMPOSITE
```

But each type requires additional characteristics.

---

## 5.1 Skill Design Characteristics

Define:

```text
Clear Trigger

Stable Procedure

Limited Autonomy

Repeatable Inputs

Predictable Outputs
```

Additional Skill dimensions:

```text
Procedure

Execution Constraints

Expected Evidence
```

---

## 5.2 Agent Design Characteristics

Define:

```text
Goal

Autonomy Boundary

Reasoning Scope

Exploration Scope

Decision Authority

Stop Conditions
```

Important:

Do not define model-specific prompts.

---

## 5.3 Workflow Design Characteristics

Define:

```text
Entry Condition

Stages

Transitions

Dependencies

Artifacts

Exit Conditions
```

Important:

A Workflow should orchestrate capabilities.

Avoid embedding all capability logic inside a Workflow definition.

---

## 5.4 Composite Design Characteristics

Define:

```text
Composition Model

Child Assets

Coordination Rules

Shared Artifacts

Boundary Ownership
```

Important:

Composite should not become:

```text
Everything Container
```

---

# 6. Candidate Design Template

Create a reusable conceptual template.

Suggested structure:

```text
# Asset Design

## 1. Identity

## 2. Source Candidate

## 3. Purpose

## 4. Asset Type Rationale

## 5. Trigger Model

## 6. Input Model

## 7. Output Model

## 8. Responsibility Boundary

## 9. Dependency Model

## 10. Artifact Model

## 11. Validation Model

## 12. Lifecycle Model

## 13. Versioning

## 14. Risks and Open Questions

## 15. Implementation Readiness
```

Important:

This is a design template.

Do not instantiate it for specific Candidates in Stage D1.

---

# 7. Implementation Readiness Model

Define a conceptual readiness classification.

Suggested values:

```text
DESIGN_ONLY

REQUIRES_EVIDENCE

READY_FOR_IMPLEMENTATION

NOT_READY
```

Explain:

```text
DESIGN_APPROVED
≠
READY_FOR_IMPLEMENTATION
```

An asset may have an approved design but still require:

```text
More Evidence

Repository Integration Analysis

Runtime Architecture

Tooling Decisions
```

before implementation.

---

# 8. Open Questions Model

Define how future asset designs should record uncertainty.

Suggested categories:

```text
EVIDENCE_GAP

BOUNDARY_RISK

DEPENDENCY_RISK

IMPLEMENTATION_UNKNOWN

VALIDATION_UNKNOWN
```

Important:

Open questions should not be silently hidden.

They are first-class design information.

---

# 9. Explicit Non-Goals

Stage D1 must not:

```text
Design CANDIDATE-001

Design CANDIDATE-002

Design CANDIDATE-003

Design CANDIDATE-004

Design CANDIDATE-005
```

Do not create:

```text
Skill files

Agent files

Workflow files

Prompt templates

Automation code

Runtime orchestration
```

Do not define:

```text
LLM Provider

Model Selection

Prompt Format

Framework Implementation

LangGraph

CrewAI

AutoGen

Cursor-specific implementation
```

Stage D1 defines:

```text
Asset Design Architecture
```

not:

```text
AI Runtime Architecture
```

---

# 10. Quality Requirements

The framework should satisfy:

## Q1 — Candidate Neutrality

It must not assume:

```text
All Candidates
=
Skills
```

---

## Q2 — Implementation Neutrality

It must support future implementation in:

```text
Cursor

Claude Code

OpenAI Agents

LangGraph

Custom Python

Custom Java

Future frameworks
```

without depending on any of them.

---

## Q3 — Boundary Safety

It must explicitly support:

```text
Handles

Does Not Handle

Dependencies

Artifacts
```

---

## Q4 — Lifecycle Clarity

It must distinguish:

```text
Pattern

Candidate

Asset Design

Asset Implementation
```

---

## Q5 — Evolution Support

It must allow future:

```text
New Evidence
        ↓
Candidate Update
        ↓
Design Revision
        ↓
Implementation Evolution
```

without requiring a complete redesign.

---

# 11. Document Structure

Create:

```text
04-candidate-design-framework.md
```

Recommended structure:

```text
# Candidate Design Framework

## 1. Purpose

## 2. Design Principles

## 3. Asset Lifecycle Model

## 4. Common Asset Design Schema

### 4.1 Identity

### 4.2 Purpose

### 4.3 Trigger Model

### 4.4 Input Model

### 4.5 Output Model

### 4.6 Responsibility Boundary

### 4.7 Dependency Model

### 4.8 Artifact Model

### 4.9 Validation Model

### 4.10 Lifecycle Model

### 4.11 Versioning Model

## 5. Asset Type Specialization

### 5.1 Skill

### 5.2 Agent

### 5.3 Workflow

### 5.4 Composite

## 6. Candidate Design Template

## 7. Implementation Readiness

## 8. Open Questions Model

## 9. Design Governance

## 10. Explicit Non-Goals
```

Exact wording may improve if repository conventions suggest better terminology.

---

# 12. Design Governance

Define minimal governance rules.

At minimum:

```text
No Candidate becomes an Asset without design review.

No Asset Design becomes Implementation without readiness review.

Boundary changes require dependency review.

New evidence may revise Candidate or Asset Design.

Implementation must not silently redefine Design intent.
```

Avoid creating an overly complex governance process.

---

# 13. Milestone Status Update

Update:

```text
ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

to reflect:

```text
Stage D
IN_PROGRESS

Completed:

Stage A
Historical Process Inventory

Stage B
Engineering Pattern Extraction

Stage C
Asset Candidate Identification

Stage D1
Candidate Design Framework

Current:

Stage D2
Strong Candidate Design
```

Do not mark the entire Stage D complete.

---

# 14. Validation

Before commit:

```bash
git status
```

Expected:

```text
modified:
MILESTONE-001.md

new:
04-candidate-design-framework.md
```

Then:

```bash
git diff --check
```

Expected:

```text
No whitespace errors
```

Manually verify:

```text
[ ] No specific Candidate designed

[ ] Common schema supports all Asset Types

[ ] Pattern ≠ Candidate ≠ Asset Design ≠ Implementation is explicit

[ ] Trigger Model defined

[ ] Input / Output Model defined

[ ] Boundary Model defined

[ ] Dependency Model defined

[ ] Artifact Model defined

[ ] Validation Model defined

[ ] Lifecycle Model defined

[ ] Implementation Readiness defined

[ ] Open Questions supported

[ ] No framework-specific implementation assumptions
```

---

# 15. Final Report

Before commit, provide:

## Framework Summary

Summarize:

```text
Common Asset Design Schema

Asset Type Specialization

Lifecycle Model

Dependency Model

Artifact Model

Validation Model
```

---

## Boundary Confirmation

Explicitly confirm:

```text
No Candidate Designed

No Skill Created

No Agent Created

No Workflow Created

No Prompt Created

No Runtime Implementation Created
```

---

## Files Changed

Report:

```text
New Files

Modified Files
```

Expected:

```text
New:
04-candidate-design-framework.md

Modified:
MILESTONE-001.md
```

---

# 16. Commit

Suggested commit message:

```text
docs(milestone-001): define candidate design framework
```

Before commit:

```bash
git status
git diff --check
```

Then commit and push.

---

# 17. Stop Condition

After push:

```text
STOP.
```

Do not begin:

```text
MILESTONE-001 Stage D2 — Strong Candidate Design
```

Stage D2 requires external review.

After completion, report exactly:

```text
MILESTONE-001 Stage D1 completed and pushed.
```
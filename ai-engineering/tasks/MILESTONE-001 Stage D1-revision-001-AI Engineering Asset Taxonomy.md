# MILESTONE-001 Stage D1 Revision-001 — AI Engineering Asset Taxonomy

## 0. Mission

Perform a targeted architectural revision to:

```text
MILESTONE-001 Stage D1
Candidate Design Framework
```

The objective is to expand the Asset Type model from the current narrow classification:

```text
SKILL
AGENT
WORKFLOW
COMPOSITE
```

into a more complete but still intentionally minimal:

```text
AI Engineering Asset Taxonomy v0.1
```

This revision must preserve the existing Stage D1 framework.

This is NOT a redesign.

The intended transformation is:

```text
Existing Candidate Design Framework
        ↓
Targeted Asset Taxonomy Expansion
        ↓
AI Engineering Asset Design Framework
```

---

# 1. Mandatory Reading

Before making changes, inspect:

```text
ai-engineering/milestones/MILESTONE-001/04-candidate-design-framework.md

ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
```

Also inspect existing repository structures related to extracted AI Engineering assets, especially:

```text
ai-engineering/extraction/
```

Pay attention to any existing evidence that demonstrates repository-level asset categories beyond:

```text
Agent
Skill
Workflow
```

Important:

Do not invent taxonomy categories merely because they are theoretically possible.

Repository evidence should influence the design.

---

# 2. Revision Scope

Primary file:

```text
ai-engineering/milestones/MILESTONE-001/
04-candidate-design-framework.md
```

Optional supporting update:

```text
ai-engineering/milestones/MILESTONE-001/
MILESTONE-001.md
```

Expected scope:

```text
Primary:
Modify Asset Type Model

Secondary:
Update terminology if required
```

Do NOT modify:

```text
01-process-inventory.md

02-engineering-patterns.md

03-asset-candidates.md
```

Do NOT:

```text
Design specific Candidates

Create concrete Skills

Create concrete Agents

Create concrete Workflows

Create concrete Rules

Create concrete Templates

Create concrete Checklists

Create runtime implementation
```

---

# 3. Core Revision Objective

Upgrade the framework from:

```text
Asset Type
├── SKILL
├── AGENT
├── WORKFLOW
└── COMPOSITE
```

to a layered taxonomy.

The taxonomy should distinguish:

```text
What the asset fundamentally represents
```

rather than merely:

```text
How the asset is executed
```

---

# 4. AI Engineering Asset Taxonomy v0.1

Introduce the following conceptual taxonomy.

```text
AI Engineering Assets
│
├── EXECUTABLE
│   │
│   ├── AGENT
│   ├── SKILL
│   └── WORKFLOW
│
├── GOVERNANCE
│   │
│   └── RULE
│
├── STRUCTURAL
│   │
│   ├── TEMPLATE
│   └── CHECKLIST
│
├── KNOWLEDGE
│   │
│   └── KNOWLEDGE
│
└── COMPOSITION
    │
    └── COMPOSITE
```

This taxonomy is intentionally minimal.

Do NOT add additional categories such as:

```text
POLICY

CONSTRAINT

PLAYBOOK

PROCEDURE

SCHEMA

CONTRACT

RUBRIC

VALIDATOR

QUALITY_GATE

SCRIPT

HOOK

TRIGGER

INTEGRATION
```

at this stage.

These may become future taxonomy extensions only when sufficient evidence exists.

---

# 5. Asset Category Definitions

Define each top-level category.

---

## 5.1 EXECUTABLE

Purpose:

```text
Assets that perform, coordinate, or guide engineering work.
```

Includes:

```text
AGENT
SKILL
WORKFLOW
```

Clarify that:

```text
Executable Asset
```

does not necessarily imply:

```text
Autonomous Runtime
```

A Skill may be manually invoked.

A Workflow may be a conceptual orchestration contract.

---

# 5.2 GOVERNANCE

Purpose:

```text
Assets that constrain or govern acceptable behavior.
```

v0.1 type:

```text
RULE
```

A Rule should be:

```text
Constraint-oriented

Non-procedural

Potentially cross-cutting

Stable
```

Examples may be conceptual only.

Do not create actual Rule assets.

Important distinction:

```text
RULE
≠
WORKFLOW
```

A Rule constrains behavior.

A Workflow defines progression.

---

# 5.3 STRUCTURAL

Purpose:

```text
Assets that provide reusable structure or verification scaffolding.
```

Includes:

```text
TEMPLATE

CHECKLIST
```

Define:

### TEMPLATE

```text
Reusable structural skeleton.
```

### CHECKLIST

```text
Explicit verification or completion items.
```

Important distinction:

```text
CHECKLIST
≠
WORKFLOW
```

A Checklist does not define orchestration.

It defines verification items.

---

# 5.4 KNOWLEDGE

Purpose:

```text
Assets that preserve reusable, confirmed engineering knowledge.
```

v0.1 type:

```text
KNOWLEDGE
```

Important distinction:

```text
KNOWLEDGE Asset
```

versus:

```text
Generated Context
```

Clarify:

```text
KNOWLEDGE
=
Long-lived
Confirmed
Reusable
Maintained
```

While:

```text
Generated Context
=
Derived
Potentially Regenerable
State-dependent
```

Do not define concrete storage locations yet.

Do not introduce:

```text
.ai-context
knowledge/
```

implementation details unless already required by existing repository terminology.

---

# 5.5 COMPOSITION

Purpose:

```text
Assets that coordinate or compose multiple assets.
```

v0.1 type:

```text
COMPOSITE
```

Define:

```text
Composition Model

Child Assets

Coordination Rules

Shared Artifacts

Boundary Ownership
```

Important:

A Composite must not become:

```text
Everything Container
```

A Composite should have a clear composition purpose.

---

# 6. Asset Type Classification Principle

Add an explicit principle:

```text
Asset Type should be assigned after reusable value has been identified.
```

The recommended reasoning sequence:

```text
Historical Evidence
        ↓
Pattern Identification
        ↓
Reusable Value Identification
        ↓
Asset Candidate
        ↓
Asset Nature Classification
        ↓
Asset Type Assignment
```

Do NOT recommend:

```text
Historical Pattern
        ↓
Immediately guess
Agent / Skill / Workflow
```

The classification question should be:

```text
What does this reusable asset fundamentally represent?
```

Potential answers include:

```text
Capability

Process

Constraint

Structure

Verification

Knowledge

Composition
```

Then assign the appropriate Asset Type.

Important principle:

```text
Classification follows nature.
Nature does not follow preferred implementation.
```

---

# 7. Update Common Asset Design Schema

Review the existing:

```text
Common Asset Design Schema
```

and confirm it remains applicable to all v0.1 Asset Types.

Where necessary, clarify how certain dimensions apply differently.

For example:

```text
Trigger Model
```

may be mandatory for:

```text
AGENT
SKILL
WORKFLOW
```

but potentially different for:

```text
RULE
TEMPLATE
CHECKLIST
KNOWLEDGE
```

Do NOT force artificial Trigger Models onto passive assets.

Instead distinguish:

```text
Invocation-Oriented Assets
```

from:

```text
Reference-Oriented Assets
```

Suggested principle:

```text
Not every Asset Type requires the same operational semantics.
```

However, the Common Asset Design Schema should remain conceptually unified.

---

# 8. Asset Type Specialization

Expand the existing:

```text
Asset Type Specialization
```

section.

Existing types:

```text
SKILL
AGENT
WORKFLOW
COMPOSITE
```

Add:

```text
RULE

TEMPLATE

CHECKLIST

KNOWLEDGE
```

---

## 8.1 RULE Design Characteristics

Define dimensions such as:

```text
Scope

Constraint

Applicability

Exceptions

Enforcement Expectation
```

---

## 8.2 TEMPLATE Design Characteristics

Define dimensions such as:

```text
Purpose

Structure

Required Sections

Optional Sections

Usage Guidance
```

---

## 8.3 CHECKLIST Design Characteristics

Define dimensions such as:

```text
Verification Scope

Items

Completion Criteria

Evidence Expectation
```

---

## 8.4 KNOWLEDGE Design Characteristics

Define dimensions such as:

```text
Knowledge Scope

Source Basis

Confidence

Maintenance Responsibility

Regeneration Relationship
```

Important:

Do not create concrete implementations.

---

# 9. Terminology Clarification

Introduce consistent terminology:

```text
Asset Category
```

Example:

```text
EXECUTABLE
```

and:

```text
Asset Type
```

Example:

```text
SKILL
```

The hierarchy should be explicit:

```text
Asset Category
        ↓
Asset Type
        ↓
Asset Design
        ↓
Asset Implementation
```

Also preserve:

```text
Pattern
        ↓
Candidate
        ↓
Asset Classification
        ↓
Asset Design
        ↓
Asset Implementation
```

Ensure:

```text
Pattern
≠
Candidate
≠
Asset Type
≠
Asset Design
≠
Asset Implementation
```

---

# 10. Backward Compatibility Review

Before finalizing, review whether the expanded taxonomy conflicts with:

```text
03-asset-candidates.md

Existing Extraction Structures

Existing Rules Directory

Existing Documentation
```

Do NOT modify those files merely to make terminology perfectly uniform.

Only document compatibility implications inside:

```text
04-candidate-design-framework.md
```

if necessary.

The goal is:

```text
Framework Expansion
```

not:

```text
Repository-wide Refactoring
```

---

# 11. Explicit Non-Goals

This revision must NOT:

```text
Redesign Stage D1

Modify Candidate Definitions

Reclassify Existing Candidates

Promote New Candidates

Create New Candidates

Create Actual Assets

Create New Asset Directories

Introduce Runtime Architecture

Introduce Automation Frameworks
```

Do not expand beyond:

```text
AI Engineering Asset Taxonomy v0.1
```

---

# 12. Quality Requirements

The revised framework must satisfy:

## Q1 — Taxonomy Completeness

It should support more than:

```text
Agent
Skill
Workflow
```

without becoming an uncontrolled taxonomy.

---

## Q2 — Minimality

Only introduce categories necessary for v0.1 conceptual completeness.

---

## Q3 — Classification Safety

The framework must discourage:

```text
Everything becomes a Skill.
```

---

## Q4 — Schema Compatibility

Existing Common Asset Design Schema should remain usable.

Do not duplicate separate schemas for every Asset Type unless truly necessary.

---

## Q5 — Implementation Neutrality

The taxonomy must remain independent from:

```text
Cursor

Claude Code

LangGraph

CrewAI

AutoGen

OpenAI Agents SDK

Python Runtime

Java Runtime
```

---

# 13. Milestone Update

If needed, update:

```text
MILESTONE-001.md
```

to reflect:

```text
Stage D1 Revision-001
AI Engineering Asset Taxonomy
```

Status:

```text
COMPLETED
```

Then:

```text
Current Stage:
Stage D2 — Strong Candidate Design
```

Do NOT mark Stage D complete.

---

# 14. Validation Checklist

Before commit:

```bash
git status

git diff --check
```

Verify:

```text
[ ] Existing Stage D1 structure preserved

[ ] Asset Category introduced

[ ] Asset Type hierarchy explicit

[ ] EXECUTABLE category defined

[ ] GOVERNANCE category defined

[ ] STRUCTURAL category defined

[ ] KNOWLEDGE category defined

[ ] COMPOSITION category defined

[ ] RULE specialization added

[ ] TEMPLATE specialization added

[ ] CHECKLIST specialization added

[ ] KNOWLEDGE specialization added

[ ] Classification follows nature principle added

[ ] Passive assets not forced into artificial Trigger Model

[ ] Pattern ≠ Candidate ≠ Asset Type ≠ Asset Design ≠ Implementation explicit

[ ] No specific Candidate designed

[ ] No actual Asset created

[ ] No runtime implementation introduced

[ ] No unnecessary taxonomy expansion
```

---

# 15. Final Report

Before commit, report:

## Taxonomy Summary

```text
Asset Categories

Asset Types

Classification Principles
```

---

## Framework Compatibility

Explain whether the existing:

```text
Common Asset Design Schema
```

remains compatible with all Asset Types.

---

## Scope Confirmation

Explicitly confirm:

```text
No Candidate Changed

No Candidate Designed

No Actual Asset Created

No Runtime Implementation Added
```

---

## Files Changed

Expected:

```text
Modified:
04-candidate-design-framework.md

Optional:
MILESTONE-001.md
```

---

# 16. Commit

Suggested commit:

```text
docs(milestone-001): expand ai engineering asset taxonomy
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
MILESTONE-001 Stage D1 Revision-001 completed and pushed.
```
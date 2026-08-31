# Candidate Design Framework

## 1. Purpose

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

Stage D1 defines:

```text
How assets should be designed
```

not:

```text
What a specific asset should do
```

```text
This document is candidate-neutral.

It does not formally design CANDIDATE-001 … CANDIDATE-005.

Individual candidate design occurs in later Stage D substages
subject to Stage C readiness (READY_FOR_DESIGN vs OBSERVE_ONLY).
```

```text
Pattern ≠ Candidate ≠ Asset Design ≠ Implementation
```

---

## 2. Design Principles

The framework is:

```text
Candidate-neutral
Implementation-neutral
Tool-neutral
Model-neutral
Project-neutral
```

It must support future asset types:

```text
SKILL
AGENT
WORKFLOW
COMPOSITE
```

Quality requirements:

```text
Q1 Candidate Neutrality
  Do not assume all candidates become Skills.

Q2 Implementation Neutrality
  Support future runtimes (Cursor, Claude Code, OpenAI Agents,
  LangGraph, custom Python/Java, etc.) without depending on any.

Q3 Boundary Safety
  Require Handles / Does Not Handle, Dependencies, Artifacts.

Q4 Lifecycle Clarity
  Distinguish Pattern → Candidate → Asset Design → Implementation.

Q5 Evolution Support
  Allow new evidence → candidate update → design revision →
  implementation evolution without full redesign.
```

---

## 3. Asset Lifecycle Model

### 3.1 Candidate Lifecycle (pre-asset)

```text
Pattern
        ↓
Candidate Identification
        ↓
Candidate Status
  (STRONG / EMERGING / DEFERRED pattern opportunity / REJECTED)
        ↓
Stage D Readiness
  (READY_FOR_DESIGN / NEEDS_MORE_EVIDENCE / DO_NOT_DESIGN)
        ↓
Optional Stage D Treatment
  (e.g. OBSERVE_ONLY)
```

### 3.2 Asset Lifecycle (post-candidate)

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

### 3.3 Separation rule

```text
Candidate Lifecycle
≠
Asset Lifecycle
```

Example path:

```text
Candidate
        ↓
Design (this framework + candidate design template)
        ↓
Approved Asset Design
        ↓
Implementation
```

```text
DESIGN_APPROVED
≠
READY_FOR_IMPLEMENTATION
```

An approved design may still require more evidence, integration analysis,
runtime architecture, or tooling decisions before implementation.

---

## 4. Common Asset Design Schema

Every formally designed asset should be describable through the following dimensions.

Do not define runtime storage formats in this framework.

### 4.1 Identity

```text
Asset ID
Asset Name
Asset Type
Version
Status
```

Conceptual design/status values (examples):

```text
DESIGN_DRAFT
DESIGN_REVIEW
DESIGN_APPROVED
IMPLEMENTATION_READY
IMPLEMENTED
DEPRECATED
```

### 4.2 Purpose

Every asset must define:

```text
Problem
Purpose
Value
Primary Responsibility
```

Answers:

```text
Why does this asset exist?
```

### 4.3 Trigger Model

Invocation contract — not execution logic.

Trigger categories:

```text
EXPLICIT
EVENT
STATE
CONTEXT
MANUAL
```

Examples (illustrative only):

```text
EXPLICIT  — user requests repository validation
EVENT     — a review identifies findings
STATE     — a task enters closeout
CONTEXT   — repository compatibility uncertainty detected
MANUAL    — operator chooses to invoke the capability
```

### 4.4 Input Model

Distinguish:

```text
Required Inputs
Optional Inputs
Context Inputs
Constraints
```

Example shape (illustrative):

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

Do not define JSON schemas in Stage D1.

### 4.5 Output Model

Distinguish:

```text
Primary Outputs
Secondary Outputs
Evidence Outputs
Side Effects
```

```text
Output ≠ Side Effect
```

Example:

```text
Output          — Validation Report
Evidence Output — Command Results
Side Effect     — Repository files modified
```

Assets must explicitly declare side effects.

### 4.6 Responsibility Boundary

Mandatory:

```text
Handles
Does Not Handle
```

Written from **Primary Responsibility**.
Purpose: prevent asset responsibility overlap.
Do not invent artificial exclusions.

### 4.7 Dependency Model

Conceptual dependency types:

```text
REQUIRES
REQUESTS
CONSUMES
PRODUCES_FOR
OPTIONALLY_USES
```

Examples (illustrative of Stage C relationships, not designs):

```text
Revision capability
REQUESTS
Validation capability

Closeout workflow
CONSUMES
Boundary Artifact
```

```text
Conceptual Dependency
≠
Runtime Dependency
```

Dependency must not automatically imply implementation coupling.

### 4.8 Artifact Model

Artifacts exchanged between assets describe:

```text
Artifact Name
Producer
Consumers
Purpose
Lifecycle
Format Constraints
```

```text
Artifacts remain implementation-neutral.
```

Stage D1 must not mandate concrete formats (JSON, YAML, Markdown)
unless a format is intrinsic to the asset.

### 4.9 Validation Model

Every asset design must define how success is evaluated:

```text
PRECONDITIONS
EXECUTION VALIDATION
OUTPUT VALIDATION
EVIDENCE VALIDATION
ACCEPTANCE CRITERIA
```

```text
Asset Validation
≠
Repository Validation
```

Example:

```text
Asset Validation
Did the asset produce its expected output?

Repository Validation
Does the repository pass technical validation?
```

### 4.10 Lifecycle Model

Asset designs must declare current lifecycle position and allowed transitions
consistent with §3.2.

Candidate readiness (from Stage C) gates whether formal design may begin:

```text
READY_FOR_DESIGN     → eligible for formal design
NEEDS_MORE_EVIDENCE  → observe / gap analysis only (e.g. OBSERVE_ONLY)
DO_NOT_DESIGN        → excluded from Stage D design
```

### 4.11 Versioning Model

Simple conceptual versioning:

```text
Design Version
Implementation Version
```

```text
Design Version
≠
Implementation Version
```

No complex semantic-versioning policy in Stage D1.

---

## 5. Asset Type Specialization

The common schema applies to all types. Each type adds characteristics.

### 5.1 Skill

```text
Clear Trigger
Stable Procedure
Limited Autonomy
Repeatable Inputs
Predictable Outputs
```

Additional dimensions:

```text
Procedure
Execution Constraints
Expected Evidence
```

Conceptually:

```text
Input → Procedure → Output
```

### 5.2 Agent

```text
Goal
Autonomy Boundary
Reasoning Scope
Exploration Scope
Decision Authority
Stop Conditions
```

Do not define model-specific prompts in design.

Conceptually:

```text
Goal → Explore → Reason → Decide → Produce Result
```

### 5.3 Workflow

```text
Entry Condition
Stages
Transitions
Dependencies
Artifacts
Exit Conditions
```

A Workflow orchestrates capabilities.
Avoid embedding all capability logic inside the Workflow definition.

Conceptually:

```text
Step A → Step B → Step C → Step D
```

### 5.4 Composite

```text
Composition Model
Child Assets
Coordination Rules
Shared Artifacts
Boundary Ownership
```

Composite must not become an “everything container.”

---

## 6. Candidate Design Template

Reusable conceptual template for later Stage D substages.
**Do not instantiate for specific candidates in Stage D1.**

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

---

## 7. Implementation Readiness

Conceptual readiness classification after design:

```text
DESIGN_ONLY
REQUIRES_EVIDENCE
READY_FOR_IMPLEMENTATION
NOT_READY
```

```text
DESIGN_APPROVED
≠
READY_FOR_IMPLEMENTATION
```

An asset may have an approved design and still require:

```text
More Evidence
Repository Integration Analysis
Runtime Architecture
Tooling Decisions
```

before implementation.

---

## 8. Open Questions Model

Uncertainty is first-class design information. Categories:

```text
EVIDENCE_GAP
BOUNDARY_RISK
DEPENDENCY_RISK
IMPLEMENTATION_UNKNOWN
VALIDATION_UNKNOWN
```

Open questions must not be silently hidden.

---

## 9. Design Governance

Minimal rules:

```text
No Candidate becomes an Asset without design review.

No Asset Design becomes Implementation without readiness review.

Boundary changes require dependency review.

New evidence may revise Candidate or Asset Design.

Implementation must not silently redefine Design intent.

Stage C readiness constraints remain binding:
  OBSERVE_ONLY / NEEDS_MORE_EVIDENCE / DO_NOT_DESIGN
  candidates must not receive formal implementation-oriented design.
```

Avoid overly complex process machinery.

---

## 10. Explicit Non-Goals

Stage D1 does not:

```text
Design CANDIDATE-001
Design CANDIDATE-002
Design CANDIDATE-003
Design CANDIDATE-004
Design CANDIDATE-005
```

Does not create:

```text
Skill files
Agent files
Workflow files
Prompt templates
Automation code
Runtime orchestration
```

Does not define:

```text
LLM Provider
Model Selection
Prompt Format
Framework Implementation (LangGraph, CrewAI, AutoGen, etc.)
Cursor-specific implementation
```

```text
Stage D1 = Asset Design Architecture
≠
AI Runtime Architecture
```

---

## 11. Relationship to Stage C Outputs

Stage D design substages must consume:

```text
ai-engineering/milestones/MILESTONE-001/03-asset-candidates.md
```

Known Stage C constraints (unchanged by this framework):

```text
CANDIDATE-001 READY_FOR_DESIGN
CANDIDATE-002 READY_FOR_DESIGN
CANDIDATE-003 READY_FOR_DESIGN
CANDIDATE-004 READY_FOR_DESIGN (EMERGING; lightweight design)
CANDIDATE-005 OBSERVE_ONLY (not eligible for formal design)

PATTERN-006 Deferred Pattern Opportunity (not a candidate)
```

Known Stage C dependency / artifact shapes the framework must be able to express:

```text
CANDIDATE-001 REQUESTS CANDIDATE-002
CANDIDATE-004 PRODUCES Boundary Artifact
CANDIDATE-003 CONSUMES Boundary Artifact
```

This framework does not redesign those relationships.

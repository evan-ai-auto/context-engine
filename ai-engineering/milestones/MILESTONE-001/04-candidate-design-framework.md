# Candidate Design Framework

## 1. Purpose

```text
Engineering Pattern
        ↓
Asset Candidate
        ↓
Candidate Design Framework
(+ AI Engineering Asset Taxonomy v0.1)
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
Pattern
≠
Candidate
≠
Asset Category / Asset Type
≠
Asset Design
≠
Asset Implementation
```

This framework is the AI Engineering Asset Design Framework for MILESTONE-001 Stage D.
Revision-001 expands the Asset Type model into Asset Taxonomy v0.1 without redesigning Stage D1.

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

It must support AI Engineering Asset Taxonomy v0.1 types:

```text
EXECUTABLE: AGENT, SKILL, WORKFLOW
GOVERNANCE: RULE
STRUCTURAL: TEMPLATE, CHECKLIST
KNOWLEDGE: KNOWLEDGE
COMPOSITION: COMPOSITE
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
  Distinguish Pattern → Candidate → Asset Classification →
  Asset Design → Implementation.

Q5 Evolution Support
  Allow new evidence → candidate update → design revision →
  implementation evolution without full redesign.

Q6 Taxonomy Completeness (v0.1)
  Support more than Agent/Skill/Workflow without uncontrolled expansion.

Q7 Classification Safety
  Discourage “everything becomes a Skill.”
  Classification follows nature; nature does not follow preferred implementation.
```

---

## 3. AI Engineering Asset Taxonomy v0.1

### 3.1 Taxonomy tree

```text
AI Engineering Assets
│
├── EXECUTABLE
│   ├── AGENT
│   ├── SKILL
│   └── WORKFLOW
│
├── GOVERNANCE
│   └── RULE
│
├── STRUCTURAL
│   ├── TEMPLATE
│   └── CHECKLIST
│
├── KNOWLEDGE
│   └── KNOWLEDGE
│
└── COMPOSITION
    └── COMPOSITE
```

This taxonomy is intentionally minimal.

Not in v0.1 (future extension only if evidence warrants):

```text
POLICY, CONSTRAINT, PLAYBOOK, PROCEDURE, SCHEMA, CONTRACT,
RUBRIC, VALIDATOR, QUALITY_GATE, SCRIPT, HOOK, TRIGGER, INTEGRATION
```

### 3.2 Terminology

```text
Asset Category
  Example: EXECUTABLE

Asset Type
  Example: SKILL
```

Hierarchy:

```text
Asset Category
        ↓
Asset Type
        ↓
Asset Design
        ↓
Asset Implementation
```

And with extraction lineage:

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

### 3.3 Classification principle

```text
Asset Type should be assigned after reusable value has been identified.
```

Recommended reasoning sequence:

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

Do **not**:

```text
Historical Pattern
        ↓
Immediately guess Agent / Skill / Workflow
```

Classification question:

```text
What does this reusable asset fundamentally represent?
```

Potential natures:

```text
Capability
Process
Constraint
Structure
Verification
Knowledge
Composition
```

Then assign Asset Category / Asset Type.

```text
Classification follows nature.
Nature does not follow preferred implementation.
```

### 3.4 Category definitions

#### EXECUTABLE

```text
Assets that perform, coordinate, or guide engineering work.
```

Types: `AGENT`, `SKILL`, `WORKFLOW`

```text
Executable Asset
≠
Autonomous Runtime
```

A Skill may be manually invoked.
A Workflow may be a conceptual orchestration contract.

#### GOVERNANCE

```text
Assets that constrain or govern acceptable behavior.
```

Type: `RULE`

A Rule should be:

```text
Constraint-oriented
Non-procedural
Potentially cross-cutting
Stable
```

```text
RULE ≠ WORKFLOW
```

A Rule constrains behavior. A Workflow defines progression.

#### STRUCTURAL

```text
Assets that provide reusable structure or verification scaffolding.
```

Types:

```text
TEMPLATE   — reusable structural skeleton
CHECKLIST  — explicit verification or completion items
```

```text
CHECKLIST ≠ WORKFLOW
```

A Checklist defines verification items, not orchestration.

#### KNOWLEDGE

```text
Assets that preserve reusable, confirmed engineering knowledge.
```

Type: `KNOWLEDGE`

```text
KNOWLEDGE Asset
=
Long-lived, Confirmed, Reusable, Maintained

Generated Context
=
Derived, Potentially Regenerable, State-dependent
```

Do not define concrete storage locations (e.g. `.ai-context`, `knowledge/`) in this framework.

#### COMPOSITION

```text
Assets that coordinate or compose multiple assets.
```

Type: `COMPOSITE`

Must define composition purpose; must not become an everything container.

### 3.5 Repository compatibility note

Existing repository placeholders under `ai-engineering/extraction/`:

```text
agents/
skills/
workflows/
rules/
```

align with EXECUTABLE + GOVERNANCE (RULE) categories.
TEMPLATE / CHECKLIST / KNOWLEDGE have no dedicated extraction directories yet;
v0.1 introduces them as taxonomy types only — no new directories created by this revision.

Stage C candidates remain typed with prior hypotheses (SKILL / WORKFLOW / COMPOSITE).
This revision does **not** reclassify them.

---

## 4. Asset Lifecycle Model

### 4.1 Candidate Lifecycle (pre-asset)

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

### 4.2 Asset Lifecycle (post-candidate)

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

### 4.3 Separation rule

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

## 5. Common Asset Design Schema

Every formally designed asset should be describable through the following dimensions.

The Common Asset Design Schema remains **unified** across all v0.1 Asset Types.
Not every type requires identical operational semantics.

```text
Not every Asset Type requires the same operational semantics.
```

Do not define runtime storage formats in this framework.

### 5.1 Identity

```text
Asset ID
Asset Name
Asset Category
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

### 5.2 Purpose

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

### 5.3 Trigger Model

Invocation contract — not execution logic.

Distinguish:

```text
Invocation-Oriented Assets
  AGENT, SKILL, WORKFLOW
  (Trigger Model typically mandatory)

Reference-Oriented Assets
  RULE, TEMPLATE, CHECKLIST, KNOWLEDGE
  (may use Applicability / Usage Context instead of forced Triggers)
```

Do **not** force artificial Trigger Models onto passive / reference-oriented assets.

When Trigger Model applies, categories include:

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

COMPOSITE may combine invocation-oriented coordination with reference-oriented children.

### 5.4 Input Model

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

Reference-oriented assets may emphasize **Applicability Inputs** (when/where the asset applies) rather than runtime invocation inputs.

### 5.5 Output Model

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
Reference-oriented assets may primarily produce artifacts for consumption rather than side effects.

### 5.6 Responsibility Boundary

Mandatory:

```text
Handles
Does Not Handle
```

Written from **Primary Responsibility**.
Purpose: prevent asset responsibility overlap.
Do not invent artificial exclusions.

### 5.7 Dependency Model

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

### 5.8 Artifact Model

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

### 5.9 Validation Model

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
Did the asset produce its expected output / remain applicable?

Repository Validation
Does the repository pass technical validation?
```

For RULE / TEMPLATE / CHECKLIST / KNOWLEDGE, validation may emphasize
applicability, completeness, or maintenance criteria rather than execution runs.

### 5.10 Lifecycle Model

Asset designs must declare current lifecycle position and allowed transitions
consistent with §4.2.

Candidate readiness (from Stage C) gates whether formal design may begin:

```text
READY_FOR_DESIGN     → eligible for formal design
NEEDS_MORE_EVIDENCE  → observe / gap analysis only (e.g. OBSERVE_ONLY)
DO_NOT_DESIGN        → excluded from Stage D design
```

### 5.11 Versioning Model

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

## 6. Asset Type Specialization

The common schema applies to all types. Each type adds characteristics.

### 6.1 Skill (EXECUTABLE)

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

### 6.2 Agent (EXECUTABLE)

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

### 6.3 Workflow (EXECUTABLE)

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

### 6.4 Rule (GOVERNANCE)

```text
Scope
Constraint
Applicability
Exceptions
Enforcement Expectation
```

```text
RULE ≠ WORKFLOW
```

### 6.5 Template (STRUCTURAL)

```text
Purpose
Structure
Required Sections
Optional Sections
Usage Guidance
```

### 6.6 Checklist (STRUCTURAL)

```text
Verification Scope
Items
Completion Criteria
Evidence Expectation
```

```text
CHECKLIST ≠ WORKFLOW
```

### 6.7 Knowledge (KNOWLEDGE)

```text
Knowledge Scope
Source Basis
Confidence
Maintenance Responsibility
Regeneration Relationship
```

Distinguish from generated / regenerable project context.

### 6.8 Composite (COMPOSITION)

```text
Composition Model
Child Assets
Coordination Rules
Shared Artifacts
Boundary Ownership
```

Composite must not become an “everything container.”
Child assets may span multiple Asset Categories.

---

## 7. Candidate Design Template

Reusable conceptual template for later Stage D substages.
**Do not instantiate for specific candidates in Stage D1.**

```text
# Asset Design

## 1. Identity
   (includes Asset Category + Asset Type)

## 2. Source Candidate

## 3. Purpose

## 4. Asset Category / Type Rationale
   (nature classification → type assignment)

## 5. Trigger Model / Applicability
   (invocation-oriented vs reference-oriented)

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

## 8. Implementation Readiness

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

## 9. Open Questions Model

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

## 10. Design Governance

Minimal rules:

```text
No Candidate becomes an Asset without design review.

No Asset Design becomes Implementation without readiness review.

Boundary changes require dependency review.

New evidence may revise Candidate or Asset Design.

Implementation must not silently redefine Design intent.

Asset Type assignment must follow nature classification
(not preferred runtime packaging).

Stage C readiness constraints remain binding:
  OBSERVE_ONLY / NEEDS_MORE_EVIDENCE / DO_NOT_DESIGN
  candidates must not receive formal implementation-oriented design.
```

Avoid overly complex process machinery.

---

## 11. Explicit Non-Goals

Stage D1 / this revision does not:

```text
Design CANDIDATE-001
Design CANDIDATE-002
Design CANDIDATE-003
Design CANDIDATE-004
Design CANDIDATE-005
Reclassify existing Candidates
Create new Candidates
```

Does not create:

```text
Skill / Agent / Workflow / Rule / Template / Checklist / Knowledge files
Prompt templates
Automation code
Runtime orchestration
New extraction directories
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
Stage D1 = Asset Design Architecture (+ Taxonomy v0.1)
≠
AI Runtime Architecture
```

---

## 12. Relationship to Stage C Outputs

Stage D design substages must consume:

```text
ai-engineering/milestones/MILESTONE-001/03-asset-candidates.md
```

Known Stage C constraints (unchanged by this framework / revision):

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
Taxonomy v0.1 does not require rewriting Stage C candidate type hypotheses
before Stage D2 design begins.

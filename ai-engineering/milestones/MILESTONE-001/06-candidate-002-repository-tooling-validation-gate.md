# CANDIDATE-002 — Repository Tooling Validation Gate

## 1. Design Scope

```text
Candidate
        ↓
Asset Classification
        ↓
Asset Design
```

This document is the **Asset Design Specification** for CANDIDATE-002.

```text
This stage does NOT implement the asset.

No Skill package, Agent, Workflow, validation script, tool config,
or Cursor rule is created here.
```

Design is governed by:

```text
ai-engineering/milestones/MILESTONE-001/04-candidate-design-framework.md
AI Engineering Asset Taxonomy v0.1
```

Stage C source:

```text
ai-engineering/milestones/MILESTONE-001/03-asset-candidates.md
→ CANDIDATE-002 STRONG_CANDIDATE / READY_FOR_DESIGN
```

Compatibility with:

```text
05-candidate-001-targeted-engineering-revision.md
CANDIDATE-001 REQUESTS CANDIDATE-002
```

---

## 2. Evidence Basis

### Trace

```text
Historical Process (TASK-001 / TASK-002 validation gates)
        ↓
PATTERN-003 Tooling Validation Gate
(+ PATTERN-008 supporting layered composition note)
        ↓
CANDIDATE-002 Repository Tooling Validation Gate
        ↓
This Asset Design
```

### Minimum justifying evidence

```text
Why repository validation emerged as a recurring pattern:
  TASK-001 and TASK-002 repeatedly executed pytest / ruff / mypy
  (and later hygiene checks) at accept, revision, and closeout gates.
  Evidence recorded in validation.md, checklists, and closeout.

Why validation execution should become reusable:
  The same gate trio was re-specified per stage instead of invoked
  as a shared capability. Stage C identified high reusability,
  determinism, and clear I/O — STRONG_CANDIDATE.

Why validation should not be re-designed per task:
  Embedding tool commands in every revision/closeout asset duplicates
  logic and couples callers to ecosystems. Callers need a request
  contract; repositories need inspect-before-execute gate resolution.
```

Primary references:

```text
01-process-inventory.md §9 Validation Inventory
02-engineering-patterns.md PATTERN-003 / PATTERN-008
03-asset-candidates.md CANDIDATE-002
05-candidate-001-targeted-engineering-revision.md §11 / §13
```

```text
Historical Evidence supports the design.
Historical Evidence does not automatically define implementation.
This repository’s pytest/ruff/mypy usage is an example ecosystem,
not a universal fixed gate set.
```

---

## 3. Asset Classification

### Nature

```text
What does this reusable asset fundamentally represent?

A bounded validation-execution capability:
given a validation request and repository context,
inspect the repository, resolve applicable gates,
execute them, normalize results, and return reviewable evidence —
without deciding whether validation was required or may be deferred.
```

Nature: **Capability** (executable, procedural).

### Classification

```text
Asset Category: EXECUTABLE
Asset Type:     SKILL
```

```text
Classification follows nature.
Nature does not follow preferred implementation.
```

Rationale: see §22 (Why SKILL?).

---

## 4. Asset Identity

| Field | Value |
|---|---|
| Asset Name | Repository Tooling Validation Gate |
| Candidate ID | CANDIDATE-002 |
| Asset Category | EXECUTABLE |
| Asset Type | SKILL |
| Design Version | 0.1 |
| Status | DESIGNED |

```text
Status is DESIGNED — not IMPLEMENTED.
```

---

## 5. Purpose and Value

### Purpose

Provide a reusable Skill that performs **repository-aware validation execution** and **evidence normalization**, so upstream assets (e.g. CANDIDATE-001) and humans can request validation without embedding repository tooling logic everywhere.

### Primary Value

```text
One validation-execution capability
→ consistent evidence for review and upstream assets
→ tool details stay behind a request contract
```

### Engineering Problem Solved

```text
Not merely “run pytest.”

Problem:
  Engineering processes repeatedly need repository validation, but
  callers should not re-encode tool commands, ecosystems, and
  gate selection in every Skill/Workflow.

Solution:
  Request-oriented validation gate with inspect-before-execute,
  normalized results, and reviewable evidence.
```

### Expected Reuse Context

```text
Post-revision validation (CANDIDATE-001 REQUESTS)

Pre-commit / pre-accept validation

Task / stage completion validation

Explicit human validation requests

Any bounded engineering step that needs repository quality evidence
without owning tool internals
```

---

## 6. Trigger Model

Invocation-oriented asset. Trigger Model is mandatory.

### Positive Trigger Conditions

Use when **all** of the following hold:

```text
- A Validation Request exists (from upstream asset or human)

- Repository Context is available (or can be resolved)

- There is a Validation Target / scope for the request

- The caller has determined that validation evidence is needed
  (requirement determination is external to this Skill)
```

Typical trigger sources:

```text
EXPLICIT — human or upstream asset requests validation
EVENT    — revision completed / repository change produced
STATE    — task/stage requires validation evidence before accept
```

### Negative Trigger Conditions

Do **not** use when:

```text
- Pure exploratory analysis with no validation request

- No repository context can be established

- No validation target / empty meaningless request

- Validation is not applicable to the situation
  (caller should not request; this Skill does not invent requirements)

- The request is actually revision planning/execution
  (that is CANDIDATE-001)

- The request is CI/CD orchestration or continuous monitoring
```

```text
This Skill must not become a Universal DevOps Agent.
```

---

## 7. Input Model

### Required Inputs

```text
Repository Context
  Location / identity of the repository to validate
  (path, workspace root, or equivalent conceptual reference)

Validation Request
  That validation execution is being requested

Validation Target / Scope
  What is being validated at a conceptual level
  (e.g. whole repo, changed domain package, docs-only tree)
```

### Optional Inputs

```text
Requested Gate Set
  Explicit gates requested by caller (abstract identities, not CLI)

Changed Artifact Context
  Summary of what changed (helps applicability / selection)

Acceptance Context
  Notes from caller (informational only — this Skill does not
  decide acceptance)

Known Constraints
  Timeouts, offline mode, disallow network, etc.

Declared Policy Hints
  Pointers to repository/stage conventions if already known
```

### Context Inputs

```text
Discoverable repository tooling configuration

Existing validation scripts / CI hints (as inspection signals only)

Language / package / test framework signals
```

### Constraints

```text
Caller MUST NOT be required to supply exact tool commands
  (pytest/ruff/mypy CLI strings) unless the repository’s own
  contract explicitly demands command-level override.

Prefer abstract requests such as:
  “Validate changed Python domain model”
over:
  “python -m pytest tests/test_domain.py -q”

Exact commands belong to validation execution logic after inspection.
```

---

## 8. Validation Authority Model

```text
Caller / Upstream Asset / External Authority
        │
        │ Determines validation requirement
        │ (and deferral authorization when needed)
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

### Owns

```text
How requested validation is executed within repository-aware boundaries

Gate resolution and execution

Evidence collection and result normalization

Reporting facts about what ran and what results occurred
```

### Does NOT own

```text
Whether validation is required

Whether validation may be deferred

Whether partial / incomplete validation is acceptable

Whether a revision or task may be marked complete
```

Alignment with CANDIDATE-001 Revision-001:

```text
CANDIDATE-001: requirement determination
CANDIDATE-002: execution
External Authority: deferral / acceptance of incomplete evidence
```

---

## 9. Gate Selection Model

### Gate Selection Inputs

```text
Explicit Requested Gate Set (if provided)

Repository Convention (discovered)

Change-Type / Validation Target signals

Validation Capability inventory (what can be run here)

Declared Policy hints (if supplied)
```

### Gate Selection Authority

```text
CANDIDATE-002 resolves the executable gate set for THIS request
using discoverable repository evidence + request constraints.

CANDIDATE-002 does not invent tools unsupported by repository evidence.
```

### Gate Selection Precedence

```text
1. Explicit Request
   If caller names gates, attempt those first (subject to supportability)

2. Repository Convention
   Documented / configured standard gates for the repo

3. Change-Type Inference
   Narrow applicability from Validation Target / changed artifacts
   (must not invent unrelated ecosystems)

4. Default Gate Set
   Only if convention + inference yield an empty set AND repository
   evidence supports a documented default for this project type
```

```text
Do not randomly invent tools.
Operate on discoverable repository evidence.
```

### Unsupported Gate Behavior

```text
If an explicitly requested gate cannot be resolved or executed:
  Result for that gate = ERROR or NOT_EXECUTED
  (not silently FAILED)

Do not substitute a different tool without recording that the
requested gate was unsupported.

Do not drop the requested gate from the report.
```

---

## 10. Repository Inspection Model

### Principle

```text
Inspect Before Execute
```

### Inspection scope (bounded to validation needs)

Evaluate as needed:

```text
Project Language(s)
Build System / Package Manager signals
Test Framework signals
Linting / Static Analysis signals
Existing Validation Scripts
Repository Documentation (dev/test instructions)
CI Configuration (as hints only — not orchestration ownership)
```

### Non-assumptions

```text
Do NOT assume every repository uses pytest / ruff / mypy.

Do NOT design an exhaustive repository detection engine.

Inspection is sufficient when it can resolve applicable gates
or explain why gates cannot be executed.
```

---

## 11. Validation Lifecycle

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

Distinctions enforced:

```text
Inspection ≠ Gate Selection ≠ Execution ≠ Evidence Collection ≠ Normalization
```

Avoid:

```text
Request → Immediately run commands
```

---

## 12. Validation Gate Model

Conceptual gate structure (not classes / JSON schemas):

```text
Gate Identity
  Stable abstract id (e.g. unit-test, lint, static-analysis, hygiene)

Purpose
  What quality property is being checked

Applicability
  Whether this gate applies to the current target/repo

Execution Requirement
  What is needed to run (tooling present, config, environment)

Result
  Normalized gate result (§13)

Evidence
  Why the result was produced (§15)
```

A gate may conceptually represent:

```text
Unit Test
Lint
Static Analysis
Build
Repository Consistency Check (e.g. whitespace / diff hygiene)
```

```text
A gate is not necessarily a CLI command.
Multiple repository ecosystems must be representable.
```

---

## 13. Result Model

Per-gate normalized results:

```text
PASSED
  Gate executed; validation criteria met

FAILED
  Gate executed successfully; validation criteria not met

ERROR
  Gate could not be correctly executed
  (missing tool, invalid environment, crash, unresolved gate)

NOT_APPLICABLE
  Gate does not apply to this repository / target
  (resolved as inapplicable — not a failure)

NOT_EXECUTED
  Gate was selected or requested but not run
  (blocked, skipped by constraint, interrupted)
```

```text
FAILED ≠ ERROR
NOT_APPLICABLE ≠ NOT_EXECUTED

Do not collapse all non-success into FAILED.
```

---

## 14. Aggregate Outcome Model

### Aggregate Outcome Rules

Preserve per-gate evidence always. Aggregate is a summary, not a cover-up.

```text
All Applicable Gates Passed
  → aggregate: PASSED
  (only if no required gate is ERROR / NOT_EXECUTED / FAILED)

Any Applicable Gate Failed
  → aggregate: FAILED
  (at least one FAILED among applicable executed gates)

Any Required Gate Error
  → aggregate: ERROR
  (required gate could not execute; do not call this FAILED)

Requested Gate Not Executed
  → aggregate: ERROR or NOT_EXECUTED
  (explicitly reported; not silent success)

Only Not Applicable Remain
  → aggregate: NOT_APPLICABLE
  (no applicable gates for target; report why)
```

Mixed example:

```text
Unit Tests: PASSED
Lint: PASSED
Static Analysis: ERROR

Aggregate: ERROR
Evidence: retain all three gate records
Do NOT report “overall completed / success”
Do NOT invent PARTIAL_SUCCESS unless a future policy defines it
  and External Authority interprets it — not this Skill’s job
```

```text
One failing or errored gate must remain visible in evidence.
```

---

## 15. Evidence Model

Minimum evidence contract per gate / overall report:

```text
Gate Identity
Applicability
Execution Status
Result
Evidence Summary
  Human-readable why (pass criteria met / failure theme / error cause)
Evidence Reference
  Pointer to logs/output location (implementation-neutral)
Execution Context
  Repo identity / target scope / resolved gate set
```

Optional:

```text
Timestamp
Command Reference (if a command was used)
Environment Context (high-level only)
```

```text
Objective:
Evidence sufficient for human review
+
Evidence usable by upstream assets (e.g. CANDIDATE-001)

Validation Result alone is not enough — preserve Why.
```

Avoid excessive telemetry.

---

## 16. Partial Execution Model

Example:

```text
Requested: Unit Test, Lint, Static Analysis
Executed:
  Unit Test → PASSED
  Lint → PASSED
  Static Analysis → ERROR
```

### What CANDIDATE-002 reports

```text
Per-gate results + evidence
Aggregate outcome per §14 (here: ERROR)
Explicit statement that Static Analysis did not execute successfully
```

### What CANDIDATE-002 does NOT decide

```text
Whether partial validation is acceptable
Whether the caller may proceed / complete / defer
Whether ERROR should be treated as soft warning
```

Those decisions belong to:

```text
Caller
Workflow
Policy
Human Authority
```

```text
Report facts. Do not silently make acceptance policy decisions.
```

---

## 17. Failure and Stop Conditions

### Conditions

```text
Repository Context Missing
Unsupported Repository Tooling (cannot resolve any gate)
Gate Cannot Be Resolved
Required Tool Missing
Execution Environment Invalid
Gate Execution Error
```

### Outcomes

```text
ERROR
  Could not correctly execute one or more required/resolvable gates

NOT_EXECUTED
  Selected/requested gates not run due to stop/constraint

BLOCKED
  Cannot proceed with meaningful validation (e.g. no repo context)

ESCALATED
  Hand off when tooling support is insufficient for the request
  and the Skill cannot invent substitutes
```

```text
Validation failed (FAILED)
≠
Validation could not be executed (ERROR / NOT_EXECUTED / BLOCKED)
```

Stop after reporting; do not loop into tool installation or redesign.

---

## 18. Responsibility Boundary

### Primary Responsibility

```text
Repository Tooling Validation Execution
```

### Handles (owns)

```text
Repository context inspection (validation-bounded)

Applicable gate resolution

Validation execution

Evidence collection

Result normalization

Validation reporting
```

### Does Not Handle (does not own)

```text
Revision planning / revision execution (CANDIDATE-001)

Validation requirement policy

Validation deferral authorization

Task completion decision

CI/CD orchestration / continuous monitoring

Automatic tool installation

Repository refactoring
```

```text
Compatible with:
CANDIDATE-001 REQUESTS CANDIDATE-002
```

---

## 19. Dependency Model

### Consumes (conceptual)

```text
Repository Context
Validation Request
Repository Convention (discovered)
Tooling Configuration (discovered)
```

### Requested by

```text
CANDIDATE-001 (REQUESTS)
Other callers / humans (EXPLICIT)
Future workflows (without this Skill owning those workflows)
```

### Binding rule

```text
Tool-aware ≠ Tool-bound

Examples may mention pytest / ruff / mypy / Maven / npm / CI
as repository-specific illustrations only.

Do not bind the design to Cursor, GitHub Actions, or a fixed stack.
```

---

## 20. Interaction Model

Conceptual only — not runtime orchestration:

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
Caller / External Authority
(evaluates acceptance / deferral — not CANDIDATE-002)
```

```text
The Validation Gate reports evidence.
External authority evaluates acceptance.
```

---

## 21. Non-Goals

This asset does **not**:

```text
Revision planning
Revision execution
Validation requirement policy
Validation deferral authorization
Task completion decision
CI/CD orchestration
Continuous monitoring
Repository refactoring
Automatic tool installation
Become a Universal DevOps Agent
```

---

## 22. Type Rationale — Why SKILL?

### Selected

```text
EXECUTABLE → SKILL
```

### Why not AGENT?

```text
Invocation is explicit; procedure is stable.
Does not open-endedly explore to invent a validation strategy as a goal.
Autonomy is limited to inspect → resolve → execute → report within request.
```

### Why not WORKFLOW?

```text
Does not orchestrate multi-stage engineering lifecycle.
It is one capability invoked by workflows/callers.
```

### Why not RULE?

```text
Does not merely constrain behavior; it executes validation and produces evidence.
```

### Why not CHECKLIST?

```text
A checklist lists verification items.
This Skill resolves and executes gates and normalizes results.
A checklist may later complement it; it is not the same nature.
```

### Why not TEMPLATE?

```text
Not a structural skeleton for documents.
```

### Central SKILL traits

```text
Bounded capability
Explicit invocation
Reusable procedure
Defined input/output
Explicit stop
```

---

## 23. Implementation Readiness

Framework vocabulary only (`04-candidate-design-framework.md`):

### Evaluation

| Dimension | Assessment |
|---|---|
| Identity Clarity | Clear |
| Trigger Clarity | Clear |
| Input Clarity | Clear (abstract request contract) |
| Gate Selection Model | Defined with precedence |
| Repository Inspection Model | Bounded; inspect-before-execute |
| Result Model | PASSED/FAILED/ERROR/NOT_APPLICABLE/NOT_EXECUTED |
| Evidence Model | Defined |
| Responsibility Boundary | Clear vs CANDIDATE-001 / External Authority |
| Failure Model | Explicit |

### Readiness

```text
Design Status: DESIGNED

Implementation Readiness: REQUIRES_EVIDENCE
```

Reasons:

```text
Design is reviewable and implementation-neutral.

Still requires before READY_FOR_IMPLEMENTATION:
  - concrete repository-convention discovery rules per ecosystem
  - default gate-set policies for this repo (without hard-coding globally)
  - evidence reference storage conventions
  - integration test plan with CANDIDATE-001 request interface
```

---

## 24. Open Questions

```text
EVIDENCE_GAP
  How should repository conventions be discovered consistently
  across ecosystems without an unbounded detector?

IMPLEMENTATION_UNKNOWN
  Should gate precedence be repository-configurable,
  and what is the minimum config surface?

IMPLEMENTATION_UNKNOWN
  Should a resolved “validation plan” (gates to run) become a
  first-class artifact before execution?

VALIDATION_UNKNOWN
  How should environment reproducibility be represented in evidence
  without excessive telemetry?
```

Do not force premature answers.

---

## 25. Design Summary

```text
Asset Name:     Repository Tooling Validation Gate
Asset Category: EXECUTABLE
Asset Type:     SKILL
Status:         DESIGNED
Primary Purpose:
  Repository-aware validation execution + evidence normalization
  behind an abstract request contract.
```

### Gate model summary

```text
Selection precedence:
  Explicit Request → Repository Convention → Change-Type Inference → Default

Inspection:
  Bounded inspect-before-execute (language/tools/scripts/docs/CI hints)

Unsupported gates:
  ERROR / NOT_EXECUTED — never silent substitution or silent omit
```

### Result model summary

```text
PASSED / FAILED / ERROR / NOT_APPLICABLE / NOT_EXECUTED
Aggregate preserves evidence; ERROR ≠ FAILED; no silent overall success
```

### Authority boundary

```text
External Authority / Caller:
  Determines whether validation is required
  Determines whether incomplete validation is acceptable / deferrable

CANDIDATE-002:
  Executes requested validation
  Reports normalized evidence
```

```text
CANDIDATE-001 REQUESTS CANDIDATE-002
```

```text
Implementation Readiness: REQUIRES_EVIDENCE
```

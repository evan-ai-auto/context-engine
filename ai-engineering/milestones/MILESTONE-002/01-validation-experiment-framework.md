# MILESTONE-002 Stage A — Validation Experiment Framework

## 1. Mission

```text
MILESTONE-001
Retrospective Evidence + Asset Discovery

MILESTONE-002
Prospective Evidence + Asset Validation
```

Stage A establishes the **validation method** for designed AI Engineering
assets. It does not validate any candidate and does not implement assets.

```text
Do the designed assets actually provide
repeatable value in real engineering work?
```

Governing chain for this milestone:

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

Principles inherited from MILESTONE-001 closeout:

```text
Designed Asset ≠ Validated Asset
Validated Asset ≠ Implementation Ready
Composable Portfolio ≠ Mandatory Pipeline
Asset Output ≠ External Acceptance
More Process ≠ Better Engineering
More Assets ≠ Better Portfolio
```

References:

```text
MILESTONE-001/11-stage-e-asset-validation-plan.md
MILESTONE-001/12-final-architecture-review-and-closeout.md
MILESTONE-001 designs 05, 06, 07, 10
```

---

## 2. Validation Context

### Portfolio under validation

| ID | Asset | Type | Entry State |
|---|---|---|---|
| CANDIDATE-001 | Targeted Engineering Revision | SKILL | VALIDATION_READY |
| CANDIDATE-002 | Repository Tooling Validation Gate | SKILL | VALIDATION_READY |
| CANDIDATE-003 | Task Closeout Lifecycle | WORKFLOW | VALIDATION_READY |
| CANDIDATE-004 | Explicit Task Boundary Definition | SKILL | VALIDATION_READY |

### Explicitly excluded from Stage A subjects

```text
CANDIDATE-005 — OBSERVE_ONLY
PATTERN-006   — DEFERRED
```

### What Stage A produces

```text
Validation Experiment Definition
Experiment Lifecycle
Eligibility / Selection Guidance
Evidence + Outcome + Disposition Models
Bias / Quality Controls
Emerging Lifecycle Documentation
```

### What Stage A does not produce

```text
Asset implementations, runtime components, automation,
databases, agents, validation platforms, experiment records,
or dispositions applied to 001–004
```

---

## 3. What Is an Asset Validation Experiment?

An **Asset Validation Experiment** answers:

```text
Given a real engineering task,
if a designed asset is intentionally invoked,
does it provide repeatable engineering value
with acceptable process overhead?
```

### Preferred evidence source

```text
Real Engineering Work
```

### Not an experiment

```text
Artificial Demo
Synthetic Benchmark
Self-Declared Success
Task invented only to prove the asset works
```

### Intentionality

```text
Not every real engineering task becomes an experiment.
Asset validation must be intentional:
  eligible task + selected asset + recorded observation intent.
```

---

## 4. Experiment Lifecycle

Lightweight lifecycle (ceremony minimized):

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
Observation + Evidence Capture
        ↓
Assessment (Experiment Outcome)
        ↓
Disposition Recommendation (not final portfolio lock)
```

### Merge guidance

```text
Observation and Evidence Capture may be one continuous activity.
Assessment and Disposition Recommendation stay distinct:
  Experiment Outcome ≠ Asset Disposition.
```

Framework qualities:

```text
Minimal
Practical
Repeatable
Evidence-Oriented
```

---

## 5. Experiment Eligibility

### Suitable when most of the following hold

| Dimension | Meaning |
|---|---|
| Task Relevance | Authentic engineering work, not a demo |
| Asset Relevance | Task touches the asset’s designed responsibility |
| Meaningful Complexity | Enough substance that value/overhead can be observed |
| Observable Outcome | Result can be reviewed without inventing metrics |
| Context Variation Potential | Adds diversity vs prior experiments (when any exist) |
| Repeatability Potential | Similar situations could recur in future work |

### Not suitable

```text
Task too trivial for the asset’s responsibility
No relevant asset responsibility
No observable outcome
Artificial task created only to prove success
Forced experiment when another process already fully covers the need
and invoking the asset would be pure ceremony
```

```text
Not Every Task should become an Experiment.
```

---

## 6. Asset Selection

### Selection mode

```text
Human-Guided Asset Selection
```

```text
Do NOT design automatic asset invocation.
Do NOT create an Agent.
Do NOT create an orchestration engine.
```

### Selection record (lightweight)

For each experiment, record:

```text
Why was this asset selected?
```

Optionally / briefly:

```text
Why were other potentially relevant assets not selected?
```

```text
Do not require exhaustive justification for every non-selected asset.
```

### Selection cues (from designs — not automation)

| Asset | Typical selection cue |
|---|---|
| 004 | Task start with scope-risk / ambiguity / expansion pressure |
| 001 | Bounded revision target from findings / hygiene / coverage gap |
| 002 | Need tooling evidence before acceptance/close claims |
| 003 | Task intended for formal closeout with evidence + acceptance |

Negative cues remain first-class (see §11).

---

## 7. Single Asset and Composition Experiments

### Single Asset First Principle

```text
Single Asset Validation First
generally precedes
Cross-Asset Composition Validation
```

Reason: attribution clarity.

```text
If 004 → 001 → 002 → 003 fails,
which asset caused the problem?
```

### Experiment kinds

| Kind | Purpose |
|---|---|
| Single Asset Experiment | Attribute value/overhead/failure to one designed asset |
| Composition Experiment | Test optional portfolio composition when context requires it |

```text
Generally ≠ Mandatory Universal Rule
```

Allow composition earlier when a real engineering context **genuinely
requires** multiple assets — record that the experiment is Composition
and note attribution limits.

### Stage A boundary

```text
Stage A defines the distinction only.
Stage A does NOT execute single-asset or composition experiments.
```

---

## 8. Experiment Record Structure

Conceptual evidence structure (not frozen schema):

```text
Experiment ID
Date
Engineering Task
Task Context
Selected Asset
Asset Version / Design Reference
Experiment Kind (Single / Composition)
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
Experiment Outcome
Recommended Disposition
Evidence Quality Notes
Bias / Non-Use Notes
```

```text
Do NOT create:
  Database schema / Pydantic / JSON Schema /
  runtime objects / persistence layer
```

```text
Field names are conceptual guidance — not prematurely frozen.
```

Suggested future recording home (when a later stage authorizes records):

```text
Lightweight markdown notes under ai-engineering/
(format chosen at experiment execution time)
```

---

## 9. Human Intervention Evidence

Human Intervention is a **first-class evidence dimension**, not automatic failure.

### Examples

```text
Clarification required
Boundary correction
Output correction
Manual validation
Decision override
Process skip
Unexpected recovery
```

### Interpretation

```text
Human Intervention
=
Evidence about Asset Autonomy
+
Boundary Quality
+
Process Overhead
```

### Acceptable intervention (qualitative)

```text
Expected / acceptable:
  External Authority confirmation (esp. 004 / 003 acceptance)
  Clarifying ambiguous inputs before proceeding
  Choosing not to invoke when negative criteria apply

Concerning (failure signal when repeated):
  Repeated correction of the same responsibility
  Operator doing the asset’s core job after invocation
  Frequent overrides because outputs are unusable
```

```text
Avoid artificial autonomy scores.
Prefer qualitative description of what intervention occurred and why.
```

---

## 10. Positive Validation

Indicators (qualitative accumulation):

```text
Clearer reasoning
Reduced repeated mistakes
Improved task consistency
Useful output structure
Lower revision cost
Better validation coverage / honest gate status
Improved traceability
Successful reuse across contexts
```

```text
Single Success ≠ Validation
```

Positive evidence should accumulate across **meaningful, diverse** contexts.
No arbitrary numeric thresholds in Stage A.

---

## 11. Negative Validation

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
Process overhead would exceed expected value
```

```text
Reusable ≠ Universally Applicable
Non-Invocation ≠ Failure
```

Negative evidence (correct non-use) is valuable and should be recorded
when an experiment eligibility review intentionally skips an asset.

Asset-specific non-use cues (from M1 designs / Stage E):

| Asset | Example non-use |
|---|---|
| 004 | Boundary already confirmed externally; trivial no-ambiguity chore |
| 001 | Open exploration; “run tests only”; full closeout request |
| 002 | No tooling relevance; pure planning |
| 003 | Mid-stage only; no closeout responsibility |

---

## 12. Failure Evidence

Meaningful failure examples:

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

Failure may recommend (experiment → disposition path):

```text
REFINE
NARROW_SCOPE
MERGE
DEFER
REJECT
```

```text
Not every failure means REJECT.
```

---

## 13. Process Overhead

First-class validation dimension.

Indicators:

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
Engineering Value > Process Overhead ?
```

```text
Qualitative evidence first.
Future quantitative metrics only after repeated evidence exists.
No forced numerical scoring in Stage A.
```

Especially critical for CANDIDATE-004 and lightweight vs full 003 ceremony
(carried from M1 Stage E).

---

## 14. Context Variation

Validation must eventually span different contexts.

Variation dimensions:

```text
Task Complexity
Task Type
Repository Type
Ambiguity Level
Change Size
Validation Requirements
```

```text
One Context ≠ General Reusability
```

```text
Evidence Diversity > raw repetition count
No fixed minimum sample sizes in Stage A
```

---

## 15. Experiment Outcomes

Per-experiment outcomes:

```text
SUPPORTED
PARTIALLY_SUPPORTED
NOT_SUPPORTED
INCONCLUSIVE
```

### Separation rule

```text
Experiment Outcome
≠
Asset Disposition
```

Example:

```text
Experiment Outcome:     PARTIALLY_SUPPORTED
Recommended Disposition: CONTINUE_VALIDATION
```

```text
One experiment must not automatically determine final asset status.
```

---

## 16. Asset Disposition Model

After accumulating evidence, portfolio-level dispositions may include:

```text
CONTINUE_VALIDATION
REFINE
NARROW_SCOPE
MERGE
DEFER
REJECT
VALIDATED
```

### Critical preservation

```text
VALIDATED
≠
IMPLEMENTATION_READY
```

```text
VALIDATED
        ↓
Implementation Readiness Assessment
        ↓
IMPLEMENTATION_READY
```

Stage A does not apply dispositions to any candidate.

---

## 17. Validation Stop Conditions

Pause or stop validating an asset when:

```text
Evidence sufficient for a disposition decision
Evidence repeatedly contradictory
Asset responsibility unstable
Asset duplicates another asset
Process overhead consistently excessive
No suitable real engineering context available
```

```text
No More Experiments ≠ VALIDATED
```

Possible stop result:

```text
DEFER
```

(or REFINE / REJECT / MERGE per evidence)

---

## 18. Evidence Quality

Quality dimensions:

```text
Task Authenticity
Outcome Observability
Context Diversity
Failure Visibility
Human Intervention Visibility
Traceability
Bias Awareness
```

```text
Avoid Success Narrative Only.
The framework must support evidence that challenges original designs.
```

---

## 19. Validation Bias Controls

Lightweight safeguards:

```text
Record failures
Record non-use cases
Separate experiment outcome from disposition
Do not treat compliance as value
Do not assume designed assets are useful
Allow rejection
Prefer real work over demos
Single-asset first to reduce attribution bias (generally)
```

Core principle:

```text
The purpose of validation
is not to prove the asset correct.

The purpose of validation
is to discover whether the asset deserves reuse.
```

---

## 20. Emerging Asset Lifecycle Model

Documented for Stage A review — **not** a repository-wide Rule / Final Standard.

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

Allowed side paths:

```text
VALIDATING → REFINE → VALIDATION_READY
VALIDATING → REJECTED
VALIDATING → MERGED
```

```text
Status: Emerging Lifecycle Model
Not: Final Architecture Standard
```

Current portfolio position for 001–004:

```text
VALIDATION_READY
(entering VALIDATING only when Stage B+ experiments begin)
```

---

## 21. Experimental Invocation vs Implementation

```text
Experimental Invocation ≠ Asset Packaging
```

During validation:

```text
Asset Design documents
may be used as
Experimental Procedure
```

without creating:

```text
SKILL.md
WORKFLOW.md
Agent Definition
Runtime Component
Template/Rule packages
Shared-contract schemas
```

```text
This distinction is critical to prevent premature packaging.
```

---

## 22. Future Composition Validation

Composition path (example):

```text
004 → 001 → 002 → 003
```

Stage A does **not** execute composition experiments.

Composition validation becomes appropriate when:

```text
Individual asset evidence exists (or is simultaneously justified by context)
Individual responsibilities are sufficiently stable
Composition is required by a real engineering context
Attribution limits are explicitly recorded
```

Preserve M1 composition scenarios as optional, not mandatory:

```text
004→001→002→003
001→002
002 only
External Boundary → 001
Boundary → Closeout
```

---

## 23. Stage A Conclusions

```text
MILESTONE-002 Stage A delivers a Validation Experiment Framework for
prospective validation of VALIDATION_READY assets 001–004.

Key decisions:
  - Real engineering work preferred; intentional experiments only
  - Human-guided selection; no auto-invocation
  - Single-asset first generally; composition later / when required
  - Experiment Outcome ≠ Asset Disposition
  - VALIDATED ≠ IMPLEMENTATION_READY
  - Experimental invocation ≠ packaging
  - Lifecycle model is Emerging, not a frozen standard

Stage A validates the method, not the assets.
```

---

## 24. Next Validation Boundary

```text
Recommended next stage (authorization required):
Stage B — First Asset Experimental Validation

Stage B should:
  - Select one primary asset for first experiments
  - Use this framework’s lifecycle and record structure
  - Prefer single-asset experiments
  - Produce real evidence records

Stage B should NOT (unless separately authorized):
  - Package Skills/Workflows
  - Validate all four assets at once
  - Declare VALIDATED from a single success
  - Modify MILESTONE-001 designs
```

```text
STOP after Stage A push until Stage B is authorized.
```

---

## End of Stage A Framework

```text
Document: 01-validation-experiment-framework.md
Milestone: MILESTONE-002
Stage: A — COMPLETED (framework only)
Experiments executed: NONE
Assets implemented: NONE
```

# CANDIDATE-004 — Explicit Task Boundary Definition

## 1. Mission

```text
Candidate
        ↓
Asset Type Confirmation
        ↓
Conceptual Asset Design
```

This document is the **Asset Type Confirmation and Asset Design Specification** for:

```text
CANDIDATE-004
Explicit Task Boundary Definition
```

```text
This stage does NOT implement the asset.

No Skill package, Template file, Rule file, Agent, Workflow runtime,
Python/Pydantic models, or shared-contract schema is created here.
```

Design is governed by:

```text
ai-engineering/milestones/MILESTONE-001/04-candidate-design-framework.md
AI Engineering Asset Taxonomy v0.1
```

Architecture context:

```text
08-stage-d2-strong-candidate-architecture-review.md
09-stage-d3-candidate-portfolio-reassessment.md
→ CANDIDATE-004 PROMOTE_TO_DESIGN
```

Core question answered by this design:

```text
What reusable engineering asset should
Explicit Task Boundary Definition become?
```

Answer is based on Responsibility + Execution Necessity + Input/Output
+ Reuse Pattern + Architecture Fit — not naming preference.

---

## 2. Evidence Context

### Trace

```text
Historical Process (TASK-001 / TASK-002 explicit in/out-of-scope)
        ↓
PATTERN-004 Explicit Task Boundary Definition
        ↓
CANDIDATE-004 (Stage C EMERGING / READY_FOR_DESIGN / SKILL hypothesis)
        ↓
D2 Review: Boundary Artifact producer gap for CANDIDATE-003
        ↓
D3 Portfolio: PROMOTE_TO_DESIGN
        ↓
This Asset Type Confirmation & Design
```

### Minimum justifying evidence

```text
Why the Candidate exists:
  Both completed tasks documented hard In Scope / Out of Scope / Non-Goals
  (TASK-001: no scanners/analyzers; TASK-002: domain-only, no analyzer/CLI creep).
  Closeout and review used those exclusions for scope compliance.

Why it should become an Asset:
  Distinct producer role for Boundary Artifact already consumed by designed
  CANDIDATE-003; not absorbed by 001/002/003; D3 disposition PROMOTE_TO_DESIGN.

Why type confirmation is required now:
  Stage C/D3 hypothesized SKILL, with TEMPLATE as alternate if purely skeletal.
  D4 must confirm type from nature, not inherit the hypothesis blindly.
```

Primary references:

```text
01-process-inventory.md
02-engineering-patterns.md PATTERN-004
03-asset-candidates.md CANDIDATE-004
07-candidate-003-task-closeout-lifecycle.md (Boundary Artifact consumer)
08-stage-d2-strong-candidate-architecture-review.md
09-stage-d3-candidate-portfolio-reassessment.md
```

```text
Historical Evidence supports the design.
Historical Evidence does not automatically define implementation.
```

---

## 3. Core Design Question

Is Explicit Task Boundary Definition:

| Option | Verdict |
|---|---|
| A reusable execution capability? | **Yes — primary** |
| A reusable structure? | **Yes — supporting only** (artifact skeleton) |
| A reusable policy? | **No** (does not merely constrain; it produces boundaries) |
| A reusable lifecycle? | **No** (no multi-authority lifecycle orchestration) |
| A composition of multiple asset types? | **Partial** — primary executable + supporting structural form |

```text
Primary nature: EXECUTABLE capability that derives and proposes
an explicit Task Boundary from task context.

Supporting nature: STRUCTURAL skeleton for the Boundary Artifact
(stable field layout), without independent candidate promotion.
```

Design proceeds only after this classification (see §4–§5).

---

## 4. Asset Type Analysis

### 4.1 SKILL

Skill fit when:

```text
Input Context → Reasoning / Decision Process → Structured Output
```

Evaluation:

| Question | Answer |
|---|---|
| Context-sensitive reasoning required? | **Yes** — roadmap pressure, adjacent capabilities, prior exclusions |
| Interpret task intent? | **Yes** — objective → what “this task” means |
| Identify implicit scope? | **Yes** — much scope is unspoken in briefs |
| Detect non-goals? | **Yes** — primary historical value |
| Reason about dependencies? | **Sometimes** — material constraints/dependencies only |
| Reconcile ambiguous requirements? | **Yes** — surface Open Questions; do not invent resolution |

```text
SKILL fit: STRONG
```

### 4.2 TEMPLATE

Template fit when primary reusable value is Stable Structure.

| Question | Answer |
|---|---|
| Could users manually populate a stable structure? | **Yes** — historically done in task docs |
| Main reusable component a document format? | **Partially** — format helps; reasoning still needed |
| Does execution logic add little beyond structure? | **No** — without reasoning, templates become empty lists |

```text
TEMPLATE fit: MEDIUM as supporting form; WEAK as sole primary type
```

### 4.3 RULE

| Question | Answer |
|---|---|
| Primarily restricting behavior? | **No** — produces an artifact used later for restriction |
| Define mandatory boundaries rather than generate them? | **No** — generation is the work |
| Would an explicit instruction be enough? | **No** — instruction alone does not yield reviewable Boundary Artifact |

```text
RULE fit: WEAK
```

### 4.4 WORKFLOW

| Question | Answer |
|---|---|
| Orchestrate multiple independent assets? | **No** |
| Manage lifecycle transitions? | **No** — at most light boundary version identity |
| Coordinate revision / validation / acceptance? | **No** — those remain 001 / 002 / 003 |

```text
WORKFLOW fit: REJECT
Do not classify as Workflow merely because the procedure has steps.
```

### 4.5 CHECKLIST

| Question | Answer |
|---|---|
| Primary responsibility verify completeness? | **No** — primary is to derive boundaries |
| Or derive the boundaries? | **Derive** |

```text
CHECKLIST fit: WEAK as primary; optional supporting completeness aid only
```

### 4.6 SHARED CONTRACT

| Question | Answer |
|---|---|
| Does Boundary Definition itself define the contract? | **No** — it produces content that may later share a format |
| Does it produce a contract? | **Produces Boundary Artifact** (conceptual) |
| Should Boundary Artifact become shared representation? | **Maybe later** — 003 already consumes conceptually |
| Sufficient implementation evidence for contract extraction? | **No** — formats still vary by task |

```text
SHARED CONTRACT as the asset type for CANDIDATE-004: REJECT
Shared-contract extraction of the artifact format: deferred (see §24)
```

---

## 5. Asset Type Decision

### Decision Matrix

| Asset Type | Fit | Evidence | Reasoning |
|---|---|---|---|
| SKILL | Strong | PATTERN-004 I/O; D2 producer role; intent→scope reasoning | Context-sensitive derivation of structured Boundary Artifact |
| TEMPLATE | Medium (supporting) | Task docs used stable in/out sections | Structure reusable; insufficient alone without reasoning |
| RULE | Weak | Constraints appear after boundary exists | Enforcement ≠ generation |
| WORKFLOW | Reject | No multi-asset lifecycle | Steps ≠ workflow orchestration |
| CHECKLIST | Weak (supporting) | Completeness checks useful later | Verification ≠ derivation |
| SHARED CONTRACT | Reject (as primary type) | No stable machine schema yet | Artifact format may later extract; definition remains executable |

### Final Decision

```text
PRIMARY_ASSET_TYPE: SKILL

Asset Category: EXECUTABLE
Asset Type:     SKILL

Supporting Asset Type: TEMPLATE
  (Task Boundary Template — structural skeleton for Boundary Artifact;
   not an independent Candidate; not COMPOSITE promotion)
```

```text
Not COMPOSITE as Candidate classification:
  Primary reusable value is the executable derivation procedure.
  Template is a supporting structural aid, analogous to how closeout
  may later use recording templates without becoming COMPOSITE.
```

### Type Rationale — Why SKILL?

```text
EXECUTABLE → SKILL
```

Why not TEMPLATE alone:

```text
Empty skeletons do not surface implicit scope, non-goals, or ambiguity.
Historical value came from reasoned exclusions under roadmap pressure.
```

Why not WORKFLOW:

```text
No multi-authority lifecycle; one propose → confirm → emit cycle.
```

Why not RULE:

```text
Produces boundaries; does not only constrain behavior.
```

Why not CHECKLIST:

```text
Derivation primary; verification secondary/supporting.
```

Why not SHARED CONTRACT:

```text
Asset is the producer capability, not the shared schema itself.
```

Central SKILL traits:

```text
Clear trigger (task start / scope-risk)
Stable procedure (interpret → scope → non-goals → propose)
Limited autonomy (propose ≠ approve)
Repeatable inputs / predictable Boundary Artifact output
```

---

## 6. Responsibility Boundary

### Primary Responsibility

```text
This asset is responsible for:

  Interpreting task intent and adjacent context at task-definition time
  Deriving explicit Task Boundary (in scope / out of scope / non-goals)
  Surfacing material constraints, assumptions, and unresolved ambiguity
  Proposing a Boundary Artifact for authority confirmation
  Emitting a confirmed Boundary Artifact for downstream consumers

This asset is NOT responsible for:

  Task planning / implementation / architecture redesign
  Performing engineering revisions (CANDIDATE-001)
  Owning or executing validation gates (CANDIDATE-002)
  Orchestrating closeout or granting acceptance (CANDIDATE-003)
  Silently expanding or reinterpreting boundaries during closeout
  Authorizing scope expansion mid-task without External Authority
  Creating shared-contract schemas or runtime implementations
```

### Concept Distinctions

| Concept | Meaning | Owner (conceptual) |
|---|---|---|
| Task Intent | Why the task exists; desired outcome statement | Task Owner / External Authority (input) |
| Task Scope | What work is included for this task | Derived by this asset; confirmed externally |
| Task Boundary | Explicit in/out/non-goals + material constraints as artifact | Produced by this asset |
| Revision Scope | Bounded corrective target for a revision cycle | CANDIDATE-001 (may reference Task Boundary) |
| Validation Scope | Which tooling/evidence gates apply | CANDIDATE-002 / External Authority (not this asset) |
| Closeout Scope | What must be evidenced to close | CANDIDATE-003 (consumes Task Boundary) |
| Acceptance Boundary | Conditions under which External Authority may accept | External Authority; may be *referenced* in Boundary Artifact as completion criteria, not owned here |

```text
These concepts overlap in language.
They are not identical authorities or artifacts.
```

```text
Task Boundary ≠ Revision Scope
Task Boundary ≠ Validation Scope
Task Boundary ≠ Closeout ownership
```

---

## 7. Core Concept Model

### Chosen Model

```text
External Context + Task Intent
        ↓
Boundary Definition (CANDIDATE-004)
        ↓
Task Boundary (Boundary Artifact)
        ↓
Execution Scope (constraint on work)
        ├──────────────────┐
        ▼                  ▼
Revision (001)        Closeout (003)
        │                  │
        ▼                  │
Validation (002)           │
        └──────────────────┘
```

Adjustments from the brief’s linear chain:

```text
Revision → Validation → Closeout is not the only path.
Closeout may consume Boundary without a revision cycle.
Validation is not caused by Boundary; revision may REQUEST validation.
Boundary sits upstream as optional-but-preferred scope reference.
```

### Model Answers

```text
What exists before Boundary Definition?
  Task request / objective, roadmap pressure, known constraints,
  prior exclusions, External Authority context.

What Boundary Definition produces?
  Confirmed Boundary Artifact (Task Boundary representation).

Who consumes the result?
  Primary: CANDIDATE-003 (scope compliance).
  Optional: CANDIDATE-001 (derive/check Revision Scope against Task Boundary).
  Optional: planning / multi-agent context (Future Observation).
  Not as authority owner: CANDIDATE-002.

What happens when boundaries change?
  Change requires External Authority; produce SUPERSEDED prior + new CONFIRMED
  artifact (or explicit reject / defer / split). Closeout should reference
  which Boundary Artifact version applied.
```

---

## 8. Boundary Artifact

### Decision

```text
Boundary Artifact: REQUIRED (conceptual primary output)
```

Meaningful, implementation-neutral representation consumed by Closeout
and optionally by Revision.

### Minimum Stable Boundary Representation

Required fields:

```text
Objective
  One bounded statement of task intent / outcome

In Scope
  Explicit included work

Out of Scope / Non-Goals
  Explicit exclusions (hard boundaries)
```

Conditionally required (include when material):

```text
Constraints
  Binding limits (docs-only, domain-only, no new runtime, etc.)

Open Questions
  Unresolved ambiguity that must not be silently assumed away

Assumptions
  Explicit premises the boundary depends on
```

Optional (do not require by default):

```text
Dependencies
  External work or artifacts the task relies on

Acceptance Criteria Reference
  Scope-completion criteria pointers — not acceptance authority
```

```text
Goal: Minimum Stable Boundary Representation
Not: Maximum Documentation
```

### Representation Note

```text
Format remains implementation-neutral
(document section, task contract fragment, metadata, checklist, etc.).
Stable field semantics matter more than serialization choice.
```

---

## 9. Boundary Artifact Ownership

| Role | Actor (conceptual) |
|---|---|
| Who Creates / Proposes Boundary? | CANDIDATE-004 (Skill / operating agent invoking it) |
| Who May Modify Boundary? | External Authority / Task Owner after change request; Skill may draft revision |
| Who Consumes Boundary? | CANDIDATE-003 (required preference); CANDIDATE-001 (optional); future planners |
| Who Approves / Confirms Boundary? | External Authority / Task Owner |
| Who Can Override Boundary? | External Authority / Task Owner only |

```text
Human / Task Owner / External Authority: confirmation & override
Asset / Agent invoking Skill: proposal & drafting only
Workflow (003): consume for compliance — never redefine as planning
```

```text
Proposal Authority ≠ Acceptance Authority
```

---

## 10. Boundary Lifecycle

### Necessity Questions

| Question | Answer |
|---|---|
| Needs identity across time? | **Yes** — closeout compliance needs a stable reference |
| Can it change during execution? | **Yes** — only via authorized change handling |
| Can multiple versions coexist? | **Yes** — prior SUPERSEDED + current CONFIRMED |
| Does Closeout need version awareness? | **Yes** — which boundary applied |

### Decision

```text
Lifecycle Requirement: MINIMUM CONCEPTUAL LIFECYCLE
(not a full state-machine product)
```

Minimum states:

| State | Meaning |
|---|---|
| PROPOSED | Drafted by Skill; not yet confirmed |
| CONFIRMED | External Authority accepted; active execution reference |
| SUPERSEDED | Replaced by a newer CONFIRMED boundary |

Rejected as premature:

```text
Heavy DRAFT/REVISED/… product state machines
Automatic transitions without External Authority
Runtime workflow engine for boundary alone
```

```text
Identity rule:
  A CONFIRMED Boundary Artifact should be referenceable
  (path, id, or equivalent) by Closeout evidence packages.
```

---

## 11. Boundary Change Handling

### Scenario Path

```text
Task starts
        ↓
Boundary defined (CONFIRMED)
        ↓
Revision / execution begins
        ↓
New requirement appears
```

### Decision Principles (conceptual — not implementation)

| Path | When appropriate |
|---|---|
| Reject Change | Outside Task Boundary; no authorized expansion |
| Expand Boundary | External Authority confirms expansion; emit new CONFIRMED, SUPERSEDE prior |
| Create New Boundary Version | Preferred representation of authorized expansion/narrowing |
| Defer Requirement | Record as deferred / out-of-scope for this task |
| Split Into Another Task | Material new program of work; do not silently fold in |

```text
Unauthorized Boundary Expansion is a failure mode (§21).
CANDIDATE-001 must not treat revision findings as license to redefine Task Boundary.
CANDIDATE-003 must not redefine boundaries during closeout.
```

---

## 12. Input Model

### Required Inputs

```text
Task Identity
  Which task / stage is being bounded

Task Intent / Objective
  Desired outcome statement

Scope Risk Context
  Why explicit boundary is needed (roadmap pressure, adjacent capabilities,
  known feature-creep risks) — may be brief but must be present
```

### Optional Inputs

```text
Existing Requirements / Briefs
Known Non-Goals from prior tasks
Repository / product context summaries
Constraints (tooling, docs-only, packaging)
Existing Decisions / freezes (pointers only)
Deferred work lists from related tasks
```

### External Inputs

```text
External Authority Context
  Who confirms the proposed boundary

Task Owner preferences
  Soft priorities that must not silently override hard exclusions
```

```text
Do not create Python schemas in this stage.
```

---

## 13. Output Model

### Primary Output

```text
Boundary Artifact (CONFIRMED after authority confirmation)
  Minimum fields per §8
```

### Supporting Outputs

```text
Boundary Rationale (brief)
  Why major exclusions exist — enough for review, not essays

Open Questions
  Unresolved items requiring External Authority before silent assumption

Change / Supersession Record (when replacing a prior CONFIRMED boundary)
```

### External References

```text
Pointers to task brief, roadmap notes, prior exclusions
(not owned content duplication)
```

```text
Primary Output = Boundary Artifact
Proposal without confirmation is incomplete for Closeout preference.
```

---

## 14. Execution Model

```text
Input Context
        ↓
Interpret Task Intent
        ↓
Identify In-Scope Work
        ↓
Identify Out-of-Scope / Non-Goals
        ↓
Identify Material Constraints
        ↓
Detect Ambiguity / Assumptions
        ↓
Propose Boundary Artifact (PROPOSED)
        ↓
Authority Confirmation (External)
        ↓
Boundary Artifact (CONFIRMED)
```

### Separation

```text
Boundary Generation  = Skill responsibility
Boundary Acceptance  = External Authority / Task Owner
```

```text
The asset may propose boundaries without authority to approve them.
If confirmation is refused, stop or revise proposal — do not invent approval.
```

---

## 15. Authority Model

| Question | Answer |
|---|---|
| Who Proposes Boundary? | CANDIDATE-004 / invoking operator |
| Who Confirms Boundary? | External Authority / Task Owner |
| Who Can Override Boundary? | External Authority / Task Owner |
| Who Can Request Boundary Change? | Task Owner, reviewers, executing agents (request only) |
| Who Determines Task Acceptance? | External Acceptance Authority via CANDIDATE-003 — **not** this asset |

Actors (conceptual):

```text
Asset / Agent — propose & draft
Human / Task Owner / External Authority — confirm, override, authorize change
Workflow (003) — consume for compliance assessment
```

```text
Proposal Authority ≠ Acceptance Authority
Boundary Confirmation ≠ Task Acceptance
```

---

## 16. Relationship with CANDIDATE-001

```text
CANDIDATE-004 Task Boundary Definition
vs
CANDIDATE-001 Targeted Engineering Revision
```

### Clarification

```text
Boundary ≠ Revision Scope
```

| Question | Answer |
|---|---|
| Does 001 consume Boundary? | **Optionally** — may use it to keep revision inside Task Boundary |
| Does 001 derive Revision Scope from Boundary? | **May constrain** Revision Scope; does not replace finding-triggered Revision Target |
| Can Revision exist without Boundary? | **Yes** — 001 has its own Scope Boundary input |
| Can Boundary exist without Revision? | **Yes** — common happy path |

```text
Static dependency: NONE (hard dependency rejected)
Information flow: OPTIONAL (001 MAY read Boundary Artifact)
Authority: 001 must not redefine Task Boundary via revision
```

---

## 17. Relationship with CANDIDATE-002

```text
CANDIDATE-004 Boundary Definition
vs
CANDIDATE-002 Repository Tooling Validation Gate
```

| Question | Answer |
|---|---|
| Does Boundary influence validation? | **Context only** — e.g. docs-only may imply which gates are relevant |
| Does Boundary define required validation? | **No** — Required Gate Set remains External Authority / gate policy |
| Does Validation determine its own scope? | **Yes** — 002 owns gate execution semantics |
| Can Boundary provide context without controlling authority? | **Yes** — preferred relationship |

```text
Do not transfer validation authority to Boundary Definition.
Boundary may mention constraints; it does not own pass/fail gates.
```

```text
Static dependency: NONE
Authority relationship: NONE (no control)
Information flow: OPTIONAL weak context only
```

---

## 18. Relationship with CANDIDATE-003

```text
CANDIDATE-004 Boundary Definition
vs
CANDIDATE-003 Task Closeout Lifecycle
```

D3 principle retained:

```text
Closeout consumes boundaries; it does not define them.
```

| Question | Answer |
|---|---|
| What does Closeout consume? | Boundary Artifact (Objective / In / Out / Non-Goals / material constraints); version identity when available |
| How does Closeout judge scope compliance? | Compare claimed work & diffs/evidence to CONFIRMED Boundary Artifact |
| When actual output exceeds boundary? | Record scope breach / unexpected work; do not silently expand; escalate / defer / split per External Authority |
| Version awareness? | **Yes** — evidence package should reference which CONFIRMED artifact applied |

```text
Producer → Consumer

CANDIDATE-004 PRODUCES Boundary Artifact
CANDIDATE-003 CONSUMES Boundary Artifact (preferred when present;
  equivalent explicit scope reference acceptable per 003 entry contract)
```

```text
Hard architectural dependency of 003 on implemented 004: NOT required
Conceptual dependency for preferred compliance evidence: YES
```

---

## 19. Cross-Asset Architecture

### Diagram

```text
External Context / Task Intent / External Authority
        │
        ▼
CANDIDATE-004 Explicit Task Boundary Definition (SKILL)
        │  produces (after confirmation)
        ▼
Boundary Artifact (CONFIRMED)
        │
        ├──── information flow (optional) ────► CANDIDATE-001 Revision
        │                                              │
        │                                              │ REQUESTS
        │                                              ▼
        │                                       CANDIDATE-002 Validation
        │
        └──── information flow (preferred) ───► CANDIDATE-003 Closeout
                                                 (scope compliance consume)
```

### Arrow Types

| Relationship | Kind |
|---|---|
| 004 → Boundary Artifact | Production (owns creation of proposal; confirmation external) |
| Boundary → 003 | Information flow / optional composition (preferred consume) |
| Boundary → 001 | Optional information flow |
| Boundary → 002 | Not an authority relationship; optional weak context only |
| 001 → 002 | Existing REQUESTS (unchanged; not created by 004) |

```text
Distinguish:
  Static Dependency — none required among 001/002/004
  Information Flow — Boundary Artifact to 003 (preferred), 001 (optional)
  Optional Composition — closeout without 004 if equivalent scope exists
  Authority Relationship — External Authority confirms boundary & acceptance
```

---

## 20. Reusability Model

### Contexts

| Context | Fit |
|---|---|
| Feature Development | Strong — classic scope-creep risk |
| Bug Fix | Contextual — light boundary often enough |
| Repository Refactor | Strong — explosion risk |
| Architecture Change | Strong — adjacent capability pressure |
| Task Planning | Strong — natural invocation point |
| Agent Execution | Broad — shared execution context candidate |
| Multi-Agent Coordination | Future observation — artifact as shared context |

### Reuse Scope

```text
Reuse Scope: BROAD

Not UNIVERSAL without evidence — trivial one-line chores may not need
full Boundary Artifact ceremony.

Not NARROW — evidence spans both completed milestone tasks and
general engineering scope-risk situations.
```

---

## 21. Failure Modes

| Failure Mode | Detection | Mitigation | Authority Escalation |
|---|---|---|---|
| Boundary Too Broad | Closeout/review finds vague “everything useful” scope | Narrow In Scope; add Non-Goals | Task Owner confirms narrowing |
| Boundary Too Narrow | Blocked work clearly inside intent but excluded | Authorized expand or split task | External Authority |
| Missing Non-Goals | Roadmap-adjacent work appears mid-task | Re-run derivation; add exclusions | Confirm SUPERSEDED version |
| Implicit Scope Assumptions | “Everyone knows” items never written | Force Assumptions / Open Questions fields | Confirm before execution |
| Unresolved Ambiguity | Open Questions ignored | Stop confirmation until resolved or explicitly deferred | External Authority |
| Unauthorized Boundary Expansion | Diff/work outside CONFIRMED boundary | Reject or split; do not absorb in revision | External Authority |
| Boundary Drift | Soft reinterpretation over time without new version | Require SUPERSEDE + confirm for material change | Task Owner |
| Conflicting Requirements | In Scope contradicts Non-Goals / constraints | Surface conflict in Open Questions; do not pick silently | External Authority |

```text
Over-modeling trivial typos-as-failures is rejected.
```

---

## 22. Interaction Model

Possible composition modes (conceptual only):

```text
Explicit Invocation
  Operator runs Boundary Definition at task start

Automatic Suggestion
  Planning agent suggests invoking when scope-risk signals present

Workflow Composition
  Upstream step before implementation; downstream feed to Closeout

Agent Pre-Execution Step
  Multi-agent systems establish shared Boundary Artifact before work
```

```text
Do not implement invocation logic in this stage.
```

---

## 23. Supporting Structural Assets

### Task Boundary Template (STRUCTURAL → TEMPLATE)

```text
Purpose:
  Stable field skeleton for Boundary Artifact
  (Objective / In Scope / Out of Scope / Non-Goals / …)

Relationship to Primary Asset:
  Supporting structure filled/produced by the SKILL procedure

Standalone Reuse Value:
  Medium — humans can fill manually; quality depends on judgment

Implementation Necessity:
  Useful for consistency; not required to validate SKILL nature
```

### Optional Boundary Completeness Checklist (STRUCTURAL → CHECKLIST)

```text
Purpose:
  Verify minimum fields / ambiguity surfacing before confirmation

Relationship:
  Supporting verification after derivation

Standalone Reuse Value:
  Low–Medium

Implementation Necessity:
  Optional; do not promote as independent Candidate now
```

```text
Supporting structures are NOT promoted to independent Candidates in D4.
```

---

## 24. Shared Contract Decision

```text
Shared Contract Decision: FUTURE_EXTRACTION_CANDIDATE
```

Rationale:

```text
Boundary Artifact is a real cross-asset conceptual object
(producer 004 → consumer 003).

Formats still vary; no implementation schema exists.
READY_FOR_SHARED_CONTRACT lacks strong evidence.

NOT_REQUIRED would understate the cross-asset role.
CONCEPTUAL_ONLY is true today; FUTURE_EXTRACTION_CANDIDATE
records that stable semantics may later extract without
redesigning the SKILL responsibility.
```

```text
Do not create a shared contract in this stage.
```

---

## 25. Architecture Stress Tests

### Scenario A — Simple Bug Fix

```text
Useful as a lightweight boundary (objective + short non-goals).
Full ceremony optional; Skill still valid when scope-risk is low.
Value: prevents “while we’re here” expansions.
```

### Scenario B — Large Refactor

```text
High value. Explicit Non-Goals prevent scope explosion into
unrelated subsystems. Boundary Artifact becomes primary compliance
reference for Closeout.
```

### Scenario C — Ambiguous Requirement

```text
Skill must surface Open Questions rather than invent scope.
Confirmation blocked until External Authority resolves or defers.
```

### Scenario D — Mid-Task Scope Change

```text
Distinguish:
  Revision — corrective work inside CONFIRMED boundary (001)
  Expansion — authorized SUPERSEDE + new CONFIRMED boundary
  New Task — split when work is a new program
```

### Scenario E — Multiple Agents

```text
Boundary Artifact can serve as shared execution context.
Authority confirmation remains external; agents propose only.
Detailed multi-agent protocol = Future Observation.
```

### Scenario F — Validation Failure

```text
Boundary remains stable while Revision + Validation repeat.
Validation failure does not redefine Task Boundary.
Only External Authority may change boundary version.
```

---

## 26. Final Design Decision

```text
Candidate:              CANDIDATE-004
Asset Name:             Explicit Task Boundary Definition
Asset Category:         EXECUTABLE
Primary Asset Type:     SKILL
Supporting Asset Type:  TEMPLATE (Task Boundary Template; not independent Candidate)
Design Version:         0.1
Status:                 DESIGNED

Primary Responsibility:
  At task-definition time, derive and propose an explicit Task Boundary
  and emit a confirmed Boundary Artifact for downstream compliance use.

Primary Inputs:
  Task Identity, Task Intent/Objective, Scope Risk Context
  (+ optional briefs, prior non-goals, constraints, External Authority context)

Primary Outputs:
  Boundary Artifact (CONFIRMED) — Objective, In Scope, Out of Scope/Non-Goals
  (+ material Constraints, Open Questions, Assumptions as needed)

Authority Boundary:
  Skill proposes; External Authority / Task Owner confirms and overrides.
  Skill does not grant task acceptance.

Cross-Asset Consumers:
  CANDIDATE-003 (preferred consume for scope compliance)
  CANDIDATE-001 (optional constraint on Revision Scope)
  CANDIDATE-002 (no authority; optional weak context only)

Lifecycle Requirement:
  Minimum conceptual lifecycle — PROPOSED / CONFIRMED / SUPERSEDED

Shared Contract Decision:
  FUTURE_EXTRACTION_CANDIDATE

Reuse Scope:
  BROAD
```

### Asset Identity Table

| Field | Value |
|---|---|
| Asset Name | Explicit Task Boundary Definition |
| Candidate ID | CANDIDATE-004 |
| Asset Category | EXECUTABLE |
| Asset Type | SKILL |
| Design Version | 0.1 |
| Status | DESIGNED |

```text
Status is DESIGNED — not IMPLEMENTED.
```

### Implementation Readiness (framework vocabulary only)

| Dimension | Assessment |
|---|---|
| Identity Clarity | Clear |
| Type Confirmation | Clear (SKILL + supporting TEMPLATE) |
| Trigger Clarity | Clear (task start / scope risk) |
| I/O Clarity | Clear |
| Authority Boundary | Clear |
| Consumer Fit (003) | Clear |
| Artifact Minimum Fields | Clear |
| Lifecycle | Minimum defined; not over-modeled |

```text
Design Status: DESIGNED
Implementation Readiness: REQUIRES_EVIDENCE

Still requires before READY_FOR_IMPLEMENTATION:
  - concrete Boundary Artifact persistence / reference conventions
  - confirmation UX / authority binding patterns
  - optional template packaging choices
  - shared-contract extraction review (if pursued later)
```

---

## 27. Future Observations

```text
Boundary Artifact Versioning conventions (ids, paths, supersession links)
Shared Contract Extraction timing and schema stability
Agent Authority Model for multi-agent shared Boundary context
Task Graph Integration (boundary per node vs per task)
Boundary Change Governance playbooks beyond principles above
Whether Acceptance Criteria Reference belongs in minimum fields
Lightweight vs full invocation heuristics for trivial tasks
```

Do not implement these in D4.

---

## 28. Review Summary

```text
CANDIDATE-004 is DESIGNED as EXECUTABLE → SKILL.

It fills the D2/D3 producer gap for Boundary Artifact consumed by
CANDIDATE-003, without absorbing revision, validation, or closeout.

Supporting TEMPLATE is documented but not promoted.
Shared contract remains FUTURE_EXTRACTION_CANDIDATE.
No runtime implementation created.
```

```text
Recommended next step (external review):
  Architecture review of CANDIDATE-004 design
  Do not implement until authorized
```

---

## End of Design

```text
CANDIDATE-004 Explicit Task Boundary Definition
Asset Type Confirmed: SKILL
Status: DESIGNED
Document: 10-candidate-004-explicit-task-boundary-definition.md
```

# MILESTONE-002 Stage B1 — First Experiment Selection & Definition

## 1. Mission

```text
Experiment Selection
+
Eligibility Assessment
+
Experiment Definition
```

Stage B1 identifies and defines the first real Asset Validation Experiment
for:

```text
CANDIDATE-001
Targeted Engineering Revision
```

```text
Stage B1 does NOT:
  Execute the experiment
  Invoke CANDIDATE-001
  Validate the asset
  Implement / package the asset
```

Governing method:

```text
ai-engineering/milestones/MILESTONE-002/01-validation-experiment-framework.md
```

Design reference:

```text
ai-engineering/milestones/MILESTONE-001/05-candidate-001-targeted-engineering-revision.md
```

---

## 2. Validation Subject

| Field | Value |
|---|---|
| Primary Asset | CANDIDATE-001 Targeted Engineering Revision |
| Type | SKILL |
| Design Status | DESIGNED |
| Lifecycle (unchanged) | VALIDATION_READY |
| Experiment Kind | Single Asset |

```text
CANDIDATE-002 / 003 / 004 are NOT co-primary validation subjects.
Ordinary engineering practices (git, diff review, optional tests)
may occur in later execution stages without becoming separate experiments.
```

Core responsibility (from design):

```text
Given a known finding / revision target,
plan and execute a bounded corrective revision,
request validation when needed,
report disposition — without redesign or feature expansion.
```

---

## 3. Repository Context

Inspection performed for Stage B1 (no defects introduced):

```text
Working tree: clean relative to main except Stage B1 task brief (untracked)
MILESTONE-001: COMPLETED / CLOSE_WITH_OBSERVATIONS
MILESTONE-002: IN_PROGRESS; Stage A framework COMPLETED
Product code (src/tests): no open review finding package awaiting disposition
ai-engineering/reviews: historical TASK-001 / TASK-002 reviews (already addressed in prior revisions)
```

Evidence sources checked:

```text
Milestone status documents
Final closeout Future Transition wording
Empty extraction/experiments placeholders (expected; not defects)
Project vision doc (broad; not a bounded finding by itself)
Git status / recent commits
```

```text
“we need an experiment” was NOT treated as justification for a revision.
```

---

## 4. Candidate Task Discovery

Small high-quality set (not an exhaustive inventory):

### Candidate Task A — Post-closeout Future Transition Pointer Hygiene

```text
Candidate Task:
  Update MILESTONE-001 current Future Transition Direction so it no longer
  reads as if no next milestone identity exists, after MILESTONE-002 was
  created for Asset Experimental Validation.

Why the task exists independently:
  Operators navigating from completed MILESTONE-001.md receive stale
  current guidance. MILESTONE-002 already exists on main; the index still
  says “(evidence-gated; no milestone identifier assigned here)”.

Current evidence:
  MILESTONE-001.md Future Transition Direction (lines ~180–182)
  Contrast: milestones/MILESTONE-002/ exists with Stage A completed
  Closeout doc historically said not to create M2 *in that stage*
  (accurate then); index current-status block is now misleading as guidance

Potential relevance to CANDIDATE-001:
  Bounded documentation hygiene revision after program progression —
  same class as post-review / closeout hygiene revisions in PATTERN-001

Observable outcome:
  Diff limited to transition-pointer / status guidance wording;
  M1 remains COMPLETED; no redesign of portfolio or designs

Potential risks:
  Accidental rewrite of historical closeout narrative
  Scope creep into rewriting 12-final verdicts
  Treating this as M2 process work rather than independent hygiene
```

### Candidate Task B — Closeout Document Historical Postscript (related)

```text
Candidate Task:
  Add a dated postscript to 12-final-architecture-review-and-closeout.md
  Future Transition section noting MILESTONE-002 was later created.

Why independent:
  Same navigational/traceability concern; document currently ends with
  “no milestone created here” which is stage-true but easy to misread.

Relevance to 001:
  Possible secondary target in the same hygiene revision — or deferred

Risks:
  Blurring historical record vs current pointer; better as optional
  supporting change under Task A, not a separate experiment
```

### Candidate Task C — project.md AI Engineering status refresh

```text
Candidate Task:
  Update project.md §9 to reflect M1 complete / M2 validation phase.

Why independent:
  Vision doc still describes extraction as primarily future planning.

Relevance to 001:
  Weak — more open narrative refresh than finding-triggered revision

Risks:
  Over-broad scope; redesign tone; weak acceptance criteria
```

### Candidate Task D — Product/code open findings

```text
No genuine open product revision finding was discovered that independently
requires Targeted Engineering Revision right now.
Empty extraction/.gitkeep directories are intentional placeholders, not defects.
```

---

## 5. Candidate Task Assessment

| Candidate | Authenticity | 001 Fit | Complexity | Observable | Variation | Verdict |
|---|---|---|---|---|---|---|
| A — M1 Future Transition hygiene | High | Strong | Meaningful-small | High | Docs/hygiene context | **Primary** |
| B — Closeout postscript | Medium–High | Supporting | Low | Medium | Same cluster | Optional under A |
| C — project.md refresh | Medium | Weak | Broad | Diffuse | Narrative | **Reject for B1** |
| D — Product findings | N/A | N/A | N/A | N/A | N/A | **None found** |

---

## 6. Eligibility Analysis (Stage A model)

Assessing **Candidate Task A**:

| Dimension | Assessment |
|---|---|
| Task Authenticity | Real inconsistency between completed M1 index guidance and existing M2 |
| Asset Relevance | Matches finding → bounded docs revision → disposition |
| Meaningful Complexity | Small but non-trivial: must preserve historical closeout truth vs update current pointer |
| Observable Outcome | Concrete markdown diff + reviewable before/after guidance |
| Context Suitability | Docs/hygiene; classic 001 reuse context |
| Context Variation Potential | First experiment in docs-hygiene lane (diverse from later code revisions) |
| Repeatability Potential | Program-pointer hygiene after milestone transitions can recur |

### Disqualifiers checked

| Disqualifier | Applies? |
|---|---|
| Task Too Trivial | No — judgment required on historical vs current wording |
| No Clear Revision Need | No — stale current guidance is clear |
| No Meaningful Asset Responsibility | No — targeted corrective revision |
| No Observable Outcome | No |
| Artificial Motivation | No — discovered via repo inspection after M2 creation |
| Excessive Dependency on Other Assets | No — single-asset; optional ordinary git/diff only |

```text
Eligible: YES
```

---

## 7. Candidate-001 Responsibility Match

Required natural involvement:

| Need | Match |
|---|---|
| Known Engineering Target | Yes — MILESTONE-001.md Future Transition Direction (optional: light postscript on 12-final §17) |
| Bounded Revision Need | Yes — update current transition pointer; preserve COMPLETED / closeout decision |
| Existing Context | Yes — M1 closeout + M2 Stage A already on main |
| Focused Revision | Yes — docs-only hygiene |

Must NOT primarily require (and does not):

```text
Open Exploration — no
Initial Problem Discovery — target already identified
Repository-Wide Inspection — no
Task Boundary Negotiation (004) — no
Full Task Closeout (003) — no
```

```text
CANDIDATE-001 is not being asked to become a general engineering process.
This remains Targeted Engineering Revision.
```

---

## 8. Selection Decision

```text
SELECTED
```

### Selected Task

```text
Post-closeout Future Transition Pointer Hygiene
for MILESTONE-001 index (and optional closeout postscript)
after MILESTONE-002 creation
```

### Why eligible

```text
Independent navigational/consistency need
Passes Stage A eligibility dimensions
Falsifiable value hypothesis
Observable, bounded outcome
```

### Why CANDIDATE-001 is relevant

```text
Known target + bounded docs hygiene + acceptance criteria
without redesign — core 001 trigger profile
```

### Why Single Asset

```text
Primary procedure under test is 001’s inspect→bound→plan→revise→report
Other assets not required for the corrective work
002 not co-evaluated even if ordinary checks are later used
```

### Experiment Boundary (summary)

```text
Docs-only update of current Future Transition guidance;
preserve M1 COMPLETED and historical closeout decision text;
no portfolio redesign; no asset packaging
```

### Known Risks

```text
Rewriting history instead of updating current pointer / adding postscript
Scope creep into project.md or candidate designs
Overhead of experiment recording exceeding the small hygiene fix
```

```text
No Experiment would have been chosen over a fabricated task.
A genuine eligible task exists — fabrication not required.
```

---

## 9. Selected Experiment Definition

```text
Experiment ID:              EXP-M2-001
Experiment Kind:            Single Asset
Engineering Task:           Post-closeout Future Transition Pointer Hygiene
Task Context:               MILESTONE-001 COMPLETED; MILESTONE-002 exists (Stage A done)
Why Task Exists Independently:
  MILESTONE-001.md Future Transition still presents “no milestone identifier
  assigned here” as current guidance after MILESTONE-002 was created.
Selected Asset:             CANDIDATE-001 Targeted Engineering Revision
Asset Design Reference:
  ai-engineering/milestones/MILESTONE-001/05-candidate-001-targeted-engineering-revision.md
  Design Version 0.1 / DESIGNED / VALIDATION_READY
Invocation Reason:
  Bounded documentation hygiene finding with clear target and acceptance criteria
Experiment Objective:
  Apply CANDIDATE-001 experimental procedure to plan and perform the hygiene
  revision, then observe whether the asset adds repeatable revision value
Expected Value:             see §11
Invocation Boundary:        see §10
Expected Output:
  Scoped revision plan
  Targeted markdown changes
  Explicit disposition report
  (validation request only if procedure requires; not a 002 experiment)
Observable Outcomes:        see §12
Evidence Capture Plan:      see §12
Potential Failure Signals:  see §13
Potential Process Overhead: see §14
Known Limitations:          see §15
```

### Revision Target (for Stage B2)

```text
Primary:
  ai-engineering/milestones/MILESTONE-001/MILESTONE-001.md
  — Future Transition Direction block

Optional (same experiment, if still in bound scope):
  ai-engineering/milestones/MILESTONE-001/12-final-architecture-review-and-closeout.md
  — dated postscript under Future Transition Boundary
    clarifying MILESTONE-002 was created later; do not rewrite verdicts
```

### Revision Objective

```text
Make current transition guidance accurate and navigable:
point operators to MILESTONE-002 for Asset Experimental Validation,
while preserving that MILESTONE-001 closeout correctly did not assign
a next milestone ID at closeout time.
```

### Scope Boundary / Non-Goals

```text
In scope:
  Current-status Future Transition pointer wording
  Optional historical postscript (clearly dated / labeled)

Out of scope / Non-goals:
  Reopening MILESTONE-001 architecture decisions
  Changing CLOSE_WITH_OBSERVATIONS / ACHIEVED verdicts
  Modifying candidate designs 05–10
  Promoting any asset to VALIDATED
  Implementing Skills / Workflows
  Updating project.md vision narrative (Candidate C rejected)
  Product/code changes under src/
```

### Acceptance Criteria (engineering task — not experiment success)

```text
A reader of MILESTONE-001.md can identify MILESTONE-002 as the subsequent
validation milestone without contradicting the historical closeout decision.
Diff remains docs-only and reviewable.
No candidate lifecycle promotion occurs.
```

---

## 10. Invocation Boundary

What Stage B2 will validate (smallest meaningful responsibility):

```text
Input:
  Known revision target (M1 Future Transition hygiene)
  + Existing context (M1 complete, M2 exists)
  + Revision objective + scope/non-goals + acceptance criteria

        ↓

CANDIDATE-001 Experimental Procedure
(from design doc — not packaged Skill)

        ↓

Focused Revision Guidance / Plan

        ↓

Engineering Work (bounded docs edit)

        ↓

Observed Evidence + Disposition
```

```text
Do NOT expand into:
  Full engineering lifecycle
  CANDIDATE-003 closeout experiment
  CANDIDATE-004 boundary experiment
  CANDIDATE-002 as co-primary subject
```

Ordinary practices allowed without co-evaluation:

```text
Git inspection, diff review, optional repo checks as normal engineering
```

---

## 11. Expected Value Hypothesis

Falsifiable expected value:

```text
If CANDIDATE-001 procedure is intentionally applied to this hygiene finding,
then revision reasoning and change scope should be clearer and more
traceable (target ↔ objective ↔ non-goals ↔ disposition) than ad-hoc editing,
without expanding into M1 redesign — with acceptable documentation overhead.
```

Possible observable benefits:

```text
Clearer revision reasoning
Reduced unnecessary scope expansion
Better alignment between finding and revision
Improved change traceability
Lower repeated correction
```

```text
Expected Value ≠ Success Criteria
The experiment may conclude No Meaningful Value.
```

---

## 12. Evidence Capture Plan

Stage B2/B3 should capture (lightweight — must not dominate the task):

```text
Original Engineering Context
Revision Target + Objective + Scope/Non-Goals
Invocation Record (that 001 procedure was used intentionally)
Actual Revision Process (brief)
Resulting Changes (paths + summary)
Human Intervention
Observed Benefits
Observed Problems
Unexpected Behavior
Process Overhead (qualitative)
Non-Use / Boundary Notes (what was refused)
Experiment Outcome recommendation (SUPPORTED / …)
Recommended Disposition (CONTINUE_VALIDATION / …) — not final lock
```

```text
Avoid making evidence capture more expensive than the hygiene fix itself.
```

---

## 13. Potential Failure Signals

Pre-committed honest observation list:

```text
Revision scope remains unclear under 001 procedure
Repeated human boundary correction
Output duplicates normal ad-hoc reasoning (no added structure)
No measurable or observable value
Process overhead exceeds benefit for a small docs fix
Asset responsibility overlaps M2 stage bookkeeping rather than revision
Invocation requires excessive context setup
Task turns out unsuitable once editing begins (e.g. only historical text should stay untouched)
Silent scope creep into designs / verdicts / project.md
```

```text
Failure Signals are pre-commitments — do not redefine after the fact
to preserve a success narrative.
```

---

## 14. Process Overhead Considerations

Likely overhead (qualitative, pre-B2):

```text
Additional reasoning: low–medium (historical vs current wording judgment)
Additional documentation: medium (experiment evidence notes)
Context preparation: low (targets already identified in B1)
Human clarification: low–medium if postscript vs rewrite debated
Additional review steps: low (docs-only diff review)
```

```text
Risk: experiment recording overhead > engineering work
Mitigation: keep evidence notes minimal; single short experiment record
```

```text
No ROI score. Ensure Validation Process does not dominate Engineering Work.
```

---

## 15. Known Limitations

```text
First experiment is docs/hygiene context — not code/test revision diversity
Single-repo, single finding cluster
Does not by itself justify VALIDATED
Does not validate composition
Optional closeout postscript may be skipped if it risks history rewrite
MILESTONE-001 artifacts are modification targets for B2 engineering work
  — B1 itself did not modify them
```

---

## 16. Stage B1 Conclusion

```text
Selection Decision: SELECTED

Experiment: EXP-M2-001
Asset:      CANDIDATE-001 (Single Asset)
Task:       Post-closeout Future Transition Pointer Hygiene

CANDIDATE-001 remains VALIDATION_READY (not VALIDATED).
No experiment execution occurred in Stage B1.
No asset implementation occurred.
```

---

## 17. Stage B2 Boundary

```text
Stage B2 (when authorized) should:
  - Intentionally invoke CANDIDATE-001 experimental procedure
  - Perform the bounded hygiene revision
  - Capture evidence per §12
  - Record Experiment Outcome (not final asset disposition lock)

Stage B2 should NOT:
  - Package SKILL.md / implement runtime
  - Co-validate CANDIDATE-002/003/004 as primary subjects
  - Promote CANDIDATE-001 to VALIDATED from this single run
  - Expand into project.md or portfolio redesign
```

```text
STOP after Stage B1 push until Stage B2 is authorized.
```

---

## End of Stage B1

```text
Document: 02-stage-b1-first-experiment-selection.md
Decision: SELECTED
Experiment executed: NO
```

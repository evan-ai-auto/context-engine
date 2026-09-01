# MILESTONE-002 Stage C1 — Evidence Gap Analysis & Second Experiment Selection

## 1. Mission

```text
Evidence Gap Analysis
+
Second Experiment Selection
```

After EXP-M2-001 (MIXED EVIDENCE), determine what evidence is still missing
for **CANDIDATE-001** and select **EXP-M2-002** for meaningful information gain.

```text
Do NOT run another experiment merely to increase experiment count.
```

```text
Stage C1 does NOT execute EXP-M2-002 or make final asset disposition.
```

---

## 2. Evidence Baseline (EXP-M2-001)

| Dimension | EXP-M2-001 |
|---|---|
| Task type | Documentation hygiene |
| Complexity | Low |
| Target | Known (Future Transition block) |
| Revision scope | Very narrow |
| Files | Single primary file |
| Change type | Markdown navigation pointer |
| Invocation count | One |
| Context | Single repository |
| Validation | Lightweight diff / consistency |
| Experiment constraint | Primary Target Only (strong external boundary reinforcement) |

**Strongest evidence:** boundary discipline, scope traceability, minimal plan, stop discipline.

**Major limitations:** single experiment; docs-only; small; single-file; no code/test;
no composition; boundary attribution confounded with Stage B2 Primary Target Only rule.

```text
Evidence Baseline — not final validation.
CANDIDATE-001 remains VALIDATION_READY.
```

---

## 3. Evidence Gap Analysis

| Gap | Evidence Missing | Why It Matters | EXP-M2-002 Can Address? | Priority |
|---|---|---|---|---|
| Task Complexity Gap | Medium-complexity revision behavior | M2-001 only tiny docs fix | **Yes** | **High** |
| Target Complexity Gap | Multi-step scope reasoning under softer constraints | M2-001 target was pre-known single block | **Yes** | **High** |
| Revision Scope Gap | Multi-file bounded revision | M2-001 single file | **Yes** | **High** |
| Multi-File Coordination Gap | Plan spanning related test modules | Not observed | **Yes** | **Medium** |
| Code / Test Change Gap | Procedure on test/code artifacts | M2-001 markdown only | **Yes** | **High** |
| Validation Requirement Gap | pytest/ruff as meaningful gate | M2-001 diff-only | **Yes** | **High** |
| Boundary Autonomy Gap | Scope control without Primary Target Only file lock | M2-001 confounded attribution | **Yes** | **High** |
| Context Preparation Gap | Finding discovery from plan↔tests audit | M2-001 pre-selected in B1 | Partially | Medium |
| Repeated Invocation Gap | Overhead trend across runs | n=1 | No (future) | Low |

---

## 4. Information Gain Objective

Maximize **new evidence** via contrast, not similarity.

```text
EXP-M2-001                          EXP-M2-002 (target profile)
Small / Docs / Single file    →     Medium / Tests / Multi-file (discovered)
Low complexity                →     Scope reasoning on contract tests
External file lock            →     Revision Boundary Discovery
Diff-only validation          →     pytest (+ ordinary static checks)
```

Required context difference for information gain:

```text
Test-contract completion on domain enums (code/test)
with discoverable revision boundary and meaningful validation —
directly addresses B3 unknowns on medium-complexity and boundary autonomy.
```

---

## 5. Required Experiment Profile

| Characteristic | Target |
|---|---|
| Complexity | Medium |
| Target | Known finding; potentially multiple related files |
| Change type | Test / structured contract verification (preferred over docs-only) |
| Validation | pytest (Supporting Engineering Validation) |
| Asset | CANDIDATE-001 only (Single Asset) |
| Boundary | Revision Boundary Discovery (not predetermined file list) |

Must fit **Targeted Engineering Revision** — not feature development or redesign.

---

## 6. Repository Task Discovery

Sources inspected:

```text
EXP-M2-001/B3 follow-up findings (12-final postscript)
MILESTONE-002.md background vs B2 M1 edit
TASK-002 04-test-plan.md vs tests/domain/ coverage
pytest / ruff / mypy baseline (44 passed, clean)
Product src/ (no open defect package)
CLI placeholder (out of scope — implementation, not revision)
```

```text
No artificial tasks invented.
No defects introduced for experiment purposes.
```

---

## 7. Candidate Task Pool

### CT-01 — Closeout Future Transition postscript (12-final)

| Field | Value |
|---|---|
| Location | `MILESTONE-001/12-final-architecture-review-and-closeout.md` §17 |
| Independent justification | B3 follow-up: closeout body lacks dated note that M2 was created later |
| Finding | Historical future-direction text without post-M2 pointer |
| Type / complexity | Docs / Low |
| Files | Single |
| Validation | Diff review |
| 001 fit | Hygiene revision |
| Gap addressed | Context diversity only (weak) |
| Risks | Too similar to M2-001; history rewrite |

### CT-02 — MILESTONE-002 background clarification (M1 edit policy)

| Field | Value |
|---|---|
| Location | `MILESTONE-002/MILESTONE-002.md` §2 Background |
| Independent justification | States “must NOT modify MILESTONE-001” but B2 legitimately edited M1 |
| Finding | Stale operational guidance |
| Type / complexity | Docs / Low |
| Files | Single |
| Validation | Diff review |
| 001 fit | Hygiene revision |
| Gap addressed | Low — meta-documentation only |
| Risks | Nearly duplicate of M2-001 shape |

### CT-03 — Domain enum entity-level test plan completion **(SELECTED)**

| Field | Value |
|---|---|
| Location | `tests/domain/` vs `sessions/TASK-002/04-test-plan.md` T-04–T-07 |
| Independent justification | Test plan requires each frozen enum member accepted on entity models; `test_enums.py` covers enum construction but entity tests exercise only subsets (e.g. one `DependencyScope`, one `EvidenceType`, two `ModuleType`, two `AnalysisStatus`) |
| Finding | Traceability gap between plan wording and entity-level parametrized acceptance |
| Type / complexity | Test contract / Medium |
| Files potentially affected | Multiple under `tests/domain/` (discovered during invocation) |
| Validation | pytest; ruff/mypy if imports change |
| 001 fit | Bounded revision after identified coverage gap (Rev-002 precedent) |
| Gap addressed | Code/test change, multi-file, validation, boundary discovery, complexity |
| Risks | Scope creep into production models; over-testing enum redundancy |

### CT-04 — CLI init placeholder replacement

| Field | Value |
|---|---|
| Location | `src/ai_context/cli/main.py` |
| Independent justification | Placeholder exists by design (TASK-001 scope) |
| Rejection | Greenfield / feature — not Targeted Engineering Revision |

### CT-05 — No eligible task

| Field | Value |
|---|---|
| Status | Not required — CT-03 qualifies |

---

## 8. Candidate Exclusion

| Candidate | Reason |
|---|---|
| CT-01 | Too similar to EXP-M2-001 (docs-only, single-file, low complexity) |
| CT-02 | Too similar; meta-doc hygiene; minimal information gain |
| CT-04 | Requires new capability — not bounded revision |
| CT-05 | N/A — eligible task exists |

---

## 9. EXP-M2-002 Selection

```text
Experiment ID:     EXP-M2-002
Experiment Kind:   Single Asset
Primary Subject:   CANDIDATE-001 Targeted Engineering Revision
Engineering Task:  Domain Enum Entity-Level Test Plan Completion
```

Design reference:

```text
ai-engineering/milestones/MILESTONE-001/05-candidate-001-targeted-engineering-revision.md
Supporting trace:
  ai-engineering/sessions/TASK-002/04-test-plan.md (T-04–T-07)
  ai-engineering/tasks/TASK-002-revision-002-Serialization Contract Completion.md (precedent)
```

---

## 10. Independent Task Justification

```text
TASK-002 closeout treated enum verification as satisfied via test_enums.py,
but 04-test-plan.md T-05/T-06 (and related rows) describe entity-level
acceptance: each frozen member when used on Dependency / Evidence / Module /
GenerationMetadata.

Current entity tests validate representative members and invalid cases,
not full per-member acceptance on each model.

This gap exists whether or not MILESTONE-002 runs:
  contract traceability and regression safety for frozen enums.
```

```text
Not justified by “we need experiment #2.”
```

---

## 11. Evidence Gap Coverage

EXP-M2-002 primarily addresses:

```text
High:  Task Complexity, Code/Test Change, Validation Requirement,
       Boundary Autonomy, Target/Revision Scope contrast vs M2-001
Medium: Multi-File Coordination, Context Preparation (plan audit finding)
Low:   Repeated Invocation (deferred)
```

Does **not** address in one run:

```text
Composition with 002/003/004
Cross-repository reuse
Production code revision
Large architecture-sensitive revisions
```

---

## 12. Boundary Autonomy Design

EXP-M2-001 confounded boundary discipline with **Primary Target Only**.

EXP-M2-002 uses **Revision Boundary Discovery**:

```text
CANDIDATE-001 procedure determines In Scope / Out of Scope
after Inspect + Understand + Define Revision Boundary.

Do NOT predefine exact file list in Stage C1.
```

Expected discovery space (not a commitment):

```text
Likely in scope: tests/domain/ modules tied to T-04–T-07 entity acceptance
Possible in scope: shared test helpers within tests/domain/ if needed
Out of scope unless defect proven: src/ai_context/domain/ production models
```

---

## 13. Experiment Safety Boundary

```text
Safety Boundary (hard limits — experiment safety):

Allowed area:
  TASK-002 domain contract test completion for enum entity acceptance
  tests/domain/ and directly related test-only artifacts

Forbidden:
  Domain model / architecture redesign
  New product features (CLI init, analyzers, .ai-context generation)
  Repository-wide refactor or unrelated cleanup
  MILESTONE-001 design or closeout body rewrites
  Asset packaging (SKILL.md) or lifecycle promotion
  src/ changes unless a genuine implementation defect is proven
```

```text
Safety Boundary ≠ Revision Boundary
Revision Boundary is discovered during C2 invocation within the safety envelope.
```

---

## 14. Validation Requirement

Supporting Engineering Validation (not CANDIDATE-002 experiment):

```text
pytest (required — primary)
ruff check tests/ (and src/ if touched)
mypy src (if src/ touched — expected unnecessary)
git diff --check
```

```text
Validation ≠ Automatic CANDIDATE-002 Experiment
CANDIDATE-002 is NOT co-evaluated.
```

---

## 15. Experiment Hypothesis

```text
If CANDIDATE-001 is applied to a medium-complexity targeted test-contract
revision (enum entity-level acceptance gap) with Revision Boundary Discovery
and no Primary Target Only file lock,

then the procedure should provide observable value in boundary discovery,
revision planning, scope control, and traceability to the test plan,

while requiring meaningful pytest validation,

without needing experiment-specific single-file constraints
to perform its core responsibility.
```

Falsifiable: procedure may show **no meaningful value** beyond parametrized tests an engineer would add ad hoc.

---

## 16. Expected Positive Signals

```text
Revision boundary discovered without predetermined file list
Test plan rows T-04–T-07 mapped to concrete tests
Multi-file test updates stay within discovered boundary
pytest passes after revision
Traceability from finding → plan → tests → disposition
Define Boundary step prevents src/ or docs drive-by changes
```

---

## 17. Potential Negative Signals

```text
Parametrized tests duplicate test_enums.py with no new assurance
Procedure overhead dominates a mechanical test addition
Boundary discovery collapses to “edit all domain tests anyway”
Human defines entire scope before Inspect (procedure skipped)
Validation adaptation unclear (same 002-skip question as M2-001 on test-only work)
```

---

## 18. Failure Signals (pre-execution)

```text
Boundary cannot be determined within safety envelope
Revision scope expands into production redesign
Human performs core procedure without using bound/plan steps
Procedure adds no observable structure vs ad-hoc test authoring
Tests added but do not map to stated plan rows
pytest/regression failures not resolved within bounded revision
Task reveals architecture change need → STOP / ESCALATE (out of 001 scope)
```

```text
Failure Signal ≠ Automatic Asset Failure
```

---

## 19. Experiment Contrast with EXP-M2-001

| Dimension | EXP-M2-001 | EXP-M2-002 |
|---|---|---|
| Task type | Docs hygiene | Test contract completion |
| Complexity | Low | Medium |
| Target scope | Pre-known single block | Known finding; scope discovered |
| File count | 1 primary | Multiple (expected under tests/domain/) |
| Revision type | Markdown pointer | Parametrized tests |
| Validation | Diff review | pytest (+ ordinary static checks) |
| Boundary constraint | Primary Target Only | Revision Boundary Discovery |
| Information gain | Baseline procedure trace | Complexity, test/code, autonomy, validation |

```text
Complementary Evidence — not Duplicate Evidence.
```

---

## 20. Experiment Isolation

```text
Primary Validation Subject: CANDIDATE-001 only

NOT co-evaluated:
  CANDIDATE-002, 003, 004
  Composition, Skill packaging

Ordinary pytest/ruff may be used — Supporting Engineering Validation only.
```

---

## 21. Milestone Consistency Finding

Current MILESTONE-002 planned stages (§5) list generic **Stage C — Validation Evidence Review** while executed sequence is **B1–B3 per experiment + C1 gap/selection**.

| Finding | Classification |
|---|---|
| Evidence-driven B→C1 flow matches validation mission | **No Change Required** (substance) |
| §5 stage names do not list B1/B2/B3/C1 explicitly | **Minor Plan Clarification Needed** (documentation only; not blocking) |
| §2 “must NOT modify MILESTONE-001 artifacts” vs B2 M1 edit | **Minor Plan Clarification Needed** — clarify historical exception in future milestone doc edit, not in C1 execution |

```text
No milestone architecture redesign in Stage C1.
MILESTONE-002.md updated for status only.
```

---

## 22. Stage C1 Conclusion

```text
Selection Decision: SELECTED

Experiment: EXP-M2-002
Asset:      CANDIDATE-001 (Single Asset)
Task:       Domain Enum Entity-Level Test Plan Completion

Evidence gaps explicitly identified; information gain requires contrast
with EXP-M2-001 (test/code, medium complexity, boundary discovery, pytest).

Revision Boundary: To be discovered during Stage C2 invocation.
Safety Boundary:   tests/domain/ contract completion; no redesign.

EXP-M2-002: SELECTED — NOT EXECUTED
CANDIDATE-001: VALIDATION_READY (unchanged)
Final asset disposition: NONE
```

Recommended next step (pending authorization):

```text
Stage C2 — EXP-M2-002 Experimental Invocation
```

---

## End of Stage C1

```text
Document: 05-stage-c1-evidence-gap-and-second-experiment-selection.md
Experiment selected: EXP-M2-002
Experiment executed: NO
```

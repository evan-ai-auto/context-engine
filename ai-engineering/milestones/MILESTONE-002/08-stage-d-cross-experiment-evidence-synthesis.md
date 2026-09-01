# MILESTONE-002 Stage D — Cross-Experiment Evidence Synthesis

## 1. Synthesis Scope

```text
Synthesize evidence patterns across EXP-M2-001 and EXP-M2-002.
```

| In scope | Out of scope |
|---|---|
| Cross-experiment comparison and pattern classification | Asset promotion / rejection |
| Repeated vs single-experiment signals | SKILL packaging |
| Alternative explanations and evidence gaps | Asset composition validation |
| Evidence sufficiency for disposition review | New experiment execution |
| Gap closure vs Stage C1 | Portfolio expansion |

Sources synthesized:

```text
03-stage-b2-exp-m2-001-experimental-invocation.md
04-stage-b3-exp-m2-001-evidence-and-assessment.md
05-stage-c1-evidence-gap-and-second-experiment-selection.md
06-stage-c2-exp-m2-002-experimental-invocation.md (+ C2 Revision-001)
07-stage-c3-exp-m2-002-evidence-and-assessment.md
05-candidate-001-targeted-engineering-revision.md (design reference)
```

```text
Both experiments: Single Asset — CANDIDATE-001
Both outcomes: MIXED EVIDENCE (individual assessments)
CANDIDATE-001 lifecycle: VALIDATION_READY (unchanged)
```

---

## 2. Experiment Profiles

Verified against repository records:

### EXP-M2-001

| Field | Value |
|---|---|
| Task | Post-closeout Future Transition Pointer Hygiene |
| Complexity | Small |
| Revision type | Documentation (markdown) |
| Scope | Single-file (`MILESTONE-001/MILESTONE-001.md`) |
| Boundary mode | **Primary Target Only** (external file lock) |
| Validation | Diff inspection; ordinary markdown review |
| Dependency (002) | Not tested — adaptation to diff review |
| Outcome | MIXED EVIDENCE |

### EXP-M2-002

| Field | Value |
|---|---|
| Task | Domain Enum Entity-Level Test Plan Completion |
| Complexity | Medium |
| Revision type | Test-focused engineering revision |
| Scope | Multi-file (4 entity test modules, discovered) |
| Boundary mode | **Revision Boundary Discovery** |
| Validation | pytest + ruff + diff-check (Supporting Engineering Validation) |
| Validation Requirement Determination | **Observed** |
| Dependency (002) | Not tested — experiment isolation |
| Outcome | MIXED EVIDENCE |

```text
Profiles are complementary by design (C1 information-gain objective).
Neither experiment tested production src/ changes or dependency delegation.
```

---

## 3. Synthesis Method

```text
Experiment-Level Evidence (B3, C3)
        ↓
Cross-Experiment Comparison
        ↓
Repeated + Single-Experiment + Context-Dependent Signals
        ↓
Alternative Explanations
        ↓
Evidence Gap Closure (vs C1)
        ↓
Evidence Sufficiency Assessment
        ↓
Combined Evidence Conclusion
```

Signal classification labels:

```text
REPEATED POSITIVE SIGNAL | SINGLE-EXPERIMENT POSITIVE SIGNAL
REPEATED LIMITATION | SINGLE-EXPERIMENT LIMITATION
CONTRADICTORY SIGNAL | NOT COMPARABLE | NOT TESTED
```

Evidence strength per claim:

```text
DIRECT OBSERVATION | SUPPORTED INFERENCE | WEAK INFERENCE | NOT ESTABLISHED
```

---

## 4. Cross-Experiment Comparison

High-level contrast:

| Dimension | EXP-M2-001 | EXP-M2-002 | Comparable? |
|---|---|---|---|
| Task authenticity | Strong — stale pointer | Strong — plan↔test gap | Yes |
| Finding verification | Inspect confirmed staleness | Inspect table T-04–T-07 | Yes (depth differs) |
| Boundary | External lock; written bound | Discovered; exclusions explicit | Partially |
| Multi-file | Not tested | 4 files coordinated | No |
| Validation requirement | Implicit (docs path) | Explicit YES recorded | Partially |
| Dependency delegation | Not tested | Not tested | Yes (both NOT TESTED) |
| Procedure overhead | Experiment docs heavy | Experiment docs heavy | Yes |
| Failure signals | None observed | None observed | Yes |

---

## 5. Task Authenticity

**EXP-M2-001:** Real stale Future Transition guidance after MILESTONE-002 existed; verified in git diff (B3 §3).

**EXP-M2-002:** Real TASK-002 test-plan traceability gap; pre-existing plan and tests; gap independent of MILESTONE-002 (C3 §4).

**Classification:** **Repeated Positive Signal**

Both tasks were authentic repository findings, not artificial validation tasks. EXP-M2-002 relied more on pre-existing test-plan structure (T-04–T-07 rows), which increases traceability but also means authenticity partially overlaps with **Pre-existing Planning** as alternative explanation.

**Attribution:** N/A for authenticity itself. **Confidence:** High.

---

## 6. Finding Verification

**EXP-M2-001:** Inspect confirmed stale pointer before edit; boundary written before execution (B2 §5–§9).

**EXP-M2-002:** Inspect produced per-plan-row table; Task Verification CONFIRMED before modification (C2 §5; C3 §5).

**Classification:** **Repeated Positive Signal** (procedural behavior)

Verification was non-trivial in M2-002 (multi-row audit); lighter in M2-001 (single known finding). Both influenced subsequent scope.

**Attribution to engineering outcome:** Moderate (Low–Moderate confidence). Procedure repeated ≠ procedure uniquely effective.

---

## 7. Inspection Before Modification

**EXP-M2-001:** Inspect Context step executed; confirmed staleness vs closeout integrity (B2).

**EXP-M2-002:** Inspect compared plan rows to entity tests; clarified gap type (entity traceability vs enum-class absence) (C2 §5–§6).

**Classification:** **Moderate Repeated Signal**

Inspection was consistently performed and influenced execution in both runs. M2-002 inspection was more substantive; M2-001 finding was largely pre-selected in B1 — reducing discovery independence.

**Alternative explanations:** B1 context reduced M2-001 inspect novelty; clear test plan made M2-002 inspect tractable.

**Confidence:** Moderate.

---

## 8. Revision Boundary

**EXP-M2-001:** Boundary written under **Primary Target Only** — external constraint on which file to edit; 12-final explicitly excluded (B2 §9–§10).

**EXP-M2-002:** **Revision Boundary Discovery** — four files included, three related artifacts excluded with rationale; list emerged during Define Boundary (C2 §7; C3 §6).

**Classification:** **Context-Dependent Evidence** — NOT a Repeated Positive Signal

M2-001 observed boundary behavior under external file lock. M2-002 explicitly exercised discovery and exclusion reasoning. These test different boundary evidence types.

**Synthesis:** Combined evidence supports that explicit boundary recording occurred in both experiments. Only M2-002 supports boundary **discovery** under softer constraints. M2-001 boundary discipline attribution remains confounded by Primary Target Only (B3 §7).

**Confidence:** Moderate for recording; Moderate for discovery value (M2-002 only).

---

## 9. Scope Discipline

**EXP-M2-001:** Single Future Transition block only; 12-final untouched; no portfolio rewrite (git verified).

**EXP-M2-002:** tests/domain/ only (4 files); src/ unchanged; no test_enums rewrite or shared helper (git 630e652).

**Classification:** **Repeated Positive Signal** (observed behavior consistency)

**Common alternative explanations:** Strong experiment constraints; experienced executor; task simplicity (M2-001 especially); repository structure (M2-002 plan-row mapping).

**Attribution to CANDIDATE-001 alone:** Moderate (Low–Moderate). Consistency of bounded outcomes does not prove exclusive procedure causality.

**Confidence:** Moderate.

---

## 10. Planning

**EXP-M2-001:** Lightweight plan — update pointer, preserve historical note; execution matched (B2 §11).

**EXP-M2-002:** Plan mapped T-04–T-07 to four parametrized functions; execution matched; mechanical but multi-file (C2 §8; C3 §8).

**Classification:** **Context-Dependent Procedural Evidence**

Planning was lightweight in M2-001 and more meaningful in M2-002. Both produced observable plan→execution traceability. Value scales with task complexity — not a flat Repeated Positive at equal strength.

**Confidence:** Moderate.

---

## 11. Execution Discipline

**EXP-M2-001:** Inspect → Understand → Bound → Plan → Execute → Validate → Report → Stop (B2 §12).

**EXP-M2-002:** Same chain; validation requirement and supporting validation explicitly recorded (C2 §9).

**Classification:** **Repeated Positive Signal** (procedure chain reproducibility)

This is among the strongest repeated signals: the CANDIDATE-001 procedure reference was applied with documented step order in both experiments.

**Distinction maintained:** Repeated Process Behavior ≠ Repeated Engineering Outcome Improvement.

**Confidence:** High for behavior; Moderate for outcome attribution.

---

## 12. Stop Discipline

**EXP-M2-001:** 12-final postscript recorded as follow-up, not edited; stop after report (B2 §18).

**EXP-M2-002:** No src/ changes; no shared helper; CT-01/CT-02 recorded but not acted on (C2 §10, §19).

**Classification:** **Repeated Positive Signal**

Unrelated improvements were resisted in both experiments.

**Alternative explanations:** Experiment constraints; task boundedness; executor judgment.

**Confidence:** Moderate.

---

## 13. Human Intervention

| Experiment | Key interventions | Classification |
|---|---|---|
| EXP-M2-001 | Boundary judgment; scope refusal (12-final); skip 002 gate | Normal judgment + experiment constraint |
| EXP-M2-002 | Parametrize pattern; test_enums exclusion; 002 isolation | Normal judgment + boundary step + experiment constraint |

**Classification:** **Repeated Pattern** — human judgment within procedure structure; no Human Substitution for core Inspect/Bound/Plan chain observed in either run.

**Cross-experiment:** Human intervention did not decrease; complexity in M2-002 increased boundary-step reasoning but did not bypass procedure.

**Confidence:** High.

---

## 14. Procedure Overhead

**EXP-M2-001:** Asset procedure chain acceptable; experiment documentation dominated wall time vs tiny edit (B3 §9, §18).

**EXP-M2-002:** Asset chain proportionate; experiment + invocation documentation still dominates vs ~33 lines of test code (C3 §10).

**Classification:** **Repeated Limitation** (experiment ceremony) + **Context-Dependent** (asset chain scales better in M2-002)

```text
Procedure Core (001 design steps): Stable, acceptable in both runs
Experiment Ceremony (B/C stage records): High relative to engineering delta in both runs
```

Do NOT attribute experiment documentation burden to CANDIDATE-001 design without direct justification — both assessments separate asset vs experiment cost.

**Confidence:** Moderate.

---

## 15. Validation Requirement Determination

**EXP-M2-001:** Validation via diff review; formal 002 gate skipped; adaptation documented (B2 §12–§14). Requirement determination less explicitly separated (pre-Revision-001 framing).

**EXP-M2-002:** Validation Required = YES explicitly recorded after test changes (C2 §13–§14; C3 §12). Dependency request and 002 invocation: **NOT TESTED** (C2 Revision-001).

**Classification:**

| Category | EXP-M2-001 | EXP-M2-002 | Synthesis |
|---|---|---|---|
| Validation Requirement Determination | Partially observed (docs path) | **Observed** | Partially evidenced across both |
| Dependency Request | NOT TESTED | NOT TESTED | **NOT TESTED** |
| CANDIDATE-002 Invocation | NOT TESTED | NOT TESTED | **NOT TESTED** |
| Supporting Engineering Validation | Observed (diff) | Observed (pytest/ruff) | Repeated Positive (engineering only) |

```text
Do NOT synthesize: "CANDIDATE-001 validation workflow validated"
Dependency delegation: Not tested in either experiment.
```

**Confidence:** High for separation; Moderate for requirement-determination repeatability.

---

## 16. Supporting Engineering Validation

**EXP-M2-001:** Diff inspection; markdown consistency; git status clean (B2).

**EXP-M2-002:** pytest 65 passed; ruff clean; git diff --check passed (C2 §14D).

**Classification:** **Repeated Positive Signal** (engineering validation occurred)

Both produced sufficient evidence for revision correctness within task class.

**Attribution boundary maintained:**

```text
Engineering Revision Validation ≠ Asset Composition Validation
Supporting Validation Success ≠ Validation Dependency Success
```

**Confidence:** High.

---

## 17. Experiment Isolation

**EXP-M2-001:** CANDIDATE-001 only; 002/003/004 not co-evaluated (B2 §8).

**EXP-M2-002:** CANDIDATE-001 only; 002 intentionally not invoked; C2 Revision-001 corrected attribution (C2 §14–§15).

**Classification:** **Repeated Positive Signal** (isolation preserved) + **Repeated Limitation** (realism tradeoff)

Isolation protects single-asset attribution but prevents dependency and composition evidence in both runs.

**Confidence:** High.

---

## 18. Failure Signal Comparison

| Failure Signal | EXP-M2-001 | EXP-M2-002 | Cross-Experiment Interpretation |
|---|---|---|---|
| Boundary cannot be determined | Not Observed | Not Observed | Consistent — no signal in either run (n=2) |
| Scope expands to production redesign | Not Observed | Not Observed | Consistent — bounded in both |
| Human substitutes core procedure | Not Observed | Not Observed | Consistent — bound/plan used |
| No observable structure vs ad-hoc | Inconclusive | Inconclusive | Consistent — traceability added; value task-dependent |
| Plan-test / requirement mismatch | Not Observed | Not Observed | Consistent — mapping maintained |
| Validation failure unresolved | Not Observed | Not Observed | **Not tested** — no failure scenario in either run |
| Architecture change required | Not Observed | Not Observed | Consistent — out of scope for both tasks |

```text
Not Observed ≠ Proven Absent.
No failure-recovery behavior exercised in either experiment.
```

---

## 19. Evidence Limitations

### Repeated limitations (both experiments)

```text
Single repository
Single executor (same operator/experimenter — bias persists)
Small experiment count (n=2)
No production src/ revision
No failure recovery scenario
No CANDIDATE-002 dependency delegation
No asset composition (001+002+003+004)
No long-running workflow
Experiment isolation reduces realism for dependency behavior
Causality not isolatable from constraints and executor skill
```

### Reduced by EXP-M2-002 (vs M2-001 alone)

```text
Docs-only context exclusivity
Single-file scope exclusivity
Primary Target Only boundary confound (partially)
Medium-complexity / test-code absence
Multi-file coordination absence
Explicit validation requirement determination absence
```

### Still open after both experiments

```text
Production code revisions
Failure recovery within boundary
Dependency REQUEST and CANDIDATE-002 execution
Portfolio composition
Cross-executor reproducibility
Cross-repository portability
Repeated invocation overhead trend
Packaged Skill vs design-doc adherence
Optimal ceremony outside experiment framing
```

---

## 20. Cross-Experiment Evidence Matrix

| Dimension | EXP-M2-001 | EXP-M2-002 | Pattern Classification | Confidence |
|---|---|---|---|---|
| Task Authenticity | Strong | Strong | Repeated Positive | High |
| Finding Verification | Observed | Observed (deeper) | Repeated Positive | Moderate |
| Inspection | Pre-selected finding | Plan↔test audit | Moderate Repeated | Moderate |
| Boundary | External lock + record | Discovery + exclusions | Context-Dependent | Moderate |
| Scope Discipline | Single-file bounded | Multi-file bounded | Repeated Positive | Moderate |
| Planning | Lightweight | Multi-file mapped | Context-Dependent | Moderate |
| Execution Discipline | Chain followed | Chain followed | Repeated Positive | High |
| Stop Discipline | Follow-ups deferred | Expansions excluded | Repeated Positive | Moderate |
| Human Intervention | Judgment within procedure | Judgment within procedure | Repeated Pattern | High |
| Procedure Overhead | Ceremony heavy | Ceremony heavy | Repeated Limitation | Moderate |
| Validation Requirement | Partially observed | Observed | Context-Dependent / Partial | Moderate |
| Dependency Delegation | Not tested | Not tested | NOT TESTED | High |
| Supporting Validation | Diff review | pytest/ruff | Repeated Positive | High |
| Failure Signals | None observed | None observed | Inconclusive (no failure path) | Moderate |
| Limitations | Single context | Overlapping + some reduced | Repeated Limitation | High |

No numerical scores assigned.

---

## 21. Repeated Evidence Patterns

### Pattern: Inspection Before Modification

**EXP-M2-001:** Inspect confirmed stale Future Transition before edit (B2 §5).

**EXP-M2-002:** Inspect table confirmed T-04–T-07 entity gap before edit (C2 §5).

**Classification:** Repeated Procedure Signal

**Alternative explanations:** Pre-existing finding clarity (M2-001); pre-existing test plan (M2-002); executor skill.

**Attribution strength:** Moderate | **Confidence:** Moderate

---

### Pattern: Explicit Revision Boundary Recorded Before Execution

**EXP-M2-001:** In/Out scope written; 12-final excluded (B2 §9).

**EXP-M2-002:** Four files in scope; three exclusions with rationale (C2 §7).

**Classification:** Repeated Positive Signal (recording) — discovery value M2-002 only

**Alternative explanations:** Primary Target Only (M2-001); plan-row mapping (M2-002); experiment framing.

**Attribution strength:** Moderate | **Confidence:** Moderate

---

### Pattern: Procedure Chain Executed in Documented Order

**EXP-M2-001:** Full chain through Stop (B2 §12).

**EXP-M2-002:** Full chain; validation steps explicitly separated post Revision-001 (C2 §9).

**Classification:** Repeated Positive Signal

**Alternative explanations:** Experiment protocol requirements; experimenter familiarity after M2-001.

**Attribution strength:** Moderate–Strong for reproducibility | **Confidence:** High

---

### Pattern: Scope and Stop Discipline

**EXP-M2-001:** Minimal diff; optional postscript deferred (B2; B3).

**EXP-M2-002:** tests/ only; no src/ or drive-by (git; C2 §10).

**Classification:** Repeated Positive Signal (behavioral consistency)

**Alternative explanations:** Task simplicity; experiment constraints; executor skill.

**Attribution strength:** Moderate | **Confidence:** Moderate

---

### Pattern: Experiment Documentation Overhead Dominates Engineering Delta

**EXP-M2-001:** B2/B3 record length >> 3-line edit (B3 §9).

**EXP-M2-002:** C2 record + stages >> ~33 lines of tests (C3 §10).

**Classification:** Repeated Limitation (experiment ceremony, not necessarily asset design)

**Attribution strength:** N/A | **Confidence:** Moderate

---

### Pattern: CANDIDATE-002 Dependency Not Tested

**EXP-M2-001:** 002 gate skipped; diff review used (B2 §12).

**EXP-M2-002:** 002 not invoked; isolation + Revision-001 attribution (C2 §14).

**Classification:** Repeated Limitation / NOT TESTED

**Attribution strength:** None for dependency claims | **Confidence:** High

---

## 22. Single-Experiment Evidence

### Revision Boundary Discovery (EXP-M2-002 only)

**Where observed:** Define Boundary step; four files discovered; test_enums.py, test_project_context.py, shared helper excluded (C2 §7; C3 §6).

**Why only one experiment:** EXP-M2-001 used Primary Target Only — discovery not meaningfully testable.

**Supports:** CANDIDATE-001 can structure inclusion/exclusion decisions on related artifacts under softer constraints.

**Does not support:** Universal boundary discovery without human/plan support; production-revision discovery.

**Strengthening experiment:** Medium-complexity src/ revision without predetermined file list.

---

### Multi-File Coordination (EXP-M2-002 only)

**Where observed:** Four entity test modules; T-04–T-07 plan-row mapping (C3 §9).

**Why only one experiment:** M2-001 was single-file by design.

**Supports:** Plan can coordinate multiple files before execution; mechanical but traceable.

**Does not support:** Complex cross-file dependency coordination.

**Strengthening experiment:** Multi-file production revision with interaction between changes.

---

### Validation Requirement Determination — Explicit (EXP-M2-002 stronger)

**Where observed:** Validation Required = YES recorded after test changes (C2 §13; C3 §12).

**Why uneven:** M2-001 docs-only path had implicit validation; M2-002 made determination explicit post Revision-001.

**Supports:** Requirement determination can be separated from validation execution in the record.

**Does not support:** Full validation workflow including 002 delegation.

**Strengthening experiment:** Non-isolated run with 002 REQUEST documented (composition stage).

---

## 23. Context-Dependent Signals

### Planning value scales with task complexity

M2-001 plan was trivial; M2-002 plan added multi-file coordination value. Same procedure steps, different observed utility.

### Boundary evidence type differs by experiment design

M2-001: discipline under external lock. M2-002: discovery under softer constraints. Cannot merge into one boundary conclusion.

### Validation path differs by artifact type

M2-001: diff/markdown review sufficient for docs. M2-002: pytest/ruff meaningful for tests. Supporting validation is context-appropriate — not comparable as identical signal.

### Procedure overhead relative value

Asset chain overhead more justified in M2-002 (medium task) than M2-001 (tiny fix) — aligns with B3 negative validation signal on trivial tasks under full ceremony.

### Overall experiment outcomes both MIXED EVIDENCE — consistent, not contradictory

Both positive and limiting factors present; second experiment broadened evidence without flipping to unqualified positive.

---

## 24. Combined Alternative Explanations

| Category | Persists across both? | Reduced by M2-002? | Assessment |
|---|---|---|---|
| Executor Skill | **Yes** — same executor | No | Dominant persistent bias |
| Task Simplicity | Partially — M2-002 less simple | Partially | Reduced but not eliminated |
| Experiment Constraints | **Yes** | No | Strong confound for scope discipline |
| Repository Structure | **Yes** — clear repo layout | Partially | Plan-row mapping helped M2-002 |
| Pre-existing Planning | M2-001 high; M2-002 moderate | — | M2-002 still relied on TASK-002 plan |
| Procedure Structure | Plausible in both | — | Cannot eliminate without control run |

```text
Cross-experiment repetition does NOT eliminate executor skill bias.
Two experiments with the same operator increase procedural reproducibility
observations but not independent replication.
Task variation (docs → tests, single → multi-file) partially reduces
"docs-only" and "single-file" alternative explanations.
Procedure structure remains a plausible co-explanation for all positive signals.
```

**Dominant persistent alternatives:** Executor skill + experiment constraints.

**Partially reduced alternatives:** Task simplicity; docs-only exclusivity; single-file exclusivity.

---

## 25. Evidence Gap Closure Analysis

Stage C1 gaps vs combined evidence:

| Stage C1 Evidence Gap | EXP-M2-002 Impact | Current Status |
|---|---|---|
| Task Complexity Gap | Medium task executed | **Reduced** |
| Target Complexity Gap | Softer boundary constraints | **Reduced** |
| Revision Scope Gap | Multi-file bounded revision | **Reduced** |
| Multi-File Coordination Gap | 4-file plan mapping | **Reduced** |
| Code / Test Change Gap | tests/domain/ modified | **Reduced** |
| Validation Requirement Gap | YES determination observed | **Partially Reduced** (execution/delegation not tested) |
| Boundary Autonomy Gap | Discovery without file lock | **Reduced** |
| Context Preparation Gap | Plan↔test audit in Inspect | **Partially Reduced** |
| Repeated Invocation Gap | Still n=2 sequential runs | **Open** |
| Production src/ revision | Not attempted | **Open** |
| Failure recovery | Not attempted | **Open** |
| Dependency composition | Not attempted | **Open** |
| Cross-executor replication | Same executor | **Open** |

```text
EXP-M2-002 materially reduced the high-priority gaps that motivated its selection.
Major gaps remain: dependency, composition, failure, production code, independent replication.
No gap marked Closed — Reduced or Partially Reduced only.
```

---

## 26. Evidence Sufficiency Assessment

| Dimension | Classification | Reasoning |
|---|---|---|
| Behavioral Evidence | Partially Sufficient | Repeated procedure signals across two complementary contexts |
| Complexity Coverage | Partially Sufficient | Small docs + medium tests; no production |
| Task Diversity | Partially Sufficient | Two shapes; same asset; same repo |
| Attribution Strength | Partially Sufficient | Consistent associations; causality unproven |
| Failure Coverage | **Insufficient** | No failure path in either experiment |
| Dependency Coverage | **Insufficient** | 002 never tested |
| Reproducibility | **Insufficient** | Same executor; n=2 |

```text
Is evidence sufficient to proceed to Asset Disposition Review?

Answer: YES, WITH MATERIAL LIMITATIONS
```

**Rationale:**

Two prospective single-asset experiments on real tasks produced reproducible procedure-behavior signals, complementary context coverage (docs/single-file vs tests/multi-file/boundary-discovery), and calibrated MIXED EVIDENCE outcomes. EXP-M2-002 addressed the highest-priority gaps identified in C1. Material limitations — dependency delegation untested, no failure scenarios, no production revisions, single executor — must constrain any disposition decision and preclude global VALIDATED conclusion without further evidence or explicit acceptance of limitations.

```text
Evidence sufficiency ≠ asset validated.
This assessment only determines whether the evidence base is mature enough
for a disposition decision stage — not the disposition itself.
```

---

## 27. Combined Evidence Conclusion

### Strongest Repeated Signals

```text
1. CANDIDATE-001 procedure chain (Inspect → Bound → Plan → Execute →
   Validate → Report → Stop) reproducibly applied across both experiments.
2. Explicit revision boundary recorded before execution in both runs.
3. Scope and stop discipline — bounded revisions, unrelated work deferred.
4. Task authenticity — real repository findings in both cases.
5. Supporting Engineering Validation produced for each revision type.
6. Experiment isolation preserved — single-asset attribution maintained.
```

### Strongest Single-Experiment Signals

```text
1. Revision Boundary Discovery with explicit related-artifact exclusions (M2-002).
2. Multi-file plan-to-execution coordination (M2-002).
3. Validation Requirement Determination explicitly recorded (M2-002).
4. Primary Target Only boundary under external lock (M2-001 — different evidence type).
```

### Important Context Dependencies

```text
- Boundary evidence differs: external lock (M2-001) vs discovery (M2-002).
- Planning and procedure value appear to scale with task complexity.
- Validation modality follows artifact type (diff vs pytest).
- Experiment ceremony overhead dominates both runs relative to engineering delta.
```

### Dominant Alternative Explanations

```text
Executor skill and experiment constraints persist across both runs and are NOT
eliminated by cross-experiment repetition. Pre-existing planning (especially
TASK-002 test plan) explains part of M2-002 success. Procedure structure is
associated with positive signals but causality remains unproven.
```

### Major Remaining Evidence Gaps

```text
- CANDIDATE-001 → CANDIDATE-002 dependency REQUEST and execution
- Asset composition (001+002+003+004)
- Production src/ revision under 001 procedure
- Failure recovery within bounded revision
- Cross-executor / cross-repository replication
- Repeated invocation overhead trend
- Packaged Skill vs design-doc procedure adherence
```

### Overall Evidence Pattern

```text
MIXED EVIDENCE (combined)

Two complementary single-asset experiments expand behavioral and contextual
coverage for CANDIDATE-001 beyond either run alone. Repeated procedure signals
support partial evidence for structured revision guidance. Material limitations
and dominant alternative explanations prevent global validation or rejection.
Individual experiment outcomes remain MIXED EVIDENCE; synthesis does not upgrade
to unqualified positive.
```

### Evidence Sufficiency

```text
YES, WITH MATERIAL LIMITATIONS

Proceed to Asset Disposition Review is supported, subject to explicit
acknowledgment of dependency, failure, production-code, and replication gaps.
```

---

## 28. Synthesis Boundary

```text
This stage synthesizes evidence from EXP-M2-001 and EXP-M2-002.

It does NOT:

  Promote CANDIDATE-001.
  Reject CANDIDATE-001.
  Package CANDIDATE-001.
  Validate CANDIDATE-001 globally.
  Validate dependency composition.
  Create new experiments.

CANDIDATE-001 lifecycle: VALIDATION_READY (unchanged).

Evidence Base: Cross-Experiment Synthesis COMPLETED
Evidence Sufficiency: Assessed — YES, WITH MATERIAL LIMITATIONS
Asset Disposition: NOT YET PERFORMED

The next authorized stage may perform:
  Evidence Sufficiency Review and Asset Disposition Decision.
```

---

## End of Stage D Synthesis

```text
Document: 08-stage-d-cross-experiment-evidence-synthesis.md
Experiments synthesized: EXP-M2-001, EXP-M2-002
Combined pattern: MIXED EVIDENCE
Evidence sufficiency: YES, WITH MATERIAL LIMITATIONS
Asset disposition: NONE (deferred)
```

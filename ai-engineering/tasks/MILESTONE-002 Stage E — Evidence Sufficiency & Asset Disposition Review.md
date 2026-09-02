# MILESTONE-002 Stage E — Evidence Sufficiency & Asset Disposition Review

## Execution Mode

You are executing:

**MILESTONE-002 — Stage E**

Repository:

```text
context-engine
```

Objective:

Perform the formal **Evidence Sufficiency & Asset Disposition Review** for `CANDIDATE-001`.

This stage must determine whether the evidence accumulated during MILESTONE-002 is sufficient to make a lifecycle disposition decision for `CANDIDATE-001`.

This is a **review and decision stage**.

Do not prematurely implement new Skills, Workflows, Agents, or production automation.

---

# 1. Core Principle

Maintain the following distinctions throughout the review:

```text
Evidence Sufficiency
        ≠
Asset Quality
        ≠
Asset Validation
        ≠
Asset Promotion
```

In particular:

- sufficient evidence to make a disposition decision does NOT mean the asset is universally validated;
- passing supporting engineering checks does NOT prove the candidate behavior itself;
- successful execution in one experiment does NOT establish generality;
- repeated observations do NOT automatically establish causality;
- human intervention must not be silently counted as autonomous capability;
- absence of failure does NOT prove robustness;
- a useful experimental result does NOT automatically justify production promotion.

The decision must be evidence-driven.

Do not manufacture confidence.

---

# 2. Mandatory Reading

Before modifying anything, inspect the repository and read the authoritative artifacts related to MILESTONE-002.

At minimum, locate and read:

```text
MILESTONE-002.md
```

The Stage A framework.

The Stage B1 experiment-selection record.

The Stage B2 EXP-M2-001 invocation record.

The Stage B3 EXP-M2-001 assessment.

The Stage C1 evidence-gap analysis.

The Stage C2 EXP-M2-002 invocation record.

The Stage C2 Revision-001 attribution correction.

The Stage C3 EXP-M2-002 assessment.

The Stage D cross-experiment evidence synthesis.

The authoritative definition/design of:

```text
CANDIDATE-001
```

Also inspect:

- candidate registry / lifecycle documentation;
- pattern definitions referenced by CANDIDATE-001;
- relevant project / architecture documentation;
- existing MILESTONE-002 decision records;
- existing naming conventions for Stage assessment documents.

Do not assume filenames.

Discover the actual repository structure first.

---

# 3. Objective

Answer the following questions.

## Question A — Is the current evidence sufficient to make a disposition decision?

Possible results:

```text
SUFFICIENT
SUFFICIENT_WITH_LIMITATIONS
INSUFFICIENT
```

This question is about whether the evidence is sufficient to decide what should happen next.

It is NOT asking whether CANDIDATE-001 is universally validated.

---

## Question B — What is the current disposition of CANDIDATE-001?

Select exactly one:

```text
PROMOTE
PROMOTE_WITH_CONDITIONS
RETAIN_AS_EXPERIMENTAL
REQUIRE_MORE_VALIDATION
REVISE_ASSET
REJECT
```

The selected disposition must be justified from Stage D evidence.

Do not choose a disposition merely because:

- tests passed;
- the experiment completed;
- the candidate appears useful;
- the candidate is conceptually attractive.

---

## Question C — What lifecycle state should CANDIDATE-001 enter?

Use the repository's existing lifecycle terminology if one exists.

If lifecycle terminology is not yet formalized, explicitly define the minimal state transition required by this stage without introducing unnecessary lifecycle complexity.

The lifecycle transition must be traceable to the disposition decision.

---

# 4. Evidence Dimensions

Evaluate evidence across the following dimensions.

Create an explicit assessment for each.

## 4.1 Evidence Breadth

Assess:

- number of experiments;
- task diversity;
- repository scope;
- documentation vs implementation work;
- single-file vs multi-file work;
- boundary discovery;
- multi-file coordination;
- validation-related behavior.

Determine whether current evidence is:

```text
STRONG
MODERATE
WEAK
NOT_ESTABLISHED
```

---

## 4.2 Behavioral Repeatability

Determine whether the observed candidate behavior appeared:

```text
REPEATED
PARTIALLY_REPEATED
SINGLE_INSTANCE
NOT_ESTABLISHED
```

Do not infer repeatability merely because two experiments used the same candidate.

Identify exactly which behaviors repeated.

---

## 4.3 Task Diversity

Evaluate whether CANDIDATE-001 has been exercised across meaningfully different engineering tasks.

Consider:

- documentation revision;
- implementation revision;
- multi-file changes;
- boundary discovery;
- validation determination;
- other task classes actually present in the evidence.

Do not count superficial variations as task diversity.

---

## 4.4 Attribution Strength

For each important observed outcome, determine whether it is:

```text
DIRECTLY_OBSERVED
SUPPORTED_INFERENCE
WEAK_INFERENCE
NOT_ESTABLISHED
```

Pay particular attention to the attribution correction introduced during:

```text
Stage C2 Revision-001
```

Do not regress into conflating:

```text
Validation Requirement Determination
```

with:

```text
Validation Dependency Request
```

or:

```text
CANDIDATE-002 Invocation
```

Supporting engineering validation such as:

```text
pytest
ruff
git diff --check
```

must remain separate from candidate invocation evidence.

---

# 5. Validation Coverage

Explicitly evaluate the following.

## 5.1 Candidate Behavior Validation

Was the actual behavior defined by CANDIDATE-001 directly exercised?

Classify:

```text
VALIDATED
PARTIALLY_VALIDATED
OBSERVED_BUT_NOT_VALIDATED
NOT_TESTED
```

---

## 5.2 Failure Coverage

Determine whether the experiments exercised meaningful failure or ambiguity conditions.

Consider:

- missing information;
- ambiguous requirements;
- incomplete repository context;
- conflicting signals;
- validation uncertainty;
- multi-file coordination risks;
- boundary uncertainty.

Classify:

```text
GOOD
PARTIAL
LIMITED
NOT_ESTABLISHED
```

---

## 5.3 Dependency / Composition Coverage

Determine whether the candidate has been shown to operate correctly when dependent on or interacting with other capabilities.

Do not treat mere conceptual dependency references as execution evidence.

Explicitly distinguish:

```text
DEPENDENCY_IDENTIFIED
DEPENDENCY_REQUESTED
DEPENDENCY_INVOKED
DEPENDENCY_SUCCEEDED
DEPENDENCY_FAILURE_TESTED
```

Only claim the states supported by evidence.

---

## 5.4 Human Intervention

Document any human intervention that materially affected the experiments.

Examples:

- manually resolving an ambiguity;
- manually adapting experiment conditions;
- manually selecting files;
- manually correcting an execution issue;
- manually compensating for missing infrastructure.

Do not classify experiment adaptation as autonomous capability.

If the repository already uses the terminology:

```text
Experiment Isolation Adaptation
```

retain that terminology where appropriate.

---

# 6. Reproducibility

Assess whether another engineer or agent could reproduce the experiments from the repository artifacts.

Consider:

- experiment definition;
- execution instructions;
- input conditions;
- expected outputs;
- actual outputs;
- evidence capture;
- decision criteria.

Classify:

```text
HIGH
MEDIUM
LOW
NOT_ESTABLISHED
```

Explain any missing information.

---

# 7. Evidence Sufficiency Matrix

Create a concise decision matrix.

Use dimensions similar to:

| Dimension | Assessment | Evidence | Limitation |
|---|---|---|---|
| Evidence Breadth | | | |
| Behavioral Repeatability | | | |
| Task Diversity | | | |
| Attribution Strength | | | |
| Candidate Validation | | | |
| Failure Coverage | | | |
| Dependency Coverage | | | |
| Human Intervention | | | |
| Reproducibility | | | |

Do not fill the matrix with generic statements.

Every assessment must trace back to actual MILESTONE-002 evidence.

---

# 8. Disposition Decision Rules

Use the following decision logic.

## PROMOTE

Use only if evidence is sufficiently broad, attributable, repeatable, and directly supports the intended reusable capability.

Promotion must NOT be based only on successful tests or successful completion.

If meaningful validation gaps remain, do not use unconditional PROMOTE.

---

## PROMOTE_WITH_CONDITIONS

Use when:

- the candidate demonstrates sufficient value and repeatability for controlled reuse;
- important limitations remain;
- those limitations can be expressed as explicit usage conditions;
- further evidence would improve confidence but does not prevent controlled promotion.

Conditions must be concrete.

Example categories:

```text
scope restriction
task restriction
required human review
validation requirement
dependency requirement
failure handling requirement
```

Do not invent conditions unsupported by evidence.

---

## RETAIN_AS_EXPERIMENTAL

Use when:

- the candidate appears promising;
- evidence is useful;
- but the observed behavior is still too narrow or insufficiently validated for promotion.

This is appropriate when the candidate should remain available as an experimental asset without treating it as a generally reusable production capability.

---

## REQUIRE_MORE_VALIDATION

Use when the candidate's behavior is sufficiently defined but current evidence is inadequate to determine whether it should be retained or promoted.

If selecting this disposition:

- identify exact evidence gaps;
- explain why those gaps materially affect the decision;
- define the smallest useful follow-up experiment;
- do NOT execute that experiment during Stage E.

---

## REVISE_ASSET

Use only if evidence indicates that the candidate definition itself is materially flawed.

Examples:

- incorrect boundaries;
- ambiguous behavior;
- contradictory contract;
- inappropriate abstraction;
- repeated mismatch between intended and observed behavior.

Do not select this merely because validation is incomplete.

---

## REJECT

Use only if evidence indicates that the candidate should not continue in the asset lifecycle.

Do not reject a candidate merely because the evidence is currently insufficient.

---

# 9. Evidence vs Decision

The review must explicitly separate:

```text
Observed Evidence
        ↓
Evidence Interpretation
        ↓
Evidence Sufficiency
        ↓
Disposition Decision
        ↓
Lifecycle Transition
```

Do not collapse these into a single conclusion.

The final document should make it possible for a reviewer to understand:

1. what was observed;
2. what was inferred;
3. what remains unknown;
4. why the evidence is or is not sufficient;
5. why the selected disposition follows.

---

# 10. Contradiction Handling

Review Stage D for contradictions.

For every meaningful contradiction:

1. identify the conflicting evidence;
2. determine whether the contradiction is real or caused by scope differences;
3. determine whether it affects the disposition;
4. document the resolution.

If unresolved contradictions materially affect the decision, do not hide them.

---

# 11. Evidence Gaps

Create a final list of remaining evidence gaps.

Classify each as:

```text
CRITICAL
IMPORTANT
NON_BLOCKING
```

For each gap record:

```text
Gap
Why it matters
Current evidence
What would close the gap
Whether it blocks promotion
```

Do not create speculative gaps merely to make the review appear comprehensive.

---

# 12. Conditions and Restrictions

If disposition is:

```text
PROMOTE_WITH_CONDITIONS
```

define explicit conditions.

Each condition must include:

```text
Condition
Reason
Supporting Evidence
Operational Implication
```

For example:

```text
Condition:
Candidate may only be used for repository-scoped engineering revisions.

Reason:
Current experiments do not establish behavior outside repository-scoped revision tasks.

Supporting Evidence:
Stage D synthesis.

Operational Implication:
Future consumers must not treat the asset as a general-purpose engineering agent.
```

Only use conditions justified by actual evidence.

---

# 13. Follow-Up Experiment Proposal

If additional validation is required, define the smallest experiment capable of addressing the highest-priority evidence gap.

The proposal should include:

```text
Experiment ID
Objective
Evidence Gap Addressed
Input Conditions
Expected Observation
Success Criteria
Failure Criteria
Evidence to Capture
```

Do not execute it.

Stage E is a review stage.

---

# 14. Asset Packaging Rule

Do NOT package CANDIDATE-001 into:

```text
Skill
Workflow
Agent
Production automation
```

during this stage.

Even if the disposition is:

```text
PROMOTE
```

the actual packaging decision belongs to the subsequent lifecycle stage unless existing repository architecture explicitly states otherwise.

Stage E only determines the disposition.

---

# 15. Required Documentation

Create the Stage E assessment using the repository's established documentation naming convention.

Prefer a filename equivalent to:

```text
09-stage-e-evidence-sufficiency-and-asset-disposition.md
```

if consistent with the existing sequence.

The document must contain at least:

```text
# MILESTONE-002 Stage E

## Objective

## Scope

## Authoritative Evidence

## Evidence Sufficiency Assessment

## Evidence Matrix

## Validation Coverage

## Failure Coverage

## Dependency / Composition Coverage

## Human Intervention

## Reproducibility

## Contradictions

## Remaining Evidence Gaps

## Disposition Decision

## Lifecycle Transition

## Conditions / Restrictions

## Follow-Up Validation Proposal

## Final Conclusion
```

Adjust headings only when necessary to match existing repository conventions.

---

# 16. Update MILESTONE-002

Update:

```text
MILESTONE-002.md
```

to record:

- Stage E execution;
- evidence sufficiency result;
- disposition;
- lifecycle transition;
- remaining gaps;
- whether the milestone proceeds to the next stage.

Do not rewrite historical records.

Preserve previous stage conclusions.

---

# 17. Engineering Validation

After documentation changes:

Run the repository's applicable validation commands.

At minimum, where supported:

```bash
pytest
```

```bash
ruff check .
```

```bash
mypy src
```

```bash
git diff --check
```

If any command is unavailable or fails because of an unrelated pre-existing issue:

1. record the exact issue;
2. do not misattribute it to Stage E;
3. do not silently bypass it.

---

# 18. Diff Review

Before completion:

```bash
git status
git diff --stat
git diff
```

Review the complete diff.

Check specifically for:

- accidental modification of previous experiment records;
- unsupported claims;
- attribution regression;
- accidental promotion language;
- hidden validation assumptions;
- unnecessary files;
- unnecessary architecture changes;
- generated artifacts that should not be committed.

---

# 19. Quality Gate

Stage E passes only if:

- [ ] Stage A–D evidence has been reviewed
- [ ] Evidence sufficiency is explicitly classified
- [ ] Evidence dimensions are assessed
- [ ] Candidate validation is distinguished from supporting validation
- [ ] Attribution boundaries are preserved
- [ ] Dependency invocation is not overstated
- [ ] Human intervention is documented
- [ ] Reproducibility is assessed
- [ ] Remaining evidence gaps are explicit
- [ ] Disposition is explicitly selected
- [ ] Disposition is justified from evidence
- [ ] Lifecycle transition is recorded
- [ ] No Skill/Workflow packaging is prematurely performed
- [ ] Follow-up validation is proposed only if necessary
- [ ] MILESTONE-002.md is updated
- [ ] Engineering validation passes or failures are explicitly documented
- [ ] Git diff has been reviewed

---

# 20. Execution Discipline

Follow this sequence:

```text
READ
 ↓
INSPECT
 ↓
SYNTHESIZE
 ↓
ASSESS
 ↓
DECIDE
 ↓
DOCUMENT
 ↓
VALIDATE
 ↓
DIFF REVIEW
 ↓
STOP
```

Do not:

```text
READ
 ↓
IMPLEMENT
 ↓
PACKAGE
```

Do not introduce new product functionality.

Do not refactor unrelated files.

Do not rewrite previous experiment history.

Do not execute a new experiment.

Do not create Skills, Workflows, or Agents.

---

# 21. Final Execution Report

At the end, provide a concise report containing:

```text
MILESTONE-002 Stage E completed.

Evidence Sufficiency:
<value>

Disposition:
<value>

Lifecycle Transition:
<value>

Critical Evidence Gaps:
<list>

Follow-Up Validation Required:
YES / NO

Files Changed:
<list>

pytest:
PASS / FAIL / NOT RUN

ruff:
PASS / FAIL / NOT RUN

mypy:
PASS / FAIL / NOT RUN

git diff --check:
PASS / FAIL

Git Diff Reviewed:
YES / NO
```

Do not claim completion unless the repository changes and validation state have actually been inspected.
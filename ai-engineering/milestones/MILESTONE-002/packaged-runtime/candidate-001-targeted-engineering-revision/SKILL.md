---
name: candidate-001-targeted-engineering-revision
version: 0.1-exp-m2-005
description: >-
  Experimental packaged form of CANDIDATE-001 Targeted Engineering Revision.
  Performs bounded inspect→bound→plan→execute→validate→dispose revisions.
  Use only for MILESTONE-002 EXP-M2-005 packaged runtime experiments.
  Not a production Skill.
experimental: true
milestone: MILESTONE-002
experiment: EXP-M2-005
candidate: CANDIDATE-001
disable-model-invocation: true
---

# CANDIDATE-001 — Targeted Engineering Revision (Experimental Package)

```text
Status: EXPERIMENTAL / NON-PRODUCTION
Source design: ai-engineering/milestones/MILESTONE-001/
              05-candidate-001-targeted-engineering-revision.md
Evidence basis: MILESTONE-002 EXP-M2-001 … EXP-M2-004 (design-doc invocations)
```

## When to use

Use for a **bounded engineering revision** with a known finding or clear acceptance target.

## When not to use

- Feature development / architecture redesign
- Universal “fix everything”
- Tasks without a discoverable revision boundary

## Core procedure (evidence-supported only)

Execute in order:

```text
1. Inspect
2. Understand
3. Define Revision Boundary
4. Plan
5. Execute targeted revision
6. Determine Validation Requirement (YES / NO)
7. If YES → REQUEST CANDIDATE-002 (do not skip determination)
8. Invoke validation / consume Aggregate Validation Evidence
9. Determine Disposition
10. Report
11. Stop
```

Do **not** collapse:

```text
Validation Requirement Determination
        ≠
Validation Request / Invocation
```

## Boundary rules

```text
Default: Primary Target Only for the declared in-scope files.
Do not auto-expand scope because related files were discovered.
If boundary discovery is required, record it explicitly before edits.
```

Out of scope unless explicitly in boundary:

```text
Unrelated cleanup, packaging other candidates, lifecycle promotion,
specification/architecture semantic rewrites
```

## Validation contract

```text
If Validation Required = YES:
  REQUEST CANDIDATE-002 (Repository Tooling Validation Gate)
  Preferred gates when repository supports them: Unit Tests, Lint, Static Analysis
  Consume Aggregate Validation Evidence before disposition

If Aggregate = PASSED → may RESOLVED
If Aggregate = FAILED → must NOT RESOLVED → BLOCKED (or repair within boundary)
ERROR / dependency-unavailable / malformed-evidence paths: NOT_ESTABLISHED
  (do not invent handling beyond recording NOT_ESTABLISHED)
```

Supporting commands (pytest / ruff / mypy) executed under CANDIDATE-002
are **dependency validation**, not proof that CANDIDATE-002 was skipped.

## Disposition vocabulary

```text
RESOLVED | PARTIAL | BLOCKED | ESCALATED | STOPPED
```

## Evidence classification

When reporting, classify claims as:

```text
OBSERVED | SUPPORTED_INFERENCE | WEAK_INFERENCE | NOT_ESTABLISHED
```

Do not label inference as OBSERVED.
Do not label Normal Engineering Judgment as Autonomous Capability.

## Human intervention

Record material human judgment separately.
If a human substitutes a required Skill step, do not claim Fully Autonomous.

## Stop

Stop after Report. Do not package further assets or promote lifecycle states
unless an authorized assessment stage decides.

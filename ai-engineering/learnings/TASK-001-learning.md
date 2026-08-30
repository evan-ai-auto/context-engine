# TASK-001 Learning

## What Worked

- Narrow TASK-001 scope kept the first delivery reviewable and production-oriented without product feature creep.
- Typer + CliRunner provided a fast acceptance gate for `--help`, `--version`, and placeholder `init`.
- Architecture “create packages when needed” avoided empty future layers.

## What Did Not Work

- Task status was left at `TODO` after implementation, so inventory and reality diverged.
- Structured session/review/learning artifacts lagged behind code delivery.
- Local environment friction (old pip, proxy, Scripts not on PATH) delayed validation even when code was correct.

## Process Gaps

- No explicit closeout step until TASK-001-CLOSEOUT was added.
- Validation evidence was recorded narratively in `record.md` rather than a dedicated `validation.md` with reproducible command output.
- Version consistency between package metadata and tests was not enforced until review.

## Reusable Principles

- Mark task status when Definition of Done is met, not later.
- Prefer placeholder commands over stub architecture packages.
- Treat version as a single source of truth (`__version__`) in CLI and tests.
- Separate environment failures from code failures in validation records.

## Candidate Future Skills

- Python package bootstrap (hatchling, src-layout, optional `[dev]` tooling)
- Typer CLI smoke-test skill (CliRunner help/version/command checks)
- Engineering closeout skill (status sync, session/review/learning templates)

## Candidate Future Workflows

- task bootstrap workflow
- implementation review workflow
- task closeout workflow

These are candidates only; they are not claimed to exist as packaged skills or workflows yet.

# TASK-002 Stage A — Comprehensive Domain Architecture Reconciliation

## Objective

Perform a comprehensive reconciliation and final architecture freeze for TASK-002 before any production implementation begins.

This stage intentionally allows broad specification changes.

The goal is to resolve known architectural ambiguities now rather than repeatedly changing the core domain model after implementation.

Do not implement production code.

Do not modify:

- src/
- tests/

Do not add Pydantic to pyproject.toml yet.

This is a specification and architecture reconciliation stage only.

---

# 1. Read the Current Repository Specification

Read all relevant TASK-002 documents before making changes:

- ai-engineering/tasks/TASK-002.md
- ai-engineering/reviews/TASK-002-architecture-decision-review.md
- ai-engineering/sessions/TASK-002/01-task-definition.md
- ai-engineering/sessions/TASK-002/02-implementation-plan.md
- ai-engineering/sessions/TASK-002/03-domain-model-contract.md
- ai-engineering/sessions/TASK-002/04-test-plan.md
- ai-engineering/sessions/TASK-002/05-validation-checklist.md
- ai-engineering/sessions/TASK-002/06-cursor-prompt.md
- ai-engineering/sessions/TASK-002/architecture-decisions.md
- ai-engineering/sessions/TASK-002/decisions.md
- pyproject.toml

Identify duplicated, inconsistent, or ambiguous specifications.

The final result must have a clear canonical source for architecture decisions and domain contracts.

---

# 2. Canonical Architecture Decisions

Use the following decisions as the approved architectural direction.

## ADR-001 — Pydantic

Keep Pydantic v2 as the domain model foundation.

Do not modify pyproject.toml in this stage.

Document that implementation must verify the repository Python compatibility policy before selecting the final Pydantic version constraint.

Because this is a new project, implementation planning may recommend updating the minimum supported Python version if required by the selected modern dependency and typing strategy.

Do not decide the final Python version in this stage unless the current specification already provides enough evidence.

---

## ADR-002 — Enum Strategy

Use explicit string-based enums for stable domain concepts.

The canonical enum set is:

- ModuleType
- DependencyScope
- EvidenceType
- AnalysisStatus

Do not introduce a DependencyEcosystem enum.

Dependency ecosystem must remain a string to avoid requiring Core Domain Model changes whenever a new package ecosystem is supported.

---

## ADR-003 — Evidence Strategy

Evidence is a reusable domain model.

Update the architecture from a single optional Evidence reference to multiple evidence records.

Canonical shape:

Technology.evidence -> list[Evidence]

Dependency.evidence -> list[Evidence]

Canonical Evidence fields:

- source_file
- source_type
- detail

EvidenceType must be an explicit enum.

The model must support multiple independent pieces of evidence for a single technology or dependency.

---

## ADR-004 — Module and Dependency Relationship

Keep internal module relationships separate from external package/library dependencies.

Canonical semantics:

Module.depends_on

represents internal module-to-module relationships.

ProjectContext.project_dependencies

represents external package/library dependencies.

Dependency.declared_by

optionally identifies the module that declared the dependency.

Do not create a DependencyGraph in TASK-002.

Do not add Module.dependencies.

The dependency collection must have a single canonical owner:

ProjectContext.project_dependencies

Add:

Dependency.ecosystem: str

The ecosystem identifies the dependency ecosystem, such as Maven, PyPI, npm, Cargo, Go Modules, etc.

Do not model ecosystem as an Enum.

---

## ADR-005 — Partial Context Strategy

Add a minimal Partial Context strategy.

Do not introduce per-module or per-analyzer status models.

Add:

GenerationMetadata.analysis_status: AnalysisStatus

Canonical values:

- pending
- partial
- completed
- failed

This status describes the completeness of the generated ProjectContext as a whole.

The domain model must be able to represent partially analyzed repositories.

---

# 3. Canonical Domain Model

Reconcile and update:

ai-engineering/sessions/TASK-002/03-domain-model-contract.md

The canonical domain model should be:

ProjectContext
- project: ProjectInfo
- repository: RepositoryInfo
- modules: list[Module]
- technologies: list[Technology]
- project_dependencies: list[Dependency]
- metadata: GenerationMetadata

## ProjectInfo

- name: required
- description: optional
- primary_language: optional

## RepositoryInfo

Preserve existing fields where reasonable.

Do not introduce unnecessary repository metadata.

## Module

- name: required
- path: required
- type: ModuleType
- language: optional
- build_tool: optional
- depends_on: list[str]

Do not add Module.dependencies.

## Technology

- name: required
- category: optional
- version: optional
- evidence: list[Evidence]

## Dependency

- name: required
- ecosystem: required string
- version: optional
- scope: optional DependencyScope
- declared_by: optional string
- evidence: list[Evidence]

## Evidence

- source_file: required
- source_type: EvidenceType
- detail: optional

## GenerationMetadata

- engine_version: required
- schema_version: required
- generated_at: required
- analysis_status: AnalysisStatus

Use explicit required versus optional semantics.

Remove wording that leaves required/optional decisions unresolved.

---

# 4. Naming Reconciliation

Rename:

ProjectContext.dependencies

to:

ProjectContext.project_dependencies

Update all TASK-002 specifications consistently.

This includes:

- task definition
- implementation plan
- domain model contract
- test plan
- validation checklist
- cursor prompt

Do not leave both names in the specification.

---

# 5. Architecture Decision Source

Keep:

ai-engineering/sessions/TASK-002/architecture-decisions.md

as the single canonical architecture decision document.

Delete:

ai-engineering/sessions/TASK-002/decisions.md

Ensure no document references decisions.md as a canonical source.

---

# 6. Test Plan Reconciliation

Update:

ai-engineering/sessions/TASK-002/04-test-plan.md

The test plan must cover:

1. ProjectContext construction
2. Required field validation
3. Optional field behavior
4. ModuleType enum behavior
5. DependencyScope enum behavior
6. EvidenceType enum behavior
7. AnalysisStatus enum behavior
8. Multiple Evidence records
9. Dependency ecosystem
10. project_dependencies ownership
11. Module.depends_on relationships
12. Partial context representation
13. Serialization
14. Deserialization
15. Invalid model validation

Do not write tests in this stage.

Only update the specification.

---

# 7. Validation Checklist Reconciliation

Update:

ai-engineering/sessions/TASK-002/05-validation-checklist.md

Ensure the validation checklist covers:

- domain contract consistency
- required vs optional fields
- enum consistency
- multiple evidence support
- dependency ownership
- internal module relationships
- dependency ecosystem
- partial context status
- serialization
- validation failures
- public package API

---

# 8. Implementation Prompt Reconciliation

Update:

ai-engineering/sessions/TASK-002/06-cursor-prompt.md

Make the following explicit:

1. The architecture is frozen.
2. Cursor must not make new architecture decisions during implementation.
3. The canonical domain contract is:

   ai-engineering/sessions/TASK-002/03-domain-model-contract.md

4. The canonical architecture decisions are:

   ai-engineering/sessions/TASK-002/architecture-decisions.md

5. Implementation must verify Python and Pydantic compatibility before modifying pyproject.toml.

6. If implementation discovers a conflict with the frozen contract, stop and report the conflict instead of silently redesigning the model.

---

# 9. TASK Status

Update:

ai-engineering/tasks/TASK-002.md

Set the current stage/status appropriately for architecture reconciliation.

After all specification changes are complete, the task should indicate that its specification is frozen and ready for the next pre-implementation inspection gate.

Do not mark TASK-002 as DONE.

Do not mark implementation as complete.

---

# 10. Consistency Review

After all changes are complete, perform a complete consistency review across:

- TASK-002.md
- TASK-002 architecture decision review
- architecture-decisions.md
- 02-implementation-plan.md
- 03-domain-model-contract.md
- 04-test-plan.md
- 05-validation-checklist.md
- 06-cursor-prompt.md

Check specifically for:

- old field names
- duplicate architecture decisions
- conflicting Evidence definitions
- conflicting Dependency definitions
- old ProjectContext.dependencies references
- inconsistent required/optional semantics
- inconsistent enum definitions
- references to deleted decisions.md

Fix direct inconsistencies.

Do not add unrelated architecture features.

---

# 11. Explicitly Out of Scope

Do not implement:

- repository scanning
- project analyzers
- module analyzers
- dependency analyzers
- context generation
- CLI functionality
- dependency graphs
- graph storage
- database persistence
- vector storage
- agent orchestration
- skill extraction

Do not modify:

- src/
- tests/

Do not add dependencies to pyproject.toml.

---

# 12. Required Final Report

Before committing, provide:

## Architecture Changes

List every architecture change made.

## Contract Changes

List every domain model change.

## Files Modified

List all modified files.

## Files Deleted

List deleted files.

## Consistency Fixes

List specification inconsistencies resolved.

## Remaining Risks

List unresolved architectural risks, if any.

## Scope Confirmation

Explicitly confirm:

- no production code implemented
- no tests implemented
- no dependencies added
- no analyzer logic added

---

# 13. Commit

Commit only after the final consistency review passes.

Suggested commit message:

docs(ai-engineering): reconcile and freeze TASK-002 domain architecture

Do not start TASK-002 implementation.

Stop after the specification freeze commit.
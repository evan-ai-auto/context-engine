# TASK-002 Architecture Decisions

Architecture decisions for the core Project Context domain model.

Source review:

[`ai-engineering/reviews/TASK-002-architecture-decision-review.md`](../../reviews/TASK-002-architecture-decision-review.md)

Also mirrored historically at:

[`decisions.md`](./decisions.md)

Status: **locked** (implementation not started at session bootstrap).

---

### Decision: Introduce Pydantic v2

#### Context

TASK-002 requires validated, serializable domain models (AC-003–AC-007) without using `dict[str, Any]` as the primary representation.

#### Decision

Add Pydantic v2 as the domain modeling library.

#### Reason

Typed models, JSON round-trip, and enum/required-field validation on Python 3.8+ with less custom infrastructure than dataclasses-only or a hand-rolled validator.

#### Trade-off

New runtime dependency; must pin a 3.8-compatible Pydantic 2.x line.

#### Consequences

Domain entities under `src/ai_context/domain/` will be Pydantic models using `model_dump` / `model_validate`.

---

### Decision: Closed str Enums for taxonomies; open strings for names

#### Context

AC-005 requires rejecting invalid enum values, while TASK-002 §8.5 requires extensibility for evolving ecosystems.

#### Decision

Use `class X(str, Enum)` for stable taxonomies (project/module type, technology category, dependency scope, evidence type). Use plain `str` for names, versions, paths, and fast-evolving language/build-tool labels.

#### Reason

Closed enums give hard validation for taxonomies; open strings avoid freezing every framework or language name into the schema.

#### Trade-off

New taxonomy values require a schema bump; free-form strings may need later normalization in analyzers.

#### Consequences

Tests must cover invalid enum rejection; technology/dependency names remain strings.

---

### Decision: Shared Evidence model with Optional attachment

#### Context

Technology and Dependency need a consistent way to record detection sources (AC-008) without duplicating ad-hoc dict shapes.

#### Decision

One shared `Evidence` model (`file`, `type` enum). Attach as `Optional[Evidence]` on Technology and Dependency only for v0.1.

#### Reason

Matches TASK-002 relationships, keeps a single evidence contract, and defers multi-source lists until needed.

#### Trade-off

Module/Project lack evidence in v0.1; multi-source evidence is deferred.

#### Consequences

Analyzers attach at most one primary evidence blob per tech/dep; Evidence performs no I/O.

---

### Decision: Minimal Module/Dependency relationship fix

#### Context

TASK-002’s flat package-like `Dependency` list cannot express v0.1 module→module edges required by the specification and architecture.

#### Decision

1. Keep `ProjectContext.dependencies` as package/library dependencies, with optional `declared_by`.
2. Add `Module.depends_on: List[str]` for internal module dependencies.
3. Defer first-class `DependencyGraph` until generator/analysis needs `dependencies.json`.

#### Reason

Closes the spec gap without inventing a premature graph root before analyzers exist.

#### Trade-off

Graph export is derived later; package vs module deps are separated by field location rather than a single edge model.

#### Consequences

TASK-002 implementation must include `Module.depends_on` and `Dependency.declared_by`, and must not ship the original flat-only relationship as final.

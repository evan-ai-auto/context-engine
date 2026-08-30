# TASK-002 Architecture Decision Review

## Summary / Status

| Field | Value |
|---|---|
| Related Task | TASK-002 — Core Project Context Domain Model |
| Review Type | Architecture Decision Review |
| Focus | Pydantic, Enum design, Evidence model, Module/Dependency relationships |
| Status | Decisions locked |
| Implementation | Not started |

This review locks four architecture decisions before domain-model implementation.

TASK-002 remains `READY_FOR_IMPLEMENTATION`. It is not marked DONE.

No product source code, dependencies, CLI, scanners, or `.ai-context` generation were changed in this review pass.

---

## Q1 — Introduce Pydantic?

### Context

TASK-002 requires explicit domain models with validation, serialization, and deserialization (AC-003–AC-007), including rejection of invalid enum values. The current runtime dependency surface is Typer only. Python constraint is `>= 3.8.0`.

### Decision

Introduce **Pydantic v2** as the domain modeling library for TASK-002.

### Reason

Pydantic is the smallest established fit that provides typed models, JSON round-trip (`model_dump` / `model_validate`), and structured validation without adopting `dict[str, Any]` as the primary domain representation.

### Trade-off

- Adds a new runtime dependency; must pin a Pydantic 2.x line compatible with Python 3.8.
- Rejects dataclasses-only (manual validation burden) and a custom validator stack.

### Consequences

- `pyproject.toml` will gain `pydantic` during TASK-002 implementation.
- Domain entities will be Pydantic models under `src/ai_context/domain/`.

---

## Q2 — How should Enums be designed?

### Context

TASK-002 mentions invalid enum rejection (AC-005) and extensibility (§8.5). Fields include project/module types, technology categories, dependency scopes, and evidence types, plus open-ended names and versions.

### Decision

| Field class | Representation |
|---|---|
| Stable taxonomies (`ProjectInfo.type`, `Module.type`, `Technology.category`, `Dependency.scope`, `Evidence.type`) | `class X(str, Enum)` (Python 3.8-compatible str-enum) |
| Open identifiers (`name`, versions, paths, and fast-evolving language/build-tool display values) | plain `str` |

### Reason

Closed enums satisfy AC-005 for taxonomies. Open strings keep ecosystem names extensible without freezing every framework or language into the schema.

### Trade-off

- Adding a new taxonomy value later is a schema bump.
- Free-form language/build-tool strings need analyzer-side normalization later if consistency becomes important.

### Consequences

- Unit tests must reject invalid enum strings.
- Technology and dependency **names** remain strings, not enums.

---

## Q3 — Should Evidence be a common model?

### Context

TASK-002 §6.8 / §7 / AC-008 attach Evidence to Technology and Dependency. Ad-hoc `{file, type}` dicts per entity would duplicate structure.

### Decision

Implement a single shared **`Evidence`** model (`file: str`, `type: EvidenceType` enum) in `domain/evidence.py`.

For v0.1:

- Reuse on **Technology** and **Dependency** only.
- Use **`Optional[Evidence]`** (one primary source per entity).
- Do not attach Evidence to Module or ProjectInfo yet.

### Reason

Matches the TASK-002 relationship diagram, keeps analyzers able to explain detections, and avoids duplicated evidence shapes.

### Trade-off

- Multi-source evidence (`List[Evidence]`) is deferred until analyzers need it.
- Modules lack evidence in v0.1 even when detection confidence would benefit later.

### Consequences

- Evidence has no filesystem I/O.
- Analyzers populate optional evidence when a concrete source file is known.

---

## Q4 — Is the Module / Dependency relationship sufficient?

### Finding

As written in TASK-002, flat `ProjectContext.dependencies: List[Dependency]` with `name` / `version` / `scope` models **package/library** dependencies.

That shape does **not** express v0.1 specification module→module edges:

- module context `dependencies: ["payment-service"]`
- `dependencies.json` graph (`from` / `to` / `type: module-dependency`)
- architecture’s aspirational `DependencyGraph`

**Verdict:** Not sufficient for v0.1 module dependency export if left unchanged.

### Decision (minimal fix for TASK-002 implementation)

1. Keep `ProjectContext.dependencies: List[Dependency]` as **package/library** dependencies:
   - `name`, `version`, `scope`, `evidence`
   - add optional `declared_by: Optional[str]` (module name that declared the package dependency)
2. Add `Module.depends_on: List[str]` — names of modules this module depends on (aligns with spec module JSON).
3. Defer a first-class `DependencyGraph` domain entity until the generator/analysis task that writes `dependencies.json`.

Mapping for later export:

```text
modules[] + Module.depends_on  →  dependencies.json nodes/edges
ProjectContext.dependencies    →  package/library dependency listings (not module graph edges)
```

### Reason

Closes the spec gap without inventing a second graph root before analyzers exist (TASK-002 §8.5 / “no speculative entities”).

### Trade-off

- Graph export is derived, not stored as its own domain root yet.
- Package vs module dependencies are distinguished by location (`dependencies` vs `Module.depends_on`).

### Consequences

- TASK-002 implementation must amend §6.4 / §7 relative to the original task text:
  - `Module.depends_on`
  - `Dependency.declared_by`
- Do not ship the insufficient flat-only relationship as the final contract.

```text
ProjectContext
├── ProjectInfo
├── RepositoryInfo
├── modules[] ── depends_on[] ──► module names
├── technologies[] ── evidence?
├── dependencies[] (package) ── evidence? ; declared_by? ──► module name
└── GenerationMetadata
```

---

## Implications for TASK-002 Implementation

When implementation starts, follow this checklist:

1. Add Pydantic v2 (Python 3.8-compatible) to runtime dependencies.
2. Create `src/ai_context/domain/` models per TASK-002 package layout.
3. Use closed `str` Enums for taxonomies; strings for open identifiers.
4. Implement shared `Evidence` with `Optional[Evidence]` on Technology and Dependency.
5. Implement `Module.depends_on: List[str]` and `Dependency.declared_by: Optional[str]`.
6. Cover valid/invalid serialization and enum rejection in unit tests.
7. Do not implement scanners, analyzers, CLI changes, or `.ai-context` generation in TASK-002.

---

## Explicit Non-Goals (this review)

- No repository scanning or filesystem traversal
- No Java/Python/Maven analysis
- No `.ai-context` generation
- No CLI command changes
- No domain model source implementation in this pass
- No marking TASK-002 DONE

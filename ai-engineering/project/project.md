# AI Context Engine

## 1. Project Vision

AI Context Engine is a project context generation and maintenance engine designed for AI Coding Agents.

Its purpose is to automatically transform a software repository into structured, reusable, and machine-readable project context.

The long-term goal is to provide a standardized Context Layer for:

- AI Coding Agents
- AI Engineering Workflows
- Multi-Agent Systems
- Code Analysis Tools
- Project Knowledge Management

Instead of requiring every AI Agent to repeatedly explore and understand an entire repository, AI Context Engine should provide a structured representation of the repository.

---

# 2. Problem Statement

AI Coding Agents face several recurring problems when working with software repositories.

## 2.1 Repeated Repository Exploration

When an AI Agent starts a task, it often needs to:

- scan directories
- inspect build files
- identify modules
- understand technology stacks
- inspect dependencies
- locate important source code

Different tasks may repeat the same repository exploration process.

This increases:

- context consumption
- execution time
- analysis cost
- inconsistency between agents

---

## 2.2 Context Is Usually Unstructured

Repository knowledge is typically distributed across:

- source code
- build files
- configuration files
- documentation
- Git metadata

AI Agents must reconstruct project understanding dynamically.

There is usually no standardized project context representation.

---

## 2.3 Multi-Agent Context Sharing Is Difficult

Different AI Agents may independently analyze the same project.

For example:

```text
Developer Agent
       │
       ├── scans repository
       │
Reviewer Agent
       │
       ├── scans repository again
       │
Architect Agent
       │
       └── scans repository again
```

This leads to duplicated work and inconsistent project understanding.

---

# 3. Project Goal

The goal of AI Context Engine is to establish a reusable project Context Layer.

The system should transform:

```text
Repository
    │
    ▼
Static Analysis
    │
    ▼
Structured Project Knowledge
    │
    ▼
AI Context
```

The generated context should help AI systems quickly understand:

- project structure
- project type
- modules
- programming languages
- build tools
- frameworks
- dependencies
- repository metadata

---

# 4. Core Principles

## 4.1 Context Is Generated

The `.ai-context` directory should be generated from the repository.

It should not become the primary source of business knowledge.

The repository itself remains the source of truth.

```text
Source Code
Build Configuration
Project Configuration
Git Metadata
        │
        ▼
AI Context Engine
        │
        ▼
.ai-context
```

---

## 4.2 Context Must Be Rebuildable

Generated context should always be removable and regenerated.

```bash
rm -rf .ai-context
ai-context init
```

The system should be able to rebuild the context from repository sources.

---

## 4.3 Separate Generated Context from Human Knowledge

The project knowledge system should have three independent layers.

```text
Repository
│
├── .ai-context/
│       Generated project analysis
│       Can be deleted and regenerated
│
├── knowledge/
│       Human-maintained knowledge
│       Persistent
│
└── .ai-runtime/
        Current AI execution state
        Temporary
```

These three layers must not be mixed.

---

## 4.4 Deterministic First

Early versions should prioritize deterministic static analysis.

The initial versions should not depend on:

- LLM
- Vector Database
- Embedding
- RAG

The same repository state should produce semantically consistent context.

---

## 4.5 Extensible Architecture

The system should be extensible for future support of:

- additional programming languages
- additional build tools
- framework detection
- semantic analysis
- incremental updates
- context retrieval
- dependency graphs
- AI Agent integration

---

# 5. Long-Term Architecture Vision

The long-term system can evolve into:

```text
                    Repository
                        │
                        ▼
              AI Context Engine
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
 Project Context   Knowledge Layer   Runtime Context
        │               │               │
        └───────────────┼───────────────┘
                        │
                        ▼
                  Context Layer
                        │
                        ▼
              AI Agent / Workflow
```

---

# 6. Project Evolution

## Phase 1 — Context Generation

Generate basic repository context.

Capabilities:

- project detection
- module detection
- technology detection
- dependency detection
- structured context generation

---

## Phase 2 — Context Update

Support context maintenance.

Capabilities:

- repository change detection
- incremental update
- context refresh

---

## Phase 3 — Semantic Context

Introduce deeper code understanding.

Possible capabilities:

- AST analysis
- symbol analysis
- module relationship analysis
- API relationship analysis

---

## Phase 4 — Context Retrieval

Allow AI Agents to retrieve only relevant context.

Possible capabilities:

- context query
- context filtering
- task-oriented context assembly

---

## Phase 5 — AI Engineering Integration

Integrate with:

- AI Agents
- Skills
- Workflows
- MCP
- Evaluation Systems

---

# 7. v0.1 Position

AI Context Engine v0.1 is the first MVP.

Its purpose is not to solve the complete context problem.

The goal is to validate the core pipeline:

```text
Repository
    │
    ▼
Repository Scan
    │
    ▼
Project Detection
    │
    ▼
Module Detection
    │
    ▼
Technology Analysis
    │
    ▼
Dependency Analysis
    │
    ▼
.ai-context
```

---

# 8. Supported Technologies

The initial development focus is:

## Java

- Maven
- Multi Module
- Spring Boot

## Python

- pyproject.toml
- requirements.txt
- setup.py
- common package structures

The project should be designed so that additional technologies can be added later.

---

# 9. Relationship with AI Engineering

AI Context Engine is also the first experimental project of the AI Engineering system.

The project development process should be recorded.

The purpose is to eventually extract reusable:

- Agents
- Skills
- Workflows
- Engineering Rules
- Evaluation Methods

The process is:

```text
Real Project Development
        │
        ▼
Development Process Recording
        │
        ▼
Pattern Analysis
        │
        ▼
Capability Extraction
        │
        ├── Agent
        ├── Skill
        └── Workflow
        │
        ▼
AI Engineering Library
        │
        ▼
Project Regeneration
        │
        ▼
Evaluation
        │
        ▼
Iteration
```

---

# 10. Definition of Success

The project is successful when it can provide reliable structured context for a repository and reduce repeated repository exploration by AI Coding Agents.

The first measurable milestone is:

```text
Given a Java or Python repository,

AI Context Engine can automatically generate:

.ai-context/

containing:

- project metadata
- module information
- technology stack
- dependency relationships
- generation metadata
```
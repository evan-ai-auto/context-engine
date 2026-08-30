# AI Context Engine v0.1 Architecture

## 1. Architecture Goal

The architecture should support:

- clear separation of responsibilities
- deterministic repository analysis
- testability
- extensibility
- future language support

The v0.1 architecture should remain simple.

Avoid unnecessary framework abstractions.

---

# 2. Architecture Overview

```text
┌───────────────────────────────┐
│             CLI               │
│                               │
│       ai-context init         │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│         Application           │
│                               │
│      InitContextService       │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       Analysis Pipeline       │
│                               │
│  Repository Scanner           │
│  Project Detector             │
│  Module Detector              │
│  Tech Stack Analyzer          │
│  Dependency Analyzer          │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│        Context Builder        │
│                               │
│  Project Context              │
│  Module Context               │
│  Dependency Graph             │
│  Manifest                     │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       Infrastructure          │
│                               │
│  File System                  │
│  Git                          │
│  XML Parser                   │
│  TOML Parser                  │
└───────────────────────────────┘
                │
                ▼
          .ai-context/
```

---

# 3. Package Structure

Recommended structure:

```text
src/ai_context/
│
├── cli/
│   ├── __init__.py
│   └── main.py
│
├── application/
│   └── init_context_service.py
│
├── domain/
│   │
│   ├── models/
│   │   ├── project.py
│   │   ├── module.py
│   │   ├── dependency.py
│   │   └── manifest.py
│   │
│   └── services/
│       ├── repository_scanner.py
│       ├── project_detector.py
│       ├── module_detector.py
│       ├── tech_stack_analyzer.py
│       └── dependency_analyzer.py
│
├── infrastructure/
│   │
│   ├── filesystem/
│   ├── git/
│   ├── maven/
│   └── python/
│
└── generator/
    └── context_generator.py
```

Only create packages when they are needed.

TASK-001 should not create all future implementation files.

The structure represents the target architecture, not a requirement to create empty abstractions immediately.

---

# 4. Core Execution Pipeline

The primary execution flow is:

```text
Repository Path
       │
       ▼
Repository Root Detection
       │
       ▼
Repository Scan
       │
       ├───────────────┐
       │               │
       ▼               ▼
Project Detection   Module Detection
       │               │
       └───────┬───────┘
               │
               ▼
      Technology Analysis
               │
               ▼
      Dependency Analysis
               │
               ▼
         Context Builder
               │
               ▼
        Context Generator
               │
               ▼
         .ai-context
```

---

# 5. Layer Responsibilities

## 5.1 CLI Layer

Location:

```text
src/ai_context/cli/
```

Responsibilities:

- receive command-line arguments
- validate user input
- invoke application services
- display results
- map exceptions to user-friendly messages

The CLI layer must not contain repository analysis logic.

---

## 5.2 Application Layer

Location:

```text
src/ai_context/application/
```

Responsibilities:

- orchestrate the complete use case
- coordinate analysis components
- manage execution flow
- return application results

Primary service:

```text
InitContextService
```

Conceptually:

```python
service.execute(repository_path)
```

The application layer should not contain CLI-specific logic.

---

## 5.3 Domain Layer

Location:

```text
src/ai_context/domain/
```

Responsibilities:

- core data models
- project analysis rules
- module analysis rules
- dependency analysis rules

The domain layer should not depend on:

- Typer
- CLI implementation
- output formatting

---

## 5.4 Infrastructure Layer

Location:

```text
src/ai_context/infrastructure/
```

Responsibilities:

- filesystem access
- Git metadata access
- Maven XML parsing
- Python project configuration parsing

Infrastructure components provide technical capabilities to higher layers.

---

## 5.5 Generator Layer

Location:

```text
src/ai_context/generator/
```

Responsibilities:

Convert structured analysis results into generated context files.

Output:

```text
.ai-context/
├── project.json
├── modules/
├── dependencies.json
└── manifest.json
```

The generator should not perform repository analysis.

---

# 6. Dependency Direction

The preferred dependency direction is:

```text
CLI
 │
 ▼
Application
 │
 ▼
Domain
```

Infrastructure supports the application and domain logic.

The core rule is:

```text
Business and analysis logic
must not depend on CLI details.
```

Forbidden dependencies:

```text
Domain
  ↓
CLI
```

```text
Domain
  ↓
Typer
```

Avoid coupling domain logic directly to command-line implementation.

---

# 7. Analysis Components

## RepositoryScanner

Responsibilities:

- enumerate files
- enumerate directories
- apply ignore rules

Example ignored directories:

```text
.git
.ai-context
__pycache__
target
build
node_modules
.venv
venv
```

---

## ProjectDetector

Responsibilities:

- identify Java projects
- identify Python projects
- identify unknown projects

---

## ModuleDetector

Responsibilities:

- detect Maven modules
- detect Java source roots
- detect Python package roots

---

## TechStackAnalyzer

Responsibilities:

- detect build tools
- detect frameworks
- collect technology metadata

---

## DependencyAnalyzer

Responsibilities:

- analyze Maven dependencies
- analyze Python dependencies
- identify internal module dependencies

---

# 8. Data Model

The primary domain models are:

```text
ProjectContext
ModuleContext
DependencyGraph
Manifest
```

Relationships:

```text
ProjectContext
       │
       ├── Modules
       │
       ├── Technologies
       │
       └── Dependencies
```

---

# 9. Extensibility Model

Future language support should follow an analyzer-based extension model.

Conceptually:

```text
ProjectAnalyzer
│
├── JavaProjectAnalyzer
├── PythonProjectAnalyzer
├── NodeProjectAnalyzer
└── GoProjectAnalyzer
```

Example interface:

```python
from typing import Protocol


class ProjectAnalyzer(Protocol):

    def supports(self, repository) -> bool:
        ...

    def analyze(self, repository):
        ...
```

This abstraction should only be introduced when multiple implementations actually require it.

Do not introduce unnecessary abstractions in v0.1.

---

# 10. Error Handling Strategy

Errors should be categorized into:

```text
User Error
System Error
Analysis Warning
```

Examples:

## User Error

```text
Repository path does not exist
```

The command should fail.

## System Error

```text
Unable to read file
```

The error should be reported clearly.

## Analysis Warning

```text
Unknown project type
```

The engine should continue when possible.

---

# 11. Testing Architecture

The project should include:

```text
tests/
│
├── unit/
│
├── integration/
│
├── fixtures/
│
└── golden/
```

## Unit Tests

Test individual components.

Example:

```text
RepositoryScanner
ProjectDetector
ModuleDetector
```

---

## Integration Tests

Test complete use cases.

Example:

```text
CLI
  ↓
Application Service
  ↓
Analysis Pipeline
  ↓
Generated Context
```

---

## Golden Tests

Test generated context stability.

```text
Fixture Repository
        │
        ▼
Generated Context
        │
        ▼
Golden Context
```

Generated output should match expected semantic structure.

---

# 12. Design Principles

The implementation should follow:

1. Small components
2. Single responsibility
3. Explicit data models
4. Deterministic analysis
5. Testability
6. Minimal dependencies
7. Progressive abstraction
8. No premature framework design

---

# 13. Architecture Constraints

v0.1 must not introduce:

- Agent runtime
- Workflow runtime
- MCP server
- LLM dependency
- Vector database
- Graph database
- asynchronous distributed architecture
- plugin framework

These are future concerns.

---

# 14. Future Evolution

Potential future architecture:

```text
Repository
    │
    ▼
Context Engine
    │
    ├── Static Analysis
    ├── Semantic Analysis
    ├── Incremental Update
    ├── Context Index
    └── Context Retrieval
              │
              ▼
         Context Layer
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
     Agent  Skill  Workflow
```

v0.1 should provide a clean foundation for this evolution without implementing these future components.
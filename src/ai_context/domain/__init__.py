"""Public API for the Project Context domain model."""

from ai_context.domain.dependency import Dependency
from ai_context.domain.enums import (
    AnalysisStatus,
    DependencyScope,
    EvidenceType,
    ModuleType,
)
from ai_context.domain.evidence import Evidence
from ai_context.domain.metadata import GenerationMetadata
from ai_context.domain.module import Module
from ai_context.domain.project import ProjectInfo
from ai_context.domain.project_context import ProjectContext
from ai_context.domain.repository import RepositoryInfo
from ai_context.domain.technology import Technology

__all__ = [
    "AnalysisStatus",
    "Dependency",
    "DependencyScope",
    "Evidence",
    "EvidenceType",
    "GenerationMetadata",
    "Module",
    "ModuleType",
    "ProjectContext",
    "ProjectInfo",
    "RepositoryInfo",
    "Technology",
]

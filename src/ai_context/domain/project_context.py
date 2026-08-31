"""Aggregate root for structured project context."""

from pydantic import BaseModel, Field

from ai_context.domain.dependency import Dependency
from ai_context.domain.metadata import GenerationMetadata
from ai_context.domain.module import Module
from ai_context.domain.project import ProjectInfo
from ai_context.domain.repository import RepositoryInfo
from ai_context.domain.technology import Technology


class ProjectContext(BaseModel):
    project: ProjectInfo
    repository: RepositoryInfo
    modules: list[Module] = Field(default_factory=list)
    technologies: list[Technology] = Field(default_factory=list)
    project_dependencies: list[Dependency] = Field(default_factory=list)
    metadata: GenerationMetadata

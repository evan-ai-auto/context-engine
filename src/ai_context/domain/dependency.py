"""External package/library dependency."""

from pydantic import BaseModel, Field

from ai_context.domain.enums import DependencyScope
from ai_context.domain.evidence import Evidence


class Dependency(BaseModel):
    name: str
    ecosystem: str
    version: str | None = None
    scope: DependencyScope | None = None
    declared_by: str | None = None
    evidence: list[Evidence] = Field(default_factory=list)

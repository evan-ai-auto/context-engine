"""Detected technology."""

from pydantic import BaseModel, Field

from ai_context.domain.evidence import Evidence


class Technology(BaseModel):
    name: str
    category: str | None = None
    version: str | None = None
    evidence: list[Evidence] = Field(default_factory=list)

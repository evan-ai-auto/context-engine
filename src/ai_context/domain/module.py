"""Logical project module."""

from pydantic import BaseModel, Field

from ai_context.domain.enums import ModuleType


class Module(BaseModel):
    name: str
    path: str
    type: ModuleType
    language: str | None = None
    build_tool: str | None = None
    depends_on: list[str] = Field(default_factory=list)

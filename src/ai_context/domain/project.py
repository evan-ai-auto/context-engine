"""Logical project information."""

from pydantic import BaseModel


class ProjectInfo(BaseModel):
    name: str
    description: str | None = None
    primary_language: str | None = None

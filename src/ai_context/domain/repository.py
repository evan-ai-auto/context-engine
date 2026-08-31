"""Repository-level metadata."""

from pydantic import BaseModel


class RepositoryInfo(BaseModel):
    root_path: str
    is_git_repository: bool
    branch: str | None = None
    commit: str | None = None

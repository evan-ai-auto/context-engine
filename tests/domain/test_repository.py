"""Contract tests for RepositoryInfo."""

import pytest
from pydantic import ValidationError

from ai_context.domain import RepositoryInfo


def test_repository_info_portable_root() -> None:
    repo = RepositoryInfo(root_path=".", is_git_repository=True)
    assert repo.branch is None
    assert repo.commit is None


def test_repository_info_optional_git_fields() -> None:
    repo = RepositoryInfo(
        root_path="repos/demo",
        is_git_repository=True,
        branch="main",
        commit="abc123",
    )
    assert repo.branch == "main"


def test_repository_info_missing_required_fails() -> None:
    with pytest.raises(ValidationError):
        RepositoryInfo.model_validate({"root_path": "."})

"""Contract tests for ProjectInfo."""

import pytest
from pydantic import ValidationError

from ai_context.domain import ProjectInfo


def test_project_info_required_name() -> None:
    project = ProjectInfo(name="context-engine")
    assert project.description is None
    assert project.primary_language is None


def test_project_info_optional_fields() -> None:
    project = ProjectInfo(
        name="context-engine",
        description="demo",
        primary_language="python",
    )
    assert project.description == "demo"


def test_project_info_missing_name_fails() -> None:
    with pytest.raises(ValidationError):
        ProjectInfo.model_validate({})

"""Contract tests for ProjectContext aggregate."""

from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from ai_context.domain import (
    AnalysisStatus,
    Dependency,
    DependencyScope,
    Evidence,
    EvidenceType,
    GenerationMetadata,
    Module,
    ModuleType,
    ProjectContext,
    ProjectInfo,
    RepositoryInfo,
    Technology,
)


def _metadata(
    status: AnalysisStatus = AnalysisStatus.COMPLETED,
) -> GenerationMetadata:
    return GenerationMetadata(
        engine_version="0.1.0",
        schema_version="1.0",
        generated_at=datetime(2026, 8, 31, tzinfo=timezone.utc),
        analysis_status=status,
    )


def _minimal_context() -> ProjectContext:
    return ProjectContext(
        project=ProjectInfo(name="demo", primary_language="python"),
        repository=RepositoryInfo(root_path=".", is_git_repository=True),
        project_dependencies=[Dependency(name="typer", ecosystem="PyPI")],
        metadata=_metadata(),
    )


def test_project_context_construction() -> None:
    context = ProjectContext(
        project=ProjectInfo(name="demo"),
        repository=RepositoryInfo(root_path=".", is_git_repository=False),
        modules=[
            Module(
                name="api",
                path="api",
                type=ModuleType.SERVICE,
                depends_on=["common"],
            )
        ],
        technologies=[
            Technology(
                name="FastAPI",
                evidence=[
                    Evidence(
                        source_file="pyproject.toml",
                        source_type=EvidenceType.BUILD_FILE,
                    )
                ],
            )
        ],
        project_dependencies=[
            Dependency(
                name="fastapi",
                ecosystem="PyPI",
                scope=DependencyScope.RUNTIME,
            )
        ],
        metadata=_metadata(),
    )
    assert context.project.name == "demo"
    assert "dependencies" not in ProjectContext.model_fields
    assert len(context.project_dependencies) == 1


def test_project_context_partial_status() -> None:
    context = ProjectContext(
        project=ProjectInfo(name="demo"),
        repository=RepositoryInfo(root_path=".", is_git_repository=True),
        metadata=_metadata(AnalysisStatus.PARTIAL),
    )
    assert context.modules == []
    assert context.technologies == []
    assert context.project_dependencies == []
    assert context.metadata.analysis_status is AnalysisStatus.PARTIAL


def test_project_context_collection_defaults_independent() -> None:
    a = ProjectContext(
        project=ProjectInfo(name="a"),
        repository=RepositoryInfo(root_path=".", is_git_repository=False),
        metadata=_metadata(),
    )
    b = ProjectContext(
        project=ProjectInfo(name="b"),
        repository=RepositoryInfo(root_path=".", is_git_repository=False),
        metadata=_metadata(),
    )
    a.modules.append(Module(name="m", path="m", type=ModuleType.LIBRARY))
    assert b.modules == []


def test_project_context_round_trip() -> None:
    context = _minimal_context()
    dumped = context.model_dump(mode="json")
    restored = ProjectContext.model_validate(dumped)
    assert restored.project.name == "demo"
    assert isinstance(restored.metadata.generated_at, datetime)
    assert restored.model_dump_json()


def test_project_context_json_mode_serialization() -> None:
    """T-14: datetime serializes to a JSON-friendly string in mode=json."""
    context = _minimal_context()
    dumped = context.model_dump(mode="json")
    assert isinstance(dumped["metadata"]["generated_at"], str)


def test_project_context_json_string_round_trip() -> None:
    """T-15: true JSON string round-trip via dump_json / validate_json."""
    context = _minimal_context()
    json_data = context.model_dump_json()
    restored = ProjectContext.model_validate_json(json_data)
    assert restored == context


def test_project_context_missing_required_fails() -> None:
    with pytest.raises(ValidationError):
        ProjectContext.model_validate(
            {
                "project": {"name": "demo"},
                "repository": {"root_path": ".", "is_git_repository": False},
            }
        )


def test_project_context_rejects_legacy_dependencies_field_as_alias() -> None:
    """Ensure ownership field is project_dependencies, not dependencies."""
    context = ProjectContext(
        project=ProjectInfo(name="demo"),
        repository=RepositoryInfo(root_path=".", is_git_repository=False),
        metadata=_metadata(),
    )
    assert hasattr(context, "project_dependencies")
    assert not hasattr(context, "dependencies")

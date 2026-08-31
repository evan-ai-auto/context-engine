"""Contract tests for Dependency."""

import pytest
from pydantic import ValidationError

from ai_context.domain import Dependency, DependencyScope, Evidence, EvidenceType


def test_dependency_ecosystem_is_string() -> None:
    dep = Dependency(name="requests", ecosystem="PyPI")
    assert dep.ecosystem == "PyPI"
    assert dep.scope is None
    assert dep.declared_by is None
    assert dep.evidence == []


def test_dependency_optional_fields_and_evidence() -> None:
    dep = Dependency(
        name="spring-boot-starter-web",
        ecosystem="Maven",
        version="2.7.18",
        scope=DependencyScope.COMPILE,
        declared_by="user-service",
        evidence=[
            Evidence(source_file="pom.xml", source_type=EvidenceType.BUILD_FILE),
            Evidence(source_file="pom.xml", source_type=EvidenceType.MANIFEST),
        ],
    )
    assert len(dep.evidence) == 2
    assert dep.declared_by == "user-service"


def test_dependency_missing_ecosystem_fails() -> None:
    with pytest.raises(ValidationError):
        Dependency.model_validate({"name": "requests"})


def test_dependency_invalid_scope_fails() -> None:
    with pytest.raises(ValidationError):
        Dependency.model_validate(
            {
                "name": "x",
                "ecosystem": "npm",
                "scope": "compileOnly",
            }
        )

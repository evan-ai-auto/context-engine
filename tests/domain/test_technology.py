"""Contract tests for Technology."""

import pytest
from pydantic import ValidationError

from ai_context.domain import Evidence, EvidenceType, Technology


def test_technology_evidence_defaults_empty() -> None:
    tech = Technology(name="Spring Boot")
    assert tech.evidence == []
    assert tech.category is None
    assert tech.version is None


def test_technology_multiple_evidence() -> None:
    tech = Technology(
        name="Spring Boot",
        category="framework",
        version="2.7.18",
        evidence=[
            Evidence(source_file="pom.xml", source_type=EvidenceType.BUILD_FILE),
            Evidence(
                source_file="README.md",
                source_type=EvidenceType.OTHER,
                detail="mentions Spring Boot",
            ),
        ],
    )
    assert len(tech.evidence) == 2


def test_technology_evidence_independent_defaults() -> None:
    a = Technology(name="a")
    b = Technology(name="b")
    a.evidence.append(
        Evidence(source_file="a.txt", source_type=EvidenceType.OTHER)
    )
    assert b.evidence == []


def test_technology_missing_name_fails() -> None:
    with pytest.raises(ValidationError):
        Technology.model_validate({})

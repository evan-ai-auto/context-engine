"""Contract tests for Evidence."""

import pytest
from pydantic import ValidationError

from ai_context.domain import Evidence, EvidenceType


def test_evidence_required_fields() -> None:
    evidence = Evidence(source_file="pom.xml", source_type=EvidenceType.BUILD_FILE)
    assert evidence.source_file == "pom.xml"
    assert evidence.detail is None


def test_evidence_optional_detail() -> None:
    evidence = Evidence(
        source_file="pom.xml",
        source_type=EvidenceType.BUILD_FILE,
        detail="parent pom",
    )
    assert evidence.detail == "parent pom"


def test_evidence_missing_required_fails() -> None:
    with pytest.raises(ValidationError):
        Evidence.model_validate({"source_file": "pom.xml"})


@pytest.mark.parametrize("source_type", list(EvidenceType))
def test_evidence_accepts_each_frozen_source_type(
    source_type: EvidenceType,
) -> None:
    evidence = Evidence(source_file="artifact.txt", source_type=source_type)
    assert evidence.source_type is source_type

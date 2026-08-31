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

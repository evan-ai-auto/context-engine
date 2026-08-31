"""Contract tests for GenerationMetadata."""

from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from ai_context.domain import AnalysisStatus, GenerationMetadata


def test_generated_at_native_datetime() -> None:
    meta = GenerationMetadata(
        engine_version="0.1.0",
        schema_version="1.0",
        generated_at=datetime(2026, 8, 31, 12, 0, tzinfo=timezone.utc),
        analysis_status=AnalysisStatus.COMPLETED,
    )
    assert isinstance(meta.generated_at, datetime)


def test_generated_at_iso_string_parses_to_datetime() -> None:
    meta = GenerationMetadata.model_validate(
        {
            "engine_version": "0.1.0",
            "schema_version": "1.0",
            "generated_at": "2026-08-31T12:00:00+00:00",
            "analysis_status": "partial",
        }
    )
    assert isinstance(meta.generated_at, datetime)
    assert meta.analysis_status is AnalysisStatus.PARTIAL


def test_generated_at_invalid_rejected() -> None:
    with pytest.raises(ValidationError):
        GenerationMetadata.model_validate(
            {
                "engine_version": "0.1.0",
                "schema_version": "1.0",
                "generated_at": "not-a-datetime",
                "analysis_status": "completed",
            }
        )


def test_analysis_status_invalid_rejected() -> None:
    with pytest.raises(ValidationError):
        GenerationMetadata.model_validate(
            {
                "engine_version": "0.1.0",
                "schema_version": "1.0",
                "generated_at": "2026-08-31T12:00:00Z",
                "analysis_status": "running",
            }
        )

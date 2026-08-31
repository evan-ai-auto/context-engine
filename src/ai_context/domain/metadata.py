"""Context generation metadata."""

from datetime import datetime

from pydantic import BaseModel

from ai_context.domain.enums import AnalysisStatus


class GenerationMetadata(BaseModel):
    engine_version: str
    schema_version: str
    generated_at: datetime
    analysis_status: AnalysisStatus

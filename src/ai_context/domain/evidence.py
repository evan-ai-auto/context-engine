"""Evidence supporting analysis results."""

from pydantic import BaseModel

from ai_context.domain.enums import EvidenceType


class Evidence(BaseModel):
    source_file: str
    source_type: EvidenceType
    detail: str | None = None

"""Contract tests for frozen domain enums."""

import pytest

from ai_context.domain import (
    AnalysisStatus,
    DependencyScope,
    EvidenceType,
    ModuleType,
)


@pytest.mark.parametrize(
    ("enum_cls", "values"),
    [
        (
            ModuleType,
            {"application", "library", "service", "tool", "unknown"},
        ),
        (
            DependencyScope,
            {
                "compile",
                "runtime",
                "test",
                "development",
                "optional",
                "unknown",
            },
        ),
        (
            EvidenceType,
            {
                "build_file",
                "lock_file",
                "manifest",
                "source",
                "config",
                "other",
            },
        ),
        (
            AnalysisStatus,
            {"pending", "partial", "completed", "failed"},
        ),
    ],
)
def test_enum_members_exact(enum_cls: type, values: set[str]) -> None:
    assert {member.value for member in enum_cls} == values
    for value in values:
        member = enum_cls(value)
        assert isinstance(member, str)
        assert member == value


@pytest.mark.parametrize(
    "enum_cls",
    [ModuleType, DependencyScope, EvidenceType, AnalysisStatus],
)
def test_invalid_enum_rejected(enum_cls: type) -> None:
    with pytest.raises(ValueError):
        enum_cls("not-a-valid-member")

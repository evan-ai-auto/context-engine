"""Contract tests for Module."""

import pytest
from pydantic import ValidationError

from ai_context.domain import Module, ModuleType


def test_module_depends_on_defaults_empty() -> None:
    module = Module(name="api", path="services/api", type=ModuleType.SERVICE)
    assert module.depends_on == []
    assert module.language is None
    assert module.build_tool is None


def test_module_depends_on_list() -> None:
    module = Module(
        name="api",
        path="services/api",
        type=ModuleType.SERVICE,
        depends_on=["common"],
        language="java",
        build_tool="maven",
    )
    assert module.depends_on == ["common"]


def test_module_depends_on_independent_defaults() -> None:
    a = Module(name="a", path="a", type=ModuleType.LIBRARY)
    b = Module(name="b", path="b", type=ModuleType.LIBRARY)
    a.depends_on.append("x")
    assert b.depends_on == []


def test_module_invalid_type_fails() -> None:
    with pytest.raises(ValidationError):
        Module.model_validate(
            {"name": "a", "path": "a", "type": "not-a-module-type"}
        )

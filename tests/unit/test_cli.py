"""CLI smoke tests for ai-context."""

from typer.testing import CliRunner

from ai_context import __version__
from ai_context.cli.main import app

runner = CliRunner()


def test_cli_help() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout
    assert "ai-context" in result.stdout


def test_cli_version() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_cli_init_placeholder() -> None:
    result = runner.invoke(app, ["init"])
    assert result.exit_code == 1
    assert "not implemented" in result.stdout.lower()

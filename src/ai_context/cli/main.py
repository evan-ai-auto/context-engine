"""Typer CLI entry point for AI Context Engine."""


import typer

from ai_context import __version__

app = typer.Typer(
    name="ai-context",
    help="AI Context Engine — project context for AI coding agents.",
    no_args_is_help=True,
    add_completion=False,
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    version: bool | None = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    """AI Context Engine CLI."""


@app.command("init")
def init_command() -> None:
    """Initialize project context (not implemented yet; exits with status 1)."""
    typer.echo(
        "Initialization is not implemented yet (exits with status 1). "
        "This is a placeholder from TASK-001 project setup."
    )
    raise typer.Exit(code=1)


if __name__ == "__main__":
    app()

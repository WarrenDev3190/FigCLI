# ~*~ encoding: utf-8 ~*~
"""
    fig_cli.cli
    ~~~~~~~~~~~

    This module describes components and functions related to the 
    Fig Command Line Interface.
"""
import os
import sys
import click
import pathlib
import subprocess
from cookiecutter.main import cookiecutter
from . import __version__


HERE = pathlib.Path(__file__).parent
FIG_TEMPLATE_FOLDER = HERE.joinpath("fig_project_template/")


@click.group()
def fig():
    pass


@click.command()
def version():
    click.echo(__version__)


@click.command(help="This command creates a new Fig project in the current working directory with a given [name].")
@click.argument("new", nargs=1)
def new(new):
    click.echo(f"Creating project with name {new}")
    cookiecutter(str(FIG_TEMPLATE_FOLDER), no_input=True,
                 extra_context={'project_name': new})


@click.command(help="This command starts up a development mode server to allow for local API testing, in the foreground. Stop it with CTL+C.")
def serve():
    CUR_DIR = pathlib.Path(os.getcwd())
    APP_PY = (CUR_DIR / "app.py")
    if not APP_PY.exists() or not APP_PY.is_file():
        click.echo("--- Required file [app.py] not found ---")
        click.echo("Are you sure you're in a Fig project?")
        sys.exit(4)
    click.echo("Starting fig server")
    subprocess.check_call([sys.executable, "app.py"])


fig.add_command(new)
fig.add_command(serve)
fig.add_command(version)

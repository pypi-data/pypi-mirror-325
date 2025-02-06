# flasklaunch/flasklaunch/cli.py

import click
from flasklaunch.commands import init_project, add_api, add_db, add_web, generate_requirements, run_app, create_db, drop_db, version

# Grupo de comandos CLI
@click.group()
def cli():
    pass

# Registra todos os comandos
cli.add_command(init_project)
cli.add_command(add_api)
cli.add_command(add_db)
cli.add_command(add_web)
cli.add_command(generate_requirements)
cli.add_command(run_app)
cli.add_command(create_db)
cli.add_command(drop_db)
cli.add_command(version)

if __name__ == "__main__":
    cli()


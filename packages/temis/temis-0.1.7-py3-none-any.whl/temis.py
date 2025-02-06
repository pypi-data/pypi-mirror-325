import click
import src.project_management as project_management
import src.info as info

@click.group()
def cli() -> None:
    pass

cli.add_command(project_management.create_project)
cli.add_command(info.info)
cli.add_command(info.config)


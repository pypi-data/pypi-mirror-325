import click
from src.config import data

@click.command()
def info():
    click.secho("""
    A python project manager for using virtual envs and a requirements.txt file.
    Aimed for working with VSCode devcontainers, as poetry does not supports this %100
                """, fg='black')
    
@click.command()
def config():
    config: dict = data['config']
    for k,v in config.items():
        click.echo('\t- ',nl=False)
        click.secho(f"{k}: ", fg='blue', nl=False)
        click.secho(v, fg='green',nl=True)
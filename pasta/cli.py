import click
from pasta import commands

@click.group()
def cli():
    pass

cli.add_command(commands.touch)
cli.add_command(commands.merge)
import click

@click.command()
def hello():
    """Print Hello World!"""
    click.echo("Hello World!")
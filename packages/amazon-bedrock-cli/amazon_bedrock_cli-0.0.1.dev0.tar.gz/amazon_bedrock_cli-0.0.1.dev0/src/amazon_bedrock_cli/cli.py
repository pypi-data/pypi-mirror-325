import click

from amazon_bedrock import Bedrock

from .commands import list, run


client = Bedrock()

@click.group()
def cli():
    pass

cli.add_command(list)
cli.add_command(run)


if __name__ == "__main__":
    cli()

import click

from .. import bedrock


@click.command()
def list():
    client = bedrock.get_client()
    models = client.models.list()
    for model in models:
        print(model["modelId"])

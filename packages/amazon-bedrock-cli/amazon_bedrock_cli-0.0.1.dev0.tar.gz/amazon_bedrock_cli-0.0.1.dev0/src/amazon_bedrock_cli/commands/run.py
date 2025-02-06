import click

from .. import bedrock


@click.command()
@click.argument("model")
@click.argument("prompt")
def run(model: str, prompt: str):
    client = bedrock.get_client()
    
    response = client.messages.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=model
    )

    print(response.content[-1].text)
    

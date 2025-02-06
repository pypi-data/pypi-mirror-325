import click
from endpoints.cli.sagemaker import sagemaker
from endpoints.cli.snowflake import snowflake


@click.group()
def cli():
    """
    A command line interface for deploying JSL models to various platforms.

    """
    pass


cli.add_command(sagemaker)
cli.add_command(snowflake)

if __name__ == "__main__":
    from endpoints.cli import *

    cli()

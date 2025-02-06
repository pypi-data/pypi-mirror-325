import click

from endpoints.cli.options import common_options
from endpoints.cli import internals
from endpoints.utils import Platform, Recipe


@click.group()
def snowflake():
    """
    Group of commands related to Snowflake functionality.
    """
    pass


@snowflake.command()
@common_options
@click.option(
    "--output-dir",
    help="Output directory for the Docker files. If not provided, a default directory will be used.",
)
def generate_docker_files(model: str, **kwargs):
    """
    Generates Docker files for the specified model for Snowflake.
    """

    output_dir = internals._generate_docker_files(
        model=model,
        platform=Platform.SNOWFLAKE,
        **kwargs,
    )


@snowflake.command()
@common_options
@click.option(
    "--image-name",
    default=None,
    help="Name of the Docker image to build. Defaults to the model name if not provided.",
)
@click.option(
    "--license-path",
    required=False,
    help="Path to the license file required to build the Docker image.",
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable Docker cache during build.",
)
def build_docker_image(model: str, **kwargs):
    """
    Generates Docker files for the specified model for Snowflake.
    """
    internals.build_docker_image(model=model, platform=Platform.SNOWFLAKE, **kwargs)


@snowflake.command()
@click.option("--model", required=False, help="The model to run locally.")
@click.option(
    "--language",
    required=False,
    default="en",
    help="Language of the model to load (default: 'en')",
)
@click.option(
    "--inference_model",
    required=False,
    help="Inference model to use. Must be a subclass of BaseInference",
)
@click.option(
    "--recipe",
    required=False,
    type=click.Choice([recipe.value for recipe in Recipe], case_sensitive=False),
    default=Recipe.HEALTHCARE_NLP.value,
    help="Recipe to use. Valid values: "
    + ", ".join([recipe.value for recipe in Recipe]),
)
@click.option("--port", required=False, default=8080)
def run_local(model: str, language: str, inference_model: str, recipe: str, port: int):
    """Run a local instance of the Snowflake Inference container"""
    internals.run_local(
        model=model,
        language=language,
        inference_model=inference_model,
        platform=Platform.SNOWFLAKE,
        recipe=Recipe(recipe),
        port=port,
    )

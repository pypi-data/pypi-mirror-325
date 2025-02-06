import uvicorn
from endpoints.log_utils import logger
from fastapi import FastAPI
from typing import Optional, List
from endpoints.settings import JSL_DOWNLOAD_PACKAGES, DEFAULT_JOHNSNOWLABS_VERSION

from endpoints.johnsnowlabs.inference.model import BaseInferenceModel
from endpoints.johnsnowlabs.inference.medical_nlp_model import MedicalNlpInferenceModel
from endpoints.pip_utils import install
from endpoints import Platform, Recipe
from endpoints.log_utils import configure_logging
from .routers import healthcheck


def get_requirements(
    platform: Platform,
    johnsnowlabs_version: Optional[str] = None,
    inference: Optional[BaseInferenceModel] = None,
) -> List[str]:
    """
    Generates a list of requirements  for the specified platform and inference model.

    :param str johnsnowlabs_version: The version of the John Snow Labs library.
    :param Platform platform: The platform for which the requirements are being generated.
    :param BaseInferenceModel inference: The inference model to include in the requirements.

    Returns:
        List[str] : A list of requirements.
    """
    requirements = []
    if johnsnowlabs_version:
        requirements = [f"johnsnowlabs=={johnsnowlabs_version}"]

    additional_packages = platform.get_python_requirements()
    if inference:
        additional_packages.extend(inference.get_python_requirements())
    additional_packages = [
        package
        for package in additional_packages
        if not package.startswith("johnsnowlabs")
    ]
    ##TODO: Add checks for requirements conflicts
    requirements.extend(additional_packages)

    return requirements


def _create_fast_api_app(
    inference_model: BaseInferenceModel,
    include_sagemaker_route=False,
    include_snowflake_route=False,
):
    from contextlib import asynccontextmanager

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        inference_model.predict({inference_model._input._field: "Sample request"})

        yield {"model": inference_model}

        inference_model.dispose()

    app = FastAPI(lifespan=lifespan)
    configure_logging()

    app.include_router(healthcheck.router)
    if include_sagemaker_route:
        from .routers import sagemaker

        app.include_router(sagemaker.router)
    if include_snowflake_route:
        from .routers import snowflake

        app.include_router(snowflake.router)
    return app


def serve(
    platform: Platform,
    port: int = 8080,
    inference_model: Optional[BaseInferenceModel] = None,
):
    """
    Serve the model for inferencing

    :param str platform: The platform for which the container is being served.
    :param int port: The port on which the container should be served.
    :param BaseInferenceModel inference_model: The inferencing logic to use..
    """
    if not inference_model:
        inference_model = MedicalNlpInferenceModel()

    app = _create_fast_api_app(
        inference_model,
        include_sagemaker_route=(platform == Platform.SAGEMAKER),
        include_snowflake_route=(platform == Platform.SNOWFLAKE),
    )

    uvicorn.run(app, host="0.0.0.0", port=port)


def setup_env(
    platform: Platform,
    inference_model: BaseInferenceModel,
    model: Optional[str],
    language: str = "en",
    recipe: Recipe = Recipe.HEALTHCARE_NLP,
    johnsnowlabs_version: str = DEFAULT_JOHNSNOWLABS_VERSION,
):
    """
    Install the required packages and download the model and setup the environment

    :param str platform: The platform for which the container is being served.
    :param BaseInferenceModel inference_model: The inferencing logic to use.
    :param str model: The model to download. If None, no model is downloaded.
    :param str language: The language of the model to download. Default: 'en'.
    :param Recipe recipe: The recipe to use for the model. Default: Recipe.HEALTHCARE_NLP.
    :param str johnsnowlabs_version: The version of the John Snow Labs library.
    """
    install_python_requirements(platform, inference_model, johnsnowlabs_version)
    if model:
        from endpoints.model import download_model

        download_model(
            model=model,
            language=language,
            recipe=recipe,
        )


def setup_env_and_start_server(
    platform: Platform,
    model: Optional[str] = None,
    recipe: Recipe = Recipe.HEALTHCARE_NLP,
    inference_model: Optional[BaseInferenceModel] = None,
    language: str = "en",
    port: int = 8080,
):
    """
    Setup the environment and start the inferencing server

    :param str platform: The platform for which the container is being served.
    :param str model: The model to download. If None, no model is downloaded.
    :param Recipe recipe: The recipe to use for the model.
    :param BaseInferenceModel inference_model: The inferencing logic to use.
    :param str language: The language of the model to download. Default: 'en'.
    :param int port: The port on which the container should be served. Default: 8080.
    """
    inference_model_obj = inference_model or recipe.get_default_inference_model()
    setup_env(
        model=model,
        recipe=recipe,
        inference_model=inference_model_obj,
        language=language,
        platform=platform,
    )
    serve(
        platform=platform,
        port=port,
        inference_model=inference_model_obj,
    )


def install_python_requirements(
    platform: Platform,
    inference_model: BaseInferenceModel,
    johnsnowlabs_version: Optional[str] = None,
):
    if not JSL_DOWNLOAD_PACKAGES:
        logger.info("Skipping installation of python requirements")
    else:
        requirements = get_requirements(
            platform=platform,
            inference=inference_model,
            johnsnowlabs_version=johnsnowlabs_version,
        )
        install(requirements)

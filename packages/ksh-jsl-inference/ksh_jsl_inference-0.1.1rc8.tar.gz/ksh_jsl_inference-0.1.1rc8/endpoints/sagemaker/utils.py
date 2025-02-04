import os
import re
import subprocess
from endpoints.log_utils import logger
from endpoints.utils import ProgressPercentage


def get_aws_client(service_name: str):
    """
    Utility function to initialize and return an AWS service client.

    :param service_name: Name of the AWS service (e.g., 's3', 'ecr').
    :return: Boto3 client for the specified service.
    """
    import boto3

    return boto3.client(service_name)


def upload_model_to_s3(file_path: str, bucket_name: str, s3_key: str):
    """
    Uploads a model file to an S3 bucket.

    :param file_path: Path to the model file to upload.
    :param bucket_name: Name of the S3 bucket.
    :param s3_key: S3 key (path) where the file will be stored.
    """
    s3_client = get_aws_client("s3")
    try:
        file_size = os.path.getsize(file_path)
        progress_tracker = ProgressPercentage(file_size)

        with open(file_path, "rb") as f:
            s3_client.upload_fileobj(
                f,
                bucket_name,
                s3_key,
                Callback=progress_tracker.upload_callback,
            )

        logger.info(f"Model file {file_path} uploaded to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        logger.error(f"Failed to upload model to S3: {str(e)}")
        raise


def push_image_to_ecr(local_image: str, target_repo: str, image_tag: str) -> str:
    """
    Pushes a Docker image to an ECR repository.

    :param local_image: Name of the local Docker image to push.
    :param target_repo: Name of the ECR repository.
    :param image_tag: Tag for the Docker image.
    :return: The full ECR image URI.
    """
    if not local_image or not target_repo or not image_tag:
        raise ValueError(
            "local_image, target_repo, and image_tag must be non-empty strings"
        )

    ecr_client = get_aws_client("ecr")

    try:
        try:
            logger.info(f"Creating repository '{target_repo}'...")
            ecr_client.create_repository(repositoryName=target_repo)
            logger.info(f"Repository '{target_repo}' created successfully.")
        except ecr_client.exceptions.RepositoryAlreadyExistsException:
            logger.info(f"Repository '{target_repo}' already exists. Proceeding...")

        auth_response = ecr_client.get_authorization_token()
        endpoint = auth_response["authorizationData"][0]["proxyEndpoint"]
        ecr_image_uri = f"{endpoint.replace('https://', '')}/{target_repo}:{image_tag}"
        subprocess.run(["docker", "tag", local_image, ecr_image_uri], check=True)

        logger.info(f"Pushing Docker image to ECR: {ecr_image_uri}")
        subprocess.run(["docker", "push", ecr_image_uri], check=True)
        logger.info(f"Successfully pushed Docker image to ECR: {ecr_image_uri}")

        return ecr_image_uri

    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to push Docker image to ECR: {str(e)}")
        logger.error(f"Command error output: {e.stderr}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while pushing Docker image: {str(e)}")
        raise


def format_for_sagemaker(name: str) -> str:
    """
    Formats a string to comply with SageMaker's naming conventions.
    - Replaces invalid characters (anything other than alphanumeric or hyphens) with hyphens.
    - Ensures the name starts and ends with an alphanumeric character.
    - Truncates the name if it exceeds the maximum length (63 characters).
    """

    formatted_name = re.sub(r"[^a-zA-Z0-9-]+", "-", name)

    formatted_name = formatted_name.strip("-")

    return formatted_name[:63]

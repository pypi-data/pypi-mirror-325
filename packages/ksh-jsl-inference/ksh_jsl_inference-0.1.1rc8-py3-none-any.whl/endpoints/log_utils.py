import logging
import os

LOG_ROOT_NAME = "jsl_inference"

logger = logging.getLogger(LOG_ROOT_NAME)
logger.addHandler(logging.NullHandler())


def configure_logging():
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(level=log_level)

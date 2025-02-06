import os
from endpoints.utils import Platform


MODEL_LOCATION = "/opt/ml/model"
__version__ = "0.1.1rc9"

DEFAULT_JOHNSNOWLABS_VERSION = "5.5.0"
JSL_DOWNLOAD_PACKAGES = os.environ.get("JSL_DOWNLOAD_PACKAGES", True)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGE_NAME = "ksh-jsl-inference"
TARGET_PLATFORM = Platform(os.environ.get("PLATFORM", "sagemaker"))

import os
import logging

from .client import AsyncAIssociateClient
from .models import Law


logging.basicConfig(datefmt="%Y-%m-%d %H:%M:%S")
logger: logging.Logger = logging.getLogger("aissociate")

log_level = os.environ.get("AISSOCIATE_LOG_LEVEL", "debug")
if log_level == "debug":
    logger.setLevel(logging.DEBUG)
elif log_level == "warning":
    logger.setLevel(logging.WARNING)
elif log_level == "error":
    logger.setLevel(logging.ERROR)
else:
    logger.setLevel(logging.INFO)

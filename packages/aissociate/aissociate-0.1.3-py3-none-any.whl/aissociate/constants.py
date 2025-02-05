import os
import httpx


BASE_URL = "https://aissociate.at"
DEFAULT_TIMEOUT = httpx.Timeout(timeout=200.0, connect=5.0)
API_KEY = os.environ.get("AISSOCIATE_API_KEY")

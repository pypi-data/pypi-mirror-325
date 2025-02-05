import httpx
import logging

from typing import AsyncGenerator
from .constants import DEFAULT_TIMEOUT, BASE_URL, API_KEY
from .models import Message, Event, Law
from .exceptions import AIssociateError, AIssociateAPIError
from .parser import parse_chunk as _parse_chunk


logger = logging.getLogger(__name__)


def handle_event(event: Event) -> Message:
    if isinstance(event, Message):
        return event
    else:
        raise AIssociateAPIError(event.text)


class BaseClient:
    """
    A base client for interacting with the AI:ssociate API.

    This class provides basic API client functionality, including authentication via an API key
    and setting up default request headers.

    Attributes:
        base_url (str): The base URL for API requests.
        api_key (str): The API key used for authentication.
        headers (dict): Default headers for API requests.
    """

    def __init__(self, api_key: str, base_url: str) -> None:
        self.base_url = base_url

        if api_key is None:
            raise AIssociateError(
                "The api_key parameter must be set either by passing it directly to the " +
                "client or by exporting the AISSOCIATE_API_KEY environment variable."
            )
        self.api_key = api_key
        self.headers = {
            'x-api-key': self.api_key,
            'Content-Type': 'application/json'
        }


class AsyncAIssociateClient(BaseClient):
    """
    An asynchronous client for interacting with the AI:ssociate API.

    This client extends `BaseClient` and provides asynchronous methods for sending queries and
    streaming responses.

    Attributes:
        _client (httpx.AsyncClient): An HTTPX asynchronous client with a configured timeout.
    """

    def __init__(self, api_key: str = API_KEY, base_url: str = BASE_URL) -> None:
        super().__init__(api_key, base_url)
        self._client = httpx.AsyncClient(timeout=DEFAULT_TIMEOUT)

    def ask(self, question: str, law: Law = Law.CIVIL):
        """
        Sends a query to the AI:ssociate API.

        Args:
            question (str): The user's legal question.
            law (Law, optional): The type of law to apply. Defaults to `Law.CIVIL`.

        Returns:
            AsyncGenerator[Message, None]: A generator that yields messages from the API response.
        """
        payload = {
            "question": question,
            "law": law.value,
            "file_context": []
        }

        return self._stream_response("/api/public/v1/chat/ask", payload)

    async def _stream_response(self, endpoint: str, payload: dict) -> AsyncGenerator[Message, None]:
        """
        Streams a response from the AI:ssociate API.

        This function handles partial event chunks and buffers them until complete events can be parsed.

        Args:
            endpoint (str): The API endpoint to send the request to.
            payload (dict): The JSON payload for the request.

        Yields:
            Message: Parsed messages from the event stream.

        Raises:
            AIssociateAPIError: If an error event is received.
        """
        url = f"{self.base_url}{endpoint}"

        try:
            async with self._client.stream("POST", url, headers=self.headers, json=payload) as response:
                if response.status_code == 200:
                    buffer = ""
                    async for chunk in response.aiter_text():
                        buffer += chunk
                        events: list = _parse_chunk(chunk)

                        if events:
                            for event in events:
                                try:
                                    yield handle_event(event)
                                except AIssociateAPIError as e:
                                    logger.error(e)

                        if not buffer.endswith("\n\n") and not buffer.endswith("\r\n\r\n"):
                            continue
                        else:
                            buffer = ""
                else:
                    logger.error(f"Request failed with status code {response.status_code}")
        except httpx.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")

    async def close(self):
        await self._client.aclose()

    async def __aexit__(self) -> None:
        await self.close()


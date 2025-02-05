import re
import json
import logging

from typing import List, Union
from .models.events import Message, Error, EventSource, EventType


logger = logging.getLogger(__name__)


def parse_chunk(chunk) -> List[Union[Message, Error]]:
    """
    Parses a chunk of Server-Sent Events (SSE) data and extracts individual events.

    This function splits the input chunk into multiple events based on double newlines (`\r\n\r\n` or `\n\n`),
    processes each event, and extracts key-value pairs such as `id`, `event`, and `data`. If the event data
    contains JSON, it is parsed into a `Message` or `Error` object based on the event type.

    Args:
        chunk (str or bytes): The raw SSE data chunk received from the server.

    Returns:
        List[Union[Message, Error]]: A list of parsed `Message` or `Error` objects extracted from the chunk.

    Raises:
        None: Invalid JSON data is logged and converted into an `Error` object instead of raising an exception.

    Example:
        >>> chunk = "id: 1\n event: message\n data: {\"meta\": null, \"text\": \"Hello\", \"type\": \"message\"}\n\n"
        >>> parse_chunk(chunk)
        [Message(meta=None, text="Hello", type="message")]
    """
    if not isinstance(chunk, str):
        chunk = chunk.decode('utf-8')

    events = re.split(r'\r?\n\r?\n', chunk.strip())
    parsed_messages = []

    for event_chunk in events:
        lines = event_chunk.splitlines()
        chunk_data = {}

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if ':' in line:
                key, value = line.split(':', 1)
                chunk_data[key.strip()] = value.strip()
            else:
                chunk_data[line.strip()] = ''

        if {'id', 'event', 'data'}.issubset(chunk_data):
            event = EventSource(chunk_data['id'], chunk_data['event'], chunk_data['data'])

            try:
                json_data = json.loads(event.data)

                if event.event == EventType.MESSAGE:
                    parsed_messages.append(
                        Message(
                            _meta=json_data['meta'],
                            _text=json_data['text'],
                            _type=json_data['type']
                        )
                    )
                elif event.event == EventType.ERROR:
                    parsed_messages.append(Error(_text=json_data['text']))
            except json.JSONDecodeError:
                parsed_messages.append(Error(_text="Invalid JSON in event data."))

    return parsed_messages


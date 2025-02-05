import json
from enum import StrEnum


class MessageType(StrEnum):
    MESSAGE = "message"
    DOCUMENT_NUMBER = "document_number"


class EventType(StrEnum):
    MESSAGE = "message"
    ERROR = "error"


class EventSource:
    def __init__(self, _id: str, _event: EventType, _data: str):
        self.id = _id
        self.event = _event
        self.data = _data

    def __str__(self):
        return f"{self.id}\n{self.event}\n{self.data}"


class Event:
    def __init__(self, _text: str):
        self.text = _text


class Message(Event):
    def __init__(self, _meta: dict, _text: str, _type: MessageType):
        super().__init__(_text)
        self.meta = _meta
        self.type = _type


class Error(Event):
    def __init__(self, _text: str):
        super().__init__(_text)

import asyncio
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, Coroutine, Union

from fastapi import WebSocket
from loguru import logger


class AbstractSender(ABC):
    """
    An abstract base class for WebSocket message senders.

    This class provides a framework for sending structured JSON messages to connected WebSocket clients.
    Subclasses must implement the `event_name` and `create_message_data` methods.

    Attributes:
        _connections (set[WebSocket]): A private set storing active WebSocket connections.
    """

    def __init__(self):
        """
        Initializes the sender with an empty list of WebSocket connections.
        """
        self._connections: set[WebSocket] = set()

    @property
    @abstractmethod
    def event_name(self) -> str:
        """
        Abstract property to define the event name.

        Subclasses must override this property to specify the name of the event
        that will be included in the message payload.

        Returns:
            str: The event name.
        """
        raise NotImplementedError("Must specify 'event_name' in inherited Sender")

    async def send(self) -> None:
        """
        Sends a JSON message to all connected WebSocket clients.

        The message contains the event name, data provided by `create_message_data`,
        and a timestamp.

        Raises:
            Exception: If sending fails for any connection.
        """
        timestamp = datetime.now().isoformat()

        message_data = self.create_message_data()

        if asyncio.iscoroutine(message_data):
            message_data = await message_data

        message = {
            "event": self.event_name,
            "data": message_data,
            "timestamp": timestamp
        }

        for connection in self._connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Failed to send message: {e}")

    @abstractmethod
    def create_message_data(self) -> Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
        """
        Generates the payload for a WebSocket message.

        This method must be implemented by subclasses to define the structure of the message being sent.
        It can be either synchronous (returning a dictionary) or asynchronous (returning a coroutine).

        Returns:
            Union[Dict[str, Any], Coroutine[Any, Any, Dict[str, Any]]]:
            - A dictionary representing the message payload if implemented synchronously.
            - A coroutine resolving to a dictionary if implemented asynchronously.
        """
        raise NotImplementedError()

    def add_connection(self, websocket: WebSocket) -> None:
        """
        Adds a WebSocket connection to the sender.

        Args:
            websocket (WebSocket): The WebSocket connection to be added.
        """
        if websocket not in self._connections:
            self._connections.add(websocket)

    def remove_connection(self, websocket: WebSocket) -> None:
        """
        Removes a WebSocket connection from the sender.

        Args:
            websocket (WebSocket): The WebSocket connection to be removed.

        Raises:
            ValueError: If the WebSocket connection is not found in the list.
        """
        if websocket in self._connections:
            self._connections.remove(websocket)

    def has_connection(self, websocket: WebSocket) -> bool:
        """
        Checks if the sender connected to the specified WebSocket.
        Args:
            websocket (WebSocket): The WebSocket connection to be checked.

        Returns:
            bool: if the WebSocket connection is found in the list.
        """
        return websocket in self._connections

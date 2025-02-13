"""Utility functions for the IO module."""

from dataclasses import dataclass
from enum import Enum
from multiprocessing import Queue

import dill

from .base import EMDataBase as EMData

# from .types import EMData
# from . import EMData


class StatusFlags(Enum):
    """Message classification for status messages."""

    INFO = 0
    STATUS = 1
    FINISHED = 2
    WARNING = 3
    ERROR = 4


@dataclass
class StatusMessage:
    """Status message object to send status messages for the queue."""

    flag: StatusFlags
    message: str | EMData

    def __repr__(self) -> str:
        """Return the string representation of the object."""
        return f"{self.flag.name}: {self.message}"


def dump(queue: Queue, flag: StatusFlags, message: str | EMData) -> None:
    """Assemble a message and dump it to the queue.

    Args:
        queue (Queue): Multiprocessing queue to send status messages.
        flag (StatusFlags): The message classification.
        message (str | EMData): The message or data to send in the queue.
    """
    queue.put(dill.dumps(StatusMessage(flag, message)))

from abc import ABC
from typing import Generic, TypeVar

TResponse = TypeVar("TResponse")


class Request(Generic[TResponse], ABC):
    _response = TResponse

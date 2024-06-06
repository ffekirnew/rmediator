from abc import ABC
from typing import Generic, TypeVar

TResponse = TypeVar("TResponse")


class Request(Generic[TResponse], ABC):
    """
    Abstract base class for requests in the mediator pattern.

    This class serves as a base for all request types, parameterized with the type of the response they expect.

    Attributes:
        _response (TypeVar): The type of the response expected from the request.
    """

    _response = TResponse

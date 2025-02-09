from abc import ABC, abstractmethod
from typing import Annotated, Generic, TypeVar

from typing_extensions import Doc

TRequest = TypeVar("TRequest")
TResponse = TypeVar("TResponse")


class RequestHandler(Generic[TRequest, TResponse], ABC):
    """
    Abstract base class for request handlers in the mediator pattern.

    This class serves as a base for all request handlers, parameterized with the types of the request they handle and the response they return.

    Attributes:
        _request (TypeVar): The type of the request the handler processes.
        _response (TypeVar): The type of the response the handler returns.
    """

    _request = TRequest
    _response = TResponse

    @abstractmethod
    def handle(
        self, request: Annotated[TRequest, Doc("The request object to be handled.")]
    ) -> Annotated[TResponse, Doc("The response from the handler.")]:
        """
        Abstract method to handle a request and return a response.

        Args:
            request (TRequest): The request object to be handled.

        Returns:
            TResponse: The response from the handler.
        """
        ...

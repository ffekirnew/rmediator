from abc import ABC, abstractmethod
from typing import Generic, TypeVar

TRequest = TypeVar("TRequest")
TResponse = TypeVar("TResponse")


class RequestHandler(Generic[TRequest, TResponse], ABC):
    _request = TRequest
    _response = TResponse

    @abstractmethod
    def handle(self, request: TRequest) -> TResponse:
        pass

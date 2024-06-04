from abc import ABCMeta, abstractmethod
from typing import TypeVar

TRequest = TypeVar("TRequest")
TResponse = TypeVar("TResponse")


class RequestHandler(metaclass=ABCMeta):
    request = TRequest
    response = TResponse

    @abstractmethod
    def handle(self, request: TRequest) -> TResponse:
        pass

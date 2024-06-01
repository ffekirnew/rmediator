from abc import ABCMeta, abstractmethod
from typing import Generic, Type, TypeVar

TResponse = TypeVar("TResponse")


class RequestInterface(Generic[TResponse], metaclass=ABCMeta):
    response: Type[TResponse]


TRequest = TypeVar("TRequest")


class RequestHandlerInterface(Generic[TRequest, TResponse], metaclass=ABCMeta):
    request: Type[TRequest]
    response: Type[TResponse]

    @abstractmethod
    def handle(self, request: TRequest) -> TResponse:
        pass

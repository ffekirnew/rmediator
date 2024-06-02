from abc import ABCMeta
from typing import Generic, Type, TypeVar

TResponse = TypeVar("TResponse")


class RequestInterface(Generic[TResponse], metaclass=ABCMeta):
    response: Type[TResponse]

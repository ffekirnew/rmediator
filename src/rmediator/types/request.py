from abc import ABCMeta
from typing import TypeVar

TResponse = TypeVar("TResponse")


class Request(metaclass=ABCMeta):
    response = TResponse

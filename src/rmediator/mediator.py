from threading import Lock
from typing import Any

from src.rmediator.interfaces import RequestHandlerInterface, RequestInterface


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Mediator(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.__requests = {}
        self.__request_handlers = {}

    def send(self, request: RequestInterface) -> Any:
        if type(request) not in self.__requests:
            raise ValueError(
                f"Request cannot be handled, Request {type(request)} not registered."
            )

        handler = self.__request_handlers.get(type(request))
        if not handler:
            raise ValueError(
                f"Request cannot be handled, No handler has been registered for {type(request)}."
            )

        return handler.handle(request)

    def register_request(self, request: type[RequestInterface]) -> None:
        self.__requests[request] = request.response  # type: ignore

    def register_handler(self, handler: type[RequestHandlerInterface]) -> None:
        request, response = handler.request, handler.response  # type: ignore
        if request not in self.__requests:
            raise ValueError(
                f"Handler cannot be registered, Request {request} has been not registered."
            )

        if response != self.__requests[request]:
            raise ValueError(
                f"Handler cannot be registered, Handler response {response} does not match request response {self.__requests[request]}."
            )

        if request in self.__request_handlers:
            raise ValueError(
                f"Handler cannot be registered, Another handler for request type {request} has already been registered."
            )

        self.__request_handlers[request] = handler()

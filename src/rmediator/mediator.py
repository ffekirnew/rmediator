from threading import Lock
from typing import Any, Dict

from rmediator.types import Request, RequestHandler


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
        self.__request_handlers: Dict[type, RequestHandler] = {}

    def send(self, request: Request) -> Any:
        handler = self.__request_handlers.get(type(request))
        if not handler:
            raise ValueError(
                f"Request cannot be handled, No handler has been registered for {type(request)}."
            )

        return handler.handle(request)

    def register_handler(
        self, request_type: type[Request], handler: RequestHandler
    ) -> None:
        self.__check_request_validity(request_type)
        self.__check_request_handler_validity(type(handler))

        if handler.response is not request_type.response:  # type: ignore
            raise ValueError(
                f"Handler cannot be registered; handler response {handler.response} does not match request response {request_type.response}."
            )

        if request_type in self.__request_handlers:
            old_handler = self.__request_handlers[request_type]

            if type(handler) is not type(old_handler):
                raise ValueError(
                    f"Handler cannot be registered; another handler for request type {request_type} has already been registered. Check {type(self.__request_handlers[request_type])}."
                )

        self.__request_handlers[request_type] = handler

    def __check_request_validity(self, request_type: type[Request]) -> None:
        if not hasattr(request_type, "rmediator_decorated_request"):
            raise ValueError(
                f"Handler cannot be registered; the request {request_type} class has not been decorated using @request."
            )

    def __check_request_handler_validity(
        self, handler_type: type[RequestHandler]
    ) -> None:
        if not hasattr(handler_type, "rmediator_decorated_request_handler"):
            raise ValueError(
                f"Handler cannot be registered; the request handler {type(handler_type)} class has not been decorated using @request_handler."
            )

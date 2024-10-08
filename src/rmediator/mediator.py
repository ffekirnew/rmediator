from threading import Lock
from typing import Annotated

from typing_extensions import Doc

from rmediator.types import Request, RequestHandler


class SingletonMeta(type):
    """
    A thread-safe implementation of Singleton metaclass.

    This metaclass ensures that only one instance of a class is created and provides a global point of access to that instance.

    Attributes:
        _instances (dict): A dictionary to hold the single instance of each class.
        _lock (Lock): A lock object to ensure thread-safe instantiation of the singleton.
    """

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Controls the instantiation of the singleton instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            object: The single instance of the class.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Mediator(metaclass=SingletonMeta):
    """
    Mediator class to handle the registration and dispatching of requests to their corresponding handlers.

    Attributes:
        __request_handlers (dict[type, RequestHandler]): A dictionary mapping request types to their handlers.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Mediator class.
        """
        self._request_handlers: dict[type, RequestHandler] = {}
        self._lock = Lock()

    def send(
        self,
        request: Annotated[
            Request,
            Doc("The request object to be handled."),
        ],
    ):
        """
        Sends a request to its corresponding handler and returns the handler's response.

        Args:
            request (Request): The request object to be handled.

        Returns:
            Any: The response from the handler.

        Raises:
            ValueError: If no handler has been registered for the type of the request.
        """
        handler = self._request_handlers.get(type(request))
        if not handler:
            raise ValueError(
                f"Request cannot be handled; no handler has been registered for {type(request)}."
            )

        return handler.handle(request)

    def register_handler(
        self,
        request_type: Annotated[
            type[Request],
            Doc("The type of the request to be handled."),
        ],
        handler: Annotated[
            RequestHandler,
            Doc("The handler to process the request."),
        ],
    ) -> None:
        """
        Registers a handler for a specific request type.

        Args:
            request_type (type[Request]): The type of the request to be handled.
            handler (RequestHandler): The handler to process the request.

        Raises:
            ValueError: If the handler's response type does not match the request's response type,
                        or if another handler for the same request type has already been registered.
        """
        self.__check_request_validity(request_type)
        self.__check_request_handler_validity(type(handler))

        if handler._response != request_type._response:  # type: ignore
            raise ValueError(
                f"Handler cannot be registered; handler response {handler._response} does not match request response {request_type._response}."
            )

        if request_type in self._request_handlers:
            old_handler = self._request_handlers[request_type]

            if type(handler) is not type(old_handler):
                raise ValueError(
                    f"Handler cannot be registered; another handler for request type {request_type} has already been registered. Check {type(self._request_handlers[request_type])}."
                )

        self._request_handlers[request_type] = handler

    def __check_request_validity(self, request_type: type) -> None:
        """
        Checks if a request type has been decorated using @request.

        Args:
            request_type (type): The request type to be checked.

        Raises:
            ValueError: If the request type has not been decorated using @request.
        """
        if not hasattr(request_type, "_rmediator_decorated_request"):
            raise ValueError(
                f"Handler cannot be registered; the request {request_type} class has not been decorated using @request."
            )

    def __check_request_handler_validity(self, handler_type: type) -> None:
        """
        Checks if a request handler type has been decorated using @request_handler.

        Args:
            handler_type (type): The request handler type to be checked.

        Raises:
            ValueError: If the handler type has not been decorated using @request_handler.
        """
        if not hasattr(handler_type, "_rmediator_decorated_request_handler"):
            raise ValueError(
                f"Handler cannot be registered; the request handler {type(handler_type)} class has not been decorated using @request_handler."
            )

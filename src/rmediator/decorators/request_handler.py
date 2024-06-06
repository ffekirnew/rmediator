import inspect
from typing import Union


def request_handler(request_type: type, response_type: Union[type, None]):
    """
    A decorator to register a request handler class with specified request and response types.

    Args:
        request_type (type): The type of the request that the handler should process.
        response_type (Union[type, None]): The type of the response that the handler should return, or None if no response is expected.

    Returns:
        type: The decorated class.

    Raises:
        AttributeError: If the request type is None, if the class does not contain a 'handle' method,
                        or if the 'handle' method does not have exactly one parameter (excluding 'self').
        ValueError: If the type of the 'handle' method's parameter does not match the request type,
                    or if the return type of the 'handle' method does not match the response type.

    Example:
        @request_handler(RequestType, ResponseType)
        class MyHandler:
            def handle(self, request: RequestType) -> ResponseType:
                # Handle the request and return a response
                pass
    """

    def decorator(cls: type):
        if request_type is None:
            raise AttributeError(
                f"Request handler class cannot be registered; request type cannot be {None}."
            )

        if "handle" not in cls.__dict__:
            raise AttributeError(
                f"Request handler class cannot be registered; {cls} must contain method 'handle' that handles the request."
            )

        handle_method_signature = inspect.signature(cls.handle)
        if len(handle_method_signature.parameters) != 2:
            raise AttributeError(
                f"Request handler class cannot be registered; {cls} handle method must have exactly one parameter."
            )

        request_parameter = None
        for name in handle_method_signature.parameters.keys():
            if name == "self":
                continue

            request_parameter = name

        if cls.handle.__annotations__.get(request_parameter, None) != request_type:
            raise ValueError(
                f"Request handler class cannot be registered; {cls} handle method must have 'request' parameter of type {request_type}. In your method, {request_parameter} must have type {request_type}"
            )

        if cls.handle.__annotations__.get("return", None) != response_type:
            raise ValueError(
                f"Request handler class cannot be registered; {cls} handle method must have return type of {response_type}."
            )

        cls._request = request_type
        cls._response = response_type
        cls._rmediator_decorated_request_handler = True

        return cls

    return decorator

from typing import Union


def request(response_type: Union[type, None]):
    """
    A decorator to register a request class with a specified response type.

    Args:
        response_type (Union[type, None]): The type of the response expected from the request, or None if no response is expected.

    Returns:
        type: The decorated class.

    Example:
        @request(ResponseType)
        class MyRequest:
            # Define the request class
            pass
    """

    def decorator(cls: type):
        cls._response = response_type
        cls._rmediator_decorated_request = True

        return cls

    return decorator

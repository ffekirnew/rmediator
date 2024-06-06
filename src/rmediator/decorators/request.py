from typing import Annotated, Union

from typing_extensions import Doc


def request(
    response_type: Annotated[
        Union[type, None],
        Doc(
            "The type of the response expected from the request, or None if no response is expected."
        ),
    ]
):
    """
    Decorate a class to register a request class with a specified response type.

    Args:
        response_type (Annotated[Union[type, None], Doc]): The type of the response expected from the request, or None if no response is expected.

    Returns:
        decorator: The decorator function.

    Example:
    ```python
    @request(ResponseType)
    class MyRequest:
        # Define the request class
        pass
    ```
    """

    def decorator(cls: type):
        cls._response = response_type
        cls._rmediator_decorated_request = True

        return cls

    return decorator

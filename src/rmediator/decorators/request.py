from typing import Annotated, Callable, Optional, Type, TypeVar

from typing_extensions import Doc

T = TypeVar("T", bound=Type)


def request(
    response_type: Annotated[
        Optional[Type],
        Doc(
            "The expected response type for the request, or None if no response is expected."
        ),
    ]
) -> Callable[[T], T]:
    """
    Decorator to register a request class with a specified response type.

    Args:
        response_type (Annotated[Optional[Type], Doc]): Expected response type or None.

    Returns:
        Callable: A class decorator.
    """

    def decorator(cls: T) -> T:
        setattr(cls, "_response", response_type)
        setattr(cls, "_rmediator_decorated_request", True)

        return cls

    return decorator

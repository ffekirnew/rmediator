from src.rmediator import Mediator
from src.rmediator.interfaces import RequestHandlerInterface


def request_handler(cls):
    if not issubclass(cls, RequestHandlerInterface):
        raise ValueError(
            f"Request handler class cannot be registered, {cls} must be a subclass of RequestHandlerInterface."
        )

    if "request" not in cls.__dict__:
        raise ValueError(
            f"Request handler class cannot be registered, {cls} must contain attribute 'request' to signify the reequest it handles."
        )

    if "response" not in cls.__dict__:
        raise ValueError(
            f"Request handler class cannot be registered, {cls} must contain attribute 'response' to signify the response it sends after handling request."
        )

    if cls.request is None:  # type: ignore
        raise ValueError(
            f"Request handler class cannot be registered, {cls} must contain attribute 'request' to signify the request it handles."
        )

    if cls.handle.__annotations__.get("request", None) != cls.request:  # type: ignore
        raise ValueError(
            f"Request handler class cannot be registered, {cls} handle method must have 'request' parameter of type {cls.request}."  # type: ignore
        )

    if cls.handle.__annotations__.get("return", None) != cls.response:  # type: ignore
        raise ValueError(
            f"Request handler class cannot be registered, {cls} handle method must have return type of {cls.response}."  # type: ignore
        )

    try:
        Mediator().register_handler(cls)
    except ValueError as e:
        raise e

    return cls

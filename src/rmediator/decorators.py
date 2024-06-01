from rmediator.interfaces import RequestHandlerInterface, RequestInterface
from rmediator.mediator import Mediator


def request(cls):
    if not issubclass(cls, RequestInterface):
        raise ValueError(
            f"Request class cannot be registered, {cls} must be a subclass of RequestInterface."
        )

    if "response" not in cls.__dict__:
        raise ValueError(
            f"Request class cannot be registered, {cls} must contain attribute 'response' to signify the response expected for this request."
        )

    Mediator().register_request(cls)

    return cls


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

    Mediator().register_handler(cls)

    return cls

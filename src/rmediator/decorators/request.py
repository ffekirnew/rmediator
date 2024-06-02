from src.rmediator import Mediator
from src.rmediator.interfaces import RequestInterface


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

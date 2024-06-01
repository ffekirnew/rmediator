from threading import Lock

from rmediator.interfaces import RequestHandlerInterface, RequestInterface


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
    _instance = None

    def __init__(self) -> None:
        self.requests = {}
        self.request_handlers = {}

    def send(self, request: RequestInterface) -> RequestInterface.response:  # type: ignore
        if type(request) not in self.requests:
            raise ValueError(
                f"Request cannot be handled, Request {type(request)} not registered."
            )

        handler = self.request_handlers.get(type(request))
        if not handler:
            raise ValueError(
                f"Request cannot be handled, No handler has been registered for {type(request)}."
            )

        return handler.handle(request)

    def register_request(self, request: type[RequestInterface]) -> None:
        self.requests[request] = request.response  # type: ignore

    def register_handler(self, handler: type[RequestHandlerInterface]) -> None:
        request, response = handler.request, handler.response  # type: ignore
        if request not in self.requests:
            raise ValueError(
                f"Handler cannot be registered, Request {request} has been not registered."
            )

        if response != self.requests[request]:
            raise ValueError(
                f"Handler cannot be registered, Handler response {response} does not match request response {self.requests[request]}."
            )

        if request in self.request_handlers:
            raise ValueError(
                f"Handler cannot be registered, Another handler for request type {request} has already been registered."
            )

        self.request_handlers[request] = handler()

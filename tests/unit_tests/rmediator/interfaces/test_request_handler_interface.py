import unittest

from src.rmediator.interfaces import RequestHandlerInterface, RequestInterface


class TestRequestHandlerInterface(unittest.TestCase):
    def test_request_handler_interface_invalid_not_subclass(self):
        class InvalidRequestHandler:
            pass

        assert (issubclass(InvalidRequestHandler, RequestHandlerInterface)) is False
        assert (hasattr(InvalidRequestHandler, "handle")) is False

    def test_request_handler_interface_valid(self):
        class ValidRequestHandler(RequestHandlerInterface):
            def handle(self, request: RequestInterface) -> None:
                pass

        assert (issubclass(ValidRequestHandler, RequestHandlerInterface)) is True
        assert (hasattr(ValidRequestHandler, "handle")) is True
        assert (
            ValidRequestHandler.handle.__annotations__.get("request", None)
            == RequestInterface
        )
        assert ValidRequestHandler.handle.__annotations__.get("return", None) is None

    def test_request_handler_interface_invalid_no_handle(self):
        class InvalidRequestHandler(RequestHandlerInterface):
            pass

        assert (issubclass(InvalidRequestHandler, RequestHandlerInterface)) is True
        assert InvalidRequestHandler.__dict__.get("handle", None) is None

    def test_request_handler_interface_invalid_handle_wrong_type(self):
        class InvalidRequestHandler(RequestHandlerInterface):
            def handle(self, request: RequestInterface) -> None:  # type: ignore
                pass

        assert (issubclass(InvalidRequestHandler, RequestHandlerInterface)) is True
        assert (hasattr(InvalidRequestHandler, "handle")) is True
        assert (
            InvalidRequestHandler.handle.__annotations__.get("request", None)
            == RequestInterface
        )
        assert InvalidRequestHandler.handle.__annotations__.get("return", None) is None

    def test_request_handler_interface_invalid_handle_no_type(self):
        class InvalidRequestHandler(RequestHandlerInterface):
            def handle(self, request) -> None:
                pass

        assert (issubclass(InvalidRequestHandler, RequestHandlerInterface)) is True
        assert (hasattr(InvalidRequestHandler, "handle")) is True
        assert InvalidRequestHandler.handle.__annotations__.get("request", None) is None
        assert InvalidRequestHandler.handle.__annotations__.get("return", None) is None

    def test_request_handler_interface_invalid_handle_no_request(self):
        class InvalidRequestHandler(RequestHandlerInterface):
            def handle(self) -> None:  # type: ignore
                pass

        assert (issubclass(InvalidRequestHandler, RequestHandlerInterface)) is True
        assert (hasattr(InvalidRequestHandler, "handle")) is True
        assert InvalidRequestHandler.handle.__annotations__.get("request", None) is None
        assert InvalidRequestHandler.handle.__annotations__.get("return", None) is None

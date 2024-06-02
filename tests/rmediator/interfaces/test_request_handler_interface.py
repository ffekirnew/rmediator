import unittest

from src.rmediator.interfaces import RequestHandlerInterface, RequestInterface


class TestRequestHandlerInterface(unittest.TestCase):
    def test_request_handler_interface_invalid_not_subclass(self):
        class InvalidRequestHandler:
            pass

        self.assertFalse(issubclass(InvalidRequestHandler, RequestHandlerInterface))
        self.assertFalse(hasattr(InvalidRequestHandler, "handle"))

    def test_request_handler_interface_valid(self):
        class ValidRequestHandler(RequestHandlerInterface):
            def handle(self, request: RequestInterface) -> None:
                pass

        self.assertTrue(issubclass(ValidRequestHandler, RequestHandlerInterface))
        self.assertTrue(hasattr(ValidRequestHandler, "handle"))
        self.assertEqual(
            ValidRequestHandler.handle.__annotations__.get("request", None),
            RequestInterface,
        )
        self.assertEqual(
            ValidRequestHandler.handle.__annotations__.get("return", None), None
        )

    def test_request_handler_interface_invalid_no_handle(self):
        class InvalidRequestHandler(RequestHandlerInterface):
            pass

        self.assertTrue(issubclass(InvalidRequestHandler, RequestHandlerInterface))
        self.assertEqual(InvalidRequestHandler.__dict__.get("handle", None), None)

    def test_request_handler_interface_invalid_handle_wrong_type(self):
        class InvalidRequestHandler(RequestHandlerInterface):
            def handle(self, request: RequestInterface) -> None:  # type: ignore
                pass

        self.assertTrue(issubclass(InvalidRequestHandler, RequestHandlerInterface))
        self.assertTrue(hasattr(InvalidRequestHandler, "handle"))
        self.assertEqual(
            InvalidRequestHandler.handle.__annotations__.get("request", None),
            RequestInterface,
        )
        self.assertEqual(
            InvalidRequestHandler.handle.__annotations__.get("return", None), None
        )

    def test_request_handler_interface_invalid_handle_no_type(self):
        class InvalidRequestHandler(RequestHandlerInterface):
            def handle(self, request) -> None:
                pass

        self.assertTrue(issubclass(InvalidRequestHandler, RequestHandlerInterface))
        self.assertTrue(hasattr(InvalidRequestHandler, "handle"))
        self.assertEqual(
            InvalidRequestHandler.handle.__annotations__.get("request", None),
            None,
        )
        self.assertEqual(
            InvalidRequestHandler.handle.__annotations__.get("return", None), None
        )

    def test_request_handler_interface_invalid_handle_no_request(self):
        class InvalidRequestHandler(RequestHandlerInterface):
            def handle(self) -> None:  # type: ignore
                pass

        self.assertTrue(issubclass(InvalidRequestHandler, RequestHandlerInterface))
        self.assertTrue(hasattr(InvalidRequestHandler, "handle"))
        self.assertEqual(
            InvalidRequestHandler.handle.__annotations__.get("request", None),
            None,
        )
        self.assertEqual(
            InvalidRequestHandler.handle.__annotations__.get("return", None), None
        )

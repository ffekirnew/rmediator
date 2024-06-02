import unittest

from src.rmediator.interfaces import RequestInterface


class TestRequestInterface(unittest.TestCase):
    def test_request_interface_invalid_not_subclass(self):
        class InvalidRequest:
            pass

        self.assertFalse(issubclass(InvalidRequest, RequestInterface))
        self.assertFalse(hasattr(InvalidRequest, "response"))

    def test_request_interface_valid(self):
        class ValidRequest(RequestInterface):
            response = bool

        self.assertTrue(issubclass(ValidRequest, RequestInterface))
        self.assertTrue(hasattr(ValidRequest, "response"))
        self.assertEqual(ValidRequest.response, bool)  # type: ignore

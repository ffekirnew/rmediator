import unittest

from src.rmediator.decorators import request
from src.rmediator.interfaces import RequestInterface


class TestRequest(unittest.TestCase):
    def test_request_invalid_not_subclass(self):
        class InvalidRequest:
            pass

        with self.assertRaises(ValueError):
            request(InvalidRequest)

    def test_request_invalid_does_not_have_response(self):
        class InvalidRequest(RequestInterface):
            pass

        with self.assertRaises(ValueError):
            request(InvalidRequest)

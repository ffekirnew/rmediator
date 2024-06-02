import unittest

from src.rmediator.decorators import request_handler


class TestRequestHandler(unittest.TestCase):
    def test_request_handler_invalid_not_subclass(self):
        with self.assertRaises(ValueError):

            @request_handler
            class InvalidRequestHandler:
                pass

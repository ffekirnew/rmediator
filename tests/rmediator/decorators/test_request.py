import unittest

from src.rmediator.decorators import request


class TestRequest(unittest.TestCase):
    def test_request_invalid_not_subclass(self):
        with self.assertRaises(ValueError):

            @request
            class InvalidRequest:
                pass

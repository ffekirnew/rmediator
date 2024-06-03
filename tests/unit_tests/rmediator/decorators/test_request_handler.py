import unittest

from src.rmediator.decorators import request, request_handler
from src.rmediator.interfaces import RequestHandlerInterface


class TestRequestHandler(unittest.TestCase):
    def test__request_handler__not_subclass__raises_value_error(self):
        class InvalidRequestHandler:
            pass

        with self.assertRaises(ValueError):
            request_handler(InvalidRequestHandler)

    def test__request_handler__no_request_attribute__raises_value_error(self):
        class InvalidRequestHandler(RequestHandlerInterface):
            pass

        with self.assertRaises(ValueError):
            request_handler(InvalidRequestHandler)

    def test__request_handler__no_response_attribute__raises_value_error(self):
        request_class = self.__get_valid_request()

        print("Here:", request_class)

        class InvalidRequestHandler(RequestHandlerInterface):
            request = request_class

        with self.assertRaises(ValueError):
            request_handler(InvalidRequestHandler)

    def test__request_handler__no_handle_method__raises_value_error(self):
        request_class, response_class = (
            self.__get_valid_request(),
            self.__get_response(),
        )

        class InvalidRequestHandler(RequestHandlerInterface):
            request = request_class
            response = response_class

        with self.assertRaises(ValueError):
            request_handler(InvalidRequestHandler)

    def __get_valid_request(self):
        @request
        class Request:
            response = self.__get_response()

        return Request

    def __get_response(self):
        class Response:
            pass

        return Response

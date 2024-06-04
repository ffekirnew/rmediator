import pytest

from rmediator.decorators import request, request_handler


class TestRequestHandler:
    def test__request_handler__no_request_attribute__raises_value_error(self):
        class InvalidRequestHandler:
            pass

        with pytest.raises(ValueError):
            request_handler(InvalidRequestHandler)

    def test__request_handler__no_response_attribute__raises_value_error(
        self, get_valid_request
    ):
        request_class = get_valid_request

        class InvalidRequestHandler:
            request = request_class

        with pytest.raises(ValueError):
            request_handler(InvalidRequestHandler)

    def test__request_handler__no_handle_method__raises_value_error(
        self, get_valid_request
    ):
        request_class, response_class = get_valid_request, get_valid_request.response

        class InvalidRequestHandler:
            request = request_class
            response = response_class

        with pytest.raises(ValueError):
            request_handler(InvalidRequestHandler)

    def test__request_handler__request_type_mismatch__raises_value_error(
        self, get_valid_request
    ):
        request_class, response_class = get_valid_request, get_valid_request.response

        class InvalidRequestHandler:
            request = request_class
            response = response_class

            def handle(self, request: get_valid_request.response):
                pass

        with pytest.raises(ValueError):
            request_handler(InvalidRequestHandler)

    def test__request_handler__response_type_mismatch__raises_value_error(
        self, get_valid_request
    ):
        request_class, response_class = get_valid_request, get_valid_request.response

        class InvalidRequestHandler:
            request = request_class
            response = response_class

            def handle(self, request: get_valid_request) -> get_valid_request:
                pass

        with pytest.raises(ValueError):
            request_handler(InvalidRequestHandler)


@pytest.fixture
def get_valid_request(get_response):
    @request
    class Request:
        response = get_response

    return Request


@pytest.fixture
def get_response():
    class Response:
        pass

    return Response

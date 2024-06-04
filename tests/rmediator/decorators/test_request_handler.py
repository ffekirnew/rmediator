import pytest

from rmediator.decorators import request, request_handler


class TestRequestHandler:
    def test__request_handler__no_request_attribute__raises_value_error(self):
        with pytest.raises(AttributeError):

            @request_handler
            class InvalidRequestHandler:
                pass

    def test__request_handler__no_response_attribute__raises_value_error(
        self, get_valid_request
    ):
        request_class = get_valid_request

        with pytest.raises(AttributeError):

            @request_handler
            class InvalidRequestHandler:
                request = request_class

    def test__request_handler__no_handle_method__raises_value_error(
        self, get_valid_request
    ):
        request_class, response_class = get_valid_request, get_valid_request.response

        with pytest.raises(AttributeError):

            @request_handler
            class InvalidRequestHandler:
                request = request_class
                response = response_class

    def test__request_handler__request_type_mismatch__raises_value_error(
        self, get_valid_request
    ):
        request_class, response_class = get_valid_request, get_valid_request.response

        with pytest.raises(ValueError):

            @request_handler
            class InvalidRequestHandler:
                request = request_class
                response = response_class

                def handle(self, request: get_valid_request.response):
                    pass

    def test__request_handler__response_type_mismatch__raises_value_error(
        self, get_valid_request
    ):
        request_class, response_class = get_valid_request, get_valid_request.response

        with pytest.raises(ValueError):

            @request_handler
            class InvalidRequestHandler:
                request = request_class
                response = response_class

                def handle(self, request: get_valid_request) -> get_valid_request:
                    pass

    def test__request_handler__none_type_request__raises_value_error(
        self,
    ):
        with pytest.raises(AttributeError):

            @request_handler
            class InvalidRequestHandler:
                request = None
                response = str

                def handle(self, request: None) -> str:
                    return ""

    def test__request_handler__valid_handler__successful(self, get_valid_request):
        request_class, response_class = get_valid_request, get_valid_request.response

        @request_handler
        class InvalidRequestHandler:
            request = request_class
            response = response_class

            def handle(self, request: get_valid_request) -> get_valid_request.response:
                pass


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

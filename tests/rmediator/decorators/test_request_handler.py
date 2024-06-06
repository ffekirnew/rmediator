import pytest

from rmediator.decorators import request, request_handler


class TestRequestHandler:
    def test__request_handler__no_handle_method__raises_value_error(
        self, get_valid_request, get_response
    ):
        with pytest.raises(AttributeError):

            @request_handler(get_valid_request, get_response)
            class InvalidRequestHandler:
                pass

    def test__request_handler__request_type_mismatch__raises_value_error(
        self, get_valid_request, get_response
    ):
        with pytest.raises(AttributeError):

            @request_handler(get_valid_request, get_response)
            class InvalidRequestHandler:
                def handle(self, request: get_valid_request.response) -> None:
                    pass

    def test__request_handler__response_type_mismatch__raises_value_error(
        self, get_valid_request, get_response
    ):
        with pytest.raises(ValueError):

            @request_handler(get_valid_request, get_response)
            class InvalidRequestHandler:
                def handle(self, request: get_valid_request) -> get_valid_request:
                    pass

    def test__request_handler__none_type_request__raises_value_error(self):
        with pytest.raises(AttributeError):

            @request_handler(None, str)  # type: ignore
            class InvalidRequestHandler:
                def handle(self, request: None) -> str:
                    return ""

    def test__request_handler__valid_handler__successful(
        self, get_valid_request, get_response
    ):
        @request_handler(get_valid_request, get_response)
        class ValidRequestHandler:
            def handle(self, request: get_valid_request) -> get_response:
                pass

    def test__request_handler__valid_handler_different_request_parameter_name__successful(
        self, get_valid_request, get_response
    ):
        @request_handler(get_valid_request, get_response)
        class ValidRequestHandler:
            def handle(self, some_request: get_valid_request) -> get_response:
                pass

    def test__request_handler__invalid_handler_request_parameter_wrong_type__successful(
        self, get_valid_request, get_response
    ):
        with pytest.raises(ValueError):

            @request_handler(get_valid_request, get_response)
            class InvalidRequestHandler:
                def handle(self, some_request: str) -> get_response:
                    pass

    def test__request_handler__invalid_handler_multiple_parameters_in_handle__successful(
        self, get_valid_request, get_response
    ):
        with pytest.raises(AttributeError):

            @request_handler(get_valid_request, get_response)
            class InvalidRequestHandler:
                def handle(
                    self, request: get_valid_request, additonal: int
                ) -> get_response:
                    pass


@pytest.fixture
def get_valid_request(get_response):
    @request(get_response)
    class Request:
        pass

    return Request


@pytest.fixture
def get_response():
    class Response:
        pass

    return Response

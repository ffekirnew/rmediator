import pytest

from rmediator import Mediator
from rmediator.decorators import request, request_handler


class TestMediator:
    def test__mediator__valid_registration(
        self, mediator, get_valid_request, get_valid_request_handler
    ):
        mediator.register_handler(get_valid_request, get_valid_request_handler())

    def test__mediator__invalid_types_given_to_register_funciton__raises_value_error(
        self, mediator
    ):
        with pytest.raises(ValueError):
            mediator.register_handler(str, bool)

    def test__mediator__invalid_duplicate_registration__raises_value_error(
        self, mediator, get_valid_request, get_valid_request_handler
    ):
        mediator.register_handler(get_valid_request, get_valid_request_handler())

        with pytest.raises(ValueError):
            mediator.register_handler(get_valid_request, get_valid_request_handler())


@pytest.fixture
def mediator():
    return Mediator()


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


@pytest.fixture
def get_valid_request_handler(get_valid_request, get_response):
    @request_handler
    class RequestHandler:
        request = get_valid_request
        response = get_response

        def handle(self, request: get_valid_request) -> get_response:
            pass

    return RequestHandler

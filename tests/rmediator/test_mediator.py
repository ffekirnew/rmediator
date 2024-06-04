import pytest

from rmediator import Mediator
from rmediator.decorators import request, request_handler


class TestMediator:
    def test__mediator__valid_registration__successful(
        self, mediator, get_valid_request, get_valid_request_handler_first_type
    ):
        mediator.register_handler(
            get_valid_request, get_valid_request_handler_first_type()
        )

    def test__mediator__valid_registration_valid_handling__successful(
        self, mediator, get_valid_request, get_valid_request_handler_first_type
    ):
        mediator.register_handler(
            get_valid_request, get_valid_request_handler_first_type()
        )
        response = mediator.send(get_valid_request())

        assert type(response) is get_valid_request.response

    def test__mediator__undecorated_request__raises_value_error(
        self, mediator, get_undecorated_request, get_valid_request_handler_first_type
    ):
        with pytest.raises(ValueError):
            mediator.register_handler(
                get_undecorated_request, get_valid_request_handler_first_type()
            )

    def test__mediator__undecorated_request_handler__raises_value_error(
        self, mediator, get_valid_request, get_undecorated_request_handler
    ):
        with pytest.raises(ValueError):
            mediator.register_handler(
                get_valid_request, get_undecorated_request_handler()
            )

    def test__mediator__invalid_types_given_to_register_funciton__raises_value_error(
        self, mediator
    ):
        with pytest.raises(ValueError):
            mediator.register_handler(str, bool)

    def test__mediator__valid_duplicate_handlers_registration__successful(
        self, mediator, get_valid_request, get_valid_request_handler_first_type
    ):
        mediator.register_handler(
            get_valid_request, get_valid_request_handler_first_type()
        )
        mediator.register_handler(
            get_valid_request, get_valid_request_handler_first_type()
        )

    def test__mediator__invalid_same_request_different_handlers_registration__raises_value_error(
        self,
        mediator,
        get_valid_request,
        get_valid_request_handler_first_type,
        get_valid_request_handler_second_type,
    ):
        with pytest.raises(ValueError):
            mediator.register_handler(
                get_valid_request, get_valid_request_handler_first_type()
            )
            mediator.register_handler(
                get_valid_request, get_valid_request_handler_second_type()
            )

    def test__mediator__unregistered_request__raises_value_error(
        self,
        mediator,
        get_valid_request,
    ):
        with pytest.raises(ValueError):
            mediator.send(get_valid_request())

    def test__mediator__request_and_request_handler_response_type_mismatch__raises_value_error(
        self,
        mediator,
        get_valid_request,
        get_valid_request_handler_third_type,
    ):
        with pytest.raises(ValueError):
            mediator.register_handler(
                get_valid_request, get_valid_request_handler_third_type()
            )

    def test__mediator__none_request_request_handler__raises_value_error(
        self,
        mediator,
        get_valid_request,
        get_none_request_request_handler,
    ):
        with pytest.raises(ValueError):
            mediator.register_handler(
                get_valid_request, get_none_request_request_handler()
            )


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
def get_undecorated_request(get_response):
    class Request:
        response = get_response

    return Request


@pytest.fixture
def get_response():
    class Response:
        pass

    return Response


@pytest.fixture
def get_valid_request_handler_first_type(get_valid_request, get_response):
    @request_handler
    class RequestHandler:
        request = get_valid_request
        response = get_response

        def handle(self, request: get_valid_request) -> get_response:
            return get_response()

    return RequestHandler


@pytest.fixture
def get_undecorated_request_handler(get_valid_request, get_response):
    class RequestHandler:
        request = get_valid_request
        response = get_response

        def handle(self, request: get_valid_request) -> get_response:
            return get_response()

    return RequestHandler


@pytest.fixture
def get_none_request_request_handler(get_valid_request, get_response):
    class RequestHandler:
        request = None
        response = get_response

        def handle(self, request: None) -> get_response:
            return get_response()

    return RequestHandler


@pytest.fixture
def get_valid_request_handler_second_type(get_valid_request, get_response):
    @request_handler
    class RequestHandler:
        request = get_valid_request
        response = get_response

        def handle(self, request: get_valid_request) -> get_response:
            pass

    return RequestHandler


@pytest.fixture
def get_valid_request_handler_third_type(get_valid_request, get_response):
    @request_handler
    class RequestHandler:
        request = get_valid_request
        response = None

        def handle(self, request: get_valid_request) -> None:
            pass

    return RequestHandler

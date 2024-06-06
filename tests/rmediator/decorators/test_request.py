from types import FunctionType

from rmediator.decorators import request


class TestRequest:
    def test__request__invalid_registration_no_response__raises_value_error(self):
        @request
        class InvalidRequest:
            pass

        assert type(InvalidRequest) is FunctionType
        assert type(InvalidRequest) is not type

    def test__request__valid_registration__successful(self):
        @request(str)
        class ValidRequest:
            pass

        assert ValidRequest._response is str
        assert hasattr(ValidRequest, "_rmediator_decorated_request") is True

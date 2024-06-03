import pytest

from src.rmediator.decorators import request
from src.rmediator.interfaces import RequestInterface


class TestRequest:
    def test_request_invalid_not_subclass(self):
        class InvalidRequest:
            pass

        with pytest.raises(ValueError):
            request(InvalidRequest)

    def test_request_invalid_does_not_have_response(self):
        class InvalidRequest(RequestInterface):
            pass

        with pytest.raises(ValueError):
            request(InvalidRequest)

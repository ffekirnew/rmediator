from src.rmediator.interfaces import RequestInterface


class TestRequestInterface:
    def test_request_interface_invalid_not_subclass(self):
        class InvalidRequest:
            pass

        assert issubclass(InvalidRequest, RequestInterface) is False
        assert hasattr(InvalidRequest, "response") is False

    def test_request_interface_valid(self):
        class ValidRequest(RequestInterface):
            response = bool

        assert issubclass(ValidRequest, RequestInterface) is True
        assert hasattr(ValidRequest, "response") is True
        assert ValidRequest.response is bool  # type: ignore

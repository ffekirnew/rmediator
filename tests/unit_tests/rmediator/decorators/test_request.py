import pytest

from src.rmediator.decorators import request


class TestRequest:
    def test__request__invalid_no_response__raises_value_error(self):
        with pytest.raises(ValueError):

            @request
            class InvalidRequest:
                pass

    def test__request__valid(self):

        @request
        class ValidRequest:
            response = str

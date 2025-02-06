"""Http Error testing"""

from pyttp import HttpError
from pyttp import HttpStatus

import pytest


class TestHttpError:
    def test_details(self) -> None:
        message = "msg"
        status_code = HttpStatus.FORBIDDEN
        with pytest.raises(HttpError) as e:
            raise HttpError(message=message, status_code=status_code)
        assert e.value.details == {"message": message, "status_code": status_code}

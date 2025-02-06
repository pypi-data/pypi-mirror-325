"""HTTP error utilities"""

from typing import override, TypedDict


class HttpErrorDetails(TypedDict):
    """`HttpError` details"""

    message: str
    status_code: int


class HttpError(Exception):
    """Defines an HTTP error / exception.

    This exception can be raised within api routes to construct responses,
    after registering this error to your server instance.


    Attributes:
        message (str):
        status_code (int): The HTTP status code of the error.
            `HttpStatus` provides an integer enum for Http Status codes.
        is_critical (bool): Whether or not this error is critical.
            Useful for distinguising between user and programmer errors.
    """

    @override
    def __init__(
        self, message: str, status_code: int, is_critical: bool = False
    ) -> None:
        """Instantiate an HttpError

        This error contains helpful attributes to throw within api routes
        such as `status_code`.

        Example:
            ```python
            from pyttp import HttpStatus, HttpError


            @app.post("/error")
            def error_route() -> None:
                raise HttpError("an error message", HttpStatus.I_AM_A_TEAPOT, False)
            ```

        Args:
            message (str): The error message.
            status_code (int): The HTTP status code.
            is_critical (bool): Whether or not this error is critical.
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.is_critical = is_critical

    @property
    def details(self) -> HttpErrorDetails:
        """Return the `HttpErrorDetails`. A dictionary containing the message and status code"""
        return {"message": self.message, "status_code": self.status_code}

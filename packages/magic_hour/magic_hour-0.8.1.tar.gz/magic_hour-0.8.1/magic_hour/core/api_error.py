import typing


class ApiError(Exception):
    """
    A custom exception class for handling API-related errors.

    This class extends the base Exception class to provide additional context
    for API errors, including the HTTP status code and response body.

    Attributes:
        status_code: The HTTP status code associated with the error.
            None if no status code is applicable.
        body: The response body or error message content.
            Can be any type depending on the API response format.
    """

    status_code: typing.Optional[int]
    body: typing.Any

    def __init__(
        self, *, status_code: typing.Optional[int] = None, body: typing.Any = None
    ) -> None:
        """
        Initialize the ApiError with optional status code and body.

        Args:
            status_code: The HTTP status code of the error.
                Defaults to None.
            body: The response body or error message content.
                Defaults to None.

        Note:
            The asterisk (*) in the parameters forces keyword arguments,
            making the instantiation more explicit.
        """
        self.status_code = status_code
        self.body = body

    def __str__(self) -> str:
        """
        Return a string representation of the ApiError.

        Returns:
            str: A formatted string containing the status code and body.
                Format: "status_code: {status_code}, body: {body}"
        """
        return f"status_code: {self.status_code}, body: {self.body}"

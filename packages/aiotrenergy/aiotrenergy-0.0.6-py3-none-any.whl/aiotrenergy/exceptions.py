class AiotrenergyException(Exception):
    """Base class for exceptions in this module."""
    pass

class NetworkError(AiotrenergyException):
    """Raised when a network error occurs."""
    pass

class HttpStatusError(AiotrenergyException):
    """Raised when an HTTP status error occurs."""
    pass


class TrenergyApiError(AiotrenergyException):
    """Raised when an API error occurs."""
    pass

class TrenergyStatusError(TrenergyApiError):
    """Raised when an API returns a status error."""
    def __init__(self, message: str = "Api returned 'false' status"):
        self.message = message
        super().__init__(self.message)


class TrenergyError(HttpStatusError):
    """Raised when an error occurs in the Trenergy API."""
    def __init__(self, status: int, error: str, errors: dict):
        self.status = status
        self.error = error
        self.errors = errors
        super().__init__(f"{status}: {error}")


class NotEnoughFundsError(TrenergyError):
    """Raised when there are not enough funds in the wallet."""
    pass


def raise_error(status: int, error: dict):
    """Parse an error response from the Trenergy API and raise"""
    error_message = error.get("error")
    errors = error.get("errors")
    if error == "not enough funds":
        raise NotEnoughFundsError(status, error_message, errors)
    raise TrenergyError(status, error_message, errors)

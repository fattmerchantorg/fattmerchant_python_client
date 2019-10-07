import logging

logger = logging.getLogger(__name__)


class FattmerchantException(Exception):
    """
    Base exception class for the Fattmerchant Client

    :param str message: Message to use for this exception.
    """
    default_code = 422
    default_message = 'An error has occured.'

    def __init__(self, status_code=None, message=None):
        self._message = message or self.default_message
        self.code = status_code or self.default_code

        super(Exception, self).__init__(self._message)


class InvalidTokenException(FattmerchantException):
    """
    Exception that should be raised when the token fails to validate
    for any reason.

    :param str message: Message to use for this exception.
    """
    default_code = 401
    default_message = 'The token used is invalid.'


class ResourceDoesNotExistException(FattmerchantException):
    """
    Exception that should be raised when a resource is expected but none
    are returned

    :param str message: Message to use for this exception.
    """
    default_code = 404
    default_message = 'The resource requested does not exist.'


class ResourceNotCreatedException(FattmerchantException):
    """
    Exception that should be raised when a resource is could not be
    created.

    :param str message: Message to use for this exception.
    """
    default_code = 422
    default_message = 'The resource could not be created.'


class DuplicateResourceException(FattmerchantException):
    """
    Exception that should be raised when an attempt to create or update a
    resource would have resulted in a duplicate.

    :param str message: Message to use for this exception.
    """
    default_code = 409
    default_message = 'The resource trying to be created already exists.'


class InvalidRequestDataException(FattmerchantException):
    """
    Exception that should be raised if any expected data for a request
    is missing or invalid.

    :param str message: Message to use for this exception.
    """
    default_code = 422
    default_message = 'The request data is missing or invalid.'

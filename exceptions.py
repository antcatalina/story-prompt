# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class NumberTooLowError(Error):
    """Raised when the input number is too low"""
    pass

class NumberTooHighError(Error):
    """Raised when the input number is too high"""
    pass

class LengthTooShortError(Error):
    """Raised when the input string is too short"""
    pass

class LengthTooLongError(Error):
    """Raised when the input string is too long"""
    pass

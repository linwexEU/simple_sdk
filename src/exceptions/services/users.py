

class InvalidUserEmailError(Exception):
    """Invalid user email error"""


class UserAlreadyExistsServiceError(Exception):
    """User already exists error"""


class UserNotFoundServiceError(Exception):
    """User not found error"""

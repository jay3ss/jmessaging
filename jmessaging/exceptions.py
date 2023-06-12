"""
Custom exceptions
"""


class BaseException(Exception):
    pass


class InvalidBackground(BaseException):
    pass


class InvalidColor(BaseException):
    pass


class InvalidStyle(BaseException):
    pass

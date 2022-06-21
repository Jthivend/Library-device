"""
application error (related to user)
"""


class ApplicationError(Exception):
    """ Generic error for error related to user """

    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class ParamError(ApplicationError):
    """ Something went wrong on param set by user """

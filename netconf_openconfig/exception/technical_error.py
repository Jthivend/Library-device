"""
technical error (non related to user)
"""


class TechnicalError(Exception):
    """ Generic error for error non related to user """

    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

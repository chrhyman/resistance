class GameError(Exception):
    """
    An exception caused by a game rules violation.
    Attributes:
        - message: the error message
        - summary: (optional) a version of the message with no hidden game information
    """
    def __init__(self, message, summary=''):
        if summary == '':
            summary = message

        self.summary = summary
        self.message = message

        super().__init__(self.message)


class IllegalAction(GameError):
    pass

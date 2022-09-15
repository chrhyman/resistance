class GameError(Exception):
    """
    An exception caused by a game rules violation.
    Attributes:
        - message: the error message
        - summary: (optional) a version of the message with no hidden game information

    The message is raised as an Exception.
    """

    def __init__(self, message, summary=""):
        if summary == "":
            summary = message

        self.summary = summary
        self.message = message

        super().__init__(self.message)


class IllegalActionGameError(GameError):
    pass


class InvalidNumberGameError(GameError):
    pass

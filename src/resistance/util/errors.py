from typing import Optional


class BaseGameError(Exception):
    """A base class for errors in this package."""


class GameError(BaseGameError):
    """
    An exception caused by a game rules violation in the ``resistance`` package.
    In addition to the ``message``, there is an optional ``summary`` which keeps any hidden information concealed.
    ``__str__`` returns the ``summary``.
    This base class should not be raised directly, but can be used in this way::

        try:
            ...
        except GameError as err:
            print(err.summary)  # only summary
            print(err)          # only summary
            print(err.message)  # access full error
            raise err           # shows err.summary

    If a ``summary`` is not provided, its value will be the same as ``message`` (required).
    """

    def __init__(self, message: str, summary: Optional[str] = None) -> None:
        if summary is None or summary == "":
            summary = message

        self.summary = summary
        self.message = message

    def __str__(self) -> str:
        return str(self.summary)


class IllegalActionGameError(GameError):
    pass


class InvalidNumberGameError(GameError):
    pass

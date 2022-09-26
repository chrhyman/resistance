from abc import ABC, abstractmethod


class Alignment(ABC):
    """
    An Alignment in a game of the Resistance. Determines the teams Good and Evil.

    ----

    **Instance Properties**::

        Alignment.name: str
        Alignment.good: bool
        Alignment.member: str
        Alignment.member_pl: str

    **Implements**::

        Alignment.__eq__  # checks that types match
        str(Alignment) == Alignment.name
        bool(Alignment) == Alignment.good
    """
    def __bool__(self) -> bool:
        return bool(self.good)

    def __eq__(self, other) -> bool:
        return type(self) is type(other)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        return str(self.name)

    @property
    @abstractmethod
    def name(self) -> str:
        """The team's name"""

    @property
    @abstractmethod
    def good(self) -> bool:
        """Whether this team is Good"""

    @property
    @abstractmethod
    def member(self) -> str:
        """The name of a generic member of this team"""

    @property
    @abstractmethod
    def member_pl(self) -> str:
        """The plural form of ``Alignment.member``"""

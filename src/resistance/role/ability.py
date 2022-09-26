from abc import ABC, abstractmethod
from typing import TypeVar

Self = TypeVar("Self", bound="Ability")


class Ability(ABC):
    """
    A single Ability for a Role. Implemented as a wrapper around a boolean value.

    ----

    **Instance Properties**::

        Ability.name: str
        Ability.value: bool

    **Implements**::

        Ability.__eq__  # checks that types and values match
        str(Ability)    # 'can X' or 'cannot X' where X is name
        bool(Ability) == Ability.value
    """
    def __init__(self, value: bool) -> None:
        self.value = bool(value)

    def __bool__(self) -> bool:
        return bool(self.value)

    def __eq__(self, other: Self) -> bool:
        return self.value == other.value and type(self) is type(other)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({bool(self.value)})"

    def __str__(self) -> str:
        return f'{"can" if self.value else "cannot"} {self.name}'

    @property
    @abstractmethod
    def name(self) -> str:
        """The name of the ability"""

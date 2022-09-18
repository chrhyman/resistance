from abc import ABC, abstractmethod


class Ability(ABC):
    def __init__(self, value: bool) -> None:
        self.value = bool(value)

    def __bool__(self) -> bool:
        return bool(self.value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({bool(self.value)})"

    def __str__(self) -> str:
        return f'{"can" if self.value else "cannot"} {self.name}'

    @property
    @abstractmethod
    def name(self) -> str:
        pass

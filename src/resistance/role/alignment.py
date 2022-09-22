from abc import ABC, abstractmethod


class Alignment(ABC):
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
        pass

    @property
    @abstractmethod
    def good(self) -> bool:
        pass

    @property
    @abstractmethod
    def member(self) -> str:
        pass

    @property
    @abstractmethod
    def member_pl(self) -> str:
        pass

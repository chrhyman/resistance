from abc import ABC, abstractmethod
from typing import Union

from .alignment import Alignment
from .ability import Ability
from .abilities import SeeSpies, ShootMerlin


class Role(ABC):
    @property
    @abstractmethod
    def alignment(self) -> Alignment:
        pass

    @property
    @abstractmethod
    def can_see_spies(self) -> SeeSpies:
        pass

    @property
    @abstractmethod
    def can_shoot_merlin(self) -> ShootMerlin:
        pass

    def can(self, ability: Union[Ability, type]) -> Ability:
        def is_type(type_str):
            return isinstance(ability, type) and ability.__name__ == type_str

        if isinstance(ability, SeeSpies) or is_type("SeeSpies"):
            return self.can_see_spies

        if isinstance(ability, ShootMerlin) or is_type("ShootMerlin"):
            return self.can_shoot_merlin

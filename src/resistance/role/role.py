from abc import ABC, abstractmethod
from typing import TypeVar

from .alignment import Alignment
from .ability import Ability
from .abilities import SeeSpies, ShootMerlin, SeeMerlin, LookLikeMerlin, HideFromMerlin, HideFromSpies

Self = TypeVar("Self", bound="Role")


class Role(ABC):
    def __eq__(self, other: Self) -> bool:
        return type(self) is type(other)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        return self.name

    @property
    @abstractmethod
    def name(self) -> str:
        pass

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
    def can_see_merlin(self) -> SeeMerlin:
        pass

    @property
    @abstractmethod
    def can_shoot_merlin(self) -> ShootMerlin:
        pass

    @property
    @abstractmethod
    def can_look_like_merlin(self) -> LookLikeMerlin:
        pass

    @property
    @abstractmethod
    def can_hide_from_merlin(self) -> HideFromMerlin:
        pass

    @property
    @abstractmethod
    def can_hide_from_spies(self) -> HideFromSpies:
        pass

    def can(self, ability: type | Ability) -> Ability:
        def class_or_instance_of(cls: type) -> bool:
            return ability is cls or isinstance(ability, cls)

        if class_or_instance_of(SeeSpies):
            return self.can_see_spies

        if class_or_instance_of(ShootMerlin):
            return self.can_shoot_merlin

        if class_or_instance_of(SeeMerlin):
            return self.can_see_merlin

        if class_or_instance_of(LookLikeMerlin):
            return self.can_look_like_merlin

        if class_or_instance_of(HideFromMerlin):
            return self.can_hide_from_merlin

        if class_or_instance_of(HideFromSpies):
            return self.can_hide_from_spies

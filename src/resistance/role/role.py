from abc import ABC, abstractmethod
from typing import TypeVar

from .alignment import Alignment
from .ability import Ability
from .abilities import SeeSpies, ShootMerlin, SeeMerlin, LookLikeMerlin, HideFromMerlin, HideFromSpies

Self = TypeVar("Self", bound="Role")


class Role(ABC):
    """
    A Role in a game of the Resistance. Determines ``Alignment`` and defines all ``Ability``'s.
    Instantiated with no parameters, e.g. ``Merlin()`` or ``Oberon()``.

    ----

    **Instance Properties**::

        Role.name: str
        Role.alignment: Alignment
        Role.can_see_spies: SeeSpies
        Role.can_see_merlin: SeeMerlin
        Role.can_shoot_merlin: ShootMerlin
        Role.can_look_like_merlin: LookLikeMerlin
        Role.can_hide_from_merlin: HideFromMerlin
        Role.can_hide_from_spies: HideFromSpies

    **Implements**::

        Role.__eq__  # checks that types match for subclasses
        str(Role) == Role.name

    **Methods**::

        Role.can(ability: type | Ability) -> Ability
    """
    def __eq__(self, other: Self) -> bool:
        return type(self) is type(other)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        return self.name

    @property
    @abstractmethod
    def name(self) -> str:
        """The string representing this Role"""

    @property
    @abstractmethod
    def alignment(self) -> Alignment:
        """The ``Alignment`` (e.g. ``Good`` or ``Evil``) for this Role"""

    @property
    @abstractmethod
    def can_see_spies(self) -> SeeSpies:
        """
        Whether this Role is able to see spies (``BaseEvil``).
        ``True`` for ``Merlin`` and all ``BaseEvil`` except ``Oberon``.
        """

    @property
    @abstractmethod
    def can_see_merlin(self) -> SeeMerlin:
        """
        Whether this Role is able to see Merlin.
        ``True`` for ``Percival``.
        """

    @property
    @abstractmethod
    def can_shoot_merlin(self) -> ShootMerlin:
        """
        Whether this Role can attempt to shoot Merlin for the Spies to win an otherwise lost game.
        ``True`` for ``Assassin`` and ``MordredAssassin``.
        """

    @property
    @abstractmethod
    def can_look_like_merlin(self) -> LookLikeMerlin:
        """
        Whether this Role looks like Merlin to Percival.
        ``True`` for ``Merlin`` and ``Morgana``.
        """

    @property
    @abstractmethod
    def can_hide_from_merlin(self) -> HideFromMerlin:
        """
        Whether this Role is not visible as a spy to Merlin.
        ``True`` for ``Mordred`` and ``MordredAssassin``.
        """

    @property
    @abstractmethod
    def can_hide_from_spies(self) -> HideFromSpies:
        """
        Whether this Role is not visible as a spy to other spies.
        ``True`` for ``Oberon``.
        """

    def can(self, ability: type | Ability) -> Ability | None:
        """
        Retrieves the provided Ability for this Role. e.g.::

            Merlin().can(SeeSpies) => SeeSpies(True)

        Note that if an instance is passed, its value is not used::

            Merlin().can(SeeSpies(False)) => SeeSpies(True)

        For clarity, it is recommended to use the ``type``, not an instance.

        :param ability: class or instance of Ability to retrieve for Role
        :return: True/False value for Role if valid Ability, else None
        """
        def class_or_instance_of(cls: type) -> bool:
            """
            Helper function that determines if ``ability`` is the given ``type`` or an instance of it.

            :param cls: type to retrieve value for this Role
            :return: bool
            """
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

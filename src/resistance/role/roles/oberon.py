from .base_evil import BaseEvil
from ..abilities import SeeSpies, HideFromSpies
from ...util.constants import OBERON


class Oberon(BaseEvil):
    """
    A member of the Evil team who cannot see fellow Evil team members, and who cannot be seen by them either.
    Merlin can see Oberon as Evil.

    AKA: Blind Spy
    """
    @property
    def name(self) -> str:
        return OBERON

    @property
    def can_see_spies(self) -> SeeSpies:
        return SeeSpies(False)

    @property
    def can_hide_from_spies(self) -> HideFromSpies:
        return HideFromSpies(True)

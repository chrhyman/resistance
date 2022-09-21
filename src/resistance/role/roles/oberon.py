from .base_evil import BaseEvil
from ..abilities import SeeSpies, HideFromSpies
from ...util.constants import OBERON


class Oberon(BaseEvil):
    @property
    def name(self) -> str:
        return OBERON

    @property
    def can_see_spies(self) -> SeeSpies:
        return SeeSpies(False)

    @property
    def can_hide_from_spies(self) -> HideFromSpies:
        return HideFromSpies(True)

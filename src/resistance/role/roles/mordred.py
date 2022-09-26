from .base_evil import BaseEvil
from ..abilities import HideFromMerlin
from ...util.constants import MORDRED


class Mordred(BaseEvil):
    """
    The leader of the Evil team. Merlin is not able to tell that Mordred is Evil, unlike other Evil Roles.

    AKA: Deep Spy
    """
    @property
    def name(self) -> str:
        return MORDRED

    @property
    def can_hide_from_merlin(self) -> HideFromMerlin:
        return HideFromMerlin(True)

from .base_evil import BaseEvil
from ..abilities import HideFromMerlin
from ...util.constants import MORDRED


class Mordred(BaseEvil):
    @property
    def name(self) -> str:
        return MORDRED

    @property
    def can_hide_from_merlin(self) -> HideFromMerlin:
        return HideFromMerlin(True)

from .base_evil import BaseEvil
from ..abilities import LookLikeMerlin
from ...util.constants import MORGANA


class Morgana(BaseEvil):
    @property
    def name(self) -> str:
        return MORGANA

    @property
    def can_look_like_merlin(self) -> LookLikeMerlin:
        return LookLikeMerlin(True)

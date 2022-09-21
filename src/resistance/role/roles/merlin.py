from .base_good import BaseGood
from ..abilities import SeeSpies, LookLikeMerlin
from ...util.constants import MERLIN


class Merlin(BaseGood):
    @property
    def name(self) -> str:
        return MERLIN

    @property
    def can_see_spies(self) -> SeeSpies:
        return SeeSpies(True)

    @property
    def can_look_like_merlin(self) -> LookLikeMerlin:
        return LookLikeMerlin(True)

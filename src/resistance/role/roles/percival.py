from .base_good import BaseGood
from ..abilities import SeeMerlin
from ...util.constants import PERCIVAL


class Percival(BaseGood):
    @property
    def name(self) -> str:
        return PERCIVAL

    @property
    def can_see_merlin(self) -> SeeMerlin:
        return SeeMerlin(True)

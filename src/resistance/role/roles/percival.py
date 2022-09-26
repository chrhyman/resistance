from .base_good import BaseGood
from ..abilities import SeeMerlin
from ...util.constants import PERCIVAL


class Percival(BaseGood):
    """
    A member of the Good team who can identify Merlin.
    If Morgana is in the game, there will be two possible Merlins.

    AKA: Body Guard
    """
    @property
    def name(self) -> str:
        return PERCIVAL

    @property
    def can_see_merlin(self) -> SeeMerlin:
        return SeeMerlin(True)

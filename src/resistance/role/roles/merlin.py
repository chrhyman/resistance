from .base_good import BaseGood
from ..abilities import SeeSpies, LookLikeMerlin
from ...util.constants import MERLIN


class Merlin(BaseGood):
    """
    The leader of the Good team. Able to see all which players are Evil (except Mordred),
    but must remain hidden. If the Evil team identifies and shoots Merlin, the Evil team wins.
    Merlin looks like a normal Good player to Evil players, but Percival can see Merlin (and Morgana).

    AKA: Commander
    """
    @property
    def name(self) -> str:
        return MERLIN

    @property
    def can_see_spies(self) -> SeeSpies:
        return SeeSpies(True)

    @property
    def can_look_like_merlin(self) -> LookLikeMerlin:
        return LookLikeMerlin(True)

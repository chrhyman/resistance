from .base_evil import BaseEvil
from ..abilities import LookLikeMerlin
from ...util.constants import MORGANA


class Morgana(BaseEvil):
    """
    A member of the Evil team who can fool Percival into thinking they are Merlin.
    If Merlin and Morgana are both in a game, Percival sees both as equal candidates to be the true Merlin.

    AKA: False Commander
    """
    @property
    def name(self) -> str:
        return MORGANA

    @property
    def can_look_like_merlin(self) -> LookLikeMerlin:
        return LookLikeMerlin(True)

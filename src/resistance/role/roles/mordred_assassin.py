from .assassin import Assassin
from .mordred import Mordred
from ...util.constants import MORDRED_ASSASSIN


class MordredAssassin(Mordred, Assassin):
    """
    This Role has all abilities of Mordred (Deep Spy) and Assassin combined.
    Used in games that require both roles with too few players to separate.
    """
    @property
    def name(self) -> str:
        return MORDRED_ASSASSIN

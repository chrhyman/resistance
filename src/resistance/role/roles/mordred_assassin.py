from .assassin import Assassin
from .mordred import Mordred
from ...util.constants import MORDRED_ASSASSIN


class MordredAssassin(Mordred, Assassin):
    @property
    def name(self) -> str:
        return MORDRED_ASSASSIN

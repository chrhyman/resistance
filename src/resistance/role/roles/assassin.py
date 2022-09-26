from .base_evil import BaseEvil
from ..abilities import ShootMerlin
from ...util.constants import ASSASSIN


class Assassin(BaseEvil):
    """
    A basic Evil team member who can attempt to shoot Merlin
    at the end of the game if the Evil team would otherwise lose.
    If the Assassin shoots Merlin, the Evil team wins.
    If the Assassin shoots anyone else, the Good team wins.
    """
    @property
    def name(self) -> str:
        return ASSASSIN

    @property
    def can_shoot_merlin(self) -> ShootMerlin:
        return ShootMerlin(True)

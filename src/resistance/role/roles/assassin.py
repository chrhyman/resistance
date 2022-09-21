from .base_evil import BaseEvil
from ..abilities import ShootMerlin
from ...util.constants import ASSASSIN


class Assassin(BaseEvil):
    @property
    def name(self) -> str:
        return ASSASSIN

    @property
    def can_shoot_merlin(self) -> ShootMerlin:
        return ShootMerlin(True)

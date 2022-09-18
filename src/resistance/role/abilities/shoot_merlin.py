from ..ability import Ability
from ...util.constants import MERLIN


class ShootMerlin(Ability):
    @property
    def name(self) -> str:
        return f"shoot {MERLIN}"

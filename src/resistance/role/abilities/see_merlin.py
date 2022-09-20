from ..ability import Ability
from ...util.constants import MERLIN


class SeeMerlin(Ability):
    @property
    def name(self) -> str:
        return f"see {MERLIN}"

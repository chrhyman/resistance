from ..ability import Ability
from ...util.constants import MERLIN


class HideFromMerlin(Ability):
    @property
    def name(self) -> str:
        return f"hide from {MERLIN}"

from ..ability import Ability
from ...util.constants import MERLIN


class LookLikeMerlin(Ability):
    @property
    def name(self) -> str:
        return f"look like {MERLIN}"

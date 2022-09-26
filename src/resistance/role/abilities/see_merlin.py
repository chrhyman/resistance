from ..ability import Ability
from ...util.constants import MERLIN


class SeeMerlin(Ability):
    """
    If ``True``, this Role sees all potential Merlins.
    True for Percival.
    """
    @property
    def name(self) -> str:
        return f"see {MERLIN}"

from ..ability import Ability
from ...util.constants import MERLIN


class LookLikeMerlin(Ability):
    """
    If ``True``, Percival sees this Role as a potential Merlin.
    True for Merlin and Morgana.
    """
    @property
    def name(self) -> str:
        return f"look like {MERLIN}"

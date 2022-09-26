from ..ability import Ability
from ...util.constants import MERLIN


class HideFromMerlin(Ability):
    """
    If ``True``, Merlin sees that Evil Role as Good.
    True for Mordred.
    """
    @property
    def name(self) -> str:
        return f"hide from {MERLIN}"

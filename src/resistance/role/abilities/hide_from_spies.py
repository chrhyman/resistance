from ..ability import Ability
from ...util.constants import EVIL_TEAM


class HideFromSpies(Ability):
    """
    If ``True``, Evil team members see that Evil Role as Good.
    True for Oberon.
    """
    @property
    def name(self) -> str:
        return f"hide from {EVIL_TEAM}"

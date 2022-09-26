from ..ability import Ability
from ...util.constants import EVIL_TEAM_MEMBER_PL


class SeeSpies(Ability):
    """
    If ``True``, this Role can see all Evil players. (Some roles have further limitations.)
    True for Merlin and for all Evil Roles except Oberon.
    """
    @property
    def name(self) -> str:
        return f"see {EVIL_TEAM_MEMBER_PL}"

from ..alignment import Alignment
from ...util.constants import GOOD_TEAM, GOOD_TEAM_MEMBER, GOOD_TEAM_MEMBER_PL


class Good(Alignment):
    @property
    def name(self) -> str:
        return GOOD_TEAM

    @property
    def good(self) -> bool:
        return True

    @property
    def member(self) -> str:
        return GOOD_TEAM_MEMBER

    @property
    def member_pl(self) -> str:
        return GOOD_TEAM_MEMBER_PL

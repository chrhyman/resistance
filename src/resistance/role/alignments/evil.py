from ..alignment import Alignment
from ...util.constants import EVIL_TEAM, EVIL_TEAM_MEMBER, EVIL_TEAM_MEMBER_PL


class Evil(Alignment):
    @property
    def name(self) -> str:
        return EVIL_TEAM

    @property
    def good(self) -> bool:
        return False

    @property
    def member(self) -> str:
        return EVIL_TEAM_MEMBER

    @property
    def member_pl(self) -> str:
        return EVIL_TEAM_MEMBER_PL

from ..ability import Ability
from ...util.constants import EVIL_TEAM_MEMBER_PL


class SeeSpies(Ability):
    @property
    def name(self) -> str:
        return f"see {EVIL_TEAM_MEMBER_PL}"

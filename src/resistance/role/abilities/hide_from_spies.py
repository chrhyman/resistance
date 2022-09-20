from ..ability import Ability
from ...util.constants import EVIL_TEAM


class HideFromSpies(Ability):
    @property
    def name(self) -> str:
        return f"hide from {EVIL_TEAM}"

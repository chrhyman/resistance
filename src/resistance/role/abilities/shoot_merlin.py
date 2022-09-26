from ..ability import Ability
from ...util.constants import MERLIN


class ShootMerlin(Ability):
    """
    If ``True``, this Evil Role can try to shoot Merlin at the end of the game if the Good team won 3 missions.
    If the player shoots Merlin, the Evil team wins. If they don't, the Good team wins.
    True for Assassin and MordredAssassin.
    """
    @property
    def name(self) -> str:
        return f"shoot {MERLIN}"

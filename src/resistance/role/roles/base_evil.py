from ..role import Role
from ..alignment import Alignment
from ..alignments import Evil
from ..abilities import SeeSpies, SeeMerlin, ShootMerlin, LookLikeMerlin, HideFromMerlin, HideFromSpies


class BaseEvil(Role):
    @property
    def name(self) -> str:
        return self.alignment.member

    @property
    def alignment(self) -> Alignment:
        return Evil()

    @property
    def can_see_spies(self) -> SeeSpies:
        return SeeSpies(True)

    @property
    def can_see_merlin(self) -> SeeMerlin:
        return SeeMerlin(False)

    @property
    def can_shoot_merlin(self) -> ShootMerlin:
        return ShootMerlin(False)

    @property
    def can_look_like_merlin(self) -> LookLikeMerlin:
        return LookLikeMerlin(False)

    @property
    def can_hide_from_merlin(self) -> HideFromMerlin:
        return HideFromMerlin(False)

    @property
    def can_hide_from_spies(self) -> HideFromSpies:
        return HideFromSpies(False)
    
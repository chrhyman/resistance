from src.resistance.role import BaseGood
from src.resistance.role.alignments import Good
from src.resistance.role.abilities import (SeeSpies, SeeMerlin, ShootMerlin,
                                           LookLikeMerlin, HideFromMerlin, HideFromSpies)
from src.resistance.util.constants import GOOD_TEAM_MEMBER


class TestBaseGood:
    def test_name(self):
        r = BaseGood()
        assert r.name == GOOD_TEAM_MEMBER
        assert str(r) == GOOD_TEAM_MEMBER

    def test_alignment(self):
        r = BaseGood()
        assert isinstance(r.alignment, Good)

    def test_abilities(self):
        r = BaseGood()

        # verify correct boolean value via Ability.__bool__
        assert not r.can_see_spies
        assert not r.can_see_merlin
        assert not r.can_shoot_merlin
        assert not r.can_look_like_merlin
        assert not r.can_hide_from_spies
        assert not r.can_hide_from_merlin

        # verify correct type via Role.can and Ability.__eq__
        assert r.can_see_spies == r.can(SeeSpies)
        assert r.can_see_merlin == r.can(SeeMerlin)
        assert r.can_shoot_merlin == r.can(ShootMerlin)
        assert r.can_look_like_merlin == r.can(LookLikeMerlin)
        assert r.can_hide_from_merlin == r.can(HideFromMerlin)
        assert r.can_hide_from_spies == r.can(HideFromSpies)

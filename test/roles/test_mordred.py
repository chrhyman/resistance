from src.resistance.role import Mordred
from src.resistance.role.alignments import Evil
from src.resistance.role.abilities import (SeeSpies, SeeMerlin, ShootMerlin,
                                           LookLikeMerlin, HideFromMerlin, HideFromSpies)
from src.resistance.util.constants import MORDRED


class TestMordred:
    def test_name(self):
        r = Mordred()
        assert r.name == MORDRED
        assert str(r) == MORDRED

    def test_alignment(self):
        r = Mordred()
        assert isinstance(r.alignment, Evil)

    def test_abilities(self):
        r = Mordred()

        # verify correct boolean value via Ability.__bool__
        assert r.can_see_spies
        assert not r.can_see_merlin
        assert not r.can_shoot_merlin
        assert not r.can_look_like_merlin
        assert not r.can_hide_from_spies
        assert r.can_hide_from_merlin

        # verify correct type via Role.can and Ability.__eq__
        assert r.can_see_spies == r.can(SeeSpies)
        assert r.can_see_merlin == r.can(SeeMerlin)
        assert r.can_shoot_merlin == r.can(ShootMerlin)
        assert r.can_look_like_merlin == r.can(LookLikeMerlin)
        assert r.can_hide_from_merlin == r.can(HideFromMerlin)
        assert r.can_hide_from_spies == r.can(HideFromSpies)

from src.resistance.role import Merlin
from src.resistance.role.alignments import Good
from src.resistance.role.abilities import (SeeSpies, SeeMerlin, ShootMerlin,
                                           LookLikeMerlin, HideFromMerlin, HideFromSpies)
from src.resistance.util.constants import MERLIN


class TestMerlin:
    def test_name(self):
        assert Merlin.name == MERLIN
        assert str(Merlin()) == MERLIN

    def test_alignment(self):
        m = Merlin()
        assert isinstance(m.alignment, Good)

    def test_abilities(self):
        m = Merlin()

        # verify correct boolean value via __bool__
        assert m.can_see_spies
        assert m.can_look_like_merlin
        assert not m.can_see_merlin
        assert not m.can_shoot_merlin
        assert not m.can_hide_from_spies
        assert not m.can_hide_from_merlin

        # verify correct type via Role.can and __eq__
        assert m.can_see_spies == m.can(SeeSpies)
        assert m.can_see_merlin == m.can(SeeMerlin)
        assert m.can_shoot_merlin == m.can(ShootMerlin)
        assert m.can_look_like_merlin == m.can(LookLikeMerlin)
        assert m.can_hide_from_merlin == m.can(HideFromMerlin)
        assert m.can_hide_from_spies == m.can(HideFromSpies)

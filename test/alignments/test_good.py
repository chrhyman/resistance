from src.resistance.role.alignments.good import Good
from src.resistance.util.constants import GOOD_TEAM, GOOD_TEAM_MEMBER, GOOD_TEAM_MEMBER_PL


class TestGood:
    def test_name(self):
        g = Good()
        assert g.name == GOOD_TEAM
        assert str(g) == GOOD_TEAM

    def test_member_name(self):
        g = Good()
        assert g.member == GOOD_TEAM_MEMBER
        assert g.member_pl == GOOD_TEAM_MEMBER_PL

    def test_good(self):
        g = Good()
        assert g.good
        assert g

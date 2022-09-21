from src.resistance.role.alignments.evil import Evil
from src.resistance.util.constants import EVIL_TEAM, EVIL_TEAM_MEMBER, EVIL_TEAM_MEMBER_PL


class TestGood:
    def test_name(self):
        e = Evil()
        assert e.name == EVIL_TEAM
        assert str(e) == EVIL_TEAM

    def test_member_name(self):
        e = Evil()
        assert e.member == EVIL_TEAM_MEMBER
        assert e.member_pl == EVIL_TEAM_MEMBER_PL

    def test_good(self):
        e = Evil()
        assert not e.good

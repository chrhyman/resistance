from src.resistance.role.abilities import SeeSpies
from src.resistance.util.constants import EVIL_TEAM_MEMBER_PL


class TestSeeSpies:
    def test_name(self):
        name = f"see {EVIL_TEAM_MEMBER_PL}"
        t = SeeSpies(True)
        f = SeeSpies(False)
        assert t.name == name
        assert f.name == name

    def test_str(self):
        name = f"see {EVIL_TEAM_MEMBER_PL}"
        t = SeeSpies(True)
        f = SeeSpies(False)
        assert str(t) == f"can {name}"
        assert str(f) == f"cannot {name}"

    def test_bool(self):
        t = SeeSpies(True)
        f = SeeSpies(False)
        assert t
        assert not f

        # conversion to bool for non-bool args
        assert SeeSpies("") == f
        assert SeeSpies("nonempty") == t
        assert SeeSpies([]) == f
        assert SeeSpies([0]) == t
        assert SeeSpies(None) == f
        assert SeeSpies(0) == f
        assert SeeSpies(10) == t

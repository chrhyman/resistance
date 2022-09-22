from src.resistance.role.abilities import HideFromSpies
from src.resistance.util.constants import EVIL_TEAM


class TestHideFromSpies:
    def test_name(self):
        name = f"hide from {EVIL_TEAM}"
        t = HideFromSpies(True)
        f = HideFromSpies(False)
        assert t.name == name
        assert f.name == name

    def test_str(self):
        name = f"hide from {EVIL_TEAM}"
        t = HideFromSpies(True)
        f = HideFromSpies(False)
        assert str(t) == f"can {name}"
        assert str(f) == f"cannot {name}"

    def test_bool(self):
        t = HideFromSpies(True)
        f = HideFromSpies(False)
        assert t
        assert not f

        # conversion to bool for non-bool args
        assert HideFromSpies("") == f
        assert HideFromSpies("nonempty") == t
        assert HideFromSpies([]) == f
        assert HideFromSpies([0]) == t
        assert HideFromSpies(None) == f
        assert HideFromSpies(0) == f
        assert HideFromSpies(10) == t

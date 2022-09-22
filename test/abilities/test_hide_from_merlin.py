from src.resistance.role.abilities import HideFromMerlin
from src.resistance.util.constants import MERLIN


class TestHideFromMerlin:
    def test_name(self):
        name = f"hide from {MERLIN}"
        t = HideFromMerlin(True)
        f = HideFromMerlin(False)
        assert t.name == name
        assert f.name == name

    def test_str(self):
        name = f"hide from {MERLIN}"
        t = HideFromMerlin(True)
        f = HideFromMerlin(False)
        assert str(t) == f"can {name}"
        assert str(f) == f"cannot {name}"

    def test_bool(self):
        t = HideFromMerlin(True)
        f = HideFromMerlin(False)
        assert t
        assert not f

        # conversion to bool for non-bool args
        assert HideFromMerlin("") == f
        assert HideFromMerlin("nonempty") == t
        assert HideFromMerlin([]) == f
        assert HideFromMerlin([0]) == t
        assert HideFromMerlin(None) == f
        assert HideFromMerlin(0) == f
        assert HideFromMerlin(10) == t

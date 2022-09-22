from src.resistance.role.abilities import SeeMerlin
from src.resistance.util.constants import MERLIN


class TestSeeMerlin:
    def test_name(self):
        name = f"see {MERLIN}"
        t = SeeMerlin(True)
        f = SeeMerlin(False)
        assert t.name == name
        assert f.name == name

    def test_str(self):
        name = f"see {MERLIN}"
        t = SeeMerlin(True)
        f = SeeMerlin(False)
        assert str(t) == f"can {name}"
        assert str(f) == f"cannot {name}"

    def test_bool(self):
        t = SeeMerlin(True)
        f = SeeMerlin(False)
        assert t
        assert not f

        # conversion to bool for non-bool args
        assert SeeMerlin("") == f
        assert SeeMerlin("nonempty") == t
        assert SeeMerlin([]) == f
        assert SeeMerlin([0]) == t
        assert SeeMerlin(None) == f
        assert SeeMerlin(0) == f
        assert SeeMerlin(10) == t

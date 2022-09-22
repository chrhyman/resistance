from src.resistance.role.abilities import LookLikeMerlin
from src.resistance.util.constants import MERLIN


class TestLookLikeMerlin:
    def test_name(self):
        name = f"look like {MERLIN}"
        t = LookLikeMerlin(True)
        f = LookLikeMerlin(False)
        assert t.name == name
        assert f.name == name

    def test_str(self):
        name = f"look like {MERLIN}"
        t = LookLikeMerlin(True)
        f = LookLikeMerlin(False)
        assert str(t) == f"can {name}"
        assert str(f) == f"cannot {name}"

    def test_bool(self):
        t = LookLikeMerlin(True)
        f = LookLikeMerlin(False)
        assert t
        assert not f

        # conversion to bool for non-bool args
        assert LookLikeMerlin("") == f
        assert LookLikeMerlin("nonempty") == t
        assert LookLikeMerlin([]) == f
        assert LookLikeMerlin([0]) == t
        assert LookLikeMerlin(None) == f
        assert LookLikeMerlin(0) == f
        assert LookLikeMerlin(10) == t

from src.resistance.role.abilities import ShootMerlin
from src.resistance.util.constants import MERLIN


class TestShootMerlin:
    def test_name(self):
        name = f"shoot {MERLIN}"
        t = ShootMerlin(True)
        f = ShootMerlin(False)
        assert t.name == name
        assert f.name == name

    def test_str(self):
        name = f"shoot {MERLIN}"
        t = ShootMerlin(True)
        f = ShootMerlin(False)
        assert str(t) == f"can {name}"
        assert str(f) == f"cannot {name}"

    def test_bool(self):
        t = ShootMerlin(True)
        f = ShootMerlin(False)
        assert t
        assert not f

        # conversion to bool for non-bool args
        assert ShootMerlin("") == f
        assert ShootMerlin("nonempty") == t
        assert ShootMerlin([]) == f
        assert ShootMerlin([0]) == t
        assert ShootMerlin(None) == f
        assert ShootMerlin(0) == f
        assert ShootMerlin(10) == t

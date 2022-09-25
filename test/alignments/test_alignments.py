from src.resistance.role.alignment import Alignment
from src.resistance.role.alignments import Good, Evil


class TestAlignments:
    def test_eq(self):
        g1 = Good()
        g2 = Good()
        e1 = Evil()
        e2 = Evil()

        assert g1 == g2
        assert g1 is not g2
        assert e1 == e2
        assert e1 is not e2

        assert g1 != e1
        assert e2 != g2

        assert not (g1 == e2)
        assert not (e1 == g2)
        assert not (g2 != g1)
        assert not (e2 != e1)

    def test_subclass(self):
        assert issubclass(Good, Alignment)
        assert issubclass(Evil, Alignment)

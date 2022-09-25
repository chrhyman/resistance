from itertools import combinations

from src.resistance.role.ability import Ability
from src.resistance.role.abilities import *


class TestAbilities:
    def test_eq(self):
        abilities = [SeeSpies, SeeMerlin, ShootMerlin, LookLikeMerlin, HideFromMerlin, HideFromSpies]

        for ability in abilities:
            assert issubclass(ability, Ability)
            assert ability(True) == ability(True)
            assert ability(False) == ability(False)
            assert ability(True) != ability(False)
            assert ability(False) != ability(True)

        for a1, a2 in combinations(abilities, 2):
            assert a1(True) != a2(True)
            assert a1(False) != a2(False)
            assert a1(True) != a2(False)
            assert a1(False) != a2(True)

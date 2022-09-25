from itertools import combinations

from src.resistance.role import Role
from src.resistance.role.roles import *


class TestRoles:
    def test_eq(self):
        roles = [BaseGood, BaseEvil, Merlin, Percival, Assassin, Morgana, Mordred, Oberon, MordredAssassin]

        for role in roles:
            assert issubclass(role, Role)
            assert role() == role()
            assert role() is not role()

        for r1, r2 in combinations(roles, 2):
            assert r1() != r2()

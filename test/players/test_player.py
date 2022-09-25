from pytest import raises

from src.resistance.player import Player
from src.resistance.role import Role
from src.resistance.role.roles import BaseGood, BaseEvil
from src.resistance.util.errors import IllegalActionGameError

TEST_N = 1000


class TestPlayer:
    def test_id(self):
        players = [Player() for _ in range(TEST_N)]
        ids = [player.id for player in players]
        assert len(players) == len(set(ids))

    def test_name(self):
        # name is str(id)
        # (1) if name is not provided
        p1 = Player()
        assert p1.name == str(p1.id)
        assert str(p1) == str(p1.id)

        # (2) if name is not type str
        p2 = Player(None)
        assert p2.name == str(p2.id)
        assert str(p2) == str(p2.id)

        # (3) if name is empty string
        p3 = Player("")
        assert p3.name == str(p3.id)
        assert str(p3) == str(p3.id)

        # if name is provided, use that value
        p4 = Player("test")
        assert p4.name == "test"
        assert str(p4) == p4.name

        players = [p1, p2, p3, p4]
        for player in players:
            assert not player.ready
            assert player.role is None
            assert player.metadata is None

    def test_rename(self):
        player = Player("name")
        assert str(player) == "name"

        returned = player.rename("newname")
        assert player is returned
        assert str(player) == "newname"

    def test_set_ready_status(self):
        player = Player("test")
        assert not player.ready

        returned = player.set_ready_status(True)
        assert player is returned
        assert player.ready

        returned2 = player.set_ready_status(False)
        assert player is returned2
        assert not player.ready

        returned3 = player.set_ready_status("nonempty string")
        assert player is returned3
        assert player.ready

        returned4 = player.set_ready_status(None)
        assert player is returned4
        assert not player.ready

    def test_assign_role(self):
        player = Player("test")
        role = BaseGood()
        returned = player.assign_role(role)

        assert player is returned
        assert player.role is role
        assert type(player.role) is type(role)
        assert isinstance(player.role, Role)

        with raises(IllegalActionGameError):
            new_role = BaseEvil()
            player.assign_role(new_role)

        with raises(TypeError):
            Player().assign_role("BaseGood")

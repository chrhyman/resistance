from pytest import raises

from src.resistance.players import Player, Players
from src.resistance.util.constants import MIN_PLAYERS, MAX_PLAYERS
from src.resistance.util.errors import IllegalActionGameError, InvalidNumberGameError


class TestPlayers:
    def test_class_attributes(self):
        players = Players()
        assert Players.MIN == players.MIN
        assert Players.MIN == MIN_PLAYERS
        assert Players.MAX == players.MAX
        assert Players.MAX == MAX_PLAYERS

    def test_default_instance_attributes(self):
        players = Players()
        assert not players.started
        assert players.player_list == []
        assert len(players) == 0
        assert players.leader_index is None

    def test_constructor(self):
        players0 = Players(None)
        assert len(players0) == 0

        ps = [Player() for _ in range(4)]
        players1 = Players(ps)
        assert len(players1) == 4

        with raises(TypeError):
            ps = [f"player {n}" for n in range(5)]
            players2 = Players(ps)

        with raises(InvalidNumberGameError):
            ps = [Player() for _ in range(MAX_PLAYERS + 1)]
            players3 = Players(ps)

        p1 = Player()
        p2 = Player()
        p2.set_ready_status(True)
        assert p2.ready

        ps = [p1, p1, p2, p2, p2]
        players4 = Players(ps)
        assert len(players4) == 2
        assert not p2.ready

    def test_add_player(self):
        pass

    def test_all_players_ready(self):
        pass

    def test_get_leader(self):
        pass

    def test_get_player_by_id(self):
        pass

    def test_increment_leader(self):
        pass

    def test_next_leader(self):
        pass

    def test_remove_player(self):
        pass

    def test_remove_player_by_id(self):
        pass

    def test_start(self):
        pass

    def test_unready_all_players(self):
        pass

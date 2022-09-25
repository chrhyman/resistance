from copy import deepcopy

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
        players = Players(None)
        assert len(players) == 0

        ps = [Player() for _ in range(4)]
        players = Players(ps)
        assert len(players) == 4

        with raises(TypeError):
            ps = ["strings", "don't", "work"]
            Players(ps)

        # doesn't raise
        ps = [Player() for _ in range(MAX_PLAYERS)]
        Players(ps)

        # raises
        with raises(InvalidNumberGameError):
            ps = [Player() for _ in range(MAX_PLAYERS + 1)]
            Players(ps)

        # removes duplicates, sets all players to unready
        p1 = Player()
        p2 = Player()
        p2.set_ready_status(True)
        assert p2.ready
        ps = [p1, p1, p2, p1, p2, p2]
        players = Players(ps)
        assert len(players) == 2
        assert all(not player.ready for player in players)

    def test_add_player(self):
        players = Players()
        assert len(players) == 0
        p1 = Player()
        returned = players.add_player(p1)
        assert players is returned
        assert len(players) == 1

        with raises(TypeError):
            players.add_player("only Player instances work")

        # duplicate players aren't added again
        players.add_player(p1)
        players.add_player(p1)
        assert len(players) == 1

        # adding a new player sets all players to unready
        p1.set_ready_status(True)
        p2 = Player()
        players.add_player(p2)
        assert len(players) == 2
        assert not p1.ready

    def test_add_player_over_max(self):
        ps = [Player() for _ in range(MAX_PLAYERS)]
        players = Players(ps)

        with raises(InvalidNumberGameError):
            players.add_player(Player())

    def test_add_player_after_started(self):
        ps = [Player() for _ in range(MIN_PLAYERS)]
        players = Players(ps)

        for player in players:
            player.set_ready_status(True)

        players.start()

        with raises(IllegalActionGameError):
            players.add_player(Player())

    def test_all_players_ready(self):
        players = Players()
        # uses all(), and all([]) == True
        assert players.all_players_ready()

        p1 = Player()
        players.add_player(p1)
        assert not players.all_players_ready()
        p1.set_ready_status(True)
        assert players.all_players_ready()

        p2 = Player()
        players.add_player(p2)
        p2.set_ready_status(True)
        assert not players.all_players_ready()
        p1.set_ready_status(True)
        assert players.all_players_ready()

        for player in [Player() for _ in range(5)]:
            players.add_player(player)

        for player in players:
            player.set_ready_status(True)

        assert players.all_players_ready()
        p2.set_ready_status(False)
        assert not players.all_players_ready()

    def test_get_leader(self):
        ps = [Player() for _ in range(MIN_PLAYERS)]
        players = Players(ps)
        for player in players:
            player.set_ready_status(True)

        # a valid number of players and everyone is ready, but game isn't started yet
        with raises(IllegalActionGameError):
            players.get_leader()

        players.start()

        assert players.get_leader() is players.player_list[players.leader_index]
        assert players.leader_index == 0

        players.increment_leader()

        assert players.get_leader() is players[players.leader_index]
        assert players.leader_index == 1

    def test_get_player_by_id(self):
        name = "target player"
        p1 = Player(name)
        ps = [p1] + [Player() for _ in range(MIN_PLAYERS)]
        players = Players(ps)

        for player in players:
            player.set_ready_status(True)

        players.start()

        # returns Player object for method/attribute chaining
        assert players.get_player_by_id(p1.id) is p1
        assert players.get_player_by_id(p1.id).name == name

        # no player has id 0
        assert players.get_player_by_id(0) is None

        # non-int arguments will never find a player, even if it's the Player object
        assert players.get_player_by_id(p1) is None

    def test_increment_leader(self):
        ps = [Player() for _ in range(MIN_PLAYERS)]
        players = Players(ps)
        for player in players:
            player.set_ready_status(True)

        # can't call before game is started
        with raises(IllegalActionGameError):
            players.increment_leader()

        players.start()

        ls = []
        for i in range(MIN_PLAYERS):
            assert players.leader_index == i
            ls.append(players.get_leader())
            players.increment_leader()

        assert len(ls) == len(players)

        # it wraps to the beginning after the last increment
        assert players.leader_index == 0

    def test_next_leader(self):
        ps = [Player() for _ in range(MIN_PLAYERS)]
        players = Players(ps)
        for player in players:
            player.set_ready_status(True)

        players.start()
        dc_players = deepcopy(players)

        assert players is not dc_players
        assert players.get_leader() is not dc_players.get_leader()
        assert players.get_leader() == dc_players.get_leader()

        leaders = []
        for _ in range(MIN_PLAYERS * 2):
            leader = players.next_leader()
            copy_leader = dc_players.increment_leader().get_leader()
            assert leader == copy_leader
            leaders.append(leader)

        assert len(leaders) == MIN_PLAYERS * 2

        unique_leaders = []
        for player in leaders:
            if player not in unique_leaders:
                unique_leaders.append(player)

        assert len(unique_leaders) == MIN_PLAYERS

    def test_remove_player(self):
        pass

    def test_remove_player_by_id(self):
        pass

    def test_start(self):
        pass

    def test_unready_all_players(self):
        pass

from random import shuffle
from typing import TypeVar

from .player import Player
from .util.errors import IllegalActionGameError, InvalidNumberGameError
from .util.constants import MIN_PLAYERS, MAX_PLAYERS

Self = TypeVar("Self", bound="Players")


class Players:
    """
    Container for all players in a game of the Resistance.

    ----

    Constructor::

        Players(player_list: list[Player] = None)

    Properties::

        Players.player_list: list[Player]
        Players.started: bool
        Players.leader_index: int | None
        Players.player_count: int | None

    Methods::

        Players.add_player(player: Player) -> Self
        Players.all_players_reader() -> bool
        Players.get_leader() -> Player
        Players.get_player_by_id(_id: int) -> Player | None
        Players.next_leader() -> Player
        Players.remove_player(player: Player) -> Self
        Players.remove_player_by_id(self, _id: int) -> Self
        Players.start() -> None
        Players.unready_all_players() -> Self
    """
    MIN: int = MIN_PLAYERS
    MAX: int = MAX_PLAYERS

    def __init__(self, player_list: list[Player] = None) -> None:
        self.player_list: list[Player] = []
        self.started: bool = False

        if player_list is not None:
            for player in player_list:
                self.add_player(player)

        self.unready_all_players()

        self.leader_index: int | None = None
        self.player_count: int | None = None

    def add_player(self, player: Player) -> Self:
        if not isinstance(player, Player):
            raise TypeError(f"{player} is not an instance of Player")

        if len(self.player_list) >= Players.MAX:
            raise InvalidNumberGameError(f"Cannot add more than {Players.MAX} players")

        if self.started:
            raise IllegalActionGameError("Already started; cannot add new players to game in progress")

        self.player_list.append(player)
        return self

    def all_players_ready(self) -> bool:
        return all(pl.ready for pl in self.player_list)

    def get_leader(self) -> Player:
        if not self.started or self.leader_index is None:
            raise IllegalActionGameError("Game hasn't started")

        return self.player_list[self.leader_index]

    def get_player_by_id(self, _id: int) -> Player | None:
        for player in self.player_list:
            if player.id == _id:
                return player

        return None

    def next_leader(self) -> Player:
        if not self.started or self.leader_index is None:
            raise IllegalActionGameError("Game hasn't started")

        self.leader_index += 1
        if self.leader_index >= self.player_count:
            self.leader_index = 0

        return self.player_list[self.leader_index]

    def remove_player(self, player: Player) -> Self:
        if not isinstance(player, Player):
            raise TypeError(f"{player} is not an instance of Player")

        if self.started:
            raise IllegalActionGameError("Cannot remove player from game in progress")

        try:
            self.player_list.remove(player)
        except ValueError:  # player not in self.player_list
            pass

        return self

    def remove_player_by_id(self, _id: int) -> Self:
        pl = self.get_player_by_id(_id)
        if pl is not None:
            self.remove_player(pl)

        return self

    def start(self) -> None:
        if self.started:
            raise IllegalActionGameError("Game already started")

        if not self.all_players_ready():
            raise IllegalActionGameError("Not all players are ready to start")

        current_count = len(self.player_list)

        if not(Players.MIN <= current_count <= Players.MAX):
            raise InvalidNumberGameError(
                f"Invalid player count: {current_count} (must have {Players.MIN} to {Players.MAX} players)")

        shuffle(self.player_list)

        self.player_count = current_count
        self.leader_index = 0
        self.started = True

    def unready_all_players(self) -> Self:
        for pl in self.player_list:
            pl.set_ready_status(False)

        return self

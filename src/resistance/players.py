from random import shuffle
from typing import List, Optional

from .player import Player
from .util.errors import IllegalActionGameError, InvalidNumberGameError
from .util.constants import MIN_PLAYERS, MAX_PLAYERS


class Players:
    MIN = MIN_PLAYERS
    MAX = MAX_PLAYERS

    def __init__(self, player_list: List[Player] = None) -> None:
        self.player_list = []
        self.frozen: bool = False

        if player_list is not None:
            for player in player_list:
                self.add_player(player)

        self.unready_all_players()

        self.leader_index: Optional[int] = None
        self.player_count: Optional[int] = None

    def add_player(self, player: Player) -> None:
        if not isinstance(player, Player):
            raise TypeError(f"{player} is not an instance of Player")

        if len(self.player_list) >= Players.MAX:
            raise InvalidNumberGameError(f"Cannot add more than {Players.MAX} players")

        if self.frozen:
            raise IllegalActionGameError("Already started; cannot add new players to game in progress")

        self.player_list.append(player)

    def all_players_ready(self) -> bool:
        return all(pl.ready for pl in self.player_list)

    def get_leader(self) -> Player:
        if not self.frozen or self.leader_index is None:
            raise IllegalActionGameError("Game hasn't started")

        return self.player_list[self.leader_index]

    def get_player_by_id(self, _id: int) -> Optional[Player]:
        for player in self.player_list:
            if player.id == _id:
                return player
        return None

    def next_leader(self) -> Player:
        if not self.frozen or self.leader_index is None:
            raise IllegalActionGameError("Game hasn't started")

        self.leader_index += 1
        if self.leader_index >= self.player_count:
            self.leader_index = 0

        return self.player_list[self.leader_index]

    def remove_player(self, player: Player):
        if not isinstance(player, Player):
            raise TypeError(f"{player} is not an instance of Player")

        if self.frozen:
            raise IllegalActionGameError("Cannot remove player from game in progress")

        if player not in self.player_list:
            pass
        else:
            self.player_list.remove(player)

    def remove_player_by_id(self, _id: int):
        pl = self.get_player_by_id(_id)
        self.remove_player(pl)

    def start(self) -> None:
        if self.frozen:
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
        self.frozen = True

    def unready_all_players(self) -> None:
        for pl in self.player_list:
            pl.set_ready_status(False)

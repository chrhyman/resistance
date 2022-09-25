from random import shuffle
from typing import Iterator, TypeVar

from .player import Player
from .util.errors import IllegalActionGameError, InvalidNumberGameError
from .util.constants import MIN_PLAYERS, MAX_PLAYERS

Self = TypeVar("Self", bound="Players")


class Players:
    """
    A ``list``-like container for all players in a game of the Resistance.
    Maintains the player order and the current leader via their index.

    ----

    **Constructor**::

        Players(player_list: list[Player] = None)

    **Class Properties**::

        Players.MIN: int
        Players.MAX: int

    **Instance Properties**::

        Players.player_list: list[Player]
        Players.started: bool
        Players.leader_index: int | None

    **Implements**::

        Players[item] == Players.player_list[item]
        iter(Players) == iter(Players.player_list)
        len(Players) == len(Players.player_list)

    **Methods**::

        Players.add_player(player: Player) -> Self
        Players.all_players_ready() -> bool
        Players.get_leader() -> Player
        Players.get_player_by_id(_id: int) -> Player | None
        Players.increment_leader() -> Self
        Players.next_leader() -> Player
        Players.remove_player(player: Player) -> bool
        Players.remove_player_by_id(self, _id: int) -> bool
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

        self.leader_index: int | None = None

    def __getitem__(self, item: int | slice) -> Player | list[Player]:
        """
        ``Players[item] == Players.player_list[item]``
        """
        return self.player_list[item]

    def __iter__(self) -> Iterator[Player]:
        """
        ``iter(Players) == iter(Players.player_list)``
        """
        return iter(self.player_list)

    def __len__(self) -> int:
        """
        ``len(Players) == len(Players.player_list)``
        """
        return len(self.player_list)

    def add_player(self, player: Player) -> Self:
        """
        Adds a new player. Sets all players to unready.

        :param player: Player object to append
        :return: updated Players
        :raises TypeError: player is not instance of Player
        :raises InvalidNumberGameError: can't add more than Players.MAX
        :raises IllegalActionGameError: can't add after game is started
        """
        if not isinstance(player, Player):
            raise TypeError(f"{player} ({player.__class__.__name__}) is not an instance of Player")

        if len(self) >= Players.MAX:
            raise InvalidNumberGameError(f"Cannot add more than {Players.MAX} players")

        if self.started:
            raise IllegalActionGameError("Already started; cannot add new players to game in progress")

        if player not in self:
            self.player_list.append(player)

        return self.unready_all_players()

    def all_players_ready(self) -> bool:
        """
        True if all players are ready

        :return: bool
        """
        return all(player.ready for player in self)

    def get_leader(self) -> Player:
        """
        Returns the current leader

        :return: Player at Players[leader_index]
        :raises IllegalActionGameError: before game has started
        """
        if not self.started or self.leader_index is None:
            raise IllegalActionGameError("Game hasn't started")

        return self[self.leader_index]

    def get_player_by_id(self, _id: int) -> Player | None:
        """
        Returns Player object with given ID, or None

        :param _id: ID of player to get
        :return: Player if found, else None
        """
        for player in self:
            if player.id == _id:
                return player

        return None

    def increment_leader(self) -> Self:
        """
        Increments the leader index, wrapping if necessary

        :return: updated Players
        :raises IllegalActionGameError: before game has started
        """
        if not self.started or self.leader_index is None:
            raise IllegalActionGameError("Game hasn't started")

        self.leader_index += 1
        self.leader_index %= len(self)
        return self

    def next_leader(self) -> Player:
        """
        Increments leader index (wrapping if necessary) and returns the new leader

        :return: Player
        :raises IllegalActionGameError: before game has started
        """
        return self.increment_leader().get_leader()

    def remove_player(self, player: Player) -> bool:
        """
        ``True`` if ``player`` was removed from ``Players``.
        ``False`` if ``player`` isn't in ``Players`` or isn't an instance of ``Player``.
        Sets all players to unready if successful.

        :param player: Player to remove
        :return: bool
        :raises IllegalActionGameError: after game has started
        """
        if self.started:
            raise IllegalActionGameError("Cannot remove player from game in progress")

        try:
            self.player_list.remove(player)
            self.unready_all_players()
            return True
        except ValueError:  # player not in self.player_list
            return False

    def remove_player_by_id(self, _id: int) -> bool:
        """
        ``True`` if ``Player`` with given ID was removed from ``Players``.
        ``False`` if that ID isn't in ``Players``.
        Sets all players to unready if successful.

        :param _id: Player.id to remove
        :return: bool
        :raises IllegalActionGameError: after game has started
        """
        player: Player | None = self.get_player_by_id(_id)
        return self.remove_player(player)

    def start(self) -> None:
        """
        Starts the game, shuffling the player order and setting the leader index to 0.
        The game can only be started if a valid number of players are all ready.

        :return: None
        :raises IllegalActionGameError: after game has started, or if any players are not ready
        :raises InvalidNumberGameError: fewer than MIN or more than MAX players
        """
        if self.started:
            raise IllegalActionGameError("Game already started")

        if not self.all_players_ready():
            raise IllegalActionGameError("Not all players are ready to start")

        if not (Players.MIN <= len(self) <= Players.MAX):
            raise InvalidNumberGameError(
                f"Invalid player count: {len(self)} (must have {Players.MIN} to {Players.MAX} players)")

        shuffle(self.player_list)

        self.leader_index = 0
        self.started = True

    def unready_all_players(self) -> Self:
        """
        Sets all players to unready if game hasn't started.

        :return: updated Players
        """
        if not self.started:
            for player in self:
                player.set_ready_status(False)

        return self

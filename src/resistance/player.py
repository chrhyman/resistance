from typing import Any, TypeVar

from .role import Role
from .util.errors import IllegalActionGameError

Self = TypeVar("Self", bound="Player")


class Player:
    """
    Represents a single player in a game of the Resistance.

    ----

    Constructor::

        Player(name: str, metadata: Any = None)

    Instance Properties::

        Player.id: int        # unique
        Player.name: str
        Player.ready: bool
        Player.role: Role | None
        Player.metadata: Any  # optional external object

    Methods::

        Player.assign_role(role: Role) -> Self
        Player.rename(new_name: str) -> Self
        Player.set_ready_status(status: bool) -> Self
    """
    _next_id = 1

    def __init__(self, name: str = "", metadata: Any = None) -> None:
        self.id: int = Player._next_id
        Player._next_id += 1

        if name == "" or not isinstance(name, str):
            self.name = str(self.id)
        else:
            self.name = name

        self.metadata: Any = metadata
        self.ready: bool = False
        self.role: Role | None = None

    def __repr__(self) -> str:
        return f"{self.name} (id={self.id})"

    def __str__(self) -> str:
        return str(self.name)

    def assign_role(self, role: Role) -> Self:
        """
        Assigns ``Role`` instance to ``Player`` if one is not yet assigned.

        :param role: Role to be assigned
        :return: updated Player
        :raises TypeError: role is not instance of Role
        :raises IllegalActionGameError: player already has role
        """
        if not isinstance(role, Role):
            raise TypeError(f"Can only assign Role type, but {role} is {role.__class__.__name__}")

        if self.role is not None:
            raise IllegalActionGameError(f"Player {self.name} (id={self.id}) already assigned role {self.role}",
                                         summary="A role is already assigned to this player.")

        self.role = role
        return self

    def rename(self, new_name: str) -> Self:
        """
        Rename the ``Player``. Doesn't change ``Player.id``

        :param new_name: replacement name
        :return: updated Player
        """
        self.name = str(new_name)
        return self

    def set_ready_status(self, status: bool) -> Self:
        """
        Set ``Player.ready`` to ``bool(status)``

        :param status: ready (True) or not ready (False)
        :return: updated Player
        """
        self.ready = bool(status)
        return self

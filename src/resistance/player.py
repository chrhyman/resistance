from typing import Any, Optional, TypeVar

from .role import Role
from .util.errors import IllegalActionGameError

Self = TypeVar("Self", bound="Player")


class Player:
    _next_id = 1

    def __init__(self, name: str = "", metadata: Optional[Any] = None) -> None:
        self.id = Player._next_id
        Player._next_id += 1

        if name == "":
            self.name = str(self.id)
        else:
            self.name = str(name)

        self.metadata = metadata
        self.ready = False
        self.role = None

    def __str__(self) -> str:
        if self.name == str(self.id):
            return str(self.id)

        return f"{self.name} (id={self.id})"

    def assign_role(self, role: Role) -> Self:
        if self.role is not None:
            raise IllegalActionGameError(f"Player {self.name} (id={self.id}) already assigned role {self.role}",
                                         summary="A role is already assigned to this player.")

        if not isinstance(role, Role):
            raise TypeError(f"Can only assign Role type, but {role} is {role.__class__.__name__}")

        self.role = role
        return self

    def rename(self, new_name: str) -> Self:
        self.name = str(new_name)
        return self

    def set_ready_status(self, status: bool) -> Self:
        self.ready = bool(status)
        return self

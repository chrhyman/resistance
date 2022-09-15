from typing import Any

from ..role import Role
from ..util import IllegalActionGameError


class Player:
    _next_id = 1

    def __init__(self, name: str = '', metadata: Any = None):
        self.id = Player._next_id
        Player._next_id += 1

        if name == '':
            self.name = str(self.id)
        else:
            self.name = str(name)

        self.metadata = metadata
        self.role = None

    def __str__(self) -> str:
        if self.name == str(self.id):
            return str(self.id)

        return f"{self.name} (id={self.id})"

    def assign_role(self, role: Role):
        if self.role is not None:
            raise IllegalActionGameError(f"Player {self.name} (id={self.id}) already assigned role {self.role}",
                                         summary="A role is already assigned to this player.")

        if not isinstance(role, Role):
            raise TypeError(f"Can only assign Role type, but {role} is {type(role)}")

        self.role = role

    def rename(self, new_name: str):
        self.name = str(new_name)

"""Контракты (протоколы) для модулей."""

from typing import Any, Protocol


class PostRepository(Protocol):
    def get_all(self) -> list[Any]: ...
    def add(self, post: Any) -> None: ...

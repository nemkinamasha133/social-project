"""Контракты (протоколы) для модулей."""

from typing import Protocol


class PostRepository(Protocol):
    def get_all(self) -> list: ...
    def add(self, post) -> None: ...

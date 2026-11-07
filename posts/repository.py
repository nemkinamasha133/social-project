"""Репозиторий постов."""

from posts.models import Post


class PostRepository:
    """Доступ к постам в БД."""

    def __init__(self, conn) -> None:
        self.conn = conn

    def get_all(self) -> list[Post]:
        """Вернуть все посты."""
        return []

    def add(self, post: Post) -> None:
        """Добавить пост."""
        pass

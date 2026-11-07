"""Репозиторий постов."""

class PostRepository:
    def __init__(self, conn):
        self.conn = conn

    def add(self, post):
        # TODO: реализовать сохранение поста в БД
        raise NotImplementedError
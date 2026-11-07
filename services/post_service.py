"""Сервис постов."""
from repositories.post_repo import PostRepository

class PostService:
    """Бизнес-логика постов."""
    def __init__(self, repo: PostRepository) -> None:
        self.repo = repo

    def list_posts(self):
        """Список постов."""
        return self.repo.get_all()

"""Модель поста."""
class Post:
    """Пост в социальной сети."""
    def __init__(self, author_id: int, text: str) -> None:
        self.author_id = author_id
        self.text = text

    def __repr__(self) -> str:
        return f"Post(author_id={self.author_id}, text={self.text!r})"
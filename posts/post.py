"""Модель поста."""

class Post:
    def __init__(self, author_id: int, text: str):
        self.author_id = author_id
        self.text = text

    def __repr__(self):
        return f"Post(author_id={self.author_id}, text={self.text!r})"
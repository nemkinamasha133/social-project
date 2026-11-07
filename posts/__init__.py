"""Модуль работы с постами."""

from posts.models import Post
from posts.service import PostService

__all__ = ["Post", "PostService"]

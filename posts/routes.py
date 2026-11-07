"""HTTP-роуты для постов."""

from flask import Blueprint, jsonify

bp = Blueprint("posts", __name__, url_prefix="/posts")


@bp.get("/")
def list_posts():
    """Список постов."""
    return jsonify({"posts": []})

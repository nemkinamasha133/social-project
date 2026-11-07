"""Тесты для проверки запуска."""


def test_list_posts_returns_empty(client):
    """GET /posts/ возвращает пустой список."""
    response = client.get("/posts/")
    assert response.status_code == 200
    assert response.get_json() == {"posts": []}

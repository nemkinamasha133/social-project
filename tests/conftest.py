"""Фикстуры для тестов."""
import pytest
from app import create_app

@pytest.fixture
def app():
    """Тестовое приложение."""
    app = create_app()
    app.config.update(TESTING=True)
    yield app

@pytest.fixture
def client(app):
    """Flask test client."""
    return app.test_client()
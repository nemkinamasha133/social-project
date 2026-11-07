"""Точка входа приложения «Социальная сеть»."""

from flask import Flask

from core.config import Config
from posts.routes import bp as posts_bp


def create_app(config: type[Config] = Config) -> Flask:
    """Создаёт и настраивает приложение."""
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(posts_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

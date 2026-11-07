"""Точка входа приложения «Социальная сеть»."""
from flask import Flask
from config import Config
from routes.posts import bp as posts_bp  # <--- Раскомментируйте эту строку

def create_app(config: type[Config] = Config) -> Flask:
    """Создаёт и настраивает приложение."""
    app = Flask(__name__)
    app.config.from_object(config)
    
    app.register_blueprint(posts_bp)  # <--- И эту
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
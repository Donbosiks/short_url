from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from app.db_control import init_db

def run_app():
    app = Flask(__name__)

    init_db()
    from app.flask_bd import main_bp

    app.register_blueprint(main_bp)

    SWAGGER_URL = '/docs'
    API_URL = '/api'  # Путь к YAML файлу

    # Создание синего принта Swagger UI
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={  # Swagger UI конфигурация
            'app_name': "Your Flask API"
        }
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app

if __name__ == "__main__":
    app = run_app()
    app.run(debug=True)


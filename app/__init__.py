from flask import Flask
from app.db_control import init_db


def run_app():

    app = Flask(__name__)
    init_db()
    from app.flask_bd import main_bp

    app.register_blueprint(main_bp)

    return app
# app.py

from flask import Flask
import config
from routes.chat_routes import register_chat_routes
from routes.dash_app import init_dash_app

def create_app():
    app = Flask(__name__)
    # Carga constantes (APP_NAME, DDL_COMMANDS…) en app.config si lo necesitas
    app.config.from_object(config)

    register_chat_routes(app)
    init_dash_app(app)
    return app

if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=5000)
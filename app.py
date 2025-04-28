from flask import Flask
from routes.chat_routes import register_chat_routes
from routes.dash_app import init_dash_app

app = Flask(__name__)

register_chat_routes(app)
init_dash_app(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
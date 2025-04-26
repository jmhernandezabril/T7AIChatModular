from flask import Flask
from main import register_routes

app = Flask(__name__)

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
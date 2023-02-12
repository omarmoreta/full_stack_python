from flask import Flask;

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, Animal Hangout Spot"

    return app
from flask import Flask
import os

# APP FACTORY
def create_app():
    # FLASK INSTANCE
    app = Flask(__name__)
    app.config["FLASK_DEBUG"] = True

    # INDEX ROUTE
    @app.route("/")
    def hello():
        return "Hello from the Animal Spa!"

    # REGISTER ANIMAL BLUEPRINT
    from . import animal
    app.register_blueprint(animal.bp)

    # RETURN THE APP
    return app

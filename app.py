# CONFIG
from flask import Flask

# CREATE APP INSTANCE
app = Flask(__name__)

# INDEX ROUTE


@app.route("/")
def index():
    return "Hello, this is an Animal Hangout Spot"

# ANIMAL INDEX ROUTE


@app.route("/animals")
def animals():
    return "These are the pets that are just chillin' at the Animal Hangout Spot"

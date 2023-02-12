# CONFIG
from flask import Blueprint, render_template
import json

# IMPORT MOCK DATA
animals = json.load(open("animals.json"))
print(animals)

# BLUEPRINT INSTANCE
bp = Blueprint("animal", __name__, url_prefix="/animals")

# GET /animals
@bp.route("/")
def index():
    return render_template("index.html", animals=animals)

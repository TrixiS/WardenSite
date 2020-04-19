import logging

from flask import request, session, render_template, make_response, url_for
from app import WardenApp
from config import Config

logging.basicConfig(level=logging.INFO)

app = WardenApp(__name__, static_folder="static", template_folder="templates")

# TODO:
#   вставлять язык в сессию и получать оттуда

@app.route("/setlang/<lang>")
def setlang(lang: str):
    pass

@app.route('/')
@app.route("/home/")
def index():
    return "Just for a test"


app.secret_key = Config.secret_key
app.run(debug=True)
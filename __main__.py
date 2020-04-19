import logging

from flask import request, session, render_template, make_response, url_for, redirect
from flask_language import Language, current_language
from app import WardenApp
from config import Config

logging.basicConfig(level=logging.INFO)

app = WardenApp(__name__, static_folder="static", template_folder="templates")
lang = Language(app)


@lang.allowed_languages
def get_allowed_languages():
    return list(app.langs.keys())


@lang.default_language
def get_default_language():
    return "en"


@app.route("/setlang/")
def setlang():
    lang.change_language(request.args.get("new_lang") or "en")
    return redirect(url_for(".index"))


@app.route('/')
def index():
    return "TODO: home"


app.secret_key = Config.secret_key
app.run(debug=True)
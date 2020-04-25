import logging

from flask import jsonify, request, session, render_template, make_response, url_for, redirect
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


def render_with_lang(*args, **kwargs):
    name = args[0].split('.')[0]
    kwargs["lang"] = app.langs[current_language]
    kwargs["langs"] = tuple(l for l in app.langs.keys() if l != kwargs["lang"]["lang_code"])
    kwargs["title"] = kwargs["lang"][name]
    return render_template(*args, **kwargs)


@app.route("/setlang/")
def setlang():
    lang.change_language(request.args.get("new_lang") or "en")
    return jsonify({
        "language": str(current_language)
    })


@app.route('/')
def index():
    return render_with_lang("index.html")


@app.route("/commands/")
def commands():
    return render_with_lang("commands.html")


app.secret_key = bytes(Config.secret_key, encoding="utf-8")
app.run(debug=True)
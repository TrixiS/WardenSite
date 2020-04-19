import json
from flask import Flask
from pathlib import Path


class WardenApp(Flask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.langs = self.load_langs()

    def load_langs(self):
        lang_path = Path(self.root_path).joinpath(self.static_folder).joinpath("langs")
        langs = dict()

        for file in filter(lambda x: x.is_file(), lang_path.glob("*.json")):
            with file.open(encoding="utf-8", mode="r+") as f:
                langs[file.stem.lower()] = json.load(f)

        return langs

import json
import os


def load_json(website: str):
    __basedir = os.path.dirname(__file__)
    __dir = os.path.join(__basedir, "json", f"{website.lower()}.json")

    if not os.path.exists(__dir):
        raise FileNotFoundError(f"File {__dir} not found")

    with open(__dir, "r", encoding="utf-8") as f:
        text = f.read()
        return json.loads(text)

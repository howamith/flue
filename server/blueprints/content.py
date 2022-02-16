# Flask modules.
from flask import Blueprint, send_file
from flask.typing import ResponseValue

content = Blueprint(
    "content", __name__, static_folder="../../client/www", static_url_path=""
)


@content.get("/")
def index() -> ResponseValue:
    return send_file("../client/www/index.html")

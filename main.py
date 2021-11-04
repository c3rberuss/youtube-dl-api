import json
import os
from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class UrlType(str, Enum):
    yt = "yt"
    vimeo = "vimeo"


@app.get("/urls/")
def get_dash_url(url: str):
    yt_result = os.popen("youtube-dl -f \"best[height<=480]\" -g {0}".format(url))
    new_url = yt_result.read().strip()

    return {"url": new_url}


@app.get("/formats")
def get_formats(url: str):
    yt_result = os.popen("youtube-dl --dump-json {0}".format(url))
    data = yt_result.read().strip()

    return json.loads(data)

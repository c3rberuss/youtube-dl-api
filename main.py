import json
import os
from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/download")
def download_audio(url: str):
    yt_result = os.popen("youtube-dl -j -f 'bestaudio[ext=m4a]' {0}".format(url))
    data = yt_result.read().strip()

    video_info = json.loads(data)

    return video_info

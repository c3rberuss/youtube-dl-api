import json
import os
from urllib import request
from fastapi import FastAPI
from starlette.responses import FileResponse, StreamingResponse

app = FastAPI()


@app.get("/audio")
def audio_url(url: str):
    yt_result = os.popen("youtube-dl -j -f 'bestaudio[ext=m4a]' {0}".format(url))
    data = yt_result.read().strip()

    video_info = json.loads(data)

    return video_info

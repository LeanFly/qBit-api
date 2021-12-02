# coding=utf-8

from qbittorrent import Client
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8002",
    "http://127.0.0.1:8002",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/qbit")
async def qBitDownload(magnet: str):
    # 连接qbit的webUI
    qbit = Client("http://100.102.167.97:7070/")
    # 登录webUI
    qbit.login("admin", "qbit666")

    # 打印已有的torrent
    # torrents = qbit.torrents()
    # for torrent in torrents:
    #     print(torrent["name"])
    qbit.download_from_link(magnet)
    return "done"


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8008)

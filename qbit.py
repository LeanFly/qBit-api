# coding=utf-8

from qbittorrent import Client
from transmission_rpc import Client as trans
from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()


@app.get("/qbit")
async def qBitDownload(magnet: str):
    # 连接qbit的webUI，填写相应的qbit webUI访问地址
    qbit = Client("http://ip:port")
    # 登录webUI，填写相应的用户名、密码
    qbit.login("username", "password")
    # 开始下载
    qbit.download_from_link(magnet)
    return "done"


@app.get("/trans")
async def transDownload(url: str):
    # connect transmision
    # host 填ip或域名，不带http；port是端口，默认是9091，有转发请填转发后的
    tr = trans(host="127.0.0.1", port=9091, username="", password="")
    # download；这里做了判断，如果是 .torrent 的下载链接用requests先做处理
    key = url.split(".")[-1]
    if key == "torrent":
        torentUrl = requests.get(url).content
        tr.add_torrent(torentUrl)
    else:
        tr.add_torrent(url)
    return "done"

if __name__ == "__main__":
    uvicorn.run(app="qbit:app", host="0.0.0.0", port=8000, reload=True)

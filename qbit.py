# coding=utf-8

from qbittorrent import Client
from transmission_rpc import Client as trans
from fastapi import FastAPI
import uvicorn
import requests
import configparser

# 获取配置信息
conf = configparser.ConfigParser()
conf.read("config.ini")

app = FastAPI()


@app.get("/qbit")
async def qBitDownload(magnet: str):
    # 连接qbit的webUI，填写相应的qbit webUI访问地址
    qbit = Client(conf.get("qbit", "host"))
    # 登录webUI，填写相应的用户名、密码
    qbit.login(conf.get("qbit", "username"), conf.get("qbit", "password"))
    # 开始下载
    qbit.download_from_link(magnet)
    return "done"


@app.get("/trans")
async def transDownload(url: str):
    # connect transmision
    # host 填ip或域名，不带http；port是端口，默认是9091，有转发请填转发后的
    tr = trans(host=conf.get("trans", "host"), port=int(conf.get("trans", "port")),
               username=conf.get("trans", "username"), password=conf.get("trans", "password"))
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

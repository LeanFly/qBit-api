# coding=utf-8

from qbittorrent import Client
from fastapi import FastAPI
import uvicorn

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


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)

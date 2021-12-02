## 基于 python-qbittorrent fastapi
## 使用fastapi创建API，使用python-qbittorrent访问qbit的webUI
## 访问创建的API，传入下载链接一键下载

# Docker的实现方式
    - docker pull leanfly/qbit-api:latest
    - docker run -dit --name qbit-api -p 8008:8000 -v $PWD/qbit.py:/code/qbit.py leanfly/qbit-api:latest
    - 浏览器访问：http://ip:port/qbit?magnet=(下载链接)
    - 示例：
        - http://127.0.0.1:8008/qbit?magnet=magnet:?xt=urn:btih:61769ede98c4276d47aaa3b41f05c951c41d2265&dn=The.Last.Duel.2021.1080p.WEBRip.DD2.0.x264-NOGRP&tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2820&tr=udp%3A%2F%2F9.rarbg.to%3A2770&tr=udp%3A%2F%2Ftracker.thinelephant.org%3A12800&tr=udp%3A%2F%2Ftracker.fatkhoala.org%3A13800

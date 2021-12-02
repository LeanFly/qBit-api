// [rule: 下载 ? ]

// 获取传入的下载链接
var key = param(1);

var data = request({
    url: "http://ip:port/qbit?magnet=" + key,
    method: "get",
})

sendText(data)

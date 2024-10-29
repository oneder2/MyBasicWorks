# 需要对每一个键值加引号，并且在每一个键值对之间加入逗号
"""
Host: movie.douban.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br, zstd
Referer: https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=
X-Requested-With: XMLHttpRequest
Connection: keep-alive
Cookie: bid=Q19paatYCf4; __utma=30149280.698854594.1702632619.1702632619.1702632619.1; ll="108288"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1726428978%2C%22https%3A%2F%2Fm.douban.com%2F%22%5D; _pk_id.100001.4cf6=997560a6acf1dd22.1726428978.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __yadk_uid=SFsIA8n0vVfB8DWSNcTOfvhSWnmQcG0Q
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Sec-GPC: 1
TE: trailers
"""

import requests

headers = {
    "Host": "movie.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Cookie": "bid=Q19paatYCf4; __utma=30149280.698854594.1702632619.1702632619.1702632619.1; ll='108288'; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1726428978%2C%22https%3A%2F%2Fm.douban.com%2F%22%5D; _pk_id.100001.4cf6=997560a6acf1dd22.1726428978.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __yadk_uid=SFsIA8n0vVfB8DWSNcTOfvhSWnmQcG0Q",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "TE": "trailers",
}

response = requests.get("https://movie.douban.com/j/chart/top_list", headers=headers)
print(response.text)



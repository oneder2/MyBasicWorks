"""
响应对象.text 获取字符串数据
响应对象.content 获取字节数据
响应对象.json() json数据

https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=
找到了top_list

https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start=20&limit=20




"""

import requests

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start=20&limit=20"

header = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    # 'Referer: https': 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start=20&limit=20',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Cookie': 'bid=Q19paatYCf4; __utma=30149280.698854594.1702632619.1702632619.1702632619.1; ll="108288"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1726428978%2C%22https%3A%2F%2Fm.douban.com%2F%22%5D; _pk_id.100001.4cf6=997560a6acf1dd22.1726428978.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __yadk_uid=SFsIA8n0vVfB8DWSNcTOfvhSWnmQcG0Q',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1'
}

res = requests.get(url, headers=header)
data = res.json()

for i in data:
    print(i['title'])

# print(type(data))

"""
top_list 

https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start=40&limit=20
https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start=60&limit=20

滚动分页：参数值不一样，数据不一样

每一页只有20条数据（limit = 20）

"""

import requests


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
}

count = 1
for i in range(1, 1001, 20):
    print("进入循环")
    url = f"https://movie.douban.com/j/chart/top_list?type=11&interval_id=100:90&action=&start={i}&limit=20"
    # 发起请求
    res = requests.get(url, headers = header)
    # 获取响应
    data = res.json()
    # 解析数据
    for item in data:
        print(f"{count} -- 电影的名称：{item['title']}")
        count += 1

"""
指定餐厅地址查询

获取餐厅的数据

通过输入关键字发起：
    https://www.mcdonalds.com.cn/ajaxs/search_by_keywords
    得到的是通过关键字搜索的模糊地址

通过点击某一个地址，发起
    https://www.mcdonalds.com.cn/ajaxs/search_by_point
    获取地址附件的餐厅地址
"""

import requests


url = "https://www.mcdonalds.com.cn/ajaxs/search_by_point"

# 发起Post请求，一般需要携带参数
abc = {
    'point' : '28.146841,113.065296',
    'type' : ''
}

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'
}

res = requests.post(url, data = abc, headers = header)
 
m = res.json()

for i in m['data']:
    print(i["city"], i["district"], i["address"])
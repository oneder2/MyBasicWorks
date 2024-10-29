"""
分析网页请求url
https://join.qq.com/api/v1/position/searchPosition?timestamp=1726703319614
https://join.qq.com/api/v1/position/searchPosition?timestamp=1726703385359
"""

import requests
import re

# 分页页面
page_url = "https://join.qq.com/api/v1/position/searchPosition?timestamp=1726704269203"

# 请求头
headers = {
    "content-type": "application/json"
    }

data = {"projectIdList":[1],"keyword":"","bgList":[],"workCountryType":0,"workCityList":[],"recruitCityList":[],"positionFidList":[],"pageIndex":1,"pageSize":10}

res = requests.post(page_url, headers=headers, json=data)
for i in res.json()["data"]["positionList"]:
    print(i["id"], i["position"], i["positionTitle"], i["positionFamily"], i["projectId"], i["workCities"])

# # 使用正则表达式提取数据
# pattern = re.compile(r'')

# # 使用findall方法获取所有匹配的数据
# position_ids = pattern.findall(res.text)

# print(position_ids)
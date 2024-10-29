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

address = input('请输入你想要查询的地址：')

address_url = 'https://www.mcdonalds.com.cn/ajaxs/search_by_keywords'
rest_url = 'https://www.mcdonalds.com.cn/ajaxs/search_by_point'

# 长沙
address_data = {
    "keywords": address,
    "location[info]": "OK",
    "location[position][lng]": "121.47004",
    "location[position][lat]": "31.23136"
}

res = requests.post(address_url, data = address_data)
add_res_data = res.json()

# 循环获得一条地址数据，进而获取所有餐厅
for i in add_res_data["data"]:
    # print(i["address"])
    # 发去获取餐厅的url需要携带坐标参数，即地址经纬度
    dining_room_data = {
        "point":i["location_format"].replace('|', ',') ,
        "type": ""
    }

    dining_room_url_res = requests.post(rest_url, data = dining_room_data)
    rest_res = rest_res.json()

    for i in dining_room_url_res['data']:
        print(i["city"], i["district"], i["address"])

    # break

    


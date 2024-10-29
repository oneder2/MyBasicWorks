import requests

# url = "https://www.mcdonalds.com.cn/top/map"

address = input("请输入想要查询的地址：")

url = "https://www.mcdonalds.com.cn/ajaxs/search_by_keywords"
point_url = "https://www.mcdonalds.com.cn/ajaxs/search_by_point"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
}

data = {
    "keywords": address,
    "location[info]": "OK",
    "location[position][lng]": "121.47004",
    "location[position][lat]":"31.23136"
    }

res = requests.post(url, data = data, headers = headers)
res.encoding = "UTF-8"

resJson = res.json()

for loc in resJson["data"]:
    rest_data = {
        "point" : loc["location_format"].replace("|", ","), 
        "type" : ""
        }
    
    rest_res = requests.post(url = point_url, data = rest_data)
    for rest in rest_res.json()["data"]:
        print(f'餐厅名称：{rest["title"]}；餐厅地址：{rest["address"]}')
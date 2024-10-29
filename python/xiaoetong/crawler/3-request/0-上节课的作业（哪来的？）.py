import requests


url = "http://www.tjwenming.cn/"

res = requests.get(url)
res.encoding = "gb2312"

# 输出相应数据
print(res.text)


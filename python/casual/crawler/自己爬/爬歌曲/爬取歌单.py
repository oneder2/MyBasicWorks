import requests
import re
from bs4 import BeautifulSoup

url = "https://music.163.com/#/song?id=751996"

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"
}

res = requests.get(url, headers = headers)
res.encoding = "utf-8"

print(res)

soup = BeautifulSoup(res.text, "lxml")
print(soup)

# print(res.content)

# ppt_info = re.findall('href="/article/.*?/(.*?).html"', res.text)

# statecode = res.status_code

# print(statecode)

import requests

url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}

session = requests.session()

session.get(url, headers=headers)

print(session.cookies.get_dict())

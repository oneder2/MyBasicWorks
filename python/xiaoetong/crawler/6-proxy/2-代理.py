import requests

url = "https://httpbin.org/get"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

proxies = {
    "http": "http://127.0.0.1:3128",
    "https": "http://127.0.0.1:3128"
}

res = requests.get(url, headers=headers, proxies=proxies)

print(res.text)
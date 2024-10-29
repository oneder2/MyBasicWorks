import requests

qz_url = "https://my.4399.com/forums/index-getMtags?type=game&page=2"
qz_res = requests.get(url = login_url, data = data, cookies=login_res.cookies, headers= headers)
qz_res.encoding = 'utf-8'
print(qz_res.text)

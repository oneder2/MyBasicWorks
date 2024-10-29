import requests

# save the url
url = "https://www.baidu.com/"


# set out a get request
res = requests.get(url)
res.encoding = ""
print(res.text)


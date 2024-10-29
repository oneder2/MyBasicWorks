import requests


myUrl = 'https://cs.lianjia.com/ershoufang/rs/'

myHeaders = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

res = requests.get(url = myUrl, headers = myHeaders)
with open('lianjia.html', 'w', encoding = 'utf-8')as f:
    f.write(res.text)


import requests


url = 'https://www.tangsanbooks.com/book/50825.html'
headers = {
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

res = requests.get(url, headers = headers)
res.encoding = 'utf-8'

with open('noval.html', 'w') as f:
    f.write(res.text)

print(res.text)


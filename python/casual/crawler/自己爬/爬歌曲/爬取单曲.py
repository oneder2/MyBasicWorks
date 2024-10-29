import requests

url = "https://m10.music.126.net/20240605201115/ea99ded68f8339a35cc2b5550c133252/ymusic/0e32/d28b/55ac/5e6711a765e13f225c53f8458b997f10.mp3"

headers = {
    "host": "m10.music.126.net",
    "referer": "https://music.163.com/",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"
}

res = requests.get(url, headers = headers)

statecode = res.status_code

print(statecode)

open("灭敌丧钟.mp3", "wb").write(res.content)
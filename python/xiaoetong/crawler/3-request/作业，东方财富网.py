"""
主网站：https://quote.eastmoney.com/ztb/detail#type=ztgc
数据请求url：https://push2ex.eastmoney.com/getTopicZTPool?cb=callbackdata3582410&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex=0&pagesize=170&sort=fbt%3Aasc&date=20240923&_=1727104278165
"""

import requests
import json
from bs4 import BeautifulSoup

header = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "connection": "keep-alive",
    "cookie": "HAList=ty-105-NVDA-%u82F1%u4F1F%u8FBE; qgqp_b_id=f3e386595fc117684c80e0e99543167d; st_si=96075706458586; st_asi=delete; st_pvi=70368119867066; st_sp=2024-09-06%2022%3A41%3A02; st_inirUrl=https%3A%2F%2Fwww.bing.com%2F; st_sn=15; st_psi=20240923125646721-113200304537-6237578719",  # 省略具体内容
    "dnt": "1",
    "host": "push2ex.eastmoney.com",
    "referer": "https://quote.eastmoney.com/ztb/detail",
    "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

url = "https://push2ex.eastmoney.com/getTopicZTPool?cb=callbackdata4040889&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex=0&pagesize=170&sort=fbt%3Aasc&date=20240923&_=1727110605012"

abd = {
    "ut": "7eea3edcaed734bea9cbfc24409ed989",
    "dpt": "wz.ztzt",
    "Pageindex": 0,
    "pagesize": 20,
    "sort": "fbt:asc",
}

res = requests.get(url, headers=header, data=abd)

resText = res.text

resSlide = resText[20:-2]
resJson = json.loads(resSlide)

for index, line in enumerate(resJson["data"]["pool"]):
    print(f"{index}、编号：{line['c']}, 名称：{line['n']}")
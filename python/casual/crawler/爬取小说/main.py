import requests
from bs4 import BeautifulSoup
wz = {"user-agent": 
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
      "cookie":
      "zhffr=cn.bing.com; ZHID=20F3DEC8D1B77646D1F9AC3E421E50C7; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218f6c87fb6945d-04c31842a86c31-e505625-921600-18f6c87fb6a5cf%22%2C%22%24device_id%22%3A%2218f6c87fb6945d-04c31842a86c31-e505625-921600-18f6c87fb6a5cf%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sajssdk_2015_cross_new_user=1; zh_visitTime=1715512991016; PassportCaptchaId=3e4a6353bcb8b30fb2ac5b7c4002fb42; Hm_lvt_c202865d524849216eea846069349eb9=1715512994; Hm_lpvt_c202865d524849216eea846069349eb9=1715517571; ver=2018; acw_tc=ac11000117155175686356267ec2f3c9d081c4a043068c0240eb5ccc2f6232",
    #   "host":
    #   "read.zongheng.com"
     
     }

url = "https://book.zongheng.com/showchapter/1284449.html"
res = requests.get(url, headers = wz)
soup = BeautifulSoup(res.text, "lxml")
print(soup)
lis = soup.find_all("li", class_ = "col-4")
# print(lis)

# for li in lis:
#     a = li.find("a") # </a>
#     title = a.text # 标题
#     innerUrl = a.get("href") # 链接
#     print(title, innerUrl)
#     innerRes = requests.get(innerUrl, headers = wz) # 获取内容
#     soup = BeautifulSoup(innerRes.text, "lxml")
#     cons = soup.find("div", class_ = "content")
#     outputQueue = '\n'.join(cons.stripped_strings)
#     open(f"小说章节/{title}.txt", "w", encoding="utf-8").write(outputQueue)

    # print(dirLine)


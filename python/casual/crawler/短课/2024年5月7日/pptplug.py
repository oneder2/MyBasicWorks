import requests
import re

# 由于忽略证书，运行时警告
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 伪装
header = {
    "user-agent": 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    }


url = "https://www.ypppt.com/moban/" #网址

# 获取pptID
res = requests.get(url, headers = header, verify = False)# 发出请求并获取返回值
res.encoding = "utf-8" # 更改编码
print(res.text)
ppt_info = re.findall('href="/article/.*?/(.*?).html"', res.text) # 筛选pptID

# 循环遍历这些编号
# newID = []
for id, name in ppt_info:
    # 构造新链接
    url = "https://www.ypppt.com/p/d.php?aid=" + id # 准备链接
    # newID.append()
    res = requests.get(url, headers = header, verify = False) # 请求网址
    # print(res.text)
    # down_url= re.findall("https://down.ypppt.com/uploads/soft/210623/1-210623120S4.zip") 
    down_url = re.findall('href="(.*?)">下载地址1</a>',res.text)[-1]
    if "pan.baidu" in down_url:
        continue
    # print(name, down_url)

    res = requests.get(down_url, headers = header, verify = False)
    open(f'ppt模板/{name}-{id}.{down_url.split(".")[-1]}', "wb").write(res.content)



# mainPageUrl = "https://www.ypppt.com/moban/"

# downlowdPageUrl = "https://www.ypppt.com/article/2021/8257.html"

# jumpingPageUrl = "https://www.ypppt.com/p/d.php?aid=8257"

# downloadPageUrl = "https://down.ypppt.com/uploads/soft/210623/1-210623120S4.zip"

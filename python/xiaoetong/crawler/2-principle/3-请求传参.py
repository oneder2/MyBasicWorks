'''
需求：
通过输入不同的关键字，进入不同的贴吧

python吧：
https://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search
java吧：
https://tieba.baidu.com/f?ie=utf-8&kw=java&fr=search

url编码：自动编码非英文输入

'''

# # 第一种方式
# # 直接根据字符串插值内容改变url
# import requests

# tiebaInput = input("请输入想要进入的贴吧名：")
# url = f"https://tieba.baidu.com/f?ie=utf-8&kw={tiebaInput}&fr=search"

# res = requests.get(url)
# print(res.text)


# 第二种方式
# 额外定义一个变量字典
import requests

tiebaInput = input("请输入想要进入的贴吧名：")
url = "https://tieba.baidu.com/f"

p = {
    # 参数名: 参数值
    "ie": "utf-8",
    "kw": tiebaInput,
    "fr": "search"
}

res = requests.get(url, params=p)
print(res.text)

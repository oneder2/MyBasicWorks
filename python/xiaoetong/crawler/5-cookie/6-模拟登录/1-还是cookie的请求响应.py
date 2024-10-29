"""
背景：非常悲伤，4399游戏吧要么是down了，要么是我这里访问不了

需求：
进入4399网站，获取群组数据
1、登录
2、找到数据所在url
    https://my.4399.com/forums/index-getMtags?type=game&page=2
    请求方式：get

"""

"""
# 初级爬虫，手动登录，爬取信息
import requests

url = 'https://my.4399.com/forums/index-getMtags?type= game&page=2'

headers = {
    # 当在网页中登陆完成后，对方服务器返回
    # 缺点：时效性
    'Cookie':"假装有一个cookie"
}

res = requests.grt(url, headers = headers)
res.encoding = 'utf-8'
print(res.text)
"""

"""
可以自动拿cookie吗？像上节课一样？
--不行，在没有登陆的情况下，不可以在所谓“主页面”获取cookie
因此，获取cookie的前提就变为了：通过爬虫，实现模拟登录

网站的登录窗口逻辑：
通过窗口记录用户端输入的登录信息，并基于信息向服务端发出一个请求
tips：部分敏感信息，包括但不限于密码，身份证号，可能会（情况不一定）被加密为密文数据。且部分网站是静态密钥加密，部分是动态密钥加密
"""

import requests

# 第一步：模拟登录
login_url = "https://ptlogin.4399.com/ptlogin/login.do?v=1" 

data = {
    "loginFrom": "uframe",
    "postLoginHandler": "refreshParent",
    "layoutSelfAdapting": "true",
    "externalLogin": "qq",
    "displayMode": "undefined",
    "layout": "vertical",
    "bizId": "",
    "appId": "my",
    "gameId": "",
    "css": "//s1.img4399.com/base/css/ptlogin.css?1b35e55",
    "redirectUrl": "",
    "sessionId": "",
    "mainDivId": "popup_login_div",
    "includeFcmInfo": "false",
    "level": "0",
    "regLevel": "4",
    "userNameLabel": "4399用户名",
    "userNameTip": "请输入4399用户名",
    "welcomeTip": "欢迎回到4399",
    "sec": "1",
    "password": "73EP8qp8!mEBV2v",
    "username": "3431007712"
}


headers = {
    "host": "my.4399.com",
    "referer":"https://my.4399.com/forums/mtags",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

"""
验证登陆成功的方式：
发出一次需要cookie的请求，如果能成功接收数据就成功，反之失败
"""
login_res = requests.post(login_url, data = data)

print(login_res.status_code)

qz_url = "https://my.4399.com/forums/index-getMtags?type=game&page=2"
qz_res = requests.get(url = qz_url, cookies=login_res.cookies)
qz_res.encoding = 'utf-8'
print(qz_res.text)


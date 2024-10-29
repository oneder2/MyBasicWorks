import requests
from moviepy.editor import *

# 视频链接
url = "https://www.bilibili.com/video/BV1Tm421W7Q3/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=49cb783c52db491cfc0b0d2d18f156ac"

# 伪装
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
cookie = "buvid3=1C12A564-2700-FE18-AF78-1C834B42530176463infoc; b_nut=1699450576; i-wanna-go-back=-1; b_ut=7; _uuid=BCC9FAF8-9B42-F7DD-BC53-EC243D97C311077818infoc; enable_web_push=DISABLE; header_theme_version=CLOSE; buvid_fp=41f6dc8ef469d9acf2ee155990da5873; buvid4=332CE26F-4DDA-3DCF-B789-802C4A04EC9A77503-023110821-A%2BlFilB%2B3P6gLw4uVl7O1Q%3D%3D; home_feed_column=4; browser_resolution=958-918; CURRENT_FNVAL=4048; rpdid=|(J~kumkmkY)0J'uYmmRl|Yuk; SESSDATA=1052b14b%2C1730375933%2Ce585e%2A51CjCzTu1DHX4tFBV0BJ-B1R2…3f8119b3adac454; bp_video_offset_328567230=924370034077204568; fingerprint=41f6dc8ef469d9acf2ee155990da5873; buvid_fp_plain=undefined; PVID=5; CURRENT_QUALITY=80; is-2022-channel=1; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; bp_t_offset_328567230=928029088515358745; sid=4v6p3fcl; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTUwODMxNDIsImlhdCI6MTcxNDgyMzg4MiwicGx0IjotMX0.e-L_XCn-wtQytSvauYrD1OK0wNaqCKYhUgGyKRaSeU8; bili_ticket_expires=1715083082; b_lsid=62D31CDD_18F48CE5F4F"

headers = {"user-agent": user_agent.encode("utf-8"), 
           "cookie": cookie.encode("utf-8")
        #    "referer":"https://www.bilibili.com/"
           }

#请求网址
res = requests.get(url, headers = headers)

responseCode = res.status_code # 状态码
responseConstent = res.content

print(responseCode) # 返回爬取状态
print(responseConstent)

#存储信息
open("福乐.mp4", "wb").write(res.content)

"""
# 音频链接
url = "https://www.bilibili.com/video/BV1Tm421W7Q3/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=49cb783c52db491cfc0b0d2d18f156ac"

# 伪装
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0", 
           "cookie":"buvid3=1C12A564-2700-FE18-AF78-1C834B42530176463infoc; b_nut=1699450576; i-wanna-go-back=-1; b_ut=7; _uuid=BCC9FAF8-9B42-F7DD-BC53-EC243D97C311077818infoc; enable_web_push=DISABLE; header_theme_version=CLOSE; buvid_fp=41f6dc8ef469d9acf2ee155990da5873; buvid4=332CE26F-4DDA-3DCF-B789-802C4A04EC9A77503-023110821-A%2BlFilB%2B3P6gLw4uVl7O1Q%3D%3D; home_feed_column=5; browser_resolution=1920-919; CURRENT_FNVAL=4048; rpdid=|(J~kumkmkY)0J'uYmmRl|Yuk; SESSDATA=1052b14b%2C1730375933%2Ce585e%2A51CjCzTu1DHX4tFBV0BJ-B1R…34077204568; fingerprint=41f6dc8ef469d9acf2ee155990da5873; buvid_fp_plain=undefined; PVID=4; CURRENT_QUALITY=80; is-2022-channel=1; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; bp_t_offset_328567230=928009297286135849; sid=4v6p3fcl; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTUwODMxNDIsImlhdCI6MTcxNDgyMzg4MiwicGx0IjotMX0.e-L_XCn-wtQytSvauYrD1OK0wNaqCKYhUgGyKRaSeU8; bili_ticket_expires=1715083082; b_lsid=9EC82667_18F48710221; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com",
            "referer":"https://www.bilibili.com/?spm_id_from=333.1296.0.0"}

#请求网址
res = requests.get(url, headers = headers)

# responseCode = res.status_code # 响应码

# print(responseCode) # 返回爬取状态

#存储信息
open("民科.mp3", "wb").write(res.content)


video = VideoFileClip("民科.mp4")
audio = AudioFileClip("民科.mp3")

altimate = video.set_audio(audio)

altimate.write_viedofile("完整视频.mp4")

"""
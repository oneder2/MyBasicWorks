import requests # 网站请求方法
from wordcloud import WordCloud
import matplotlib.pyplot
import re


def getComments():
    # 初始化heading信息
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
    cookie = "ttwid=1%7CaNx0B_BJnpoHhALWztfNvXbO9hw5lVYBHMm8dczLdRo%7C1714998376%7C0d4c3b19e0ec465ff6016d847cb0fb4825f181e04033a04cde6871bfd161a909; douyin.com; device_web_cpu_core=8; device_web_memory_size=-1; architecture=amd64; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; dy_swidth=1920; dy_sheight=1080; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2…nt_web_domain=2; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; s_v_web_id=verify_lvuxscif_96d8fdda_4a11_cdda_0ccc_ac8ff4698d8d; download_guide=%222%2F20240506%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSVRjc3BNdWtuN0RhMldLQXNZVTErS2xMTld1dXkwUkR4VXcxNW9nYlZqbHFVaHNsQThLd0FCTWFlNGxSL0xpNGNLbmViNndCT2FETGxlT0ZuWktWTTg9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D"
    referer = "https://www.douyin.com/discover?enter=guide&modal_id=7364042458881166633"
    host = "www.douyin.com"

    # 构造heading
    header = {"user-agent": 
            user_agent.encode("utf-8"),
            "cookie":
            cookie.encode("utf-8"),
            "referer":
            referer.encode("utf-8"),
            "host":
            host.encode("utf-8")
            }

    # 获得评论信息
    url = "https://www.douyin.com/aweme/v1/web/emoji/list?device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Firefox&browser_version=125.0&browser_online=true&engine_name=Gecko&engine_version=125.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=&platform=PC&webid=7365861862338233856&msToken=woR6w1hDAegqJ7YQSTOBQA6oIdQxQ7HqWzfUkIdAwH6QgUZR4BlPOK0QKOxIejGYCKqxYY88e8UxzN_H2nqYP-a-uotz71h72P-uGN_n-CTizVCvx5xdOnCuzj0GFqY=&a_bogus=QJ80BQwgDifN6d6g5WOLfY3q64H3YZJO0trE-E2f2x3SOg39HMTV9exo96svR08jLG/lIebjy4hbYrcdrQAn0qwfHSXi/2CZmyv0SMZgso0j53iruyRkrzDF-vGWS-BBRk-lrOX0w7lHFbLhAxAn-wPvPjoja3LkFk6FOoB/"
    res = requests.get(url, headers = header)

    # 这是啥
    cursor = 0
    # 80评论一单元
    alltexts = ""

    recCode = res.status_code
    print(recCode)
    print(res.text)

    # 重复读取评论
    while True:
        JSON = res.json()
        comments = JSON["comments"]
        for line in comments():
            alltexts += line["text"]
            print(alltexts)
        if JSON["has_more"] == 0:
            break
        cursor = JSON["cursor"]

def stringCloudize():
    # 获取词库
    text = open("alltexts.txt", "r", encodeing = "utf-8").read
    # 去除符号
    text = re.sub(r"\[.*?\]", "", text)
    # 用text生成词云
    wordcloud = WordCloud(width = 1920, height = 1080, background_color = "white").generate(text)
    matplotlib.pyplot.imshow(wordcloud)
    matplotlib.pyplot.show()

def main():
    getComments()


main()
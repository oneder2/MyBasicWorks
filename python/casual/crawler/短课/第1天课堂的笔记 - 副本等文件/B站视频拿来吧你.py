import requests   # 导入请求模块
# Python剪辑工作！ 一定有一个什么模块可以干这个事情！
# 安装 pip install moviepy
from moviepy.editor import *   # 从moviepy的editor里面去导入所有的功能！

def getvedio(url):
    # 通过伪装浏览器 伪装引荐页 请求B站的后台 得到B站的视频！
    # url = 'https://xy118x182x249x46xy.mcdn.bilivideo.cn:4483/upgcxcode/42/50/1511735042/1511735042-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1714397866&gen=playurlv2&os=mcdn&oi=2936042585&trid=0000879a53a1d49e4a229d309ef822fd2f92u&mid=262711481&platform=pc&upsig=7901ad3af3752cb2b32f4d521af7b93d&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=50002723&bvc=vod&nettype=0&orderid=0,3&buvid=0C02950F-BBC6-E2A0-4626-DCEB3565AB8F37550infoc&build=0&f=u_0_0&agrr=0&bw=164689&logo=A0020000'      # 准备一个网址
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0', 'referer': 'https://www.bilibili.com/video/BV1ux4y1h746/?spm_id_from=333.999.0.0&vd_source=d9f8ce26057997c0a9d467549da09941'}
    res = requests.get(url, headers=headers)  # 请求网址 得到响应
    open('xxx.mp4', 'wb').write(res.content)  # 把得到内容写入文件

def getradio(url):
    # B站的视频  视频和音频是分开的！
    # url = 'https://xy118x182x249x46xy.mcdn.bilivideo.cn:4483/upgcxcode/42/50/1511735042/1511735042-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1714398227&gen=playurlv2&os=mcdn&oi=2936042585&trid=000033d101d6848c41b2ad72c6dd644e9ce2u&mid=262711481&platform=pc&upsig=222a65ab9dd31c7e0323b7735b0e9990&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=50002723&bvc=vod&nettype=0&orderid=0,3&buvid=0C02950F-BBC6-E2A0-4626-DCEB3565AB8F37550infoc&build=0&f=u_0_0&agrr=0&bw=21814&logo=A0020000'
    headers = {'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0', 
            'referer': 
            'https://www.bilibili.com/video/BV1ux4y1h746/?spm_id_from=333.999.0.0&vd_source=d9f8ce26057997c0a9d467549da09941'
            }
    res = requests.get(url, headers=headers)  # 请求网址 得到响应
    open('xxx.mp3', 'wb').write(res.content)  # 把得到内容写入文件

def mixVideoRadio(video, radio):
    # 1.加载素材
    # 视频数据 = VideoFileClip('xxx.mp4')
    # 音频数据 = AudioFileClip('xxx.mp3')

    # 2.剪辑工作
    finnal = video.set_audio(radio)

    # # 3.导出文件
    finnal.write_videofile('完整视频.mp4')

    # 1.加载素材
    video = VideoFileClip('完整视频.mp4')
    # 拆分
    finnal = video.subclip(20, 30)
    # 导出
    finnal.write_videofile('10s.mp4')

def main():
    videoUrl = 'https://xy118x182x249x46xy.mcdn.bilivideo.cn:4483/upgcxcode/42/50/1511735042/1511735042-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1714397866&gen=playurlv2&os=mcdn&oi=2936042585&trid=0000879a53a1d49e4a229d309ef822fd2f92u&mid=262711481&platform=pc&upsig=7901ad3af3752cb2b32f4d521af7b93d&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=50002723&bvc=vod&nettype=0&orderid=0,3&buvid=0C02950F-BBC6-E2A0-4626-DCEB3565AB8F37550infoc&build=0&f=u_0_0&agrr=0&bw=164689&logo=A0020000'      # 准备一个网址
    radioUrl = 'https://xy118x182x249x46xy.mcdn.bilivideo.cn:4483/upgcxcode/42/50/1511735042/1511735042-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1714398227&gen=playurlv2&os=mcdn&oi=2936042585&trid=000033d101d6848c41b2ad72c6dd644e9ce2u&mid=262711481&platform=pc&upsig=222a65ab9dd31c7e0323b7735b0e9990&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=50002723&bvc=vod&nettype=0&orderid=0,3&buvid=0C02950F-BBC6-E2A0-4626-DCEB3565AB8F37550infoc&build=0&f=u_0_0&agrr=0&bw=21814&logo=A0020000'
    getvedio(videoUrl)
    getradio(radioUrl)
    videodata = VideoFileClip('xxx.mp4')
    radiodata = AudioFileClip('xxx.mp3')
    mixVideoRadio(videodata, radiodata)

main()


# # 网站！
# # 1 拿到这个链接 歌曲名修改成你想听的歌曲！ 复制链接到网站上打开！
# 'https://c.musicapp.migu.cn/v1.0/content/search_all.do?text=本草纲目&pageNo=1&pageSize=20&isCopyright=1&sort=1&searchSwitch=%7B%22song%22%3A1%2C%22album%22%3A0%2C%22singer%22%3A0%2C%22tagSong%22%3A1%2C%22mvSong%22%3A0%2C%22bestShow%22%3A1%7D'
# # "contentId": "600902000006889198"  # 内容ID
# # "copyrightId": "60054701964"       # 版权ID
# # "albumsId" : "7952"                # 专辑ID

# # 2. 把前面得到的三个id 代入这个链接！
# import requests
# url = 'https://c.musicapp.migu.cn/MIGUM3.0/strategy/listen-url/v2.3?copyrightId=60054701964&contentId=600902000006889198&resourceType=2&albumId=7952&netType=01&toneFlag=PQ'
# headers = {'channel': '0140210'}
# res = requests.get(url, headers=headers)
# print(res.text)



# 爬虫 数据分析 网站！
# 兴趣爱好 玩一玩  外包接单  就业转行！
# 1.Python基础 数据库 linux 爬虫！ 网站 app 小程序 应用软件！ 逆向！
# 2.数据分析  外包 和就业
# 3.网站开发！ 后台！ 前端裁员！ 开发费用！ 维护费！
# 自动化办公  自动化运维  自动化测试
# 兴趣爱好！ 外包 赚点钱  转行  自己开心的事情
# 谁知道！ 机会！ 趋势！
# 昨天研究生！ 8980！

# 20多个老师！
# 直播 录播 一对一！
# 作业项目！
# 外包 简直 转行 就业！
# 老师带你！

# 学！
# 20-30个徒弟！
# 1.最后的12个名额！
# 2.找让你来听课的那个小班老师 预定200块钱！-2000学费！ 8980-2000 = 6980 -200 =6780
# 3.淘宝店铺付学费 12期免息的权限 500+

# 4.上课时间：1 3 5 或者 2 4 6 晚上19点30 - 21:30
# 5.6-8个月！ 2年的学习权限！
# 6.随便重修！ 项目经验更丰富！ 带你们去考一个CEAC证书！
# 7.C语言 C++免费教！ 6666666666666666666666666666666666666666666

# 没钱：
# 开一家饭店： 启动资金
# 加盟奶茶店：多少钱
# 小卖部要多少钱！
# 6000*4 24000
# 线下学： 学费25000 + 少了收入30000 + 支出12000   成本！
# 6980 预定 分期进班  500+
# 就算 在别的地方学会了 自学成才了  超强！  全程更近简历 面试 就业 ！
# 做了选择失去很多东西！ 退缩犹豫留下很多遗憾！
# 失去的东西可以再拿回来！ 留下的遗憾就不一定了！

# 没时间
# 直播 录播 2年的学习权限！
# 没有时间！ 没有时间！ 没有时间！
# 只有效率！
# 用时间来堆砌的工作  按劳分配！          80%
# 用效率来指导的任务  按生产要素分配！     20%

# 学不会！
# 年纪大！ -> 41岁的同学写代码！
# 各种！
# 抢票  赚了一波！
# 抢空投  一直在做！ 开公司了  深圳！
# 今天不来！你也不会后悔！ 大学生！ 没钱！  妈！ 20分钟！ 8980！ 表哥 杭州 云计算！ 很高！
# 高兴坏了！
# 祝大家： 永远都是追梦人！ 牛逼 越来越牛逼！
# 报名的同学： 赶紧进班  今天就进班。 (专业)职业  年龄  城市  目标 编辑好私聊给我！
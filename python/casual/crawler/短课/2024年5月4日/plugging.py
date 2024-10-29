# 导入请求模块
import requests

# 实测B站这四行没法爬，会被403（悲）
# 感谢老师让我知道vscode还可以设背景（）
# 您设的背景很可爱（什

# 视频链接
uil = "https://v2.kwaicdn.com/ksc2/yDj5QHusfDtvF2cS9j5CTGOuHJV08toJrdNMgnQeBs4JSo9oostY3jiHeWY6Q8oKtJoZEs5WxMLQanuzJrMcJDFQrggNzmEbDhcwIGy_empxVkYvrRXbRfqcrSOyJHqxO6rRPQzM5uVJNUL3_H7AkH7aoM6fb2omSmpB2y-AQ8quVmSVK3-EmBwZDQwHS9h5.mp4?pkey=AAU7OaO1qudOQ1AqhWQ-6LsRPLN672N6r1biDJVGIw1LKMO9wPAVeZBAGUOZCsDHukeNniNQW4VB-3oVrPLAxcwZBnvOyAuUynbyj-vMAQrf0qdtIQJTmlqPPry3Unt4r5g&tag=1-1714825941-unknown-0-wjafispiit-ee14a275ac04d2f6&clientCacheKey=3xi2k5yqpyci8yi_b.mp4&di=JAiCBzDAChBRP8OXsZdYrw==&bp=10004&tt=b&ss=vp"

# 爬取视频
res = requests.get(uil)

responseCode = res.status_code # 响应码

print(responseCode) # 返回爬取状态

#存储信息
open("哈尔滨.mp4", "wb").write(res.content)

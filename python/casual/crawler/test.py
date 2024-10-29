import requests

referer = "https://www.bilibili.com/video/BV1ux4y1h746/?spm_id_from=333.337.search-card.all.click"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"

headers = {
    "referer":
    referer.encode("utf-8"),
    "User-Agent":
	user_agent.encode("utf-8")
}

url = "https://upos-sz-mirror08c.bilivideo.com/upgcxcode/42/50/1511735042/1511735042-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1718038857&gen=playurlv2&os=08cbv&oi=0&trid=7365ce18b890481d997eb48797771528u&mid=0&platform=pc&og=hw&upsig=ab6b7f569fb0c6de43323be32b746095&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=DD33A429-624C-8789-414C-A58CA9B89FC253007infoc&build=0&f=u_0_0&agrr=0&bw=6659&logo=80000000"

res = requests.get(url, headers=headers)

print(res.status_code)

open("p1.mp3", "wb").write(res.content)
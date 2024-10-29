import requests

# cookie = "buvid3=1C12A564-2700-FE18-AF78-1C834B42530176463infoc; b_nut=1699450576; i-wanna-go-back=-1; b_ut=7; _uuid=BCC9FAF8-9B42-F7DD-BC53-EC243D97C311077818infoc; enable_web_push=DISABLE; header_theme_version=CLOSE; buvid_fp=cf1d32942a71112eceebe1a4f919412e; buvid4=332CE26F-4DDA-3DCF-B789-802C4A04EC9A77503-023110821-A%2BlFilB%2B3P6gLw4uVl7O1Q%3D%3D; home_feed_column=5; browser_resolution=1920-919; CURRENT_FNVAL=4048; rpdid=|(J~kumkmkY)0J'uYmmRl|Yuk; SESSDATA=ebc81cc9%2C1733362200%2C072b5%2A61CjCQrVi2Rz9VojiYYkdBs8…3adac454; fingerprint=cf1d32942a71112eceebe1a4f919412e; buvid_fp_plain=undefined; PVID=2; CURRENT_QUALITY=16; is-2022-channel=1; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; bp_t_offset_328567230=941385105383882777; sid=6npuwaix; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTgxOTc2MjUsImlhdCI6MTcxNzkzODM2NSwicGx0IjotMX0.zN4O_5a5QgZV-0at_pdlsWs_c_gwK9HgkUAN5jRzdnw; bili_ticket_expires=1718197565; b_lsid=11046102107_190022B79FB; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com"
# host = "upos-sz-mirrorcos.bilivideo.com"
# referer = "https://www.bilibili.com/video/BV1cJ4m1h7j3/?spm_id_from=333.999.0.0"
referer = "https://www.bilibili.com/video/BV1ux4y1h746/?spm_id_from=333.337.search-card.all.click"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"

headers = {
    # "cookie":
	# cookie.encode("utf-8"),
    # "host":
    # host.encode("utf-8"),
    "referer":
    referer.encode("utf-8"),
    "User-Agent":
	user_agent.encode("utf-8")
}


for i in range():
    vedio_url = "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/24/1223102418/1223102418-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1718036672&gen=playurlv2&os=cosbv&oi=0&trid=9fda67b7540548d0af4f5a2a48803428u&mid=328567230&platform=pc&og=cos&upsig=b3994e0b2b924475e6e07009a1fc35d9&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=1C12A564-2700-FE18-AF78-1C834B42530176463infoc&build=0&f=u_0_0&agrr=0&bw=15152&logo=80000000"
    radio_url = "https://upos-sz-mirrorali.bilivideo.com/upgcxcode/18/24/1223102418/1223102418-1-30216.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1718036672&gen=playurlv2&os=alibv&oi=0&trid=9fda67b7540548d0af4f5a2a48803428u&mid=328567230&platform=pc&og=cos&upsig=84a1cdb7d09a072e8ffd1c9dacd25f89&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=1C12A564-2700-FE18-AF78-1C834B42530176463infoc&build=0&f=u_0_0&agrr=0&bw=5515&logo=80000000"

    vedio_res = requests.get(vedio_url, headers=headers)
    radio_res = requests.get(radio_url, headers=headers)

    print(vedio_res.status_code, radio_res.status_code)

    open("p1.mp4", "wb").write(vedio_res.content)
    open("p1.mp3", "wb").write(radio_res.content)


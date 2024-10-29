"""
主网站：https://quote.eastmoney.com/ztb/detail#type=ztgc
数据请求url：https://push2ex.eastmoney.com/getTopicZTPool?cb=callbackdata3582410&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex=0&pagesize=170&sort=fbt%3Aasc&date=20240923&_=1727104278165
"""

import requests
import json
from bs4 import BeautifulSoup

# header = {
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br, zstd",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "connection": "keep-alive",
#     "cookie": "...",  # 省略具体内容
#     "dnt": "1",
#     "host": "push2ex.eastmoney.com",
#     "referer": "https://quote.eastmoney.com/ztb/detail",
#     "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "Windows",
#     "sec-fetch-dest": "script",
#     "sec-fetch-mode": "no-cors",
#     "sec-fetch-site": "same-site",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
# }

# url = "https://push2ex.eastmoney.com/getTopicZTPool?cb=callbackdata9575130&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex=0&pagesize=20&sort=fbt%3Aasc&date=20240923&_=1727105039744"

# abd = {
#     "ut": "7eea3edcaed734bea9cbfc24409ed989",
#     "dpt": "wz.ztzt",
#     "Pageindex": 0,
#     "pagesize": 20,
#     "sort": "fbt:asc",
#     "date": 20240923,
#     "_": 1727105719275
# }

# res = requests.get(url, headers=header, data=abd)

# resText = res.text()

# 因为网站一定时间内的访问次数限制，暂且先将返回结果保存处理，已知以上内容可以爬取到res信息

resText = 'callbackdata9575130({"rc":0,"rt":110,"svr":177618277,"lt":1,"full":0,"data":{"tc":54,"qdate":20240923,"pool":[{"c":"000004","m":0,"n":"国华网安","p":16060,"zdp":10.0,"amount":21155838,"ltsz":2028186773.58,"tshare":2126027328.9199999,"hs":1.0430911779403687,"lbc":4,"fbt":92500,"lbt":92500,"fund":192332954,"zbc":0,"hybk":"软件开发","zttj":{"days":4,"ct":4}},{"c":"002583","m":0,"n":"海能达","p":4760,"zdp":9.930715560913086,"amount":71514649,"ltsz":6103824393.24,"tshare":8654700467.84,"hs":1.171636700630188,"lbc":3,"fbt":92500,"lbt":92500,"fund":508275246,"zbc":0,"hybk":"通信设备","zttj":{"days":3,"ct":3}},{"c":"002693","m":0,"n":"双成药业","p":10150,"zdp":9.967496871948243,"amount":45942960,"ltsz":4175528274.4,"tshare":4209100901.6000006,"hs":1.1002910137176514,"lbc":7,"fbt":92500,"lbt":92500,"fund":597981160,"zbc":0,"hybk":"生物制品","zttj":{"days":7,"ct":7}},{"c":"600130","m":1,"n":"波导股份","p":4060,"zdp":10.027100563049317,"amount":45900736,"ltsz":3044999999.9999997,"tshare":3044999999.9999997,"hs":1.507413387298584,"lbc":2,"fbt":92501,"lbt":92501,"fund":122333484,"zbc":0,"hybk":"消费电子","zttj":{"days":2,"ct":2}},{"c":"600198","m":1,"n":"大 唐电信","p":8500,"zdp":9.961190223693848,"amount":75927415,"ltsz":7483865247.5,"tshare":11080630056.0,"hs":1.0145481824874879,"lbc":5,"fbt":92501,"lbt":92501,"fund":462282385,"zbc":0,"hybk":"通信设备","zttj":{"days":5,"ct":5}},{"c":"600225","m":1,"n":"卓朗科技","p":1970,"zdp":10.055866241455079,"amount":109021914,"ltsz":6715386067.55,"tshare":6720446904.96,"hs":1.6262434720993043,"lbc":3,"fbt":92501,"lbt":93155,"fund":25876344,"zbc":2,"hybk":"软件开发","zttj":{"days":3,"ct":3}},{"c":"603316","m":1,"n":"诚邦股份","p":4610,"zdp":10.023866653442383,"amount":96765687,"ltsz":1218257040.0,"tshare":1218257040.0,"hs":7.951730251312256,"lbc":2,"fbt":92501,"lbt":93555,"fund":23270542,"zbc":1,"hybk":"工程 建设","zttj":{"days":2,"ct":2}},{"c":"605086","m":1,"n":"龙高股份","p":19230,"zdp":10.011442184448243,"amount":79807810,"ltsz":3446016000.0,"tshare":3446016000.0,"hs":2.328403949737549,"lbc":1,"fbt":92501,"lbt":93131,"fund":29368825,"zbc":1,"hybk":"采掘行业","zttj":{"days":4,"ct":2}},{"c":"600721","m":1,"n":"百花医药","p":6260,"zdp":10.017574310302735,"amount":123595079,"ltsz":2391277870.2,"tshare":2391277832.64,"hs":5.174017906188965,"lbc":1,"fbt":93009,"lbt":93009,"fund":53712678,"zbc":0,"hybk":"医疗服务","zttj":{"days":1,"ct":1}},{"c":"600776","m":1,"n":"东方通信","p":10660,"zdp":10.010319709777832,"amount":538470144,"ltsz":10190960682.24,"tshare":13388960682.24,"hs":5.325674533843994,"lbc":2,"fbt":93026,"lbt":94556,"fund":61507933,"zbc":4,"hybk":"通信设备","zttj":{"days":2,"ct":2}},{"c":"000158","m":0,"n":"常山北明","p":11830,"zdp":10.04651165008545,"amount":1778664368,"ltsz":18783896522.3,"tshare":18911635797.6,"hs":9.616547584533692,"lbc":2,"fbt":93109,"lbt":93227,"fund":361984324,"zbc":1,"hybk":"综合行业","zttj":{"days":8,"ct":5}},{"c":"600619","m":1,"n":"海立股份","p":7890,"zdp":10.041841506958008,"amount":1282036720,"ltsz":6226589156.219999,"tshare":8468687316.0,"hs":23.435131072998048,"lbc":4,"fbt":93147,"lbt":144229,"fund":28481322,"zbc":0,"hybk":"家电行业","zttj":{"days":8,"ct":5}},{"c":"001313","m":0,"n":"粤海饲料","p":6890,"zdp":10.063898086547852,"amount":93307028,"ltsz":1502653886.8899999,"tshare":4823000000.0,"hs":6.30348539352417,"lbc":1,"fbt":93157,"lbt":141751,"fund":8785439,"zbc":3,"hybk":"农牧饲渔","zttj":{"days":1,"ct":1}},{"c":"600550","m":1,"n":"保变电气","p":12230,"zdp":9.982014656066895,"amount":1901016768,"ltsz":22521893310.4,"tshare":22521893310.4,"hs":8.573221206665039,"lbc":3,"fbt":93242,"lbt":93843,"fund":241625125,"zbc":3,"hybk":"电网设备","zttj":{"days":14,"ct":10}},{"c":"002686","m":0,"n":"亿利达","p":5240,"zdp":10.084033966064454,"amount":195632508,"ltsz":2739118865.92,"tshare":2967093072.6400005,"hs":7.342935562133789,"lbc":1,"fbt":93309,"lbt":93533,"fund":54000248,"zbc":1,"hybk":"通用设备","zttj":{"days":4,"ct":3}},{"c":"002547","m":0,"n":"春兴精工","p":2950,"zdp":10.074626922607422,"amount":99633276,"ltsz":3256039389.7000005,"tshare":3327768645.6000006,"hs":3.123004198074341,"lbc":1,"fbt":93324,"lbt":93324,"fund":49155808,"zbc":0,"hybk":"汽车零部","zttj":{"days":1,"ct":1}},{"c":"002722","m":0,"n":"物产金轮","p":13240,"zdp":9.966776847839356,"amount":313916448,"ltsz":2323497530.0,"tshare":2735073932.44,"hs":13.72982406616211,"lbc":1,"fbt":93433,"lbt":144733,"fund":2262716,"zbc":9,"hybk":"纺织服装","zttj":{"days":1,"ct":1}},{"c":"002339","m":0,"n":"积成电子","p":6000,"zdp":10.091742515563965,"amount":158039534,"ltsz":2872761624.0,"tshare":3024553632.0,"hs":5.557398796081543,"lbc":1,"fbt":93612,"lbt":93612,"fund":43433760,"zbc":0,"hybk":"电网设备","zttj":{"days":1,"ct":1}},{"c":"300149","m":0,"n":"睿智医药","p":5140,"zdp":20.09345817565918,"amount":211754026,"ltsz":2564325527.3799998,"tshare":2568853245.44,"hs":8.521735191345215,"lbc":1,"fbt":93809,"lbt":93809,"fund":55700144,"zbc":0,"hybk":"医疗服务","zttj":{"days":1,"ct":1}},{"c":"600696","m":1,"n":"岩石股份","p":7060,"zdp":9.968847274780274,"amount":198863354,"ltsz":2361354182.8599998,"tshare":2361354133.44,"hs":8.620753288269043,"lbc":3,"fbt":93932,"lbt":135756,"fund":4106802,"zbc":30,"hybk":" 酿酒行业","zttj":{"days":3,"ct":3}}]}})'

resSlide = resText[20:-1]
resJson = json.loads(resSlide)

for line in resJson["data"]["pool"]:
    # print(line["n"])
    print(f"编号：{line['c']}, 名称：{line['n']}")
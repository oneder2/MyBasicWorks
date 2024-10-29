import requests
from lxml import etree


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'cookie': 'lianjia_uuid=ad5b7188-5e15-43fe-92db-317d5f19e32d; _ga=GA1.2.702412531.1728938716; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221928cc7084112e9-09dc3dffc07712-1e462c6f-2073600-1928cc70842a65%22%2C%22%24device_id%22%3A%221928cc7084112e9-09dc3dffc07712-1e462c6f-2073600-1928cc70842a65%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; select_city=430100; lianjia_ssid=4c967dfc-958f-41c0-b1d9-61f999911c29; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1728938706,1729108434; HMACCOUNT=1B06E78F6D804E45; crosSdkDT2019DeviceId=-uwtuig-wngoaf-txqkjjo54g7qcqo-uo2sorek9; ftkrc_=3af4127c-8ad8-4520-996a-d4b7f191e762; lfrc_=2b015489-e1ec-41e3-bae8-11d440eeff12; _jzqa=1.875923375911874700.1728938706.1728938706.1729108487.2; _jzqc=1; _jzqx=1.1728938706.1729108487.2.jzqsr=hip%2Elianjia%2Ecom|jzqct=/.jzqsr=clogin%2Elianjia%2Ecom|jzqct=/; _jzqckmp=1; _gid=GA1.2.2098899504.1729108498; Hm_lvt_efa595b768cc9dc7d7f9823368e795f1=1729109792; login_ucid=2000000449819956; lianjia_token=2.00110c2c814646f45900a105b01049c225; lianjia_token_secure=2.00110c2c814646f45900a105b01049c225; security_ticket=g8+uJsYQd3rJsazps9dNOiUoBvZ+leUnlFsf6sDihdLz01Vms3Xm1vY5YxgXl2ZmDxcGVeISqq9+ER7n0vMzBX6WzSFUlzASrr48a33BNRTnWOYMLVpBRJ9HvEi5C0rb3H0Enf9TjuN/MJmfAGkuvaL9ZhbXqaZ+SqlSdeJYHII=; hip=LGvnJu0j8DO1SL3fSVzwFCP7s_hByCqTaZaHRZYrKypzc6FzYFfQWDWTCppA09u3jDD1riC9slidhvCyk9n11pVqG8RvaK9dyIOyEd2cSj8RtpvngPll_d1qQfwKHRnMoCpMJokU73dDJ00_x389kC1KUu07pyN9G9Tzlfni9S1FFfSUYaSQoW-1_w%3D%3D; Hm_lpvt_efa595b768cc9dc7d7f9823368e795f1=1729109956; _ga_4JBJY7Y7MX=GS1.2.1729108497.2.1.1729109986.0.0.0; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1729110256; _jzqb=1.13.10.1729108487.1'
}

for page in range(1, 6):
    mainUrl = f'https://cs.lianjia.com/ershoufang/pg{page}/'
    rawRes = requests.get(mainUrl, headers = headers)
    rawTree = etree.HTML(rawRes.text)
    resList = rawTree.xpath('//ul[@class="sellListContent"]/li')
    for res in resList:
        title = res.xpath('.//div[@class="title"]/a/text()')
        price = res.xpath('.//div[@class="totalPrice totalPrice2"]//text()')
        region = res.xpath('.//div[@class="flood"]/div[@class="positionInfo"]/a/text()')
        unitPrice = res.xpath('.//div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')
        houseInfo = res.xpath('.//div[@class="address"]/div[@class="houseInfo"]//text()')
        price = ''.join(price)
        region = ''.join(region)
        print(title, price, region, unitPrice, houseInfo)
        break






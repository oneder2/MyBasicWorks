import requests
from lxml import etree


cityPageUrl = 'https://www.lianjia.com/city/'
headers = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'cookie': 'lianjia_uuid=ad5b7188-5e15-43fe-92db-317d5f19e32d; _ga=GA1.2.702412531.1728938716; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221928cc7084112e9-09dc3dffc07712-1e462c6f-2073600-1928cc70842a65%22%2C%22%24device_id%22%3A%221928cc7084112e9-09dc3dffc07712-1e462c6f-2073600-1928cc70842a65%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_46bf127ac9b856df503ec2dbf942b67e=1728938706,1729108434; HMACCOUNT=1B06E78F6D804E45; crosSdkDT2019DeviceId=-uwtuig-wngoaf-txqkjjo54g7qcqo-uo2sorek9; ftkrc_=3af4127c-8ad8-4520-996a-d4b7f191e762; lfrc_=2b015489-e1ec-41e3-bae8-11d440eeff12; _jzqc=1; _gid=GA1.2.2098899504.1729108498; Hm_lvt_efa595b768cc9dc7d7f9823368e795f1=1729109792; login_ucid=2000000449819956; lianjia_token=2.00110c2c814646f45900a105b01049c225; lianjia_token_secure=2.00110c2c814646f45900a105b01049c225; security_ticket=g8+uJsYQd3rJsazps9dNOiUoBvZ+leUnlFsf6sDihdLz01Vms3Xm1vY5YxgXl2ZmDxcGVeISqq9+ER7n0vMzBX6WzSFUlzASrr48a33BNRTnWOYMLVpBRJ9HvEi5C0rb3H0Enf9TjuN/MJmfAGkuvaL9ZhbXqaZ+SqlSdeJYHII=; Hm_lpvt_efa595b768cc9dc7d7f9823368e795f1=1729109956; _ga_4JBJY7Y7MX=GS1.2.1729108497.2.1.1729111514.0.0.0; _ga_BGW2B8P0NN=GS1.2.1729111938.1.0.1729111938.0.0.0; Hm_lpvt_46bf127ac9b856df503ec2dbf942b67e=1729195564; _jzqckmp=1; lianjia_ssid=85a4af8b-ae1b-491d-b48f-5cd007180709; hip=oxGkovZcy87dtbqJek9bJ-ohVktcxH7HQ7uwIVitO-uL0VNlg-yYfOh-KtZYZ7kfuJQxE2y34NhGfOk5pfZwCEuUvO9n5CniKe9HZ9TryE-L87g4s0aeyDoxSpkmAbqPolTmgjnQ52LR7biiNcItU4r0By0X1SimGKT98p8-qCSCHrL6cHBy3vFhyiM%3D; _jzqa=1.875923375911874700.1728938706.1729195566.1729212833.4; _jzqx=1.1728938706.1729212833.3.jzqsr=hip%2Elianjia%2Ecom|jzqct=/.jzqsr=hip%2Elianjia%2Ecom|jzqct=/; _jzqb=1.1.10.1729212833.1; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; _ga_TJZVFLS7KV=GS1.2.1729212837.3.0.1729212837.0.0.0; _ga_WLZSQZX7DE=GS1.2.1729212837.3.0.1729212837.0.0.0'
    }

cityPageRes = requests.get(cityPageUrl, headers = headers)
tree = etree.HTML(cityPageRes.text)
lis = tree.xpath('//div[@class="city_province"]/ul/li')

cityDict = {}
for li in lis:
    # city name
    cityName = li.xpath('./a/text()')[0]
    # city url
    cityUrl = li.xpath('./a/@href')[0]
    cityDict[cityName] = cityUrl

cityName = input('Please type in city name:')

if cityName in cityDict:
    cityUrl = cityDict[cityName]
    print(cityUrl)
    count = 1
    for page in range(1, 6):
        mainUrl = f'{cityUrl}ershoufang/pg{page}/'
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
            print(count, title, price, region, unitPrice, houseInfo)
            count += 1
else:
    print('No housing source information.')





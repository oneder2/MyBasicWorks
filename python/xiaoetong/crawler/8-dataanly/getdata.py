import requests
from lxml import etree

with open('lianjia.html', 'r', encoding = 'utf-8') as f:
    html_code = f.read()
tree = etree.HTML(html_code)

# 1. collect seperately (title, price, adress...)
# allTitle = tree.xpath('//div[@class="title"]/a/text()')
# allPosition = tree.xpath('//div[@class="positionInfo"]//text()')

# 2. collect all, analyze seperately
resList = tree.xpath('//ul[@class="sellListContent"]/li')

for res in resList:
    title = res.xpath('.//div[@class="title"]/a/text()')
    price = res.xpath('.//div[@class="totalPrice totalPrice2"]//text()')
    region = res.xpath('.//div[@class="flood"]/div[@class="positionInfo"]/a/text()')
    unitPrice = res.xpath('.//div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()')
    houseInfo = res.xpath('.//div[@class="address"]/div[@class="houseInfo"]//text()')

    price = ''.join(price)
    region = ''.join(region)
    print(title, price, region, unitPrice, houseInfo)






import scrapy


class CarSpider(scrapy.Spider):
    name = "car" 
    # allowed_domains = ["car.autohome.com.cn"]
    start_urls = []

    for i in range(1,11):
        start_urls.append(f'https://car.autohome.com.cn/price/list-0-0-0-0-0-0-1-0-0-0-0-0-0-0-0-{i}.html')

    def parse(self, response):
        divs = response.xpath('//div[@class="list-cont"]')
        for div in divs:
           # xpath return list, contains tag object.
           # need to read "data" element of the object
           name = div.xpath('.//a[@class="font-bold"]/text()').get()
           score = div.xpath('.//span[@class="score-number"]/text()').get()
           desc = div.xpath('.//ul[@class="lever-ul"]/li//text()').getall()
           price = div.xpath('.//span[@class="font-arial"]/text()').get()
           print(name, score, desc, price)
 
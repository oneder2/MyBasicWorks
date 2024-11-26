import scrapy


class BaiduSpider(scrapy.Spider):
    # element
    name = "baidu"

    # allowed_domains = ["baidu.com"]

    # target url
    start_urls = ["https://www.baidu.com/"]
    
    # analyze method response
    def parse(self, response):
        print(response)



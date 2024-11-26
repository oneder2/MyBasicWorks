import scrapy


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    # allowed_domains = ["httpbin.com"]
    start_urls = ["https://httpbin.org/get"]

    def parse(self, response):
        print(response.text)

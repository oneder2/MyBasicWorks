import scrapy

from homework.items import HomeworkItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    # allowed_domains = ["career.tencent.com"]
    start_urls = ["https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1732598752798&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=1&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"]

    def parse(self, response):
        res = response.json()
        for position in res["Data"]["Posts"]:
            post_id = position["PostId"]
            country = position["CountryName"]
            location = position["LocationName"]
            about = position["Responsibility"]
            date = position["LastUpdateTime"]
            least_work_year = position["RequireWorkYearsName"]
           
            item = HomeworkItem()
            item["post_id"] = post_id
            item["country"] = country
            item["location"] = location
            item["about"] = about
            item["date"] = date
            item["least_work_year"] = least_work_year

            yield item





            

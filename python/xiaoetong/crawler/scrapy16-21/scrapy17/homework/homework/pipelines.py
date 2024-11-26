# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HomeworkPipeline:
    def open_spider(self, spider):
        self.f = open("tencent.txt", "a", encoding="utf-8")

    def process_item(self, item, spider):
        self.f.write(f'posting id num: {item["post_id"]}, country: {item["country"]}, working location: {item["location"]}, about the position: {item["about"]}, posting date: {item["date"]}, least length of service: {item["least_work_year"]}')

    def close_spider(self, spider):
        self.f.close()











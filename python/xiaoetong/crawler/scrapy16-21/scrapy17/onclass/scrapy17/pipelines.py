# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Scrapy17Pipeline:
    def open_spider(self, spider):
        self.f = open('bilibili_ranking.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(f'vedio_bvid:{item["bvid"]}, vedio_author:{item["author"]}, vedio_title:{item["title"]}, vedio_description:{item["description"]}, vedio_view_amount:{item["view_amount"]}')

    def close_spider(self, spider):
        self.f.close()


    """
    # drawback: too much system resource occupation

    def process_item(self, item, spider):
        # print
        with open('bilibili_ranking.txt', 'a', encoding='utf-8') as f:
            f.write
            (f'
            vedio_bvid:{item["bvid"]}, 
            vedio_author:{item["author"]}, 
            vedio_title:{item["title"]}, 
            vedio_description:{item["description"]}, 
            vedio_view_amount:{item["view_amount"]}
            ')
        return item
    """

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OnclassItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post_id = scrapy.Field()
    country = scrapy.Field()
    location = scrapy.Field()
    about = scrapy.Field()
    date = scrapy.Field()
    least_work_year = scrapy.Field()

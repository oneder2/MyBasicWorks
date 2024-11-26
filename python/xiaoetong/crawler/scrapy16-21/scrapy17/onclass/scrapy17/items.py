# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# If pipe line saving is used, this class have to be created
# and submit data to pipe
# 
# the number of elements related with the number of data reqires to be saved
class Scrapy17Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bvid = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    view_amount = scrapy.Field()

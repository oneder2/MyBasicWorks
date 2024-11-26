import scrapy
import time

# import format: 
# sharing direction/xxx/xxx/target_package
from scrapy17.items import Scrapy17Item


class BilibiliSpider(scrapy.Spider):
    name = "bilibili"
    # allowed_domains = ["a.com"]
    start_urls = [f"https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all&web_location=333.934&w_rid=9080a34d310e43e7374e52d4426a78e6&wts={time.time()}"]
    def parse(self, response):
        # return a dictionary
        res = response.json()
        print(res)
        for vedio_info in res["data"]["list"]:
            print(1)
            # vedio id
            bvid = vedio_info['bvid']
            # author
            author = vedio_info['owner']['name']
            # title
            title = vedio_info['title']
            # describesion
            description = vedio_info['desc']
            # play times
            view_amount = vedio_info['stat']['view']

            # create item object
            item = Scrapy17Item()
#            item.bvid = bvid
#            item.author = author
#            item.title = title
#            item.description = description
#            item.view_amount = view_amount

            item['bvid'] = bvid
            item['author'] = author
            item['title'] = title
            item['description'] = description
            item['view_amount'] = view_amount

            yield item
 


"""
(1)
    def parse(self, response):
        # print(response.text)
        # return a dictionary
        res = response.json()
        ls = []
        count = 1
        for vedio_info in res["data"]["list"]:
            # vedio id
            bvid = vedio_info['bvid']
            # author
            author = vedio_info['owner']['name']
            # title
            title = vedio_info['title']
            # describesion
            description = vedio_info['desc']
            # play times
            view_amount = vedio_info['stat']['view']
            print(bvid, author, title, description, view_amount)
            data_dict = {'vedio_id': bvid, 
                         'author': author, 
                         "title": title, 
                         "description": description, 
                         "view_amount": view_amount}
            ls.append(data_dict)
            count+=1
        return ls
"""











 







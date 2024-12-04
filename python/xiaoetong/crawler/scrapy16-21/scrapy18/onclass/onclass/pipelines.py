# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
import openpyxl


class OnclassExcelPipeline:
    def open_spider(self, spider):
        # create worksheet object
        self.wb = openpyxl.Workbook()
        # choose / create subsheet
        self.sh1 = self.wb.active
        self.sh1.title = 'occupation_data'
        # append table head
        self.sh1.append(['position_id', 
                    'country', 
                    'location', 
                    'about', 
                    'publish_date', 
                    'lease_work_year']
                    )

    def process_item(self, item, spider):
        # append data
        self.sh1.append([item["post_id"], 
                        item["country"],
                        item["location"],
                        item["about"],
                        item["date"],
                        item["least_work_year"]]
                        )
        return item

    def close_spider(self, spider):
        # save 
        self.wb.save('occupation_data.xlsx')



class OnclassMysqlPipline:
    def __init__(self):
        self.connection = 0
        self.cur = 0

    def open_spider(self, spider):
        self.connection = pymysql.Connect(host='127.0.0.1', 
                        port=3306, 
                        user='learner', 
                        password='123456', 
                        database='spider38')
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO tencent VALUES("%s", "%s", "%s", "%s", "%s", "%s")' % (
            item["post_id"], 
            item["country"], 
            item["location"], 
            item["about"], 
            item["date"], 
            item["least_work_year"]
        )

        try:
            self.cur.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(f'Error info: {e}')
            self.connection.rollback()
        return item

    def close_spider(self, spider):
        if self.cur != 0 and self.connection != 0:
            self.cur.close()
            self.connection.close()

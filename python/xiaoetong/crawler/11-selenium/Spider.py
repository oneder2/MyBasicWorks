import pymysql.charset
import requests
import pymysql
from lxml import etree

class Spider:
    def __init__(self, url, host, username, password, database) -> None:
        self.url = url
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.headers = {
            'user-agent'
        }

        self.port = 3307
        self.connector = pymysql.Connect(
            host=host, 
            user=username, 
            password=password, 
            database=database
            )
        self.cursor = self.connector.cursor()

    def send_request(self):
        res = requests.get(self.url, headers=self.headers)
        res.encoding = 'utf-8'
        self.parse(res.text, res)
    
    def parse(self, data):
        tree = etree.HTML(data)
        trs = tree.xpath('//tr[@class="t_tr1"]')
        for tr in trs:
            # base on each row of table, get all colums
            tds = tr.xpath('./td/text()')
            # data of red balls
            self.save_mysql(tds)
    
    def save_mysql(self, tds): # tds: each line of data on page
        red_nums = ','.join(tds[1:7])
        try:
            sql = f'INSERT INTO ssq VALUES (null,"{red_nums}","{tds[7]},"{tds[8]}","{tds[9]}","{tds[10]}","{tds[11]}","{tds[12]}","{tds[13]}","{tds[14]}","{tds[15]}")'
            self.cursor.execute(sql)
            self.connector.commit()
        except:
            self.connector.rollback()
    
    def close_conn(self):
        self.cursor.close()
        self.connector.close()



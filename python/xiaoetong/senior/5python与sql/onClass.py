import pymysql

# 建库
# 创建链接
db = pymysql.connect(host = "localhost", 
                     port = 3306, 
                     user = "root" ,
                     password = "root",
                     database = "day05",
                     charset = "utf8")

# 创建游标，操作数据库
youbiao = db.cursor()

"""
# 创建一个数据库
sql = 'create database day05;'
# 使用execute函数去找sql
youbiao.execute(sql)
"""


# 基础查询
"""
# 执行一个sql语句
sql = 'select * from products'
# 给一个row_count
row_count = youbiao.execute(sql)
# print(f"执行受到影响的行数：{row_count}")
# print(youbiao.fetchone())
# print(youbiao.fetchall())
for i in youbiao.fetchall():
    print(i)
"""


# 增删改
# 建表格
"""
sql = 'create table hero_kongfu(hid int, hname varchar(50), kname varchar(50));'
youbiao.execute(sql)
"""


# 插入数据
# 第一种方式
"""
sql = 'insert into hero_kongfu values (%s, %s, %s)'
data = (1, '乔峰', '降龙十八掌')
youbiao.execute(sql, data)
"""

# 第二种方式
"""
sql = "insert into hero_kongfu values (2, '段誉', '六脉神剑'), (3, '虚竹', '天山折梅手')"
youbiao.execute(sql)
"""

# 删除元素

sql = "delete from hero_kongfu where hname = '虚竹'"
youbiao.execute(sql)

db.commit()
# 关闭连接和游标
youbiao.close()
db.close()




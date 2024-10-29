import pymysql  # 导入模块

'''# 创建连接
db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='root', charset='utf8')
# 创建游标，操作数据库
youbiao = db.cursor()
# 写一个sql语句
sql = 'create database day05;'
# 用execute()函数去执行sql
youbiao.execute(sql)
youbiao.close()
db.close()'''


'''# 查询数据库里面数据
# 通过pymysql来查询mysql里面的数据
db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='root', database='day04', charset='utf8')
# 获取游标
youbiao = db.cursor()
# 执行查的sql语句
sql = 'select * from products;'
# 给一个row_count
row_count = youbiao.execute(sql)
# print(f"执行受到影响的行数：{row_count}")# 9
# fetchone()函数：获取一行数据
# print(youbiao.fetchone())
# fetchall():获取全部的数据
# print(youbiao.fetchall())
for i in youbiao.fetchall():
    print(i)
# 关闭连接和游标
youbiao.close()
db.close()'''


# 增删改呢？
db = pymysql.connect(host='localhost', port=3306, user='root',
                     password='root', database='day05', charset='utf8')
youbiao = db.cursor()
# 1.创建一个hero_kongfu表hid,hname,kname
# sql = 'create table hero_kongfu(hid int,hname varchar(50),kname varchar(50));'
# youbiao.execute(sql)


# 2.插入数据
# 第一种方式：
# sql = 'insert into hero_kongfu values (%s,%s,%s)'
# data = (1,'乔峰','降龙十八掌')
# youbiao.execute(sql,data)
# 第二种方式：
# sql = "insert into hero_kongfu values (2,'段誉','六脉神剑')"
# youbiao.execute(sql)
# 第三种方式：
# sql = "insert into hero_kongfu values (3,'慕容复','斗转星移'),(4,'虚竹','天山折梅手');"
# youbiao.execute(sql)
# 为啥没数据？
# 没有提交
# 事务：insert，update，delete
# 你搬砖搬了1000块，完成任务了，要提交

# 2.修改数据
# sql = "update hero_kongfu set kname='打狗棒法' where hname='乔峰' "
# youbiao.execute(sql)

# 3.删除数据
sql = "delete from hero_kongfu where hname='虚竹'"
youbiao.execute(sql)


# 提交事务
db.commit()
# 关闭连接和游标
youbiao.close()
db.close()


# 休息十分钟






import pymysql


# 已经安装完毕
db = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="day06"
)

# 游标
myCursor = db.cursor()

# 建库
# 预先创建完毕
# createDatabase = "create database day06"
# myCorsur.execute(createDatabase)

# 建表
# 预先创建完毕
# createTable = "create table products(id int, pname varchar(50))"
# myCursor.execute(createTable)

#插入数据
# for i in range(1, 5+1):
#     insertSQL = f"insert into products values({i}, '张三')"
#     myCursor.execute(insertSQL)

# 修改数据(似乎连sql语句也没教，不过咱试试)
# changeSQL = "update products set pname = '李四' where id = 2"
# myCursor.execute(changeSQL)

# 删除数据
deleteSQL = "delete from products where id = 5"
myCursor.execute(deleteSQL)

# 查询数据
# checkData = "select * from products"
# row_count = myCursor.execute(checkData)
# # print(f"涉及到的行数有{myCursor.execute(checkData)}行")
print(myCursor.fetchall())



# 提交结果
db.commit()

# 关闭连接和游标
myCursor.close()
db.close()

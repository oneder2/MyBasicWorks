import pymysql


stdb = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="day06"
)

myCursor = stdb.cursor()

# 创建表
# createTableSQL = "create table students(id int primary key, name varchar(50), age int, gender varchar(50))"
# myCursor.execute(createTableSQL)

# 插入数据
# for i in range(1,6):
#     addSQL = f"insert into students values({i}, '张三', 18, '男')"
#     myCursor.execute(addSQL)

# 更新数据
# updateSQL = "update students set age = 19 where id = 5"
# myCursor.execute(updateSQL)

# 删除数据
deleteSQL = "delete from students where id = 5"
myCursor.execute(deleteSQL)

# 查询数据
checkDataSQL = "select * from students"
row_affected = myCursor.execute(checkDataSQL)
# print(f'受到影响的行数有：{row_affected}行')
print(myCursor.fetchall())

# 信息呈递
stdb.commit()
# 内存安全
stdb.close()
myCursor.close()



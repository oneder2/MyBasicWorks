# 创建数据库
# 数据库的单词叫：database
# mysql5@localhost：连接数据库的链接名字
# mysql:数据库
# table：（表）在库里面是有表的
# 创建一个数据库
# 创建数据库:
# create database [if not exists] 库名 [DEFAULT CHARACTER SET utf8];
# []：里面的东西可以省略
# 创建day01数据库
# sql代码是一行一行来运行的以；为一句，python是全部代码
# ctrl+回车
create database day01;
create database day001;

# if not exists:如果你创建的这个数据库不存在就创建，存在就不报错也不创建
create database if not exists day01;
# show databases;查看当前链接中，所有的数据库有哪些？
show databases;

use day01;# 你要use 你要操作的数据库

# 查看指定库的建库语句: show create database 库名;(了解)
show create database day01;
# 查看当前使用的是哪个数据库: select database();（了解）
select database();

# 删除数据库：drop database 库名；
drop database day001;


# 1.mysql是数据库 我们学他为了，方便保存数据，后续可以把数据保存到数据库中
# 可以通过代码来创建数据库和插入数据查数据等等
# 2.软件安装和测试，pycharm连接mysql掌握
# 3.建库的代码语句
# 今天主要内容还是软件安装和连接
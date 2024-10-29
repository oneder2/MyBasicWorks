# 枚举类型：enum(x,y):类似单选，一次只能插入一个数据
# 集合类型：set(x,y):类似多选，一次可以插入多个值
use day05;
create table user(
  id int primary key auto_increment,
  uname varchar(50),
  pwd varchar(50),
  age int,
  sex enum('男','女'),
  hobby set('吃饭','学习','跟着老师上课学习')
);
#
insert into user values (1,'张三','123456',18,'男','吃饭');
#
insert into user (uname,sex) values ('小美','妖');
insert into user (uname,sex) values ('小美','女');
insert into user (uname,sex) values ('小美','男,女');
# 集合类型
insert into user (uname,hobby) values ('小帅','吃饭,学习');
insert into user (uname,hobby) values ('小帅1','吃饭');
insert into user (uname,hobby) values ('小帅1','打游戏');

# 假设允许有第三个性别：妖
alter table user change sex sex enum('男','女','妖');
insert into user (uname,sex) values ('小美','妖');


# 查看mysql中的引擎
show engines;



# 查看自动提交事务状态: select @@autocommit;
select @@autocommit; #
# 开启自动提交事务的方式:1
# 禁用自动提交事务的方式:0

# 创建一个账目表
create table student(
    id int,
    name varchar(50),
    money double
);
# 查看事务是否自动提交
select @@autocommit;
insert into student values (1,'阿三',10000);
insert into student values (2,'阿四',10000);
drop table student;
# 禁用自动提交事务
set autocommit = 0;
select @@autocommit;
# 阿四在外面鬼混，被打了，向借点钱
# 开始事务
start transaction ;
# 阿三给阿四转两千块钱
update student set money = money - 2000 where name='阿三';
update student set money = money + 2000 where name='阿四';
# 提交事务
commit ;

# 开始事务
select @@autocommit;
set autocommit =0;
start transaction ;
# 转钱 断点
update student set money = money - 2000 where name='阿三';
# 事务回滚
rollback;
# 阿四
update student set money = money + 2000 where name='阿四';





# 演示视图操作
# 查看河北省下所有的城市
use day04;
create view day04.hbs_areas as
select * from day04.areas where pid = (select id from day04.areas where title='河北省');
# 创建视图后如果以后还想查询河北省的所有城市
# 查询视图
select * from hbs_areas;

# 查看邯郸市的基本信息
create view day04.handan_areas as
select * from day04.areas where title='邯郸市';

# 删除视图
drop view day04.handan_areas;

# 修改视图数据
alter view day04.hbs_areas as select * from day04.areas where title='河北省';

# 修改视图名
rename table day04.hbs_areas to day04.areas_hbs;

# 查询视图
select * from day04.areas_hbs;

# 查看所有表包含视图
use day04;
show tables;
# 查看类型信息需要加full
show full tables;
# 查看视图中字段信息
desc day04.areas_hbs;


# pymysql是重点，其他了解就行， mysql数据库就结束了，下节课html
# 作业完成一下
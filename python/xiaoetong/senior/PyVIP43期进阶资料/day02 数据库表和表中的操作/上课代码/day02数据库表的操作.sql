# 表的操作
# table
# 创建表的语句：
# create table 表名 （字段名字 字段类型，。。。。）;
# 在库里面建表
# 先创建数据库day01
create database day01;
# 用use 指定一个数据库
use day01;
# 创建表字段，里面没有数据
create table student(
    name varchar(50),
    age int,
    address varchar(50)
);
# 修改表名
rename table student to student1;
# 查看当前库中所有的表
show tables ;
# 删除表的代码：
# 删除表: drop table 表名;
drop table student1;
# 查看表的结构
desc student;



# 针对表就行操作
# 在表中添加一列: alter table 表名 add  字段名 字段类型;
# 重新创建一个数据库
create database day02;
# 使用day02
use day02;

# 创建一个表
create table student(
    name varchar(50) ,
    age int,
    address varchar(50),
    class varchar(50)
);
# 给这个student表加一字段
# mobile：电话
alter table student add mobile int;
# 在表中删除一列: alter table 表名 drop  字段名;
alter table student drop age;
# 把class这个字段（varchar）的字段类型改成int
# 1.change  旧字段名  新字段名 新字段类型
alter table student change class class int;
# address字段改成youzhengbianma
alter table student change address youzhengbianma varchar(50);
# 2.modify 只能修改类型
# modify 旧字段名 新字段类型
alter table student modify class varchar(50);
desc student;
drop table student;
# 一直再讲表的创建和修改，库的创建和删除
# 创建好之后是不是该用了？添加数据
# 往表中插入记录:
# 	插入一条: insert into 表名 (字段1名,字段2名, ...) values (值1,值2, ...);
# 	插入多条: insert into 表名 (字段1名,字段2名, ...) values (值1,值2, ...) , (值1,值2, ...) , (值1,值2, ...);
insert into student(name,class) values ('张三','43班');
insert into student values ('张三',12,'湖南','43班');
insert into student(name) values ('张三');
# 会发生隐式类型转换  数字的字符串会自动转int，有中文就不行
insert into student(name, age) values ('张三1', 22);
insert into student(name, age) values ('张三2', '22');
insert into student(name, age) values ('张三2', '22岁');
insert into student values('张三',22,'湖南','43'),('李四',23,'湖北','42');
# update 表名 set 字段名=值 where 条件；
# 提醒你是不是要对所有age字段或者class字段的数据都进行修改？
# 就会把age字段所有数据都改成22
update student set age=22 where name='李四';

# 从表中删除记录:
# 删除部分记录: delete from 表名 where 条件;
# 删除所有记录方式1: delete from 表名;
# 删除所有记录方式2: truncate [table] 表名;
delete from student ; # 是什么样的结果？清空表（慎用）
truncate table student; # 也可以删除全部数据
delete from student where name='李四';



# 约束：
# 1。主键约束（非空唯一） primary key
create table stu1(
    sid int primary key ,
    name varchar(50),
    class int
);
# 插入数据的时候，约束字段的数据要非空唯一
insert into stu1 values (1,'小帅',43);
insert into stu1 values (2,'小美',43);
# mysql中的空是null  不是字符串'null'
# insert into stu1 values (3,'null',43);
insert into stu1 values (null,'小美',43);

# 2.主键自增约束（primary key auto_increment）
# 特点：自动加1
create table stu2(
    sid int primary key auto_increment,
    name varchar(50),
    class int
);
# 插入数据
insert into stu2 values (1,'小路',43);
insert into stu2(name, class) values ('小路',43);
insert into stu2(name, class) values ('小路',43);
insert into stu2(name, class) values ('小路',43);
# 如果是null和0呢代表自增
insert into stu2 values (0,'小路',43);
insert into stu2 values (null,'小路',43);
insert into stu2 values (11,'小路',43);

# 3.非空约束：not null  不能为空
create table stu3(
    sid int primary key auto_increment,
    name varchar(50) not null,
    class int
);
insert into stu3(sid,name,class) values (110,'旺财',43);
insert into stu3(sid,name,class) values (111,null,43);



# 4.唯一约束：unique   唯一，不能重复
create table stu4(
    sid int primary key auto_increment,
    name varchar(50) not null,
    class int,
    mobile int unique
);
insert into stu4 values (110,'旺财',43,110);
insert into stu4 values (111,'keke',43,110);

# 5.default :(函数的默认参数一样原理) 默认值 （默认约束）
# 如果不指定，就使用默认值插入到表中
create table stu5(
    sid int primary key auto_increment,
    name varchar(50) not null,
    class int default 43,
    mobile int unique
);
insert into stu5 values (110,'旺财',43,110);
insert into stu5 values (112,'旺财',null,1);
# insert into stu5 values (110,'旺财',0,12);
insert into stu5(sid,name,mobile) values (111,'keke',111);


# 约束：五个约束要理解，建库建表和修改库，插入数据（掌握）
# 这部分实操较强，完成好作业
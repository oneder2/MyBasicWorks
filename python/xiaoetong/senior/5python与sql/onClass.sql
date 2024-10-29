use day05;

create table user(
    id int primary key auto_increment,
    uname varchar(50),
    pwd varchar(50),
    age int,
    sex enum('男', '女'),
    hobby set('吃饭' ,'学习', '画画')
);

insert into user values (1, '张三', '123456', 18, '男', '画画');

alter table user 
change sex sex enum('男', '女', '妖');

insert into user (uname, sex) values ('八云紫', '妖');

create database day06;

create database students;
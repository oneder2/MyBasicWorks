-- Active: 1725127272463@@127.0.0.1@3306
use day02;

create table stu2(
    side int primary key auto_increment,
    name varchar(50),
    class int
);

insert into stu2 values(1, '姬小陆赖纲', 43);
insert into stu2(name, class) values('宇都宫秀佳', 43);
insert into stu2(name, class) values(0, '长曾我部元亲', 43)

create table stu3(
    sid int primary key auto_increment,
    name varchar(50) not null,
    class int
);
insert into stu3(sid, name, class) values (110, '铁蛋儿', 48);
insert into stu3(sid, name, class) values (111, 'null', 48);

create table stu4(
    sid int primary key auto_increment,
    name varchar(50) not null,
    class int,
    mobile int unique
);
insert into stu4 values (110, '铁蛋儿', 48, 133);
insert into stu4 values (111, 'null', 48, 133);

create table stu5(
    sid int primary key auto_increment,
    name varchar(50) not null,
    class int default 43,
    module int unique
);
insert into stu5 values(110, '铁蛋', 43, 133);
insert into stu5 (sid, name, module)values(111, '铁蛋', 136)



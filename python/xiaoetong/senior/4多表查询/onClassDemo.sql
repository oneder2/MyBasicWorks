create database day04;
use day04;

-- 主表
create table catagory(
    cid varchar(50) primary key,
    cname varchar(50)
);

-- 从表
drop table product;
create table product(
    pid varchar(50) primary key,
    pname varchar(50),
    price double,
    catagory_id varchar(50),
    constraint foreign key (catagory_id) references catagory(cid)
);

-- 创建主表键
insert into catagory values ('c001', '数码产品');
insert into catagory values ('c002', '日用品');

-- 将插入从表的数据与主表进行字段关联
insert into product values ('1111', '相机', 12, 'c001');
-- 当
delete from catagory where cid = 'c001';
delete from product where catagory_id = 'c001';


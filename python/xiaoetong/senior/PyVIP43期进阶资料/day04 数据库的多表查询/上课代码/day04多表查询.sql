# 在从表中添加外键约束格式:
# [constraint 外键名称] FOREIGN KEY(外键) references 主表名(主键)
# 创建day04数据库
create database day04;
use day04;
# 分类表 主表
create table category(
    cid varchar(50) primary key ,
    cname varchar(50)
);
# 商品表  （从表）
create table product(
    pid varchar(50) primary key ,
    pname varchar(50),
    price double,
    category_id varchar(50),
    constraint foreign key (category_id) references category(cid)
);

# 限制从表的插入操作：保证主从表数据一致性
insert into category values ('c001','数码产品'),('c002','日用品');
insert into product values ('1111','可乐',12,'c003'); # 插入失败，因为外键约束了，必须cid有这个类别
insert into product values ('1111','电脑',6000,'c001');

# 限制了主表的删除操作：保证数据的完整性
delete from category where cid='c001';
# 因为从表product的category_id字段的数据，引用了cid的数据，如果你想删主表的数据，必须保证从表没有c001了
delete from product where category_id='c001';
# 再执行删除主表的c001
delete from category where cid='c002';



# 多表查询　　现在我想把商品表的所有字段和分类表的所有字段同时查出来
# 英雄表 hero
create table hero(
    hid int primary key ,
    hname varchar(50),
    kongfu_id int
);
# 功夫表 kongfu
create table kongfu(
    kid int primary key ,
    kname varchar(50)
);
# 插入几条数据
insert into hero values (1,'鸠摩智',9),(3,'乔峰',1),(4,'虚竹',4),(5,'段誉',12);
insert into kongfu values (1,'降龙十八掌'),(2,'乾坤大挪移'),(3,'猴子偷桃'),(4,'天山折梅手');

# 内连接：内连接关键字:  inner join ... on       注意: inner 可以省略

# 只保留两个表的交集（公共一样的部分），其他数据过滤掉

# 查询有对应功夫的英雄名，显示英雄名字和对应的功夫名
# 显示内连接：select 字段名 from 左表 inner join 右表 on 两个表的关联条件
select hname,kname from hero join kongfu on hero.kongfu_id=kongfu.kid;
select hname,kname from kongfu join hero on hero.kongfu_id=kongfu.kid;

# 快速将代码上下移动：ctrl+shift+方向键


# 外连接：就是两个表的并集
# 左外连接：left outer join ... on ...   outer 可以省略
# 右外连接：right outer join ...on ...
# 左表所有的数据都有，包括共同的部分，左表没对应上的就是null
select hname,kname from hero h left join kongfu k on h.kongfu_id=k.kid;
# 右外：
select hname,kname from hero right join kongfu on hero.kongfu_id=kongfu.kid;
select hname,kname from kongfu left join hero on hero.kongfu_id=kongfu.kid;



# 子连接：
# 一个完整的select语句作为另外一个select语句的表或者条件来使用
# 准备实战数据
CREATE TABLE category1(
  cid VARCHAR(32) PRIMARY KEY ,
  cname VARCHAR(50)
);
CREATE TABLE products(
  pid VARCHAR(32) PRIMARY KEY ,
  pname VARCHAR(50),
  price INT,
  flag VARCHAR(2),    #是否上架标记为：1表示上架、0表示下架
  category_id VARCHAR(32),
  CONSTRAINT products_fk_test FOREIGN KEY (category_id) REFERENCES category1 (cid)
);
drop table category1;
drop table products;

# 分类表插入数据
INSERT INTO category1(cid,cname) VALUES('c001','家电');
INSERT INTO category1(cid,cname) VALUES('c002','服饰');
INSERT INTO category1(cid,cname) VALUES('c003','化妆品');
INSERT INTO category1(cid,cname) VALUES('c004','奢侈品');
#商品表插入数据
INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p001','联想',5000,'1','c001');
INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p002','海尔',3000,'1','c001');
INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p003','雷神',5000,'1','c001');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p004','JACK JONES',800,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p005','真维斯',200,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p006','花花公子',440,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p007','劲霸',2000,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p008','香奈儿',800,'1','c003');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p009','相宜本草',200,'1','c003');



# 查询化妆品分类下的所有商品信息
# 先查分类表化妆品对应的cid，然后再用这个cid商品表去查
select cid from category1 where cname='化妆品'; # c003
select * from products where category_id='c003';
select * from products where category_id= (select cid from category1 where cname='化妆品');

# 查询化妆品和家电两个分类下的所有商品信息
select * from products where category_id in (select cid from category1 where cname in ('化妆品','家电'));


# 自连接：一种特例，可以将一个表作为两个表使用  可以连接自己
# 省市区表
# 查询河北省所有的城市
# 先查河北省的pid ，然后再查河北省下的id
select id from areas where title='河北省';
# 石家庄的pid就是河北省的id
# 子连接：
select * from areas where pid = (select id from areas where title='河北省');
# 自连接：给areas 这个表起两个别名分别当省和市表来用
select * from areas sheng join areas shi on sheng.id=shi.pid where sheng.title='湖南省';

# 把作业写好，听懂还是得写，不然还是不会   下课啦
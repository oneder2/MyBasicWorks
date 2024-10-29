-- 主表
CREATE TABLE hero
(
hid INT PRIMARY KEY,
hname VARCHAR(255),
kongfu_id INT
);

-- 从表
CREATE TABLE kongfu
(
kid INT PRIMARY KEY,
kname VARCHAR(255)
);

-- 插数据
INSERT INTO hero VALUES(1, '鸠摩智', 9),(3, '乔峰', 1),(4, '虚竹', 4),(5, '段誉',12);
INSERT INTO kongfu VALUES(1, '降龙十八掌'),(2, '乾坤大挪移'),(3, '猴子偷桃'),(4, '天山折梅手');


-- 内连接练习
-- 方式一
select hname, kname 
from hero inner 
join kongfu 
on hero.kongfu_id = kongfu.kid;
-- 方式二
select hname, kname 
from hero, kongfu 
where kongfu_id = kid;


-- 外连接练习
-- 需求
select hname, kname 
from hero 
left join kongfu 
on hero.kongfu_id = kongfu.kid;

-- 需求
select hname, kname 
from kongfu 
left join hero 
on hero.kongfu_id = kongfu.kid;


-- 内外连接查询实战练习
use day04;
-- 由于之前已经建过category和products,并且加了外界约束,需要删除重新建表并插入新数据
-- 先删除从表
drop table if exists products;
-- 再删除主表
drop table if exists category;

-- 准备实战数据
CREATE TABLE category (
cid VARCHAR(32) PRIMARY KEY ,
cname VARCHAR(50)
);

CREATE TABLE products(
pid VARCHAR(32) PRIMARY KEY ,
pname VARCHAR(50),
price INT,
flag VARCHAR(2), -- 是否上架标记为：1表示上架、0表示下架
category_id VARCHAR(32),
CONSTRAINT products_fk_test FOREIGN KEY (category_id) REFERENCES category(cid)
);x

-- 分类表（主表）插入数据
INSERT INTO category(cid,cname) VALUES('c001','家电');
INSERT INTO category(cid,cname) VALUES('c002','服饰');
INSERT INTO category(cid,cname) VALUES('c003','化妆品');
INSERT INTO category(cid,cname) VALUES('c004','奢侈品');
-- 商品表（从表）插入数据
INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p001','联想',5000,'1','c001');
INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p002','海尔',3000,'1','c001');
INSERT INTO products(pid, pname,price,flag,category_id) VALUES('p003','雷神',5000,'1','c001');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p004','JACKJONES',800,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p005','真维斯',200,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p006','花花公子',440,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p007','劲霸',2000,'1','c002');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p008','香奈儿',800,'1','c003');
INSERT INTO products (pid, pname,price,flag,category_id) VALUES('p009','相宜本草',200,'1','c003');

-- 需求1
select distinct category_id 
from products 
where flag = 1;

-- 需求2
select category_id, count(*)
from products
group by category_id;

-- 需求3
select cid, count(category_id) -- 展示所有种类，以及根据从表统计出的cid数量
from category -- 主表（left）
left join products -- 从表
on category.cid = products.category_id
group by cid; -- 统计category_id与cid相等，并非cid数量

-- 需求4
select *
from products
where category_id = (
    select cid
    from category
    where cname = '化妆品'
);

-- 需求5
select *
from products
where category_id in(
    select cid
    from category
    where cname in('化妆品', '家电')
);


-- 自连接查询
-- 需求1
-- 子查询
select *
from areas 
where pid = (
    select id
    from areas 
    where title = '湖南省'
    );

-- 自查询
select shi.title -- 由于join将两表拼接，因此存在分别来自sheng和shi的表头，需要特殊注明'shi.xxx'
from areas sheng
join areas shi
on sheng.id = shi.pid
where sheng.title = '湖南省'


-- 需求2
-- 子查询
select title
from areas 
where pid = (
    select id
    from areas 
    where title = '株洲市'
    );

-- 自查询
select shi.title -- 由于join将两表拼接，因此存在分别来自sheng和shi的表头，需要特殊注明'shi.xxx'
from areas sheng
join areas shi
on sheng.id = shi.pid
where sheng.title = '株洲市';

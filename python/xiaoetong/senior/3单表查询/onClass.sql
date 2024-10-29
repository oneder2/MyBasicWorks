create database day03;
use day03;

CREATE TABLE product
(
pid INT PRIMARY KEY,
pname VARCHAR(20),
price DOUBLE,
category_id VARCHAR(32)
);

INSERT INTO product(pid,pname,price,category_id) VALUES(1,'联想',5000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(2,'海尔',3000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(3,'雷神',5000,'c001');
INSERT INTO product(pid,pname,price,category_id) VALUES(4,'杰克琼斯',800,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(5,'真维斯',200,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(6,'花花公子',440,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(7,'劲霸',2000,'c002');
INSERT INTO product(pid,pname,price,category_id) VALUES(8,'香奈儿',800,'c003');
INSERT INTO product(pid,pname,price,category_id) VALUES(9,'相宜本草',200,'c003');
INSERT INTO product(pid,pname,price,category_id) VALUES(10,'面霸',5,'c003');
INSERT INTO product(pid,pname,price,category_id) VALUES(11,'好想你枣',56,'c004');
INSERT INTO product(pid,pname,price,category_id) VALUES(12,'香飘飘奶茶',1,'c005');
INSERT INTO product(pid,pname,price,category_id) VALUES(13,'海澜之家',1,'c002');

select pname as 商品名称, price as 商品价格 from product;

-- distinct: 查重
select distinct category_id from product;

-- where：条件查询
-- 比大小：= != > >= < <=
select * from product where price > 2000;

-- 查区间：between x and y
select * from product where price between 300 and 5000;

-- 查特殊值：in(x, y)
select * from product where price in(3000, 5000);

-- 查关键字符：-, %
select pname from product where pname like "%想%";

insert into product VALUES(14, "小米汽车", 210000, null);
-- 判断是否为空：null
select pname from product where category_id is not null;

-- 顺序排序：order by
select * from product order by price; -- 升序
select * from product order by price desc; -- 降序，衔接在每一个字段之后
select * from product order by price,category_id desc;
select * from product order by price desc,category_id;

-- 聚合查询
select count(pid) from product;-- 查询唯一key值
select count(category_id) from product; -- 查询不唯一字段值（不计null）
select count(*) from product; -- 查询所有值（计入null)
select sum(price) from product; -- 求特定字段数值总和
select avg(price) from product; -- 求平均值
select min(price) from product; -- 求最小值
select max(price) from product; -- 求最大值

-- 分组查询
-- select 分组字段名，聚合函数 from 表名 group by 分组字段名;
select category_id as 分类编号, count(*) as 数量 from product group by category_id;
-- 使用聚合表达式改变输出结果的显示效果
select category_id, sum(price) from product group by category_id desc;
select category_id, avg(price) from product group by category_id desc;
-- round语句保留小数位数
select category_id, round(avg(price), 2) from product group by category_id desc;

-- 分组查询 + 条件查询
select category_id, count(*) 
from product 
where category_id is not null
group by category_id 
having count(*) > 1;

-- 分页查询
select * from product limit 0,5;
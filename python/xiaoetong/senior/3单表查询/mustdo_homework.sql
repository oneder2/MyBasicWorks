-- 1.准备工作
create database home_work1;
use home_work1;
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
INSERT INTO product(pid,pname,price,category_id) VALUES(14,'奔波儿灞',123, null);
INSERT INTO product(pid,pname,price,category_id) VALUES(15,'灞波儿奔',321, null);
INSERT INTO product(pid,pname,price,category_id) VALUES(16,'浪波儿浪',132, null);

-- 2.简单查询练习
-- 需求1
select * from product;
-- 需求2
select pname, price from product;
-- 需求3
select pname as 商品名称, price as 商品价格 from product;
select pname 商品名称, price 商品价格 from product;
-- 需求4
select distinct category_id from product; 


-- 3.条件查询练习
-- 3.1比较运算符
-- 需求1
select * from product where price > 2000;
-- 需求2
select * from product where price < 2000;
-- 需求3
select * from product where price >= 2000;
-- 需求4
select * from product where price <= 2000;
-- 需求5
select * from product where price != 2000;
select * from product where not price = 2000;

-- 3.2逻辑运算符
-- 需求6
select * from product where price >= 200 and price <= 2000;
-- 需求7
select * from product where price in(3000, 5000);
select * from product where price = 3000 or price = 5000;
-- 需求8
select * from product where not price = 2000;
-- 需求9
select * from product where not (200 <= price and price <= 2000);

-- 3.3范围查询
-- 需求不明确，在此将课上随笔代码上交：
select * from product where price between 300 and 5000;

-- 3.4模糊查询
-- 需求10
select * from product where pname like("香%");
-- 需求11
select * from product where pname like("香__");
-- 需求12
select * from product where pname like("%想%");
-- 需求13
select * from product where pname like("%斯");
-- 需求14
select * from product where pname like("__斯");


-- 4.排序查询
-- 需求1
select * from product order by price;
-- 需求2
select * from product order by price desc;
-- 需求3
select * from product order by price, category_id;
-- 需求4
select * from product order by price, category_id desc;

-- 5.聚合查询
-- 需求1
select count(*) from product;
-- 需求2
select count(*) from product where category_id is not null;
-- 需求3
select sum(price) from product;
-- 需求4
select avg(price) from product;
-- 需求5
select max(price) from product;
-- 需求6
select min(price) from product;

-- 6.分组查询
-- 分组查询
-- 需求1
select category_id, count(*) from product group by category_id;
-- 需求2
select category_id, sum(price) from product group by category_id;
-- 需求3
select category_id, max(price) from product group by category_id;
-- 需求4
select category_id, min(price) from product group by category_id;
-- 需求5
select category_id, avg(price) from product group by category_id;
-- 需求6
select category_id, round(avg(price), 2) from product group by category_id;

-- 分组+条件查询
-- 需求1
select pname from product where category_id is not null;
-- 需求2
select category_id, count(*) from product 
where category_id is not null 
group by category_id;
-- 需求3
select category_id, count(*) from product 
where category_id is not null 
group by category_id
having count(*) > 1;

-- 7.分页查询
-- 需求1
select * from product limit 5;
-- 需求2
select * from product limit 4;

-- ??.topN
-- 需求1
select * from product order by price limit 3;
-- 需求2
select * from product order by price desc limit 3;

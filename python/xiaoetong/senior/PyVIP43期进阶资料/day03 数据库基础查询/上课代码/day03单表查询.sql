# 操作库的前提: 先启动mysql服务并连接它
# 操作表的前提: 先有库并使用它
create database day03;
use day03;
# 创建商品表
CREATE TABLE product
(
    pid         INT PRIMARY KEY,
    pname       VARCHAR(20),
    price       DOUBLE,
    category_id VARCHAR(32)
);
# 插入数据
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



# 查询的基本语法：
# select 和 from
# select 字段名  from 表名;
# 查询product所有的数据
# * ：代表表中全部字段
select * from product;
# 单单查商品的名称和价格
select pname,price from product;

# as:起别名
select pname as 商品名称,price as 商品价格 from product;

# 一共有多个类别？
select category_id from product;
# distinct:去重
select distinct category_id from product;


# 条件查询：where
# select 字段名  from 表名 where 条件;
# 比较运算符：> < >= <=  !=
# 查询商品价格大于2000的商品信息
# 查什么？商品信息，pid，pname，price，category_id
# 条件是啥？商品的价格大于2000
select * from product where price > 2000;
# 查询商品价格大于等于2000的商品信息
select * from product where price >= 2000;
# 查询商品价格不等于2000的商品信息
select * from product where price != 2000;

# 逻辑运算符： and:并且   or：或者  not：取反
# 查询商品价格大于等于200并且小于等于2000的商品信息
# 查什么？商品信息  *
# 条件？商品价格大于等于200并且小于等于2000   price  200-2000
select * from product where price >= 200 and price <= 2000;
# 查询商品价格等于3000或者等于5000 的商品信息
select * from product where price = 3000 or price = 5000;
# 查询商品价格不等于200的商品信息
select * from product where not (price = 200);

# 范围 查询:  between x and y: x到y的连续范围       in(x,y): x或者y
# 查询商品价格大于等于200并且小于等于等于2000的商品信息
select * from product where price between 200 and 2000;
# 查询商品价格等于3000或者等于5000 的商品信息
select * from product where price in (3000,5000);

# 模糊 查询:  like(像):模糊查询关键字   %:0个或者多个字符   _: 1个字符
# 查询商品名称以香字开头的所有商品信息
# 查什么？所有商品信息  *
# 条件？商品名称以香字开头 pname
select * from product where pname like '香%';
# 查询商品名称以香字开头并且名称三个字的商品信息
select * from product where pname like '香__';
# 查询商品名称之间包含 想 字的商品信息
select * from product where pname like '%想%';

# 空 判 断 :  is null: 判断为空    is not null: 判断不为空
insert into product values (14,'xiaomiqiche',210000,null);
# 查询没有分类的商品信息
# 没有分类：category_id is null
select * from product where category_id is null;
# 查询有分类的商品信息
# 有分类：category_id is not null
select * from product where category_id is not null;


# 排序查询：order by
# asc:升序  1234    desc:降序   4321
# 格式：select 字段名 from 表名 order by 排序的字段名 asc or desc;
# 查询所有商品信息，按照价格升序排序
select * from product order by price ;
# 不写默认就是升序
select * from product order by price asc;
# 查询所有商品信息，按照价格降序排序
select * from product order by price desc;
# 查询所有商品信息，价格也是升序排序，如果价格相同再按照分类编号去降序排序
select * from product order by price ,category_id desc;


# 聚合查询：
# 聚合查询函数:  count()数量  sum()求和   avg()平均值  max()最大值  min()最小值
# 格式：select 聚合函数 from 表名；
# 查询表product有多少条数据？
select count(pid) from product; # 14

select count(category_id) from product; # 13
# * 他不会忽略null值。也会算null
select count(*) from product;

# 查询商品价格总和  price
select sum(price) from product;

# 查询商品价格平均值
select avg(price) from product;
# 查询商品价格最贵的
select max(price) from product;
# 查询商品价格最便宜
select min(price) from product;


# 分组查询：group by
# 格式：select 分组字段名，聚合函数 from 表名 group by 分组字段名;
# 想查询每个商品分类中商品的个数
# c001 3
# c002 5
select category_id as 分类编号,count(*) as 数量 from product group by category_id;
# 查询每个商品分类商品价格总和
select category_id, sum(price) from product group by category_id;
select category_id,avg(price) from product group by category_id;
select category_id,round(avg(price),2) from product group by category_id;
select round(3.1415926,2);

# 分组查询基础+条件格式:
# select 聚合函数 from 表名 [where 非聚合条件] group by 分组字段名 [having 聚合条件];
# 查询每一个商品分类的个数
# 分析：先查询有商品分类的商品，然后再按照商品分类编号进行分组，统计每个分类的个数
select category_id,count(*)
from product
where category_id is not null
group by category_id;
# 查询每个商品分类的个数，分类不包括null，并且只显示分组商品商品个数大于1的分组信息
select category_id,count(*)
from product
where category_id is not null
group by category_id
having count(*) > 1;


# 分页查询关键字:  limit
# 分页查询基础格式: select 字段名 from 表名 limit x,y;
# 		x: 整数,代表查询的起始索引 注意: 索引默认是从0开始数
# 		y: 整数,代表查询的条数(每页展示的数量)
# 如果一个表有100w条数据，难道全部展示一个界面给你看到吗？
# 查询表中前五条数据
select * from product limit 0,4;
select * from product limit 5;

# 查询表中第二页
select * from product limit 4,4;
# 第三页
select * from product limit 8,4;

# 把作业写一下可以下课了
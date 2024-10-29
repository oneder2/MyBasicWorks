# 操作表的前提: 先创建库并使用它
create database day04;
use day04;
# 分类表
CREATE TABLE category
(
    cid   VARCHAR(32) PRIMARY KEY,
    cname VARCHAR(100) #分类名称
);
# # 商品表
CREATE TABLE products
(
    pid varchar(32) PRIMARY KEY,
    pname VARCHAR(40) ,
    price DOUBLE ,
    category_id varchar(32),
    constraint FOREIGN KEY(category_id) references category(cid)
);
# 注意: 想要使用外键约束,mysql底层需要配置成innodb存储引擎


# 演示外键约束的作用
# 限制从表的插入操作: 保证了主从表数据的一致性
insert into products values (1,'联想',9999,'c001'); # 报错:无法添加或更新子行,因为category表中没有c001记录
# 为了演示效果,向主表中插入数据,然后从表再插入查看效果
insert into category values ('c001','电脑'); # 为了演示效果,向主表中插入数据
insert into products values (1,'联想',9999,'c001'); # 插入成功,因为category表中已经有了c001记录


# 限制主表的删除操作: 保证了数据的准确性和完整性
delete from category where cid='c001'; # 报错: 无法删除或更新父行,因为从表正在引用主表的c001记录
# 就想删除主表的c001记录,怎么办?
# 可以先把从表的引用去掉(方式1:直接干掉引用的那条记录  方式2:把引用的那条记录外键值改为null)
delete from products where category_id='c001';
# 再次在主表中删除c001记录
delete from category where cid='c001'; # 删除成功,因为c001记录没有被引用了


# 准备数据
# 创建hero表
CREATE TABLE hero
(
    hid       INT PRIMARY KEY,
    hname     VARCHAR(255),
    kongfu_id INT
);

# 创建kongfu表
CREATE TABLE kongfu
(
    kid   INT PRIMARY KEY,
    kname VARCHAR(255)
);
# 插入hero数据
INSERT INTO hero VALUES(1, '鸠摩智', 9),(3, '乔峰', 1),(4, '虚竹', 4),(5, '段誉', 12);
# 插入kongfu数据
INSERT INTO kongfu VALUES(1, '降龙十八掌'),(2, '乾坤大挪移'),(3, '猴子偷桃'),(4, '天山折梅手');

# 演示内连接查询
# 需求: 查询有对应功夫的英雄,要求展示英雄名和他的功夫
# 显式内连接格式: select 字段名 from 左表 inner join 右表 on 左右表关联条件;
select hname,kname from hero inner join kongfu on hero.kongfu_id=kongfu.kid;
# 当然也可以给左右表分别起别名
select hname,kname from hero h inner join kongfu k on h.kongfu_id=k.kid;

# 隐式内连接格式: select 字段名 from 左表,右表 where 左右表关联条件;
select hname,kname from hero , kongfu where hero.kongfu_id=kongfu.kid;
# 当然也可以给左右表分别起别名
select hname,kname from hero h ,kongfu k where h.kongfu_id=k.kid;




# 演示左外连接查询
# 需求: 查询所有英雄对应的功夫,注意:没有对应功夫的用null补全
# 分析:  如果使用左外连接,左表: 英雄表
# 左外连接
select hname,kname from hero left join kongfu on hero.kongfu_id=kongfu.kid;
# 当然也可以起表名
select hname,kname from hero h left join kongfu k on h.kongfu_id=k.kid;



# 需求: 查询所有功夫,并且只展示有对应功夫的英雄
# 分析:   如果使用左外连接,左表: 功夫表
# 左外连接
select hname,kname from kongfu left join hero on hero.kongfu_id=kongfu.kid;
# 当然也可以起表名
select hname,kname from kongfu k left join hero h on h.kongfu_id=k.kid;



# 演示右外连接查询
# 需求: 查询所有英雄对应的功夫,注意:没有对应功夫的用null补全
# 分析:  如果使用右外连接,右表: 英雄表
select hname,kname from kongfu right join hero on hero.kongfu_id=kongfu.kid;
# 当然也可以起表名
select hname,kname from kongfu k right join hero h  on h.kongfu_id=k.kid;

# 需求: 查询所有功夫,并且只展示有对应功夫的英雄
# 分析:   如果使用右外连接,右表: 功夫表
select hname,kname from hero right join kongfu on hero.kongfu_id=kongfu.kid;
# 当然也可以起表名
select hname,kname from  hero h right join kongfu k on h.kongfu_id=k.kid;


# 内外连接查询实战练习
use day04;
# 由于之前已经建过category和products,并且加了外界约束
# 先删除从表
drop table if exists products;
# 再删除主表
drop table if exists category;
# 准备实战数据
CREATE TABLE category (
  cid VARCHAR(32) PRIMARY KEY ,
  cname VARCHAR(50)
);
CREATE TABLE products(
  pid VARCHAR(32) PRIMARY KEY ,
  pname VARCHAR(50),
  price INT,
  flag VARCHAR(2),    #是否上架标记为：1表示上架、0表示下架
  category_id VARCHAR(32),
  CONSTRAINT products_fk_test FOREIGN KEY (category_id) REFERENCES category (cid)
);

# 分类表插入数据
INSERT INTO category(cid,cname) VALUES('c001','家电');
INSERT INTO category(cid,cname) VALUES('c002','服饰');
INSERT INTO category(cid,cname) VALUES('c003','化妆品');
INSERT INTO category(cid,cname) VALUES('c004','奢侈品');
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


# 需求1 : 查询哪些分类的商品已经上架,	要求:只展示商品分类名称
# 分析: 先需要两表连接,再判断哪些商品已经上架,最后确定展示的结果
select distinct cname
from category c
         inner join products p on c.cid = p.category_id
where p.flag=1;

# 需求2: 查询各个分类的商品个数,	要求:展示各商品分类名称和对应个数
# 分析: 先需求两表连接,再根据分类名称分组,最后统计个数
select cname,count(*)
from category c
         inner join products p on c.cid = p.category_id
group by cname;


# 需求3: 查询各个分类的商品个数,	要求:展示各商品分类名称和对应个数
# 要求:所有分类都要展示出来(即使分类下没有商品也要展示0)

/*select *
from category c
         left outer join products p on c.cid = p.category_id;*/
# 最终sql语句
select cname,count(category_id)
from category c
         left outer join products p on c.cid = p.category_id
group by cname;


# 需求4: 查询化妆品分类下的所有商品详情
# 分析: 先在分类表中查询化妆品分类id,再根据这个分类id去商品表中找到对应所有商品
# 方式1: 子查询作为主查询语句的条件使用
select *
from day04.products
where category_id = (select cid from day04.category where cname = '化妆品');

# 方式2: 子查询作为主查询语句的表使用
# 显示内连接
select * from products p
    inner join (select cid,cname from day04.category where cname = '化妆品') c
    on p.category_id=c.cid;

# 隐式内连接
select * from products p, (select cid,cname from day04.category where cname = '化妆品') c
where p.category_id=c.cid;

# 需求5: 查询化妆品和家电两个分类的所有商品详情
# 分析: 先查询化妆品和家电两个分类的id,再根据分类id去商品表中查询对应的商品
# 方式1: cname使用范围查询
select *
from products
where category_id in (select cid from category where cname in ('化妆品', '家电'));

# 方式2: cname使用逻辑运算符查询
select *
from products
where category_id in (select cid from category where cname ='化妆品' or cname ='家电');





#  演示自连接查询
# 需求1: 查询河北省所有的城市
# 分析: 省市区三级都在一个表中,那么就可以使用自连接
# 子查询方式: 先查询河北省的id,再根据河北省id查询下面所有的城市
select * from areas where pid = (select id from areas where title = '河北省');
# 自连接方式: 给areas表起两个别名分别当成省表和市表使用
select * from areas sheng
                join areas shi on shi.pid=sheng.id
where sheng.title = '河北省';



# 需求2: 查询邯郸市下面所有的区县
# 子查询方式: 先查询邯郸的id,再根据邯郸id查询下面所有的区县
select * from areas where pid = (select id from areas where title = '邯郸市');
# 自连接方式: 给areas表起两个别名分别当成市表和区县表使用
select * from areas shi
                join areas xian on xian.pid=shi.id
where shi.title = '邯郸市';















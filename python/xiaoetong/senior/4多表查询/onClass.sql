use day04;
create table hero(
    hid int primary key,
    hname varchar(50),
    kongfu_id int
);

create table kongfu(
    kid int primary key,
    kname varchar(50)
);

insert into hero values(1, '鸠摩智', 9), (3, '乔峰', 1), (4, '虚竹', 4), (5, '段誉', 12);
insert into kongfu values(1, '降龙十八掌'), (2, '乾坤大挪移'), (3, '猴子偷桃'), (4, '天山折梅手');

select hname, kname 
from hero 
join kongfu 
on hero.kongfu_id = kongfu.kid;

select hname, kname from hero left join kongfu on hero.kongfu_id=kongfu.kid;
select hname, kname from hero right join kongfu on hero.kongfu_id=kongfu.kid;

-- 子链接
select cid from category 
where cname='化妆品';

select * from products 
where category_id = 'c003';

select * 
from products 
where category_id = (
    select cid 
    from category 
    where cname='化妆品'
    );

select * 
from products 
where category_id = (
    select cid 
    from category 
    where cname='化妆品'
    );

select * 
from products 
where category_id in (
    select cid 
    from category 
    where cname in('化妆品', '家电')
    );


-- 子链接
select * 
from areas 
where pid = (
    select id 
    from areas 
    where title='河北省'
    );

-- 自链接
select * 
from areas sheng 
join areas shi 
on sheng.id=shi.pid 
where sheng.title='河北省';


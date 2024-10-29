-- 题目一
-- (1)
create database db_hw2;
use db_hw2;
-- (2)
create table student(
    id int PRIMARY KEY auto_increment, -- (3)
    studid VARCHAR(20), 
    name VARCHAR(20), 
    chineseScore int, 
    enlishScore int, 
    mathScore int
    );

drop table student;

-- (4)
INSERT student VALUES(0, '20210908001', '张王明',89 ,78,90);
INSERT student VALUES(0, '20210908002', '李进', 67, 53, 95);
INSERT student VALUES(0, '20210908003', '王俊', 87, 78, 77);
INSERT student VALUES(0, '20210908004', '李云云', 80, 98, 92);
INSERT student VALUES(0, '20210908005', '谢来财', 82, 84, 67);
INSERT student VALUES(0, '20210908006', '张进宝', 55, 85, 89);
INSERT student VALUES(0, '20210908007', '黄蓉儿', 79, 86, 90);
INSERT student VALUES(0, '20210908008', '刘小雪', 71, 90, 91);
INSERT student VALUES(0, '20210908009', '夏金章', 89, 91, 96);
INSERT student VALUES(0, '20210908010', '杨洋', 83, 65, 90);

-- (5)
update student
set chineseScore = 88
where id = 4;

-- (6)
delete from student
where id = 10;

-- 题目二
-- (1)
select * from student;

-- (2)
select name, enlishScore from student;

-- (3)
select distinct chineseScore from student;

-- (4)
select chineseScore + enlishScore + mathScore from student;

-- (5)
select chineseScore + enlishScore + mathScore + 10 from student;

-- (6)
select name from student where enlishScore > 90;

-- (7)
select name from student where chineseScore + enlishScore + mathScore > 200;

-- (8)
select name from student where 80 < enlishScore and enlishScore < 90;

-- (9)
select name from student where not (80 < enlishScore and enlishScore < 90);

-- (10)
select name from student where mathScore in(89,90,91);

-- (11)
select enlishScore from student where name like("李%");

-- (12)
select name from student where mathScore = 80 and chineseScore = 80;

-- (13)
select name from student where enlishScore = 80 or enlishScore + chineseScore + mathScore = 200;


-- 题目三
create database db_hw3;
use db_hw3;

CREATE TABLE emp(
empno INT,
ename VARCHAR(50),
job VARCHAR(50), 
mgr INT, -- 上级领导编号
hiredate DATE,-- 入职日期
sal INT,
comm INT, -- 奖金
deptno INT -- 部门编号
) ;

INSERT INTO emp VALUES
(7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20),
(7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600,300,30),
(7521,'WARD','SALESMAN',7698,'1981-02-22',1250,500,30),
(7566,'JONES','MANAGER',7839,'1981-04-02',2975,NULL,20),
(7654,'MARTIN','SALESMAN',7698,'1981-09-28',1250,1400,30),
(7698,'BLAKE','MANAGER',7839,'1981-05-01',2850,NULL,30),
(7782,'CLARK','MANAGER',7839,'1981-06-09',2450,NULL,10),
(7788,'SCOTT','ANALYST',7566,'1987-04-19',3000,NULL,20),
(7839,'KING','PRESIDENT',NULL,'1981-11-17',5000,NULL,10),
(7844,'TURNER','SALESMAN',7698,'1981-09-08',1500,0,30),
(7876,'ADAMS','CLERK',7788,'1987-05-23',1100,NULL,20),
(7900,'JAMES','CLERK',7698,'1981-12-03',950,NULL,30),
(7902,'FORD','ANALYST',7566,'1981-12-03',3000,NULL,20),
(7934,'MILLER','CLERK',7782,'1982-01-23',1300,NULL,10);

-- 1
select * 
from emp 
where deptno != 10
order by empno ;

-- 2 为什么会涉及到判空处理，没搞明白
select *
from emp
where ename not like("_A%") and sal > 800
order by sal desc;

-- 3
select avg(sal), deptno
from emp
group by deptno;

-- 4
select max(sal), deptno
from emp
group by deptno;

-- 5
select job, deptno, avg(sal)
from emp
group by job, deptno
order by deptno, job;

-- 6
select deptno
from emp
group by deptno
having avg(sal) > 2000;

-- 7
select avg(sal), deptno
from emp
group by deptno
having avg(sal) > 1500
order by avg(sal);






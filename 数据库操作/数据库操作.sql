# 在users表中查询注册时间最早的十条会员信息
select * from users order by cdate limit 10;

# 从两个表中查询点赞数最高的5条博客信息，要求显示字段：
#   （博文id，标题，点赞数，会员名）
select b.id,b.title,b.pcount,u.name from users u right join blog b on u.id = b.uid order by b.pcount desc limit 5;

# 统计每个会员的发表博文数量（降序），要求显示字段（会员id号，姓名，博文数量）
select u.id,u.name,count(b.title) num from users u left join blog b on u.id = b.uid group by u.id order by num desc;

# 获取会员的博文平均点赞数量最高的三位。显示字段（会员id，姓名，平均点赞数）
select u.id,u.name,avg(b.pcount) pavg from users u left join blog b on u.id = b.uid group by u.id order by pavg desc limit 3;

# 删除没有发表博文的所有会员信息
#(可以对查询的中间结果的表取别名并结合in来实现从原表中删除子查询的结果)
delete from users where id in (select e.id from (select u.id,count(b.title) num from users u left join blog b on u.id = b.uid group by u.id) e where e.num=0);
# 数据库操作
# 数据库修改操作（事务型）
# 修改操作一般是基于主键进行的
# 后面就可以封装成为一个数据库修改函数

# 导入MySql包
import pymysql

# 生成数据库对象，获取数据库连接
db = pymysql.connect(host='localhost',user='root',password='',db='mydb',charset='utf8')

# 生成游标对象
cursor = db.cursor()

# 数据库操作
# 定义sql语句
data = ('uu200',25,'m','python04',16)
sql = "update stu set name='%s',age='%d',sex='%s',classid='%s' where id = '%d'"%(data)

# 操作数据库
try :
	# 执行sql，并记录影响行数
	n = cursor.execute(sql)
	# 事务提交,pymysql对数据库的增删改操作是基于事务的，它不会自动提交需要使用commit
	db.commit()
	# 使用cursor.rowcout属性来获取影响条数
	#print(f'成功修改{cursor.rowcount}条')
	print(f'成功修改{n}条数据')
except Exception as err :
	print('SQL执行错误',err)
	db.rollback()


# 关闭数据库对象，关闭数据库对象
db.close()
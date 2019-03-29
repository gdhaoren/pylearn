# 将redis中的数据信息导入mysql
import pymysql
import redis
import json

def main():
	# 连接redis获取数据
	rediscl = redis.StrictRedis(host='localhost',port=6379,db=0)
	# 连接mysql
	mysql = pymysql.Connect(host='localhost',user='root',password='',db='db_book',charset='utf8')
	# 创建游标对象
	cursor = mysql.cursor()
	# 监控数据库内的数据，只要出现就保存出来
	while True:
		# 采用先进先出FIFO的方法
		source,data = rediscl.blpop('book_slaver:items')
		print(source)
		# 数据入库
		try:
			item = json.loads(data)
			# 组装sql语句
			# 数据字典化
			item_dict = dict(item)
			# 获取数据的key，并拼装成一个字符串
			keys = ','.join(item_dict.keys())
			# 拼装传入参数的语句,根据字典长度计算参数个数
			values = ','.join(['%s']*len(item_dict))
			# 生成sql语句
			sql = f'insert into books({keys}) values({values})'
			# 指定参数并执行添加操作
			cursor.execute(sql,tuple(item_dict.values()))
			# 事物提交
			mysql.commit()
			print('数据写入成功')
		except Exception as err:
			# 事物回滚
			mysql.rollback()
			print('SQL执行错误,原因： ',err)


if __name__ == '__main__':
	main()
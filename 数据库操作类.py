import pymysql

class db_operate() :
	def __init__(self,host,user,password,db,charset):
		self.__db = pymysql.connect(host=host,user=user,password=password,db=db,charset=charset)
		self.__cursor = self.__db.cursor()
# sql语句中需要有'' 那必须要在外面打上'' ，对于数值型不需要''则可打可不打，以保证最后的字符串和mysql中的执行语句一致，注意字符型变量的''是不会通过变量带过来的
	def db_update(self,table,data,sid):
		sql = f"update {table} set name='{data[0]}',age={data[1]},sex='{data[2]}',classid='{data[3]}' where id={sid}"
		try :	
			n = self.__cursor.execute(sql)
			self.__db.commit()
			print(f'成功修改{n}条数据')
		except Exception as err :
			print(f'SQL执行错误',err)
			self.__db.rollback()

	def db_insert(self,table,data):
		sql = f"insert into {table}(name,age,sex,classid) values('{data[0]}',{data[1]},'{data[2]}','{data[3]}')"
		try :	
			n = self.__cursor.execute(sql)
			self.__db.commit()
			print(f'成功插入{n}条数据')
		except Exception as err :
			print(f'SQL执行错误',err)
			self.__db.rollback()

	def db_delete(self,table,data) :
		sql = f"delete from {table} where id={data}"
		try :	
			n = self.__cursor.execute(sql)
			self.__db.commit()
			print(f'成功删除{n}条数据')
		except Exception as err :
			print(f'SQL执行错误',err)
			self.__db.rollback()

	def __del__(self):
		self.__db.close()

if __name__ == '__main__':
	'''
# 数据添加

	db = db_operate('localhost','root','','mydb','utf8')
	data = ('123',19,'m','python08')
	table = 'stu'
	db.db_insert(table,data)

# 数据修改

	db = db_operate('localhost','root','','mydb','utf8')
	sid = 14
	data = ('uu12',28,'m','python04')
	table = 'stu'
	db.db_update(table,data,sid)
	'''

# 数据删除
	db = db_operate('localhost','root','','mydb','utf8')
	sid = 14
	table = 'stu'
	db.db_delete(table,sid)
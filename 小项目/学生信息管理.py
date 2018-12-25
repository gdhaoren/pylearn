import pymysql
 
class stu_operate:
	'''stu数据库操作类'''
	def __init__(self,host,user,password,db,charset):
		'''链接数据库'''
		self.__db = pymysql.connect(host=host,user=user,password=password,db=db,charset=charset)
		self.__cursor = self.__db.cursor()

	def findAll(self) :
		'''查看学生信息'''
		sql = 'select * from stu'
		try :
			self.__cursor.execute(sql)
			stu_data = self.__cursor.fetchall()
			if stu_data :
				for stu in stu_data:
					print(stu)
			else :
				print('没有学生信息')
		except Exception as err :
			print('SQL执行错误',err)

	def delete(self,id) :
		'''删除学生信息'''
		n = 0
		try :
			for i in id :
				sql = f'delete from stu where id = {i}'
				n += self.__cursor.execute(sql)
				self.__db.commit()
			print(f'成功删除{n}条数据')
		except Exception as err :
			print('SQL执行错误',err)
			self.__db.rollback()

	def insert(self,data) :
		'''添加学生信息'''
		n = 0
		try :
			for info in data :
				sql = f"insert into stu(name,age,classid) values('{info[0]}','{info[1]}','{info[2]}')"
				n += self.__cursor.execute(sql)
				self.__db.commit()
			print(f'成功添加{n}条数据')
		except Exception as err :
			print('SQL执行错误',err)
			self.__db.rollback()

	def __del__(self) :
		'''关闭数据库连接'''
		self.__db.close()

if __name__ == '__main__' :
	stu_operate = stu_operate('localhost','root','','studb','utf8')
	while True:
		# 输出初始界面
		print("="*12,"学员管理系统","="*14)
		print("{0:1} {1:13} {2:15}".format(" ","1. 查看学员信息","2. 添加学员信息"))
		print("{0:1} {1:13} {2:15}".format(" ","3. 删除学员信息","4. 退出系统"))
		print("="*40)
		key = input("请输入对应的选择：")
		# 根据键盘值，判断并执行对应的操作
		if key == "1":
			print("="*12,"学员信息浏览","="*14)
			stu_operate.findAll()
			input("按回车键继续：")
		elif key == "2":
			print("="*12,"学员信息添加","="*14)
			stulist=[]
			while True:
				name=input("请输入要添加的姓名：")
				age=input("请输入要添加的年龄：")
				classid=input("请输入要添加的班级号：")
				stulist.append([name,age,classid])
				press=input('按n键继续添加学生信息：')
				if press != 'n':
					break
			stu_operate.insert(stulist)
			stu_operate.findAll()
			input("按回车键继续：")
		elif key == "3":
			print("="*12,"学员信息删除","="*14)
			stu_operate.findAll()
			sid_list=[]
			sid = input("请输入你要删除的信息id号，多个id以空格分割：\n")
			sid = sid.split()
			sid_list = [int(x) for x in sid]
			stu_operate.delete(sid_list)
			stu_operate.findAll()
			input("按回车键继续：")
		elif key == "4":
			print("="*12,"再见","="*14)
			break
		else:
			print("======== 无效的键盘输入！ ==========")
	

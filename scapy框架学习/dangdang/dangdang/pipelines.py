# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re
from scrapy import Request
from scrapy.pipelines.images  import ImagesPipeline
class DataCleanPipeline(object):
	def process_item(self,item,spider):
		# 数据清理
		# 去掉空格
		for key in item:
			if item[key]:
				item[key] = item[key].strip()
		# 去掉价格前面的修饰
		item['price'] = re.findall(r'¥([0-9\.]+)',item['price'])[0]
		#print(item['price'])
		return item

class ImagePipeline(ImagesPipeline):
	# 下载图片
	# 生成图片下载请求
	def get_media_requests(self,item,info):
		'''通过抓取的item对象获取图片信息，并创建Request请求对象添加调度队列，等待调度执行下载'''
		yield Request(item['imgsrc'])

	def file_path(self,request,response=None,info=None):
		'''返回图片下载后保存的名称，没有此方法Scrapy则自动给一个唯一值作为图片名称'''
		url = request.url
		file_name = url.split("/")[-1]
		return file_name

	def item_completed(self, results, item, info):
		''' 下载完成后的处理方法，其中results内容结构如下说明'''
		# image_paths = [x['path'] for ok, x in results if ok]
		# if not image_paths:
		# 	raise DropItem("Item contains no images")
		#item['image_paths'] = image_paths
		return item


class MysqlPipeline(object):
	# 初始化类需要的参数
	def __init__(self,host,user,password,database,port):
		self.host = host
		self.user = user
		self.password = password
		self.database = database
		self.port = port

	# 设置从settings配置文件获取参数
	@classmethod
	def from_crawler(cls,crawler):
		return cls(	
			host = crawler.settings.get("MYSQL_HOST"),
			user = crawler.settings.get("MYSQL_USER"),
			password = crawler.settings.get("MYSQL_PASS"),
			database = crawler.settings.get("MYSQL_DATABASE"),
			port = crawler.settings.get("MYSQL_PORT")
			)

	def process_item(self, item, spider):
		# 数据入库

		# item数据字典化
		data = dict(item)
		#print(data)
		keys = ','.join(data.keys())
		#print(len(data.keys()))
		#print(keys)
		values = ','.join(['%s']*len(data))
		#print(len(data.values()))
		#print(values)
		sql = f'insert into {item.table}({keys}) values({values})'
		#print(data.values())
		# 参数实例化
		# 一定要将data.values()转化为元祖才能赋值
		#print(data.values())
		#print(keys)
		#print(sql)
		self.cursor.execute(sql,tuple(data.values()))
		# data = dict(item)
		# keys = ','.join(data.keys())
		# values=','.join(['%s']*len(data))
		# sql = "insert into %s(%s) values(%s)"%(item.table,keys,values)
		# print(sql)
		#指定参数，并执行sql添加
		#self.cursor.execute(sql,tuple(data.values()))
		# 事务提交
		self.db.commit()
		return item

	def open_spider(self,spider):
		# 连接数据库
		self.db = pymysql.connect(self.host,self.user,self.password,self.database,charset='utf8',port=self.port)
		# 生成数据库操作器
		self.cursor = self.db.cursor()

	def close_spider(self,spider):
		# 关闭数据库
		self.db.close()
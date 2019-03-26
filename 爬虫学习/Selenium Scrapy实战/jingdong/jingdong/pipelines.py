# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class JdMongoPipeline(object):
	def __init__(self,mongo_uri,mongo_db):
		'''获取数据库信息'''
		self.mongo_db = mongo_db
		self.mongo_uri = mongo_uri

	# 数据注入
	@classmethod
	def from_crawler(cls,crawler):
		return cls(mongo_uri=crawler.settings.get('MONGO_URI'),mongo_db=crawler.settings.get('MONGO_DB'))

	def open_spider(self,spider):
		'''连接数据库'''
		self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]

	def process_item(self, item, spider):
		'''存储数据'''
		self.db[item.collection].insert(dict(item))
		return item

	def close_spider(self,spider):
		'''关闭数据库'''
		self.client.close()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis,re

class DbMasterPipeline(object):
	def __init__(self,host,port):
		'''连接redis数据库'''
		self.r = redis.Redis(host=host,port=port,decode_responses=True)

	@classmethod
	def from_crawler(cls,crawler):
		'''注入参数'''
		return cls(host=crawler.settings.get('REDIS_HOST'),port=crawler.settings.get('REDIS_PORT'))


	def process_item(self, item, spider):
		# 获取图书编号,使用findall 不要使用search只是匹配
		bookid = re.findall('https://book.douban.com/subject/([0-9]+)/',item['url'])
		# 如果能获取到图书编号说明url地址合法
		if bookid:
			# 使用图书编号去重
			if self.r.sadd('books:id',bookid[0]):
				self.r.lpush('books:start_urls',item['url'])
		# 如果不能获取到图书id，则把url存出来看看是出现了什么错误
		else:
			self.r.lpush('books:no_urls',item['url'])

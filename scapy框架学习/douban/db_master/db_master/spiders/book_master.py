# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import redis
from scrapy import Request
from db_master.items import DbMasterItem
from urllib.parse import quote

class BookMasterSpider(CrawlSpider):
	name = 'book_master'
	allowed_domains = ['book.douban.com']
	item = DbMasterItem()
	base_url = 'https://book.douban.com'

	def start_requests(self):
		'''从redis中获取对应标签的url来提取数据链接'''
		# 数据name
		name = 'book:tag_urls'
		r = redis.Redis(host=self.settings.get('REDIS_HOST'),port=self.settings.get('REDIS_PORT'))
		# 如果数据库中存在待爬取的url则执行爬取，直到全部爬完
		while r.llen(name):
			tag = r.rpop(name)
			# 注意url的拼装，存在格式的问题
			url = self.base_url + quote(tag)
			yield Request(url=url,callback=self.tag_parse,dont_filter=True)

	def tag_parse(self, response):
		# 获取当前页面中所有书籍的url地址
		urllist = response.css('div.info h2 a::attr(href)').extract()
		if urllist:
			for url in urllist:
				self.item['url'] = url
				yield self.item

		# 获取下一页的url地址继续解析
		next_page = response.css('span.next a::attr(href)').extract_first()
		# 判断是否是最后一页
		if next_page:
			# 注意url的拼装，存在格式的问题
			url = response.urljoin(next_page)
			#print(url)
			# 要想持续获得下一页数据进行解析 要使用yield 使用return直接就一轮就跳出了
			yield Request(url=url,callback=self.tag_parse)


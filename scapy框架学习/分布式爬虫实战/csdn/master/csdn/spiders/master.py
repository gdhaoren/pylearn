# -*- coding: utf-8 -*-
from csdn.items import UrlItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

# 更改主爬虫的父类，
class CourseSpider(CrawlSpider):
	# 更改主爬虫的名字 方便区分
	name = 'master'
	allowed_domains = ['edu.csdn.net']
	start_urls = ['https://edu.csdn.net/courses/k']
	item = UrlItem()

	# 从初始访问页面中抽取子url地址,使用正则的方式提取
	# 从初始访问页面中爬取更多的url地址信息
	rules = (Rule(LinkExtractor(allow=('https://edu.csdn.net/courses/k/p[0-9]+',)),callback='parse_item',follow=True),)
	def parse_item(self, response):
		dlist = response.css("div.course_item")
		for d in dlist:
			item = self.item
			item['url'] = d.css("a::attr(href)").extract_first()
			yield item
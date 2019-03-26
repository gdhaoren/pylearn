# -*- coding: utf-8 -*-
import scrapy
from csdn.items import CourseItem
from scrapy_redis.spiders import RedisSpider

# 更换爬虫的父类，从而实现url地址从redis数据库中获取
class CourseSpider(RedisSpider):
	name = 'course'
	# 确定redis数据库中取url地址的key，slave连接到redis调度库
	redis_key = 'coursespider:start_urls'

	def __init__(self, *args, **kwargs):
		# 初始化对象并自动确定domain
		domain = kwargs.pop('domain', '')
		self.allowed_domains = filter(None, domain.split(','))
		super(CourseSpider, self).__init__(*args, **kwargs)

	def parse(self, response):
		'''爬虫处理'''
		item = CourseItem()
		item['title'] = response.css("div.container div.pr div.info_right h1::text").extract_first()
		item['num'] = response.css("div.course_status span::text").extract_first()
		item['price'] = response.css("div.sale div.price_wrap sapn.money::text").extract_first()
		item['teacher'] = response.xpath("//div[@class='professor_name']/a/text()").extract_first()
		item['course'] = ','.join(response.css("div.J_outline_content dl dt.clearfix span::text").extract()).replace(" ", '')
		return item

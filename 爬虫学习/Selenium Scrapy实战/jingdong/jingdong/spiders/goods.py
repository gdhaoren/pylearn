# -*- coding: utf-8 -*-
import scrapy
from jingdong.items import JingdongItem

class GoodsSpider(scrapy.Spider):
	name = 'goods'
	allowed_domains = ['www.jd.com']
	base_url = 'https://list.jd.com/list.html?cat=670,671,672'

	# 生成请求
	def start_requests(self):
		for page in range(1,self.settings.get('MAX_PAGE')+1):
			# 每次分页其实都是访问的首页，然后把page值传过去，在selenium中使用页面跳转框跳转加载页面后提取数据
			url = self.base_url
			yield scrapy.Request(url=url,callback=self.parse,meta={'page':page},dont_filter=True)

	def parse(self, response):
		# css解析还是要多看看
		lilist = response.css('div#plist ul li')
		for li in lilist:
			item = JingdongItem()
			item['name'] = li.css('div.p-name a em::text').extract_first()
			item['price'] = li.css('div.p-price strong i::text').extract_first()
			item['shop'] = li.css('div.p-shop a::text').extract_first()
			yield item

        

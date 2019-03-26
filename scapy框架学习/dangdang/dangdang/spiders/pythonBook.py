# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem


class PythonbookSpider(scrapy.Spider):
	name = 'pythonBook'
	allowed_domains = ['www.dangdang.com']
	start_urls = ['http://search.dangdang.com/?key=python&act=input']

	def parse(self, response):
		page_index = 1
		for i in range(1,61,1):
			item = DangdangItem()
			li = response.selector.css(f'li.line{i}')
			item['title'] = li.css('p.name a::attr(title)').extract_first()
			item['bookurl'] = li.css('p.name a::attr(href)').extract_first()
			item['detail'] = li.css('p.detail::text').extract_first()
			item['price'] = li.css('span.search_now_price::text').extract_first()
			item['author'] = li.css('a[name="itemlist-author"]::attr(title)').extract_first()
			item['press'] = li.css("a[name='P_cbs']::attr(title)").extract_first()
			item['imgsrc'] = li.css('a.pic img::attr(data-original)').extract_first()
			item['bid'] = li.xpath('./@id').extract_first()
			#print(item)
			#print(len(item))
			yield item
		if page_index < 3:
			page_index += 1
			next_url = f'http://search.dangdang.com/?key=python&act=input&page_index={page_index}'
			yield scrapy.Request(url=next_url,callback=self.parse)

    		

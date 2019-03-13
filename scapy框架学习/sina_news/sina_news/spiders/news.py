# -*- coding: utf-8 -*-
import scrapy
from sina_news.items import SinaNewsItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide']

    def parse(self, response):
    	# 自动回调处理响应
    	# 获取新浪新闻页面
        htmllist = response.css('div.section')
        for html in htmllist:
        	# 初始化三级标题的存储
        	l3list = []
        	item = SinaNewsItem()
        	print('#'*40)
        	# 一级标题
        	item['level1'] = html.css('h2.tit01::text').extract()
        	print(html.css('h2.tit01::text').extract())
        	# 二级标题
        	item['level2'] = html.css('h3.tit02 a::text').extract()
        	print(html.css('h3.tit02 a::text').extract())
        	# 三级标题
        	divlist = html.css('div.clearfix')
        	for div in divlist:
        		url = div.css('ul.list01 li a::attr(href)').extract()
        		#print(url)
        		title = div.css('ul.list01 li a::text').extract()
        		#print(title)
        		dic = dict(zip(title,url))
        		l3list.append(dic)
        	item['level3'] = l3list
        	#print(l3list)
        	# 注意生成一个item就yeild一次 不要把yeild写错位置了
        	yield item


# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from db_slaver.items import BookItems
import re

class BookSlaverSpider(RedisSpider):
    name = 'book_slaver'
    redis_key = 'books:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(BookSlaverSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
    	item = BookItems()
    	html = response.css('#wrapper')
    	# id号
    	item['id'] = html.re_first('id="collect_form_([0-9]+)"')
    	# 书名
    	item['title'] = html.css('h1 span::text').extract_first()

    	# 从info中获取其余信息
    	info = html.css('#info').extract_first()
    	authors = re.search('<span.*?作者.*?</span>(.*?)<br.?>',info,re.S).group(1)
    	item['author'] = "、".join(re.findall('<a.*?>(.*?)</a>',authors,re.S))
    	item['press'] = ' '.join(re.findall('<span.*?出版社:</span>\s*(.*?)<br.?>',info,re.S))
    	item['original'] = ' '.join(re.findall('<span.*?原作名:</span>\s*(.*?)<br.?>',info,re.S))
    	trans = re.search('<span.*?译者.*?</span>(.*?)<br.?>',info,re.S)
    	if trans:
    		item['translator'] = '、'.join(re.findall('<a.*?>(.*?)</a>',trans.group(1),re.S))
    	else:
    		item['translator'] = ''
    	item['year'] = re.search('<span.*?出版年:</span>\s*(.*?)<br.?>',info).group(1)
    	item['pages'] = re.search('<span.*?页数:</span>\s*([0-9]+)<br.?>',info).group(1)
    	item['price'] = re.search('<span.*?定价:</span>.*?([0-9\.]+)元?<br.?>',info).group(1)
    	item['binding'] = ' '.join(re.findall('<span.*?装帧:</span>\s*(.*?)<br.?>',info))
    	item['series'] = ' '.join(re.findall('<span.*?丛书:</span>.*?<a .*?>(.*?)</a><br.?>',info))
    	item['isbn'] = re.search('<span.*?ISBN:</span>\s*([0-9]+)<br.?>',info).group(1)

    	item['score'] = html.css('strong.rating_num::text').extract_first().strip()
    	item['number'] = html.css('a.rating_people span::text').extract_first()
    	#print(item)
    	yield item

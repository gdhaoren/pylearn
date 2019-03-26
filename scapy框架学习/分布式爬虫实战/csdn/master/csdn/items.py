# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UrlItem(scrapy.Item):
    # 主爬虫是用来生成url队列的
    url = scrapy.Field()

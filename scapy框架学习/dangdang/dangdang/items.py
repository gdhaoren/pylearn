# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    table = 'bookinfo'
    bid = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    author = scrapy.Field()
    detail = scrapy.Field()
    bookurl = scrapy.Field()
    press = scrapy.Field()
    imgsrc = scrapy.Field()
    

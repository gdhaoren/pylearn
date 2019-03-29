# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItems(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    press = scrapy.Field()
    original = scrapy.Field()
    translator = scrapy.Field()
    year = scrapy.Field()
    pages = scrapy.Field()
    price = scrapy.Field()
    binding = scrapy.Field()
    series = scrapy.Field()
    isbn = scrapy.Field()
    score = scrapy.Field()
    number = scrapy.Field()
    

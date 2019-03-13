# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaNewsItem(scrapy.Item):
    # define the fields for your item here like:
    level1 = scrapy.Field()
    level2 = scrapy.Field()
    level3 = scrapy.Field()
    

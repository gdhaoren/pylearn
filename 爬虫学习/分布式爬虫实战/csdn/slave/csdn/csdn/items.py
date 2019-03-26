# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    # 课时
    time = scrapy.Field()
    # 讲师
    teacher = scrapy.Field()
    # 适合人群
    crowd = scrapy.Field()
    # 学习人数
    num = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 课程大纲
    course = scrapy.Field()

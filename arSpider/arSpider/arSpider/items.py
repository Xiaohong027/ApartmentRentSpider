# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BisheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    # flag = scrapy.Field()
    region = scrapy.Field()
    # source = scrapy.Field()
    price = scrapy.Field()
    content = scrapy.Field()
    direction = scrapy.Field()
    phone = scrapy.Field()
    lon = scrapy.Field() #经度
    lat = scrapy.Field() #维度


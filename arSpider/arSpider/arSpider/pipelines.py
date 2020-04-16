# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from settings import MONGODB_SERVER, MONGODB_PORT

class BishePipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
        self.bishe = self.client['bishe']
        self.ty = self.bishe['ty']

    def process_item(self, item, spider):
        data = {
            'url': item['url'],
            'title': item['title'],
            'info': item['info'],
            'flag': 1,
            'region': item['region'],
            'source': 'anjuke',
            'price': item['price'],
            'content': item['content'],
            'direction': item['direction'],
            'phone': item['phone'],
            # 'lon': item['lon'],
            # 'lat': item['lat']
        }
        self.ty.insert(data)
        return item

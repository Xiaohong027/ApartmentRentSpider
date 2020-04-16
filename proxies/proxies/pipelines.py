# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from proxies.settings import MONGODB_SERVER,MONGODB_PORT

class ProxiesPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
        self.proxies = self.client['proxies']
        self.version1 = self.proxies['version1']

    def process_item(self, item, spider):
        data = {
            'address': item['address'],
            'flag': 1
        }
        self.version1.insert(data)
        return item

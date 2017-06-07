# -*- coding: utf-8 -*-
from pymongo import MongoClient
from .items import ShopsItem,CommentItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
client = MongoClient('127.0.0.1',27017)
db = client['耶里夏丽']

class ShopsPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,ShopsItem):
            collection = db['shops']
            collection.save(dict(item))

class CommentPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CommentItem):
            # name = item['name']
            collection = db['4星']
            collection.save(dict(item))
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
class Homework2Pipeline(object):
    client = MongoClient()
    db = client.spider
    collection = db.spiders_001
    def process_item(self, item, spider):
        print(item)
        self.collection.insert_one(item)
        return item
    

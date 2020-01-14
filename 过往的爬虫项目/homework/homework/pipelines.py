# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from dateutil import parser
from pymongo import MongoClient


class HomeworkPipeline(object):
    def open_spider(self, spider):
        client = MongoClient()
        db = client.spider
        self.collection = db.spider_1

    def process_item(self, item, spider):
        print('1kill!')
        classify = item['classify']
        region = item['region']
        title = item['title']
        herf = item['herf']
        datetime = item['datetime']
        self.collection.insert({
            'classify': classify,
            'region': region,
            'title': title,
            'herf': herf,
            'datetime': parser.parse(datetime)
        })
        return item

    def close_spider(self, spider):
        for i in self.collection.find():
            print(i)

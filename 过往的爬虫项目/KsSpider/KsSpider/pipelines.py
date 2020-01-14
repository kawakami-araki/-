# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pymongo import MongoClient

class KsspiderPipeline(object):
    def __init__(self):
        self.connect = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            db="scrapy",  # 数据库名
            user="root",  # 数据库用户名 
            passwd="000000",  # 密码
            charset="utf8")
        self.cursor = self.connect.cursor()
        client = MongoClient()
        db = client.spider
        self.table = db.kaoshi
        self.file = open('./KsSpider/白居易.txt', 'w', encoding='utf-8')



    def process_item(self, item, spider):
        title = item['title']
        author = item['author']
        content = item['content']
        print(item)
        # 存储txt文件 
        if title:
            self.file.write(title)
            for i in author:
                self.file.write(i)
            for i in content:
                self.file.write(i)

            # 存储mongodb
            self.table.insert(item)

        # 存储mysqldb
        pass

    def close_spider(self, spider):
        # 关闭游标和连接
        # self.cursor.close()
        # self.connect.close()
        self.file.close()
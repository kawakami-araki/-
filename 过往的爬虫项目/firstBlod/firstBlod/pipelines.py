# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pymongo import MongoClient
from redis import Redis
import csv

class FirstblodPipeline(object):
    fp = None
    # 设定在管道运行开始之前优先运行的代码
    def open_spider(self, spider):
        print('爬虫1开始运行~~~~~~~')
        # 通过在管道运行开始之前打开文件的形式来确保这个文件每次只需要打开一次
        with open('data.csv', 'w', encoding='utf-8') as csvf:
            # 构建csv文件基础属性,内容的分隔符
            writer = csv.writer(csvf,delimiter=',')
            # 写入文件,传入的参数是一个列表
            # writer.writerow(['Job_title', 'Corporate_name','address','experience','Education'])
            writer.writerow(['Job_title', 'Corporate_name'])

        self.fp = open('data.csv', 'a', encoding='utf-8')

    # 当数据被提交时执行的代码,在这里进行数据持久化存储
    def process_item(self, item, spider):
        Job_title = item['Job_title']
        Corporate_name = item['Corporate_name']
        # address = item['address']
        # experience = item['experience']
        # Education = item['Education']
        # self.fp.writerow([Job_title,Corporate_name,address,experience,Education])
        self.fp.writerow([Job_title,Corporate_name])
        # 调用已经打开的文件,并在里面进行写入操作
        print('写入完成')
        return item
    # 当管道关闭时执行的代码
    def close_spider(self, spider):
        print('爬虫1结束运行~~~~~~~')
        # 在代码整体运行结束的时候,关闭打开的文件
        self.fp.close()

class MysqlPip(object):
    conn = None
    cursor = None

    # 设定在管道运行开始之前优先运行的代码
    def open_spider(self, spider):
        # 通过在管道运行开始之前打开文件的形式来确保这个文件每次只需要打开一次
        print('爬虫2开始运行~~~~~~~')
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='000000',db='spider',charset='utf8')
        print(self.conn)
    # 当数据被提交时执行的代码,在这里进行数据持久化存储
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        sql = 'insert into bs values ("%s","%s")'% (author,content)
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self, spider):
        print('爬虫2结束运行~~~~~~~')
        self.cursor.close()
        self.conn.close()

class RedisPip(object):
    conn = None
    cursor = None

    # 设定在管道运行开始之前优先运行的代码
    def open_spider(self, spider):
        # 通过在管道运行开始之前打开文件的形式来确保这个文件每次只需要打开一次
        print('爬虫3开始运行~~~~~~~')
        self.conn = Redis()
    # 当数据被提交时执行的代码,在这里进行数据持久化存储
    def process_item(self, item, spider):
        self.conn.lpush('all_data',item)
        return item
    def close_spider(self, spider):
        print('爬虫3结束运行~~~~~~~')
        # print(self.conn.rpoplpush('all_data','all_data'))

class MongoPip(object):
    conn = None

    # 设定在管道运行开始之前优先运行的代码
    def open_spider(self, spider):
        # 通过在管道运行开始之前打开文件的形式来确保这个文件每次只需要打开一次
        print('爬虫4开始运行~~~~~~~')
        conn = MongoClient()
        db = conn.local
        self.collection = db.spider
        print(self.collection)
    # 当数据被提交时执行的代码,在这里进行数据持久化存储
    def process_item(self, item, spider):
        self.collection.insert({'author': item['author'],'content': item['content']})
        print('插入成功')
        return item
    def close_spider(self, spider):
        print('爬虫4结束运行~~~~~~~')
        for item in self.collection.find():
            print(item)
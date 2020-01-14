# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline

class ManhuaPipeline(object):
    client = MongoClient()
    db = client.spider
    table = db.spiders_003
    def process_item(self, item, spider):
        self.table.insert(item)
        print(item['book_name'], '已存入数据库')
        return item

class ImgSpidersPipeline(ImagesPipeline):
    
    # 对一个图片链接进行请求发送
    # item 就是scrapy提交过来的item数据
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    # 准备文件名
    def file_path(self, request, response=None, info=None):
        file_name = request.url.split('/')[-1]
        print('图片正在下载',file_name,'............')
        return file_name
    # 将item传递给下一个即将执行的管道类
    def item_completed(self, results, item, info):
        return item
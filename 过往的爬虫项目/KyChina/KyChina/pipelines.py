# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
class KychinaPipeline(object):
    client = MongoClient()
    db = client.spider
    table = db.spiders_002
    def process_item(self, item, spider):
        print(item)
        self.table.insert(item)
        return item



import scrapy
from scrapy.pipelines.images import ImagesPipeline
from .settings import IMAGES_STORE
class ImgSpidersPipeline(ImagesPipeline):
    file_path_name = ''
    # 对一个图片链接进行请求发送
    # item 就是scrapy提交过来的item数据
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    # 准备文件名
    def file_path(self, request, response=None, info=None):
        self.file_name = request.url.split('/')[-1]
        self.file_path_name = IMAGES_STORE + self.file_name
        print('正在下载', self.file_name,'............')
        return self.file_name
    # 将item传递给下一个即将执行的管道类
    def item_completed(self, results, item, info):
        print('存放位置', self.file_path_name)
        return item
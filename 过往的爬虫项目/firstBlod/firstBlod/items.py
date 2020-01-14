# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstblodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 构建新的item对象中的参数
    # 格式为    name = scrapy.Field()
    # 使用field文件格式的时候,兼容几乎所有的文件类型
    # 包括但不仅限于   列表,元组,字典,字符串,数字,二进制流等各种各样的形式
    author = scrapy.Field()
    content = scrapy.Field()

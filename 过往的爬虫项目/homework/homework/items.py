# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    classify = scrapy.Field()
    region = scrapy.Field()
    title = scrapy.Field()
    herf = scrapy.Field()
    datetime = scrapy.Field()

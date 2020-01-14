# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KychinaItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    user = scrapy.Field()
    tag = scrapy.Field()
    src = scrapy.Field()
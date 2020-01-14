# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from selenium.webdriver import Chrome

class KyzgSpider(CrawlSpider):
    name = 'kyzg'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.oschina.net/blog']
    pro = Chrome()
    pro.page_source
    

    rules = (
        Rule(LinkExtractor(allow=r'blog\?classification=\d+'), callback='parse_item', follow=False),
    )
    def parse_item(self, response):
        print(response)
        print(1)
        yield

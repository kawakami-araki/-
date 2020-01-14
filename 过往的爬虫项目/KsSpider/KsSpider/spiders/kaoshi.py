# -*- coding: utf-8 -*-
import scrapy


class KaoshiSpider(scrapy.Spider):
    name = 'kaoshi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://so.gushiwen.org/authorv_85097dd0c645.aspx']

    def parse(self, response):
        with open('./KsSpider/baijuyi.html', 'w', encoding='utf-8') as f:
            f.write(response.text)


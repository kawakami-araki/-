# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_redis.spiders import RedisCrawlSpider
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
option = Options()
option.add_argument('--headless')
option.add_argument('--disable-gpu')


class FenbuproSpider(RedisCrawlSpider):
    name = 'fenbupro'
    pro = Chrome(chrome_options=option)
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    redis_key = 'fenbuQueue'
    rules = (Rule(LinkExtractor(allow=r'/bxnn/\d+\.htm'),
                  callback='parse_item',
                  follow=True), )

    def parse_item(self, response):
        # title = response.xpath('//div[4]/div[1]/div[2]/ul/li//text()').extract_first()
        # href = response.xpath('//div[4]/div[1]/div[2]/ul/li/b/a/@href').extract_first()
        p_list = response.xpath('//*[@id="text110"]/p')
        for p in p_list:
            text = p.xpath('./text()').extract_first()
            print(text)
            item = {}
            item['text'] = text
            yield item
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

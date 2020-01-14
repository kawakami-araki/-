# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Homework1Item, Homework1ContentItem


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'http://wz.sun0769.com/index.php/question/questionType?type=4'
    ]

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+'),
             callback='parse_item',
             follow=True),
        Rule(LinkExtractor(allow=r'question/\d+/\d+\.shtml'),
             callback='parse_detail',
             follow=False),
    )

    def parse_item(self, response):
        tr_list = response.xpath(
            '//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            title = tr.xpath('./td[2]/a[2]/@title').extract_first()
            detail = tr.xpath('./td[3]/span/text()').extract_first()
            # print(title,detail)
            item = Homework1ContentItem()
            item['title'] = title
            item['detail'] = detail
            yield item

        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
    def parse_detail(self, response):

        content = response.xpath(
            '/html/body/div[9]/table[2]//tr[1]//text()').extract()
        content = ''.join(content)
        item = Homework1Item()
        item['content'] = content

        yield item

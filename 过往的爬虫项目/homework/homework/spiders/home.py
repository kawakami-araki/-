# -*- coding: utf-8 -*-
import scrapy
# LinkExtractor 链接提取器
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HomeSpider(CrawlSpider):
    name = 'home'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    # 实例化一个LinkExtractor
    link = LinkExtractor(allow=r'type=4&page=\d+')

    rules = (
        # 实例化一个Rule(规则解析器)的对象
        Rule(link, callback='parse_item', follow=True),
    )
    # rules = (
    #     # 实例化一个Rule(规则解析器)的对象
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        tr_list = response.xpath('//*[@id="morelist"]/div/table[2]/tbody/tr/td/table/tbody/tr')
        for tr in tr_list:
            title = tr.xpath('./td[2]/a[2]/@title').extract_first()
            content = tr.xpath('./td[3]/span/text()').extract_first()
            print(title,content)

        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        # return item

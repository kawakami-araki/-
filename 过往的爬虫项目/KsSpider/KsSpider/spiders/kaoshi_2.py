# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Kaoshi2Spider(CrawlSpider):
    name = 'kaoshi_2'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://so.gushiwen.org/authors/authorvsw_85097dd0c645A5.aspx']

    rules = (
        Rule(LinkExtractor(allow=r'https://so.gushiwen.org/authors/authorvsw_85097dd0c645A\d+\.aspx'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # /html/body/div[3]/div[1]/div[7]/div[1]
        div_list = response.xpath('//div[@class="cont"]')
        # print(div_list[0].xpath('./div[@class="sons"]'))
        # print(div_list)
        for div in div_list:
            # 标题\
            title = div.xpath('./p[1]/a/b/text()').extract_first()
            # 作者
            author = div.xpath('./p[2]//text()').extract()
            # 内容
            content =div.xpath('./div[2]/text()').extract()

            item = {}
            item['title'] = title
            item['author'] = author
            item['content'] = content
            yield item
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

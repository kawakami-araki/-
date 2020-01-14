# -*- coding: utf-8 -*-
import scrapy
from homework.items import HomeworkItem


class WorkSpider(scrapy.Spider):
    name = 'work'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://lnzxzb.cn/gcjyxx/subpage.html']
    url = 'http://lnzxzb.cn/gcjyxx/%d.html'
    page_num = 1

    def parse(self, response):
        li_list = response.xpath('//*[@id="showList"]/li')
        for li in li_list:
            classify = li.xpath('./p/a/font[1]/text()').extract_first()
            region = li.xpath('./p/a/font[2]/text()').extract_first()
            title = li.xpath('./p/a/text()').extract_first()
            herf = li.xpath('./p/a/@href').extract_first()
            datetime = li.xpath('./span/text()').extract_first()
            item = HomeworkItem()
            item['classify'] = classify
            item['region'] = region
            item['title'] = title
            item['herf'] = herf
            item['datetime'] = datetime
            yield item
        print('第%d页完成' % self.page_num)
        if self.page_num < 50:
            self.page_num += 1
            new_url = self.url % self.page_num
            yield scrapy.Request(url=new_url, callback=self.parse)

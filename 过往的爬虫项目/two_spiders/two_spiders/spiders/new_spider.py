# -*- coding: utf-8 -*-
import scrapy
from two_spiders.items import TwoSpidersItem

class NewSpiderSpider(scrapy.Spider):
    name = 'new_spider'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/gaozhongxiaohua']
    url = 'http://www.521609.com/gaozhongxiaohua/list5%d.html'
    page_num = 1
    def parse(self, response):
        li_list = response.xpath('//div[@class="index_img list_center"]/ul/li')
        for li in li_list:
            img_src = 'http://www.521609.com' + li.xpath('./a[1]/img/@src').extract_first()
            item = TwoSpidersItem()
            item['src'] = img_src
            yield item
        if self.page_num < 50:
            self.page_num += 1
            new_url = format(self.url%self.page_num)
            yield scrapy.Request(url=new_url,callback=self.parse,meta={})


    def movie_parse(self, response):

        pass
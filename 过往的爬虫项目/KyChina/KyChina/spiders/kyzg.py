# -*- coding: utf-8 -*-
import scrapy
from ..items import KychinaItem

class KyzgSpider(scrapy.Spider):
    name = 'kyzg'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.oschina.net/blog']

    def parse(self, response):
        print(response)
        a_list = response.xpath('//*[@id="mainScreen"]/div/div[1]/div/div[1]/div[1]/a')[1:]
        for a in a_list:
            new_url = a.xpath('./@href').extract_first()
            tag = a.xpath('./text()').extract_first()
            item = {}
            item['tag'] = tag
            yield scrapy.Request(url=new_url,callback=self.detail_parse,meta={'item': item})
    
    def detail_parse(self, response):
        div_list = response.xpath('//*[@id="recommendArticleList"]/div[1]/div')
        for div in div_list:
            tag = response.meta['item']['tag']
            item = KychinaItem()
            title = div.xpath('./div/a/@title').extract_first()
            content = div.xpath('./div/div[1]//text()').extract_first()
            user = div.xpath('./div/div[2]/div/div[1]/a/text()').extract_first()
            img_url = div.xpath('./a/img/@src').extract_first()
            item['title'] = title
            item['content'] = content
            item['user'] = user
            item['tag'] = tag
            if img_url:
                item['src'] = img_url
            else:
                item['src'] = 'http://img3.imgtn.bdimg.com/it/u=2440262118,2742320497&fm=26&gp=0.jpg'
            yield item

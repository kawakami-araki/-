# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from ..items import ZlsMovieproItem


class ZlsSpider(CrawlSpider):
    name = 'zls'
    conn = Redis()
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.4567tv.tv/index.php/vod/show/id/8.html']

    rules = (
        Rule(LinkExtractor(allow=r'id/8/page/\d+\.html'),
             callback='parse_item',
             follow=True),
        # Rule(LinkExtractor(allow=r'/show/id/8/page/\d+\.html'), callback='detail_parse', follow=True),
    )

    def parse_item(self, response):
        li_list = response.xpath('//div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            movie_name = li.xpath('./div/div/h4/a/text()').extract_first()
            detail_url = 'https://www.4567tv.tv' + li.xpath(
                './div/div/h4/a/@href').extract_first()
            ex = self.conn.sadd('movie_url_data', detail_url)
            if ex == 1:
                print('哦~一块新鲜的奶酪!')
                item = ZlsMovieproItem()
                item['movie_name'] = movie_name
                yield scrapy.Request(url=detail_url,
                                     callback=self.detail_parse,
                                     meta={'item': item})
            else:
                print('腐朽的味道!!!')

    def detail_parse(self, response):
        item = response.meta['item']
        detail_text = response.xpath(
            '//div[1]/div/div/div/div[2]/p[5]/span[3]/text()').extract_first()
        item['detail_text'] = detail_text
        print(item)
        yield item
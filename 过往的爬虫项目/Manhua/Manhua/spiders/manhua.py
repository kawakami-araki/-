# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis


class ManhuaSpider(CrawlSpider):
    name = 'manhua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.181mh.com/list/wanjie/']
    conn = Redis()
    rules = (
        Rule(LinkExtractor(allow=r'/list/\w+-wanjie/'),
             callback='parse_item',
             follow=False),
        # Rule(LinkExtractor(allow=r'/list/\w+-wanjie/\d+/'), callback='page_parse', follow=True),
    )
    url_cate = {}

    def parse_item(self, response):
        page_url = response.xpath(
            '//*[@id="w1"]/div/ul/li/a/@href').extract()[2:-2]
        for page in page_url:
            yield scrapy.Request(url='https://www.181mh.com' + page,
                                 callback=self.page_parse)

    def page_parse(self, response):
        li_list = response.xpath('//*[@id="contList"]/li')
        for li in li_list:
            book_url = li.xpath('./a/@href').extract_first()
            book_name = li.xpath('./a/@title').extract_first()
            db = self.conn.sadd('book_url_set',book_url)
            if db == 1:
                print('这是一本新书')
                yield scrapy.Request(url=book_url,
                                    callback=self.detail_parse,
                                    meta={
                                        'book_name': book_name,
                                    })
            else:
                print('这本书已经有了')

    def detail_parse(self, response):
        # 书名
        book_name = response.meta['book_name']
        # 分类
        book_cate = response.xpath('/html/body/div[4]/div/div/div[2]/div[1]/div[1]/div[2]/ul/li[2]/span[1]/a/text()').extract()
        # 作者
        author = response.xpath(
            '/html/body/div[4]/div/div/div[2]/div[1]/div[1]/div[2]/ul/li[2]/span[2]/a/text()'
        ).extract_first()
        # 简介
        content = response.xpath(
            '//*[@id="intro-cut"]/p/text()').extract_first()
        # 章节总数
        total_chapters = len(response.xpath('//*[@id="chapter-list-4"]/li'))
        # 最后更新时间
        update_time = response.xpath(
            '/html/body/div[4]/div/div/div[2]/div[1]/div[1]/div[2]/ul/li[3]/span/span/text()'
        ).extract_first()
        # 图片
        src = response.xpath(
            '/html/body/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/p/img/@src').extract_first()
        item = {}
        item['book_name'] = book_name
        item['book_cate'] = book_cate
        item['author'] = author
        item['content'] = content
        item['total_chapters'] = total_chapters
        item['update_time'] = update_time
        item['src'] = src
        yield item

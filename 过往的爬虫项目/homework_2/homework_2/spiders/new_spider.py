# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from dateutil import parser
class NewSpiderSpider(CrawlSpider):
    name = 'new_spider'
    conn = Redis()
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhangxinxu.com/wordpress/']

    rules = (
        Rule(LinkExtractor(allow=r'wordpress/page/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        div_list = response.xpath('//*[@id="content"]/div')[2:-1]
        for div in div_list:
            print(response)
            # 博客标题
            title = div.xpath('./h2/a/@title').extract_first()
            # 发帖时间
            data_time = div.xpath('./small/span[1]/text()').extract_first()
            data_time = data_time.replace('年', '-').replace('月', '-').replace('日', '-')
            data_time = parser.parse(data_time)
            # 阅读次数
            count = div.xpath('./small/text()').extract_first()
            # 内容简介
            content = div.xpath('./div/p[2]//text()').extract()[-1]
            # 图片url
            img_src = div.xpath('./div/p[1]/img/@src').extract_first()
            # 帖子标签
            tag = div.xpath('.//p/a/text()').extract()[:-2]
            # 评论数
            comments = div.xpath('.//p/a/text()').extract()[-1]
            rd = self.conn.sadd('title_list', title)
            if rd == 1:
                print('获取到一条新数据')
                item = {}
                item['title'] = title
                item['data_time'] = data_time
                item['count'] = count
                item['content'] = content
                item['tag'] = tag
                item['img_src'] = img_src
                item['comments'] = comments
                yield item
            else:
                print('已存在的数据,自动略过')
                continue

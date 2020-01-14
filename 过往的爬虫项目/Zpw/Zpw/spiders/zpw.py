# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZpwSpider(CrawlSpider):
    name = 'zpw'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python']

    rules = (
        Rule(LinkExtractor(allow=r'query=python&page=\d+$'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print(response)
        li_list = response.xpath('//*[@id="main"]/div/div[2]/ul')
        print(li_list)
        for li in li_list:
            # 职位名称
            primary = li.xpath('./div/div[1]/h3/a/div[1]/text()').extract_first()
            # 工资
            red = li.xpath('./div/div[1]/h3/a/span').extract_first()
            # 地址,工作经验,学历
            line, work_exp,xueli = li.xpath('./div/div[1]/p').extract()
            # 单位
            Gsmc = li.xpath('./div/div[2]/div/h3/a/text()').extract_first()
            print(primary,red,line, work_exp,xueli,Gsmc)

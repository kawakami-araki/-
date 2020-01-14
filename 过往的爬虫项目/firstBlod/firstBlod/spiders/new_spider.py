# -*- coding: utf-8 -*-
import scrapy
from firstBlod.items import FirstblodItem

class NewSpiderSpider(scrapy.Spider):
    # 爬虫文件的名称,相当于爬虫文件的唯一标识
    name = 'new_spider'
    # 循序的域名, 通常情况下不会使用
    # allowed_domains = ['www.baidu.com']
    # 起始的url列表, scrapy将会对列表中的url自动进行请求发送
    start_urls = [
        'https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=',
        ]
    url = 'https://www.zhipin.com/c101010100/?query=python&page=%d&ka=page-%d'
    page_name = 1
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.parse)
    def parse(self, response):
        li_list = response.xpath('//div[@class="job-list"]')
        print(li_list)
        # all_data = []
        for li in li_list:
            # 职位名称
            Job_title = li.xpath('./div/div[1]/h3/a/div[1]/text()').extract()[0]
            # 公司名称
            Corporate_name = li.xpath('./div/div[1]/a/text()').extract()[0]
            # 地址
            all_address = li.xpath('./div/div[1]/p//text()').extract()[0]
            # 经验 experience
            # address,experience,Education = all_address.split('|')
            #学历 Education
            # dic = {
            #     'Author': author,
            #     'Content': content
            # }
            # all_data.append(dic)
            item = FirstblodItem()
            item['Job_title'] = Job_title
            item['Corporate_name'] = Corporate_name
            yield item
        if self.page_name <= 5:
            self.page_name += 1
            new_url = format(self.url%(self.page_name,self.page_name))
            yield scrapy.Request(new_url,callback=self.parse)
        else:
            return li_list
        # return all_data
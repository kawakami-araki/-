# -*- coding: utf-8 -*-
import scrapy
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.options import Options
from wangyi.items import WangyiItem
option = ChromeOptions()
# option.add_experimental_option('excludeSwithes', ['enable-automation'])
chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    pro = Chrome(chrome_options=chrome_option)
    cls_url_list = []

    def parse(self, response):
        # print(response.text)
        index_list = [3, 4]
        li_list = response.xpath(
            '//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li'
        )
        # print(li_list)
        for index in index_list:
            li = li_list[index]
            new_url = li.xpath('./a/@href').extract_first()
            news = li.xpath('./a/text()').extract_first()
            self.cls_url_list.append(new_url)
            yield scrapy.Request(url=new_url, callback=self.new_prase)

    def new_prase(self, response):
        div_list = response.xpath(
            '/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div/h3/a/text()').extract_first()
            new_url = div.xpath('./div/div/h3/a/@href').extract_first()
            item = WangyiItem()
            item['title'] = title
            yield scrapy.Request(url=new_url,
                                 callback=self.content_parse,
                                 meta={'item': item})

    def content_parse(self, response):
        item = response.meta['item']
        content = response.xpath('//*[@id="endText"]/p/text()').extract()
        item['content'] = ''.join(content)
        yield item

    def closed(self, spider):
        self.pro.quit()
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from time import sleep
from scrapy.http import HtmlResponse
from fake_useragent import UserAgent
class Homework2DownloaderMiddleware(object):
    ua = UserAgent()
    def process_request(self, request, spider):
        request.headers['User-Agent'] = self.ua.Chrome
        request.headers['Cookie'] = 'd=22e1b19af7c00014||t=1577688828|et=730|cs=002213fd488db2bbf641bcee92'
        return None

    def process_response(self, request, response, spider):
        pro = spider.pro
        if request.url != 'https://www.oschina.net/blog':
            pro.get(request.url)
            js = 'window.scrollTo(0,document.body.scrollHeight)'
            for num in range(3):
                pro.execute_script(js)
                sleep(2)
            page_text = pro.page_source
            response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
        return response 
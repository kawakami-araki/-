# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from scrapy.http import HtmlResponse

from time import sleep

from scrapy import signals


class FenbuDownloaderMiddleware(object):


    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        pro = spider.pro
        pro.get(request.url)
        sleep(1)
        response_text = pro.page_source
        return HtmlResponse(url=request.url,body=response_text,encoding='utf-8',request=request)
        


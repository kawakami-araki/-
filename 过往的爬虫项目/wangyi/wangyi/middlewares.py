# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from time import sleep

class WangyiDownloaderMiddleware(object):
    def process_response(self, request, response, spider):
        pro = spider.pro
        if request.url in spider.cls_url_list:
            pro.get(request.url)
            sleep(1)
            page_text = pro.page_source
            new_response = HtmlResponse(url=request.url,
                                        body=page_text,
                                        encoding='utf-8',
                                        request=request)
            return new_response
        return response
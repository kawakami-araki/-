# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from requests.sessions import Session
from fake_useragent import UserAgent
class ZpwDownloaderMiddleware(object):


    def process_request(self, request, spider):
        request.headers['Cookie'] = 'sid=sem; toUrl=/; __g=sem; lastCity=101010100; __c=1577690698; __l=r=https%3A%2F%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3DNew-%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D-05%26unit%3D%25E5%2593%2581%25E7%2589%258C%252B%25E8%2581%258C%25E4%25BD%258D-%25E4%25BF%25A1%25E6%2581%25AF%26keyword%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25A5%25BD%25E7%2594%25A8%25E5%2590%2597%26bd_vid%3D17399182057516737945&l=%2Fwww.zhipin.com%2F%3Fka%3Dheader-home&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3DNew-%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-1%26unit%3D51%26keyword%3Dwww.zhipin.com%26bd_vid%3D18188860027770810474&friend_source=0&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1577690695,1578358471; __a=29527690.1577690715.1577690715.1577690698.13.2.12.13; __zp_stoken__=887arVBKGQ8%2Bhg7xNCanXvX7urEiChrKZibtEac8RIaJQWyaKmBhLvcU9kRhPbWvk8YGCiMbsvtYXcgl2ryBBztjay9OaDhXjLCXLvryOA%2F%2BCFtjkWJqMc3FrQt5VKX77nut; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1578628529'
        print(request.headers)
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

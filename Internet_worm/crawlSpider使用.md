[TOC]



# 基于crawlSpider进行的全栈数据爬取

## crawlspider是爬虫类中spider的一个子类

## 使用流程

创建一个基于crawlspider的爬虫文件

-   ​	scrapy genspider -t crawl spiderName www.xxx.com
    -   使用指令创建一个基于crawlSpider的爬虫文件
-   构造链接提取器和构造解析器
    -   链接提取器
        -   可以根据制定的规则进行指定链接的提取
    -   构造解析器

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import Homework1Item, Homework1ContentItem


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'http://wz.sun0769.com/index.php/question/questionType?type=4'
    ]

    rules = (
        # 进行链接提取,follow开启深度提取 ,
        Rule(LinkExtractor(allow=r'type=4&page=\d+'),
             callback='parse_item',
             follow=True),
        # 进行详情页链接提取,但是关闭深度提取
        Rule(LinkExtractor(allow=r'question/\d+/\d+\.shtml'),
             callback='parse_detail',
             follow=False),
    )
	# 在进行上述的网页处理的时候,这两个将会同步进行,也就是说,在第一个深度提取运行一次的时候,另一个也会一起运行一次
    # 这种情况下,每次我们获取一个新的页面,第二个提取器将会对这个新的页面进行处理,然后再处理下一个页面
    # 正常的spider和这个crawlspider是通用的,也就是说,在使用这个crawlspdier进行深度爬取的时候,其他的spider操作也是没问题的
    def parse_item(self, response):
        tr_list = response.xpath(
            '//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            title = tr.xpath('./td[2]/a[2]/@title').extract_first()
            detail = tr.xpath('./td[3]/span/text()').extract_first()
            # print(title,detail)
            item = Homework1ContentItem()
            item['title'] = title
            item['detail'] = detail
            yield item
    def parse_detail(self, response):

        content = response.xpath(
            '/html/body/div[9]/table[2]//tr[1]//text()').extract()
        content = ''.join(content)
        item = Homework1Item()
        item['content'] = content

        yield item
```


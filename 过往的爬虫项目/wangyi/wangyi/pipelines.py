# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from aip import AipNlp


class WangyiPipeline(object):
    def open_spider(self, spider):
        self.fp = open('./news.txt', 'w', encoding='utf-8')
        """ 你的 APPID AK SK """
        APP_ID = '18141048'
        API_KEY = 'CPKSpk7Up1aATfxAaP9xln1O'
        SECRET_KEY = 'miR2GGKYfx214xEGUO0i83cgFmD3T1Z3'
        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    def process_item(self, item, spider):
        title = item['title']
        title = title.replace('\xa0', ' ')
        content = item['content']
        content = content.replace('\xa0', ' ')
        wd_dic = self.client.keyword(title, content)
        to_dic = self.client.topic(title, content)
        print(wd_dic, to_dic)

        # # print(item)
        # self.fp.write('[' + 'title' + ':' + title + ',' + 'content' + ':' + content + ']' + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()
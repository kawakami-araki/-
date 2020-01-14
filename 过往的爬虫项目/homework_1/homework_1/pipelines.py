# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Homework1Pipeline(object):
    def process_item(self, item, spider):
        if item.__class__.__name__ == 'Homework1Item':
            content = item['content']
            print(content)
        else:
            title = item['title']
            detail = item['detail']
            print(title, detail)

        return item

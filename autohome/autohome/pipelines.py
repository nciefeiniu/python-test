# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json

class AutohomePipeline(object):
    def process_item(self, item, spider):
        if item['replys'] > 2000:
            return item
        else:
            raise DropItem("评论数少，drop it")

class JsonWriterPipeline(object):
    def __init__(self):
        self.file  = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
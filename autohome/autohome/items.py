# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomeItem(scrapy.Item):
    #标题
    title = scrapy.Field()
    #链接
    link = scrapy.Field()
    #id号
    id = scrapy.Field()
    #评论量
    replys = scrapy.Field()



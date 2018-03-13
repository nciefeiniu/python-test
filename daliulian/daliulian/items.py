# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaliulianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #电视剧名字
    name = scrapy.Field()
    #电视剧的链接
    link = scrapy.Field()
    #电视剧资源的链接
    '''
    两种链接，
    一种是百度云的
    另一种是种子edk2
    '''
    baidu_link = scrapy.Field()
    edk2_link = scrapy.Field()
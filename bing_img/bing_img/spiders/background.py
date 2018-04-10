import scrapy
import json
from scrapy.selector import Selector
from bing_img.items import BingImgItem

class background(scrapy.Spider):
    name = 'bing_background'
    allow_domains = ['cn.bing.com']
    start_urls = [
        'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1621425175463&pid=hp',
    ]

    def parse(self, response):
        response.body.decode('utf-8')
        for r in response.xpath('//body/p/text()').extract():
            detail = json.loads(r)
            for d in detail['images']:
                item = BingImgItem()
                item['url'] = d['url'].encode('utf-8')
                item['name'] = d['copyright'].encode('utf8')
                item['time'] = d['enddate']
                yield item

# 分辨率
sgreen = [
    '1920x1080',
    '1366x768',
    '1280x768',
    '1024x768',
    '800x600',
    '800x480',
    '768x1280',
    '720x1280',
    '640x480',
    '480x800',
    '400x240',
    '320x240',
    '240x320'
]
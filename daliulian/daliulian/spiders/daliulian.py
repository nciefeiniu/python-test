import scrapy
from daliulian.items import DaliulianItem

#抓取已完结的连续剧
class tvspider(scrapy.Spider):
    name = "tvspider_end"
    allow_domains = ["www.llduang.com"]
    start_urls = [
        'http://www.llduang.com/lianxuju/%E5%B7%B2%E5%AE%8C%E7%BB%93',
    ]

    #首页搜集电视剧的链接
    def parse(self, response):
        response.body.decode('utf8')
        for i in response.xpath('//*[@id="post_container"]/li'):
            item = []
            item = i.xpath('./div/a[1]/@href').extract()
            for url in item:
                yield scrapy.Request(url, meta={'f_url':url}, callback=self.parse_next)
        #采集完一页，继续向下一页采集
        next_page  = response.xpath("/html/body/div[5]/div[3]/div[2]/div/a[@class='next']/@href").extract()
        if next_page is not None:
            # print(type(next_page))
            yield scrapy.Request(next_page[0], callback=self.parse)

    #进一步深入，提取资源链接
    def parse_next(self, response):
        item = DaliulianItem()
        item['link'] = response.meta['f_url']
        item['name'] = response.xpath('//*[@id="content"]/div[1]/h1/text()')


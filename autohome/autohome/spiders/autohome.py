import scrapy

from autohome.items import AutohomeItem

class QuotesSpider(scrapy.Spider):
    name = "autohome"

    start_urls = [
            'https://club.autohome.com.cn/jingxuan/104/1',
        # 'https://club.autohome.com.cn/jingxuan/104/2',
        # 'https://club.autohome.com.cn/jingxuan/104/3',
        # 'https://club.autohome.com.cn/jingxuan/104/4',
        # 'https://club.autohome.com.cn/jingxuan/104/5',
        # 'https://club.autohome.com.cn/jingxuan/104/6',

        ]

    def parse(self, response):

        for u in response.xpath('//ul[@class="content"]/li/div[@class="pic_txt"]'):
            item = AutohomeItem()
            #提取文章标题
            item['title'] = u.xpath('.//p/a/text()').extract()[0]
            #提取文章id号
            id = u.xpath('.//span[@class="read"]').extract()[0][14:22]
            item['id'] = id
            #提取文章的url
            item['link'] = u.xpath('.//p/a/@href').extract()[0]
            #请求评论量
            xhr_url = r'https://club.autohome.com.cn/JingXuan/GetTopicClicksByTopicIds?ids=' + id
            yield scrapy.Request(xhr_url, callback=self.parse_select)
            # print("--------------------------------------------")
            # print(item['title'], item['id'], item['link'])

    def parse_select(self, response):
        detail = response.xpath('.//p/text()')
        de = detail.extract()[0]
        print(type(de))
        print('===============================')
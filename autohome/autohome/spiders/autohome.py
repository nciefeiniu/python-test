import scrapy

from autohome.items import AutohomeItem

class QuotesSpider(scrapy.Spider):
    name = "autohome"

    start_urls = [
            'https://club.autohome.com.cn/jingxuan/104/7',
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

            """通过meta参数，把item这个字典，赋值给meta中的'key'键（记住meta本身也是一个字典）。
              Scrapy.Request请求url后生成一个"Request对象"，这个meta字典（含有键值'key'，'key'的值也是一个字典，即item）
              会被“放”在"Request对象"里一起发送给parse_select()函数 
           """
            yield scrapy.Request(xhr_url,meta={'item1':item}, callback=self.parse_select)
            # item['replys'] = comment
            # print(item['title'], item['id'], item['link'], item['replys'])
            # print("--------------------------------------------")


    def parse_select(self, response):
        item2 = response.meta['item1']
        detail = response.xpath('.//p/text()')
        #提取评论数
        reply = detail.extract()[0].split(",")[1][9:]
        # item = AutohomeItem()
        item2['replys'] = reply
        # print(item['replys'])
        # print('===============================')
        url = r'https:'+ item2['link']
        # print(item2['title'], item2['id'], item2['link'], item2['replys'])
        yield scrapy.Request(url, meta={'item2':item2}, callback=self.parse_detail)
        # yield item2

    def parse_detail(self, response):
        item3 = response.meta['item2']
        images_urls = []
        conttxt = response.xpath('//*[@id="F0"]/div[2]/div[2]/div[1]')
        img_url = conttxt.xpath('.//img/@src').extract()
        print(img_url)
        print('==================================================')

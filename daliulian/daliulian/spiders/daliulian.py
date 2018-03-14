import scrapy
from daliulian.items import DaliulianItem

#抓取已完结的连续剧
class tvspider(scrapy.Spider):
    name = "tvspider_end"
    allow_domains = ["www.llduang.com"]
    start_urls = [
        'http://www.llduang.com/lianxuju/%E5%B7%B2%E5%AE%8C%E7%BB%93/page/8',
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
        # next_page  =
        try:
            next_page = response.xpath("/html/body/div[5]/div[3]/div[2]/div/a[@class='next']/@href").extract()
        except:
            pass
        else:
            # print(type(next_page))
            yield scrapy.Request(next_page[0], callback=self.parse)

    #进一步深入，提取资源链接
    def parse_next(self, response):
        item = DaliulianItem()
        #这是在大榴莲中的url
        item['link'] = response.meta['f_url']
        item['name'] = response.xpath('//*[@id="content"]/div[1]/h1/text()')
        detail = response.xpath('//div[@id="post_content"]')
        # print(detail.extract())
        #magnet链接
        magnet_link = detail.xpath('./p/a[starts-with(@href,"magnet:?")]')
        magnets = {}
        ed2ks = {}
        if magnet_link:
            #列表不为空
            for m in magnet_link:
                title = m.xpath('./text()').extract()
                url = m.xpath('./@href').extract()
                magnets[title[0]] = url[0]

        #ed2k链接
        ed2k_link = detail.xpath('./p/a[starts-with(@href,"ed2k:")]')
        if ed2k_link:
            for e in ed2k_link:
                title = e.xpath('./text()').extract()
                url = e.xpath('./@href').extract()
                ed2ks[title[0]] = url

        try:
            if len(magnets) > 0 :
                item['magnet_link'] = magnets
            else:
                item['magnet_link'] = None
        except BaseException:
            print('error'+'这里发生点问题')

        try:
            if len(ed2ks) > 0 :
                item['ed2k_link'] = ed2ks
            else:
                item['ed2k_link'] = None
        except BaseException:
            print('error' + '这里发生点问题')

        #百度云链接
        baidu_link = []
        baidu = detail.xpath('.//a[contains(text(),"https://pan.baidu.com/")]/text()').extract()
        if baidu:
            mima = response.xpath('//span[contains(text(),"密码")]/text()').extract()
            baidu_link.append(baidu[0])
            baidu_link.append(mima[0])
            item['baidu_link'] = baidu_link
            print("有百度云：")
            print( item['ed2k_link'], item['baidu_link'], item['magnet_link'])
            print("========================================")
        else:
            print("没百度云：")
            print( item['ed2k_link'], item['magnet_link'])
            print("=======================================================")





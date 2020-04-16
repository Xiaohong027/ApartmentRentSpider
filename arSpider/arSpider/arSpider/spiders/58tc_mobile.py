import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from items import BisheItem


class Spider_58tc_mobile(scrapy.Spider):
    name = 'Spider_58tc_mobile'
    allowed_domains = ['m.58.com']
    #start_urls = ['http://ty.58.com/chuzu/pn{}/'.format(i for i in range(1,71,1))]
    url = 'http://m.58.com/ty/chuzu/pn'

    def start_requests(self):
        for i in range(22, 31, 1):
            url = self.url + str(i)
            yield Request(url, self.parse)

    def parse(self, response):
        link_list = response.xpath('//ul[@class="list-info hpic"]/li/a[1]/@href').extract()
        for link in link_list:
            print(link)
            yield scrapy.Request(link,callback=self.parse_item)

    def parse_item(self, response):
        item = BisheItem()
        title = (response.xpath('//div[@class="meta-tit"]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        price = (response.xpath('//ul[@class="houseInfo-detail bbOnepx"]/li[2]/i/text()').extract())[0].strip().replace(' ','').replace('\n','')
        info1 = (response.xpath('//ul[@class="houseInfo-detail bbOnepx"]/li[1]/i/text()').extract())[0].strip().replace(' ','').replace('\n','')
        info2 = (response.xpath('//ul[@class="houseInfo-meta bbOnepx"]/li[2]/span[1]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        info = info1 + '' + info2
        direction = None
        region1 = (response.xpath('//ul[@class="houseInfo-detail bbOnepx"]/li[3]/i/text()').extract())[0].strip().replace(' ','').replace('\n','')
        region2 = (response.xpath('//ul[@class="houseInfo-meta bbOnepx"]/li[1]/span[1]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        #region3 = (response.xpath('//ul[@class="f14"]/li[6]/span[2]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        region = region2 + ' ' + region1
        try:
            phone = (response.xpath('//span[@class="meta-phone"]/text()').extract())[0].strip()
        except(IndexError):
            phone = None
        # if phone == '扫码看电话':
        #     phone = None
        # else:
        #     pass
        url = response.url
        content = str((response.xpath('//p[@class="panel-description desClose"]').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','')
        #content = (response.xpath('//p[@class="panel-description desClose"]/text()').extract())[0].strip().replace(' ','').replace('\n','')

        #print(title, price, info, direction, phone, url, region, content)

        item['url'] = url
        item['title'] = title
        item['info'] = info
        item['region'] = region
        item['price'] = price
        item['content'] = content
        item['direction'] = direction
        item['phone'] = phone

        yield item


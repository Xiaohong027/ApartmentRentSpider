import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from items import BisheItem

class Spider_fangtianxia(scrapy.Spider):
    name = 'Spider_fangtianxia'
    allowed_domains = ['fang.com']
    url = 'http://zu.taiyuan.fang.com/house/i3'
    host = 'http://zu.taiyuan.fang.com'
    def start_requests(self):
        for i in range(1, 101, 1):
            url = self.url + str(i)
            yield Request(url, self.parse)

    def parse(self, response):
        link_list = response.xpath('//p[@class="title"]/a/@href').extract()
        for link in link_list:
            url = self.host + link
            print(url)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = BisheItem()
        title = (response.xpath('//div[@class="title"][1]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        try:
            price = (response.xpath('//div[@class="trl-item sty1"]/i/text()').extract())[0].strip().replace(' ','').replace('\n','')
        except(IndexError):
            price = None
        info1 = str((response.xpath('//div[@class="trl-item1 w182"]/div[1]').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','').replace('\t','')
        info2 = str((response.xpath('//div[@class="trl-item1 w132"]/div[1]').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','').replace('\t','')
        info = info1 + '' + info2
        try:
            direction = (response.xpath('//div[@class="tr-line clearfix"][2]/div/div[1]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        except(IndexError):
            direction = None
        region = (response.xpath('//div[@class="rcont"]/a[1]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        try:
            phone = (response.xpath('//div[@class="tjcont-list-cline3 font16"]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        except(IndexError):
            phone = None
        url = response.url
        content = str((response.xpath('fyms_modify').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','')
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


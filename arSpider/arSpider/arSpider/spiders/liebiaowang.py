import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from items import BisheItem

class Spider_liebiaowang(scrapy.Spider):
    name = 'Spider_liebiaowang'
    allowed_domains = ['liebiao.com']
    url1 = 'http://taiyuan.liebiao.com/zufang/index'
    url2 = '.html'
    def start_requests(self):
        for i in range(1, 21, 1):
            url = self.url1 + str(i) + self.url2
            yield Request(url, self.parse)

    def parse(self, response):
        link_list = response.xpath('//div[@class="post-thumb-box"]/a/@href').extract()
        for link in link_list:
            yield scrapy.Request(link, callback=self.parse_item)

    def parse_item(self, response):
        item = BisheItem()
        title = (response.xpath('//h1[@class="ellipsis"]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        try:
            price = (response.xpath('//dd[@class="field-detail price"]/span[1]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        except(IndexError):
            price = None
        info1 = str((response.xpath('//div[@class="dec-params clf"]/dl[2]/dd').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','').replace('\t','')
        info2 = str((response.xpath('//div[@class="dec-params clf"]/dl[3]/dd').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','').replace('\t','')
        info = info1 + '' + info2
        direction = None
        region = (response.xpath('//div[@class="dec-params clf"]/dl[1]/dd/text()').extract())[0].strip().replace(' ','').replace('\n','')
        try:
            phone = (response.xpath('//span[@class="phone"]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        except(IndexError):
            phone = None
        url = response.url
        content = str((response.xpath('//div[@class="content-wrap"]').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','')
        print(title, price, info, direction, phone, url, region, content)

        item['url'] = url
        item['title'] = title
        item['info'] = info
        item['region'] = region
        item['price'] = price
        item['content'] = content
        item['direction'] = direction
        item['phone'] = phone

        yield item


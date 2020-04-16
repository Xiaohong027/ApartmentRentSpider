import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from items import BisheItem

class Spider_107room(scrapy.Spider):
    name = 'Spider_107room'
    allowed_domains = ['107room.com']
    #start_urls = ['http://ty.58.com/chuzu/pn{}/'.format(i for i in range(1,71,1))]
    url = 'http://ty.107room.com/z2_a740_'
    host = 'http://ty.107room.com'
    def start_requests(self):
        for i in range(1, 41, 1):
            url = self.url + str(i)
            yield Request(url, self.parse)

    def parse(self, response):
        link_list = response.xpath('//div[@class="oneHouse setStyle"]/a/@href').extract()
        for link in link_list:
            url = self.host + link
            print(url)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = BisheItem()
        title = None
        price = (response.xpath('//span[@class="monthPrice"]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        info1 = str((response.xpath('//table[@class="allHouseCondition1"]').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','').replace('\t','')
        info2 = str((response.xpath('//table[@class="allHouseCondition2"]').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','').replace('\t','')
        info = info1 + '' + info2
        try:
            direction = (response.xpath('//td[@class="roomSubDetailItem"]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        except(IndexError):
            direction = None
        region = (response.xpath('//div[@class="community_top"]/div/a/text()').extract())[0].strip().replace(' ','').replace('\n','')
        phone = None
        url = response.url
        content = str((response.xpath('//div[@class="houseFromType rentDetail"]/li[@class="agentWords"]/h3').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','')
        lon = (response.xpath('//div[@class="pointlng"]/text()').extract())[0].strip()
        lat = (response.xpath('//div[@class="pointlat"]/text()').extract())[0].strip()
        #print(title, price, info, direction, phone, url, region, content, lon, lat)

        item['url'] = url
        item['title'] = title
        item['info'] = info
        item['region'] = region
        item['price'] = price
        item['content'] = content
        item['direction'] = direction
        item['phone'] = phone
        item['lon'] = lon
        item['lat'] = lat

        yield item


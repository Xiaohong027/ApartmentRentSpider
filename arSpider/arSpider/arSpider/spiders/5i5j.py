import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from items import BisheItem

headers = {
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Length':'221',
'Content-Type':'text/plain',
}
class Spider_5i5j(scrapy.Spider):
    name = 'Spider_5i5j'
    allowed_domains = ['5i5j.com']
    #start_urls = ['http://ty.58.com/chuzu/pn{}/'.format(i for i in range(1,71,1))]
    url = 'https://ty.5i5j.com/zufang/n'
    host = 'https://ty.5i5j.com'
    def start_requests(self):
        for i in range(1, 3, 1):
            url = self.url + str(i)
            yield Request(url, self.parse)

    def parse(self, response):
        link_list = response.xpath('//h3[@class="listTit"]/a/@href').extract()
        for link in link_list:
            url = self.host + link
            print(url)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = BisheItem()
        title = (response.xpath('//h1[@class="house-tit"]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        price = (response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/p[1]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        info = str((response.xpath('//div[@class="jlquannei fonthongse"]').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','').replace('\t','')
        direction1 = (response.xpath('//div[@class="zushous"]/ul/li[3]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        direction2 = (response.xpath('//div[@class="zushous"]/ul/li[2]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        region = (response.xpath('//div[@class="zushous"]/ul/li[1]/a/text()').extract())[0].strip().replace(' ','').replace('\n','')
        #region2 = (response.xpath('//div[@class="zushous"]/ul/li[8]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        #region3 = (response.xpath('//ul[@class="f14"]/li[6]/span[2]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        direction = direction1 + '' + direction2
        phone = (response.xpath('//li[@class="daikcon fl"]/label/text()').extract())[0].strip()
        # if phone == '扫码看电话':
        #     phone = None
        # else:
        #     pass
        url = response.url
        content = str((response.xpath('//ul[@class="fytese"]').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','')

        print(title, price, info, direction, phone, url, region, content)

        # item['url'] = url
        # item['title'] = title
        # item['info'] = info
        # item['region'] = region
        # item['price'] = price
        # item['content'] = content
        # item['direction'] = direction
        # item['phone'] = phone
        #
        # yield item


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from items import BisheItem

# class Spider_tc58(CrawlSpider):
#     name = 'Spider_58tc'
#     allowed_domains = ['ty.58.com']
#     # start_urls = ['http://ty.58.com/chuzu/pn{}/'.format(i for i in range(1,71,1))]
#     start_urls = ['http://ty.58.com/chuzu/pn1/']
#
#     rules = [
#         Rule(LinkExtractor(restrict_xpaths=('//a[@class="next"]')), follow=True),
#         Rule(LinkExtractor(allow=('shtml'), deny=('xiaoqu'), restrict_xpaths=('//div[@class="des"]')), callback=('parse_item'), follow=False)
#         #Rule(LinkExtractor(allow=('zufang', 'hezu'), restrict_xpaths=('//ul[@class="listUl"]/li/div[@class="des"]/h2/a]')) ,callable('parse_item'))
#     ]
#
#     def parse_item(self, response):
#         print(response.url)

headers = {
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Length':'221',
'Content-Type':'text/plain',
'Cookie':'Cookie:id58=c5/njVra8DQQfj2HAwwAAg==; als=0; wmda_uuid=aea7e89b397f877f53acd8f27bebb2ef; wmda_new_uuid=1; _ga=GA1.2.317447175.1524316183; wmda_visited_projects=%3B2385390625025%3B2427509687170; commontopbar_myfeet_tooltip=end; __utma=253535702.317447175.1524316183.1527077288.1527077288.1; __utmz=253535702.1527077288.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); city=ty; 58home=ty; commontopbar_ipcity=ty%7C%E5%A4%AA%E5%8E%9F%7C0; defraudName=defraud; 58tj_uuid=064cd8e0-0397-4e20-8444-9562baa36f90; new_session=0; new_uv=21; utm_source=; spm=; init_refer=http%253A%252F%252Fty.58.com%252Fchuzu%252Fpn70%252F%253FPGTID%253D0d3090a7-002e-4ea3-1274-1a7c5ede8a5e%2526ClickID%253D2; commontopbar_new_city_info=740%7C%E5%A4%AA%E5%8E%9F%7Cty; wmda_session_id_2385390625025=1527151891500-12081c2b-c6da-1904; ppStore_fingerprint=569E8A549CCFE1DAC8E49810287C42FE953D3C6D6613B3FF%EF%BC%BF1527151895391; xxzl_deviceid=TZFfbXTQz84a9FBJt0uC1Dp9TIWPcFSUDwIQ1jhqfLRp32JNHG7mi2Jrt3c6BAQ8'
}
class Spider_58tc(scrapy.Spider):
    name = 'Spider_58tc'
    allowed_domains = ['58.com']
    url = 'http://ty.58.com/chuzu/pn'
    # start_urls = ['http://ty.58.com/chuzu/pn{}/'.format(i for i in range(1,71,1))]
    #爬列表页

    start_urls = ['http://ty.58.com/chuzu/pn{}/?PGTID=0d3090a7-002e-4ae9-9faf-55b666ea8864&ClickID=2'.format(i) for i in range(1, 71, 1)]
    def parse(self, response):
        item = BisheItem()
        titles = (response.xpath('//div[@class="des"]/h2/a/text()').extract())
        prices = (response.xpath('//div[@class="money"]/b/text()').extract())
        infos = (response.xpath('//div[@class="des"]/p[1]/text()').extract())
        direction = None
        regions = (response.xpath('//p[@class="add"]/a[1]/text()').extract())
        phone = None
        urls = (response.xpath('//div[@class="des"]/h2/a/@href').extract())
        for title, price, info, region, url in zip(titles, prices, infos, regions, urls):
            item['url'] = url
            item['title'] = title.strip().replace(' ','').replace('\n','')
            item['info'] = info.strip().replace(' ','').replace('\n','')
            item['region'] = region
            item['price'] = price
            item['content'] = None
            item['direction'] = direction
            item['phone'] = phone
            yield item




    # 爬详情页
    '''
    def start_requests(self):
        for i in range(2, 3, 1):
            url = self.url + str(i) + '/?PGTID=0d3090a7-002e-4549-7ebd-d6ea6c773845&ClickID=2'
            yield Request(url, self.parse)

    def parse(self, response):
        link_list = response.xpath('//div[@class="img_list"]/a/@href').extract()
        for link in link_list:
            yield scrapy.Request(link,callback=self.parse_item, headers=headers)

    def parse_item(self, response):
        item = BisheItem()
        title = (response.xpath('//h1[@class="c_333 f20"]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        price = (response.xpath('//b[@class="f36"]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        info = (response.xpath('//ul[@class="f14"]/li[2]/span[2]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        direction = (response.xpath('//ul[@class="f14"]/li[3]/span[2]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        region1 = (response.xpath('//ul[@class="f14"]/li[4]/span[2]/a/text()').extract())[0].strip().replace(' ','').replace('\n','')
        region2 = (response.xpath('//ul[@class="f14"]/li[5]/span[2]/a/text()').extract())[1].strip().replace(' ','').replace('\n','')
        region3 = (response.xpath('//ul[@class="f14"]/li[6]/span[2]/text()').extract())[0].strip().replace(' ','').replace('\n','')
        region = region2 + ' ' + region1 + ' ' + region3
        phone = (response.xpath('//span[@class="house-chat-txt"]/text()').extract())[0].strip()
        if phone == '扫码看电话':
            phone = None
        else:
            pass
        url = response.url
        content = str((response.xpath('//ul[@class="introduce-item"]/li[2]').xpath('string(.)')).extract()).strip().replace(' ','').replace('\n','').replace('[','').replace(']','')

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
    '''

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
'Cookie':'Cookie:id58=c5/njVra8DQQfj2HAwwAAg==; als=0; wmda_uuid=aea7e89b397f877f53acd8f27bebb2ef; wmda_new_uuid=1; _ga=GA1.2.317447175.1524316183; wmda_visited_projects=%3B2385390625025%3B2427509687170; commontopbar_myfeet_tooltip=end; __utma=253535702.317447175.1524316183.1527077288.1527077288.1; __utmz=253535702.1527077288.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); city=ty; 58home=ty; commontopbar_ipcity=ty%7C%E5%A4%AA%E5%8E%9F%7C0; defraudName=defraud; 58tj_uuid=064cd8e0-0397-4e20-8444-9562baa36f90; new_session=0; new_uv=21; utm_source=; spm=; init_refer=http%253A%252F%252Fty.58.com%252Fchuzu%252Fpn70%252F%253FPGTID%253D0d3090a7-002e-4ea3-1274-1a7c5ede8a5e%2526ClickID%253D2; commontopbar_new_city_info=740%7C%E5%A4%AA%E5%8E%9F%7Cty; wmda_session_id_2385390625025=1527151891500-12081c2b-c6da-1904; ppStore_fingerprint=569E8A549CCFE1DAC8E49810287C42FE953D3C6D6613B3FF%EF%BC%BF1527151895391; xxzl_deviceid=TZFfbXTQz84a9FBJt0uC1Dp9TIWPcFSUDwIQ1jhqfLRp32JNHG7mi2Jrt3c6BAQ8'
}
class Spider_anjuke(scrapy.Spider):
    name = 'Spider_anjuke'
    allowed_domains = ['anjuke.com']
    url = 'https://ty.zu.anjuke.com/fangyuan/p'

    #爬列表页
    start_urls = ['https://ty.zu.anjuke.com/fangyuan/p{}/'.format(i) for i in range(36, 51, 1)]#36dao51
    def parse(self, response):
        item = BisheItem()
        titles = (response.xpath('//div[@class="zu-info"]/h3/a/text()').extract())
        urls = (response.xpath('//div[@class="zu-info"]/h3/a/@href').extract())
        prices = (response.xpath('//*[@id="list-content"]/div/div[2]/p/strong/text()').extract())
        infos = ((response.xpath('//*[@id="list-content"]/div/div[1]/p[1]').xpath('string(.)')).extract())
        direction = None
        regions = ((response.xpath('//*[@id="list-content"]/div/div[1]/address').xpath('string(.)')).extract())
        phone = None
        print(titles, prices, infos, direction, phone, urls, regions)

        for title, price, info, region, url in zip(titles, prices, infos, regions, urls):
            item['url'] = url
            item['title'] = title
            item['info'] = info.strip().replace(' ','').replace('\n','')
            item['region'] = region.strip().replace(' ','').replace('\n','')
            item['price'] = price
            item['content'] = None
            item['direction'] = direction
            item['phone'] = phone
            yield item


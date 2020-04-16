import scrapy
from scrapy.http import Request
from proxies.items import ProxiesItem

class Myspider(scrapy.Spider):
    name = 'Myspider'
    allowed_domains = ['xicidaili.com']
    url_1 = 'http://www.xicidaili.com/'
    url_2 = 'nn/'

    start_urls = []

    def start_requests(self):
        for i in range(1, 3, 1):
            url = self.url_1 + self.url_2 + str(i)
        # url = 'https://cuiqingcai.com/3472.html'
            yield Request(url, self.parse)

    def parse(self, response):
        item = ProxiesItem()
        ip_addresses = response.xpath('//table[@id="ip_list"]/tr/td[2]/text()').extract()
        ports = response.xpath('//table[@id="ip_list"]/tr/td[3]/text()').extract()
        http_or_https_list = response.xpath('//table[@id="ip_list"]/tr/td[6]/text()').extract()
        for ip_address, port, http_or_https in zip(ip_addresses, ports, http_or_https_list):
            if http_or_https == 'HTTP':
                item['address'] = {'http':ip_address + ':' + port}
            else:
                item['address'] = {'https':ip_address + ':' + port}
            yield item


# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals

# class BisheSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware


class MyUserAgentMiddleware(object):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        print('this agent is '+ user_agent)
        request.headers['User-Agent'] = user_agent

IP_LIST = [
'http://182.202.223.41:61234',
'https://223.145.228.229:6666',
'https://123.169.6.155:31358',
'https://60.182.239.43:39528',
'https://113.121.244.227:39918',
'https://122.4.42.77:24447',
'https://117.57.90.146:42459',
'https://60.167.128.192:43459',
'https://222.71.89.147:46729',
'https://117.93.17.234:61234',
'https://14.118.254.185:6666',
'https://222.185.23.220:6666',
'https://115.213.224.164:26270',
'https://1.195.27.6:35934',
'https://171.13.26.82:42629',
'https://1.198.89.202:33747',
'https://36.25.57.97:43590',
'https://140.250.129.179:28069',
'https://144.255.13.58:30040',
'https://110.90.188.112:37809',
'https://49.87.75.235:49503',
'https://180.118.243.156:808',
'https://27.156.234.152:43185',
'https://113.121.244.47:808',
'https://115.203.164.177:36768',
'https://180.125.97.8:28673',
'https://120.40.133.169:25661',
'https://123.149.162.194:30378',
'https://123.161.155.228:38838',
'https://1.199.192.112:45336',
'https://222.76.187.174:8118',
'https://14.118.255.219:6666',
'https://115.202.252.4:44071',
'https://115.221.112.47:49665',
'https://60.162.19.127:40912',
'https://115.213.203.238:8070',
'https://110.85.89.245:23378',
'https://115.223.95.172:8010',
'https://1.198.89.143:31407',
'https://171.15.89.172:23710',
'https://113.128.9.18:37946',
'https://222.89.82.197:26726',
'https://120.40.252.178:33200',
'https://14.118.254.74:6666',
'https://182.34.55.79:46262',
'https://1.194.152.180:32704',
'https://114.228.75.226:6666',
'http://49.67.53.143:808',
'https://180.118.244.72:61234',
'https://125.78.7.237:40145',
'https://222.191.179.243:29379',
'https://122.241.27.115:23965',
'https://171.13.150.136:20141',
'https://115.221.126.215:24287',
'https://222.85.5.117:29967',
'https://115.223.127.57:8010',
'https://112.85.168.125:18118',
'http://119.28.194.66:8888',
'https://123.53.86.124:35680',
'https://180.122.147.124:27416',
'https://125.120.11.54:6666',
'https://114.226.105.185:6666',
'https://115.203.172.98:25064',
'https://114.228.73.134:6666',
'https://58.212.41.38:49713',
'http://61.135.217.7:80',
'https://180.122.146.47:42104',
'https://113.242.142.211:8118',
'https://218.73.136.43:20120',
'http://122.114.31.177:808',
'https://113.121.164.12:22032',
'https://180.122.146.73:26811',
'https://123.161.238.126:39342',
'https://49.85.6.114:42646',
'https://115.221.126.238:39757',
'https://183.135.248.174:22054',
'https://115.215.6.244:48828',
'https://115.230.73.106:33766',
'https://49.79.196.65:61234',
'https://121.61.89.38:61234',
'https://113.121.240.227:20119',
'https://49.85.5.33:28638',
'https://123.163.140.164:46014',
'https://106.122.171.209:8118',
'https://114.228.73.32:6666',
'https://112.85.168.125:18118',
'https://125.118.244.211:6666',
'https://144.255.121.105:6666',
'https://110.90.131.239:26038',
'https://121.60.77.180:8010',
'https://180.122.144.184:29083',
'https://49.87.0.231:29956',
'https://119.5.145.24:8118',
'https://114.236.83.138:61234',
'https://121.69.13.242:53281',
'https://115.198.38.58:6666',
'https://1.196.7.144:39125',
'http://115.221.119.165:21028',
'https://117.93.17.178:61234',
'https://1.199.135.183:35951',
'https://123.54.229.20:33161',
'https://114.226.135.53:6666',
'https://222.185.23.169:6666',
'https://183.135.253.106:45599',
'https://1.196.7.148:30759',
'https://49.85.6.73:42640',
'https://114.230.107.201:21101',
'http://180.121.161.232:22568',
'https://39.71.190.7:8118',
'https://117.93.17.158:61234',
'https://58.34.240.201:8118',
'https://14.134.169.0:808',
'https://223.145.229.81:6666',
'https://180.118.241.42:808',
'https://115.203.169.41:37138',
'https://115.226.11.75:34779',
'https://123.55.187.150:49491',
'https://42.51.12.2:808',
'https://27.40.143.171:61234',
'https://114.228.74.122:6666',
'https://118.122.92.252:37901',
'https://180.173.6.13:36621',
'https://175.171.182.14:53281',
'https://59.56.242.45:47114',
'https://1.198.194.164:27237',
'https://125.113.254.62:42816',
'https://171.8.171.46:20476',
'https://122.242.90.4:43808',
'https://121.207.78.190:36757',
'https://222.185.23.154:6666',
'https://220.184.215.52:6666',
'https://116.115.210.107:27195',
'https://1.194.119.60:44615',
'https://123.161.238.248:24644',
'https://123.160.34.80:28969',
'https://180.122.148.123:42896',
'https://171.14.209.45:46599',
'https://120.37.173.145:20060',
'https://182.39.12.92:49326',
'https://180.121.166.206:40717',
'https://218.5.89.136:8118',
'https://115.46.80.142:8123',
'https://180.122.151.43:38857',
'https://36.22.198.150:27134',
'https://110.88.127.30:24786',
'https://180.121.129.255:808',
'https://122.237.105.243:80',
'https://114.225.113.143:808',
'https://183.151.40.42:3128',
'https://110.73.41.56:8123',
'https://117.66.210.178:28995',
'https://114.239.215.250:61234',
'https://106.111.53.19:25647',
'https://121.61.89.89:61234'
]
class MyHttpProxyMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip
    def process_request(self, request, spider):
        proxies = random.choice(IP_LIST)
        print('tihs ip is '+ proxies)
        request.meta['proxy'] = proxies

IP_LIST = [
'http://182.202.223.41:61234',
'https://223.145.228.229:6666',
'https://123.169.6.155:31358',
'https://60.182.239.43:39528',
'https://113.121.244.227:39918',
'https://122.4.42.77:24447',
'https://117.57.90.146:42459',
'https://60.167.128.192:43459',
'https://222.71.89.147:46729',
'https://117.93.17.234:61234',
'https://14.118.254.185:6666',
'https://222.185.23.220:6666',
'https://115.213.224.164:26270',
'https://1.195.27.6:35934',
'https://171.13.26.82:42629',
'https://1.198.89.202:33747',
'https://36.25.57.97:43590',
'https://140.250.129.179:28069',
'https://144.255.13.58:30040',
'https://110.90.188.112:37809',
'https://49.87.75.235:49503',
'https://180.118.243.156:808',
'https://27.156.234.152:43185',
'https://113.121.244.47:808',
'https://115.203.164.177:36768',
'https://180.125.97.8:28673',
'https://120.40.133.169:25661',
'https://123.149.162.194:30378',
'https://123.161.155.228:38838',
'https://1.199.192.112:45336',
'https://222.76.187.174:8118',
'https://14.118.255.219:6666',
'https://115.202.252.4:44071',
'https://115.221.112.47:49665',
'https://60.162.19.127:40912',
'https://115.213.203.238:8070',
'https://110.85.89.245:23378',
'https://115.223.95.172:8010',
'https://1.198.89.143:31407',
'https://171.15.89.172:23710',
'https://113.128.9.18:37946',
'https://222.89.82.197:26726',
'https://120.40.252.178:33200',
'https://14.118.254.74:6666',
'https://182.34.55.79:46262',
'https://1.194.152.180:32704',
'https://114.228.75.226:6666',
'http://49.67.53.143:808',
'https://180.118.244.72:61234',
'https://125.78.7.237:40145',
'https://222.191.179.243:29379',
'https://122.241.27.115:23965',
'https://171.13.150.136:20141',
'https://115.221.126.215:24287',
'https://222.85.5.117:29967',
'https://115.223.127.57:8010',
'https://112.85.168.125:18118',
'http://119.28.194.66:8888',
'https://123.53.86.124:35680',
'https://180.122.147.124:27416',
'https://125.120.11.54:6666',
'https://114.226.105.185:6666',
'https://115.203.172.98:25064',
'https://114.228.73.134:6666',
'https://58.212.41.38:49713',
'http://61.135.217.7:80',
'https://180.122.146.47:42104',
'https://113.242.142.211:8118',
'https://218.73.136.43:20120',
'http://122.114.31.177:808',
'https://113.121.164.12:22032',
'https://180.122.146.73:26811',
'https://123.161.238.126:39342',
'https://49.85.6.114:42646',
'https://115.221.126.238:39757',
'https://183.135.248.174:22054',
'https://115.215.6.244:48828',
'https://115.230.73.106:33766',
'https://49.79.196.65:61234',
'https://121.61.89.38:61234',
'https://113.121.240.227:20119',
'https://49.85.5.33:28638',
'https://123.163.140.164:46014',
'https://106.122.171.209:8118',
'https://114.228.73.32:6666',
'https://112.85.168.125:18118',
'https://125.118.244.211:6666',
'https://144.255.121.105:6666',
'https://110.90.131.239:26038',
'https://121.60.77.180:8010',
'https://180.122.144.184:29083',
'https://49.87.0.231:29956',
'https://119.5.145.24:8118',
'https://114.236.83.138:61234',
'https://121.69.13.242:53281',
'https://115.198.38.58:6666',
'https://1.196.7.144:39125',
'http://115.221.119.165:21028',
'https://117.93.17.178:61234',
'https://1.199.135.183:35951',
'https://123.54.229.20:33161',
'https://114.226.135.53:6666',
'https://222.185.23.169:6666',
'https://183.135.253.106:45599',
'https://1.196.7.148:30759',
'https://49.85.6.73:42640',
'https://114.230.107.201:21101',
'http://180.121.161.232:22568',
'https://39.71.190.7:8118',
'https://117.93.17.158:61234',
'https://58.34.240.201:8118',
'https://14.134.169.0:808',
'https://223.145.229.81:6666',
'https://180.118.241.42:808',
'https://115.203.169.41:37138',
'https://115.226.11.75:34779',
'https://123.55.187.150:49491',
'https://42.51.12.2:808',
'https://27.40.143.171:61234',
'https://114.228.74.122:6666',
'https://118.122.92.252:37901',
'https://180.173.6.13:36621',
'https://175.171.182.14:53281',
'https://59.56.242.45:47114',
'https://1.198.194.164:27237',
'https://125.113.254.62:42816',
'https://171.8.171.46:20476',
'https://122.242.90.4:43808',
'https://121.207.78.190:36757',
'https://222.185.23.154:6666',
'https://220.184.215.52:6666',
'https://116.115.210.107:27195',
'https://1.194.119.60:44615',
'https://123.161.238.248:24644',
'https://123.160.34.80:28969',
'https://180.122.148.123:42896',
'https://171.14.209.45:46599',
'https://120.37.173.145:20060',
'https://182.39.12.92:49326',
'https://180.121.166.206:40717',
'https://218.5.89.136:8118',
'https://115.46.80.142:8123',
'https://180.122.151.43:38857',
'https://36.22.198.150:27134',
'https://110.88.127.30:24786',
'https://180.121.129.255:808',
'https://122.237.105.243:80',
'https://114.225.113.143:808',
'https://183.151.40.42:3128',
'https://110.73.41.56:8123',
'https://117.66.210.178:28995',
'https://114.239.215.250:61234',
'https://106.111.53.19:25647',
'https://121.61.89.89:61234'
]
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'#自己的
]
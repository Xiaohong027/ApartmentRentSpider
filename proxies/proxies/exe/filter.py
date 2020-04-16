# -*- coding:utf-8 -*-
import pymongo
import requests

host = 'localhost'
port = 27017
headers = {
    'Cookie': 'hidden',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

client = pymongo.MongoClient(host,port)
proxies = client['proxies']
version1 = proxies['version1']

def filter(proxies):
    url = 'http://58.com/'
    try:
        code_status = requests.get(url, headers=headers, proxies=proxies, timeout=3)
    except:
        print('wrong')
        version1.remove({'address': proxies})
    else:
        print('success')

for i in version1.find():
    proxies = i['address']
    filter(proxies)